import cv2
from src.makeup.lipstick import Lipstick
from src.makeup.eyeliner import Eyeliner
from src.utils.landmarks import detect_landmarks
from src.utils.color_palettes import get_color

def main(video_source=0, lip_color='red', eyeliner_color='black', debug=False):
    cap = cv2.VideoCapture(video_source)

    # Convert color names to RGB
    lip_rgb = get_color(lip_color)
    eyeliner_rgb = get_color(eyeliner_color)

    # Instantiate makeup effects
    lipstick = Lipstick(color=lip_rgb)
    eyeliner = Eyeliner(color=eyeliner_rgb, thickness=2)

    while True:
        ret, img = cap.read()
        if not ret:
            break

        img = cv2.resize(img, (700, 400))
        img = cv2.flip(img, 1)

        # Detect landmarks
        landmarks = detect_landmarks(img)
        if landmarks:
            # Apply lipstick
            img = lipstick.apply(img, landmarks["lips"])
            # Apply eyeliner
            img = eyeliner.apply(img, landmarks["eyes"]["left"])
            img = eyeliner.apply(img, landmarks["eyes"]["right"])

        # Debug Mode: Draw landmarks
        if debug and landmarks:
            for region, points in landmarks.items():
                if isinstance(points, dict):  # Handle nested landmarks (eyes)
                    for subregion, subpoints in points.items():
                        for x, y in subpoints:
                            cv2.circle(img, (x, y), 2, (0, 255, 0), -1)
                else:
                    for x, y in points:
                        cv2.circle(img, (x, y), 2, (0, 0, 255), -1)

        cv2.imshow("Makeup Application", img)

        if cv2.waitKey(1) & 0xFF == 27:
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main(video_source=0, lip_color='red', eyeliner_color='black', debug=True)
