import mediapipe as mp
import cv2

mp_face_mesh = mp.solutions.face_mesh

def detect_landmarks(src):
    """Detect facial landmarks in the input image."""
    with mp_face_mesh.FaceMesh(static_image_mode=False, max_num_faces=1, refine_landmarks=True) as face_mesh:
        results = face_mesh.process(cv2.cvtColor(src, cv2.COLOR_BGR2RGB))
        if results.multi_face_landmarks:
            face_landmarks = results.multi_face_landmarks[0].landmark

            height, width, _ = src.shape
            # Convert normalized landmarks to pixel coordinates
            return {
                "lips": [
                    (int(face_landmarks[i].x * width), int(face_landmarks[i].y * height))
                    for i in [
                        61, 185, 40, 39, 37, 0, 267, 269, 270, 408, 415, 272, 271, 268, 12, 38, 41, 42, 191, 78, 76,
                        61, 146, 91, 181, 84, 17, 314, 405, 320, 307, 308, 324, 318, 402, 317, 14, 87, 178, 88, 95
                    ]
                ],
                "eyes": {
                    "left": [
                        (int(face_landmarks[i].x * width), int(face_landmarks[i].y * height))
                        for i in [33, 246, 161, 160, 159, 158, 157, 173]
                    ],
                    "right": [
                        (int(face_landmarks[i].x * width), int(face_landmarks[i].y * height))
                        for i in [263, 466, 388, 387, 386, 385, 384, 398]
                    ]
                }
            }
    return None
