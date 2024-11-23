import cv2
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


# Обработка каждого кадра видео в ASCII
def frame_to_ascii(frame, new_width=100):
    image = Image.fromarray(frame)  # Преобразуем кадр (массив) в изображение PIL
    width, height = image.size
    aspect_ratio = height / width / 2  # Учитываем соотношение сторон консольных символов (~1:2)
    new_height = int(aspect_ratio * new_width)
    resized_image = image.resize((new_width, new_height))  # Изменяем размер изображения

    # Преобразуем изображение в ASCII
    ascii_image = pixel_to_ascii(resized_image)
    print_ascii_image(ascii_image)


# Основная функция для обработки видео
def video_to_ascii(video_path, new_width=100):
    cap = cv2.VideoCapture(video_path)  # Открываем видео
    if not cap.isOpened():
        print("Ошибка: не удалось открыть видео.")
        return

    # Проигрываем видео, преобразуя каждый кадр
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break  # Выход из цикла, если кадры кончились

        frame_to_ascii(frame, new_width)  # Преобразуем кадр в ASCII

        if cv2.waitKey(25) & 0xFF == ord('q'):  # Нажмите 'q', чтобы выйти
            break

    cap.release()
    cv2.destroyAllWindows()


# Пример использования1
video_to_ascii("BadApple.mp4", new_width=100)  # Укажите путь к вашему видео
