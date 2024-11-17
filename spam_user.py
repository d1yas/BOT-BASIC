import time
import pyautogui


def SendMessage():
    time.sleep(7)
    message = "Sarvar"
    iterations = 50

    for i in range(iterations):
        pass

    while iterations > 0:
        iterations -= 1

        pyautogui.typewrite(message.strip())
        pyautogui.press('enter')
    print("Вся обойма попала в нашу жертву!")


def SendText():
    time.sleep(4)
    with open('text.txt') as f:
        lines = f.readlines()
    for line in lines:
        pyautogui.typewrite(line.strip())
        pyautogui.typewrite('enter')
    print("Дело сделано, осталось успокоить нашу жертву ^_^")


print('~'*50)
print("[1] ===> Стрелять одним сообщением указанным в переменной ")
print("[2] ===> Отправлять строки из блокнота ")
print('~'*50)
option = input("[Выбирай функцию]===> ")
print("Подождите 5 секунд.")

if option == "1":
    SendMessage()
elif option == "2":
    SendText()
else:
    print('Выбирай функция 1 или 2!')