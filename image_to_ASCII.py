from PIL import Image
import numpy as np

# We set the symbols from “dark” to “light”; the larger the pixel, the “heavier” the symbol.
ASCII_CHARS = "@%#*+=-:. "

# Converting pixels to ASCII characters
def pixel_to_ascii(image):
    # Convert the image to grayscale
    grayscale_image = image.convert("L")
    # Get the pixel array
    pixels = np.array(grayscale_image)
    # Scale pixel values from 0 to len(ASCII_CHARS) - 1
    ascii_image = np.array([[ASCII_CHARS[pixel // (255 // (len(ASCII_CHARS) - 1))] for pixel in row] for row in pixels])
    return ascii_image

# Display the image in the console
def print_ascii_image(ascii_image):
    for row in ascii_image:
        print("".join(row))

# Main function
def image_to_ascii(image_path, new_width=100):
    # Load the image
    image = Image.open(image_path)
    # Scale it to the desired width
    width, height = image.size
    aspect_ratio = height / width
    new_height = int(aspect_ratio * new_width)
    resized_image = image.resize((new_width, new_height))
    # Convert the image to ASCII
    ascii_image = pixel_to_ascii(resized_image)
    # Display the image in the console
    print_ascii_image(ascii_image)

# Example usage
image_to_ascii("AnimeGirl.png")
