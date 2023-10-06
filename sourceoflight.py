import cv2
import numpy as np

# Load your image
image = cv2.imread('your_image.jpg')  # Replace 'your_image.jpg' with your image file path

# Get the height and width of the image
height, width = image.shape[:2]

# Define the gradient factor for increased brightness (adjust as needed)
gradient_factor = 2.25 # Adjust this value to control the gradient effect and brightness

# Create a linear gradient mask from right to left
gradient_mask_right_to_left = np.linspace(1.0, gradient_factor, width)

# Apply the gradient mask from right to left
image_with_gradient_right_to_left = image.copy()
for i in range(width):
    image_with_gradient_right_to_left[:, i, :] = np.clip(image[:, i, :] * gradient_mask_right_to_left[i], 0, 255)

###

# Create a linear gradient mask from left to right (reverse of previous)
gradient_mask_left_to_right = np.linspace(gradient_factor, 1.0, width)

# Apply the gradient mask from left to right
image_with_gradient_left_to_right = image.copy()
for i in range(width):
    image_with_gradient_left_to_right[:, i, :] = np.clip(image[:, i, :] * gradient_mask_left_to_right[i], 0, 255)

###

# Create a linear gradient mask from bottom to top
gradient_mask_bottom_to_top = np.linspace(1.0, gradient_factor, height).reshape(-1, 1)

# Apply the gradient mask from bottom to top
image_with_gradient_bottom_to_top = image.copy()
for i in range(height):
    image_with_gradient_bottom_to_top[i, :, :] = np.clip(image[i, :, :] * gradient_mask_bottom_to_top[i][0], 0, 255)

# Create a linear gradient mask from bottom to top
gradient_mask_top_to_bottom = np.linspace( gradient_factor, 1.0,height).reshape(-1, 1)

# Apply the gradient mask from bottom to top
image_with_gradient_top_to_bottom = image.copy()
for i in range(height):
    image_with_gradient_top_to_bottom[i, :, :] = np.clip(image[i, :, :] * gradient_mask_top_to_bottom[i][0], 0, 255)

# Save the images with the gradient effects and increased brightness

cv2.imwrite('image_with_gradient_left_to_right.jpg', image_with_gradient_left_to_right)
cv2.imwrite('image_with_gradient_right_to_left.jpg', image_with_gradient_right_to_left)
cv2.imwrite('image_with_gradient_bottom_to_top.jpg', image_with_gradient_bottom_to_top)
cv2.imwrite('image_with_gradient_top_to_bottom.jpg', image_with_gradient_top_to_bottom)
