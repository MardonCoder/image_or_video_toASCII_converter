from PIL import Image
import numpy as np

# More detailed set of symbols from dark to light
ASCII_CHARS = "@%#*+=-:. "


# Convert pixels to ASCII characters
def pixel_to_ascii(image, ascii_chars=ASCII_CHARS):
    grayscale_image = image.convert("L")  # Convert to grayscale
    pixels = np.array(grayscale_image, dtype=int)  # Convert to a pixel array with type int
    # Scale pixel values to the range of ASCII characters
    ascii_image = np.array([[ascii_chars[pixel * (len(ascii_chars) - 1) // 255] for pixel in row] for row in pixels])
    return ascii_image


# Display the ASCII image in the console
def print_ascii_image(ascii_image):
    for row in ascii_image:
        print("".join(row))


# Main function
def image_to_ascii(image_path, new_width=100):
    image = Image.open(image_path)
    width, height = image.size
    # Account for the aspect ratio of console characters (~1:2)
    aspect_ratio = height / width / 2
    new_height = int(aspect_ratio * new_width)
    resized_image = image.resize((new_width, new_height))

    # Convert the image to ASCII and display it
    ascii_image = pixel_to_ascii(resized_image)
    print_ascii_image(ascii_image)


# Example usage
image_to_ascii("AnimeGirl.png")



