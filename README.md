Here’s a well-structured and beginner-friendly README.md file for Ashley’s Image Manipulation and Filtering project:

⸻

Ashley’s Image Manipulation and Filtering

This Python project demonstrates how to perform basic image processing tasks such as grayscale conversion, blurring, edge detection, flipping, and rotating using NumPy, PIL, and SciPy.

Features
	•	Load and display images
	•	Apply a grayscale filter
	•	Apply a blur filter (box blur)
	•	Perform edge detection
	•	Flip the image horizontally
	•	Rotate the image 90° clockwise
	•	Display all transformations using matplotlib

Sample Transformations

Original	Grayscale	Blur	Edge Detection
			

(Add sample images to the docs/ folder for preview if you like)

Requirements
	•	Python 3.x
	•	NumPy
	•	Pillow (PIL)
	•	Matplotlib
	•	SciPy

Installation

Install the required packages using pip:

pip install numpy pillow matplotlib scipy

Usage

Replace "your_image.jpg" with the path to your image in the script:

apply_filters("your_image.jpg")

Then run:

python image_filters.py

Each transformation will be shown in a separate window using matplotlib.

Functions Overview
	•	load_image() – Loads and converts image to RGB array
	•	display_image() – Displays image with a title
	•	apply_grayscale() – Converts image to grayscale
	•	apply_blur() – Applies a simple box blur
	•	apply_edge_detection() – Highlights edges using a Laplacian kernel
	•	flip_horizontal() – Flips image left-to-right
	•	rotate_90() – Rotates image 90° clockwise

Customization

You can adjust:
	•	Blur intensity by changing kernel_size in apply_blur()
	•	Edge kernel for different styles of edge detection

License

MIT License

⸻

Let me know if you’d like to add image saving functionality or build a simple GUI with Tkinter!
