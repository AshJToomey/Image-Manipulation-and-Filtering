# Image Manipulation and Filtering.txt
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
from scipy.ndimage import convolve

# Load and display the image
def load_image(image_path):
    img = Image.open((r"C:\Users\ashle\OneDrive\Documents\Python\Ashleys Image Manipulation and Filtering\ASHLEY PIC.jpeg"))
    img = img.convert("RGB")  # Convert to RGB if not already
    img_array = np.array(img)
    return img_array

def display_image(img_array, title="Image"):
    plt.imshow(img_array)
    plt.title(title)
    plt.axis("off")
    plt.show()

# Grayscale filter
# Ashley's Image Manipulation and Filtering project

def apply_grayscale(img_array):
    grayscale_img = np.mean(img_array, axis=2, keepdims=True).astype(np.uint8)
    return np.repeat(grayscale_img, 3, axis=2)

# Blur filter
def apply_blur(img_array, kernel_size=5):
    kernel = np.ones((kernel_size, kernel_size)) / (kernel_size ** 2)
    blurred_img = np.stack([convolve(img_array[:,:,i], kernel) for i in range(3)], axis=2)
    return blurred_img.astype(np.uint8)

# Edge detection filter
def apply_edge_detection(img_array):
    edge_kernel = np.array([[-1, -1, -1], 
                            [-1,  8, -1], 
                            [-1, -1, -1]])
    edge_img = np.stack([convolve(img_array[:,:,i], edge_kernel) for i in range(3)], axis=2)
    edge_img = np.clip(edge_img, 0, 255)  # Clip values to be in valid pixel range
    return edge_img.astype(np.uint8)

# Flip the image horizontally
def flip_horizontal(img_array):
    return np.fliplr(img_array)

# Rotate the image 90 degrees clockwise
def rotate_90(img_array):
    return np.rot90(img_array, -1)  # Rotate -1 for clockwise, 1 for counter-clockwise

# Main function to apply and display transformations
def apply_filters(image_path):
    img_array = load_image(image_path)
    display_image(img_array, title="Original Image")
    
    grayscale_img = apply_grayscale(img_array)
    display_image(grayscale_img, title="Grayscale Filter")
    
    blurred_img = apply_blur(img_array)
    display_image(blurred_img, title="Blur Filter")
    
    edge_img = apply_edge_detection(img_array)
    display_image(edge_img, title="Edge Detection Filter")
    
    flipped_img = flip_horizontal(img_array)
    display_image(flipped_img, title="Flipped Horizontally")
    
    rotated_img = rotate_90(img_array)
    display_image(rotated_img, title="Rotated 90 Degrees Clockwise")

# Run the project with an image file
apply_filters(r"C:\Users\ashle\OneDrive\Documents\Python\Ashleys Image Manipulation and Filtering\ASHLEY PIC.jpeg")  # Replace with your image path
