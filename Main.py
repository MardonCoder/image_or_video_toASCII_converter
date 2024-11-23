#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#This is not main, ignore this file, use "image_to_ASCII", "image_to_ASCII_another"
#and for video converting "video_to_ASCII"
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~




from PIL import Image
import numpy as np

# Задаем символы от "темных" к "светлым", чем темнее пиксель, тем "тяжелее" символ.
ASCII_CHARS = "@%#*+=-:. "

# Преобразование пикселей в символы ASCII
def pixel_to_ascii(image):
    # Преобразуем изображение в оттенки серого
    grayscale_image = image.convert("L")
    # Получаем массив пикселей
    pixels = np.array(grayscale_image)
    # Масштабируем значения пикселей от 0 до len(ASCII_CHARS) - 1
    ascii_image = np.array([[ASCII_CHARS[pixel // (255 // (len(ASCII_CHARS) - 1))] for pixel in row] for row in pixels])
    return ascii_image

# Вывод изображения в консоль
def print_ascii_image(ascii_image):
    for row in ascii_image:
        print("".join(row))

# Основная функция
def image_to_ascii(image_path, new_width=100):
    # Загружаем изображение
    image = Image.open(image_path)
    # Масштабируем его до нужной ширины
    width, height = image.size
    aspect_ratio = height / width
    new_height = int(aspect_ratio * new_width)
    resized_image = image.resize((new_width, new_height))
    # Преобразуем изображение в ASCII
    ascii_image = pixel_to_ascii(resized_image)
    # Выводим изображение в консоль
    print_ascii_image(ascii_image)

# Пример использования
image_to_ascii("AnimeGirl.png")
