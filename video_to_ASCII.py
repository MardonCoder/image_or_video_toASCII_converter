import cv2
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


# Process each video frame into ASCII
def frame_to_ascii(frame, new_width=100):
    image = Image.fromarray(frame)  # Convert the frame (array) into a PIL image
    width, height = image.size
    aspect_ratio = height / width / 2  # Account for the aspect ratio of console characters (~1:2)
    new_height = int(aspect_ratio * new_width)
    resized_image = image.resize((new_width, new_height))  # Resize the image

    # Convert the image to ASCII
    ascii_image = pixel_to_ascii(resized_image)
    print_ascii_image(ascii_image)


# Main function to process video
def video_to_ascii(video_path, new_width=100):
    cap = cv2.VideoCapture(video_path)  # Open the video
    if not cap.isOpened():
        print("Error: Could not open the video.")
        return

    # Play the video, converting each frame to ASCII
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break  # Exit the loop if there are no more frames

        frame_to_ascii(frame, new_width)  # Convert the frame to ASCII

        if cv2.waitKey(25) & 0xFF == ord('q'):  # Press 'q' to exit
            break

    cap.release()
    cv2.destroyAllWindows()


# Example usage
video_to_ascii("BadApple.mp4", new_width=100)  # Specify the path to your video
