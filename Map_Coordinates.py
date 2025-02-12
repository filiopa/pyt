# Configuration - Making an image with coordinates! COORDINATES & MAPPING!!! 
image_size = 21  # Image size (21x21 for simplicity, must be odd for symmetry)
center = image_size // 2  # Center of the image

# Predefined input for testing
coordinates = [(2, 2), (-2, 2), (-2, -2), (2, -2), (0, 4), (4, 0), (5,8), (-5,-3), (9,1), (3,4), (5,-6)]
label_start = 'A'

# Initialize the grid with dots (representing empty space)
grid = [['.' for _ in range(image_size)] for _ in range(image_size)]

# Draw axis
for i in range(image_size):
    grid[center][i] = '-'  # X-axis
    grid[i][center] = '|'  # Y-axis
grid[center][center] = '+'  # Origin

# Draw points and labels
for index, (x, y) in enumerate(coordinates):
    img_x = center + x
    img_y = center - y
    label = chr(ord(label_start) + index)  # Calculate the label (A, B, C, ...)
    grid[img_y][img_x] = label

# Print the grid
for row in grid:
    print(' '.join(row))