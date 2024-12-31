def get_color(color_name):
    """Retrieve RGB color for a given name."""
    palette = {
        'orange': [0, 143, 255],
        'purple': [255, 0, 0],
        'pink': [153, 0, 157],
        'green': [0, 255, 0],
        'berry': [40, 0, 100],
        'caramel': [50, 70, 70],
        'yellow': [0, 255, 255],
        'aqua': [255, 255, 0],
        'peach': [35, 35, 139],
        'red': [2, 1, 159],
        'black': [0, 0, 0]
    }
    return palette.get(color_name, [0, 0, 0])  # Default to black if color not found
