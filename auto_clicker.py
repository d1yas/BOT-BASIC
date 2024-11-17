import pyautogui
import time

def auto_clicker(interval, duration):
    print("Начинаю тапать через 10 секунд")
    print(10)
    time.sleep(1)
    print(9)

    """
    Автокликер, который кликает через заданные промежутки времени в течение определенного времени.

    :param interval: Время между кликами в секундах.
    :param duration: Общая продолжительность работы автокликера в секундах.
    """
    end_time = time.time() + duration
    print("Начинаю кликать... Нажмите Ctrl+C, чтобы остановить.")
    try:
        while time.time() < end_time:
            pyautogui.click()  # Выполняет левый клик мыши
            time.sleep(interval)
    except KeyboardInterrupt:
        print("\nАвтокликер остановлен пользователем.")

interval = 0  # Интервал между кликами (в секундах)
duration = 60   # Общая продолжительность работы автокликера (в секундах)

auto_clicker(interval, duration)
