from PIL import Image
import numpy as np

# Более детализированный набор символов от темных к светлым
ASCII_CHARS = "@%#*+=-:. "


# Преобразование пикселей в символы ASCII
def pixel_to_ascii(image, ascii_chars=ASCII_CHARS):
    grayscale_image = image.convert("L")  # Преобразование в оттенки серого
    pixels = np.array(grayscale_image, dtype=int)  # Преобразование в массив пикселей с типом int
    # Масштабируем значения пикселей на диапазон символов
    ascii_image = np.array([[ascii_chars[pixel * (len(ascii_chars) - 1) // 255] for pixel in row] for row in pixels])
    return ascii_image


# Вывод изображения в консоль
def print_ascii_image(ascii_image):
    for row in ascii_image:
        print("".join(row))


# Основная функция
def image_to_ascii(image_path, new_width=100):
    image = Image.open(image_path)
    width, height = image.size
    # Учитываем соотношение сторон консольных символов (~1:2)
    aspect_ratio = height / width / 2
    new_height = int(aspect_ratio * new_width)
    resized_image = image.resize((new_width, new_height))

    # Преобразуем изображение в ASCII и выводим
    ascii_image = pixel_to_ascii(resized_image)
    print_ascii_image(ascii_image)


# Пример использования
image_to_ascii("photo_2024-10-29_13-49-14.jpg")


