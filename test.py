import requests
import time

API_KEY = 'ВАШ_API_КЛЮЧ'
SERVICE = 'tg'
COUNTRY = 0

BASE_URL = 'https://sms-activate.ru/stubs/handler_api.php'

def get_number():
    params = {
        'api_key': API_KEY,
        'action': 'getNumber',
        'service': SERVICE,
        'country': COUNTRY,
    }
    response = requests.get(BASE_URL, params=params)
    data = response.text.split(':')
    
    if data[0] == 'ACCESS_NUMBER':
        return data[1], data[2]
    else:
        print('Ошибка получения номера:', response.text)
        return None, None

def get_sms(activation_id):
    params = {
        'api_key': API_KEY,
        'action': 'getStatus',
        'id': activation_id,
    }
    while True:
        response = requests.get(BASE_URL, params=params)
        data = response.text
        if data.startswith('STATUS_OK'):
            return data.split(':')[1]
        elif data == 'STATUS_WAIT_CODE':
            print("Ожидание SMS...")
            time.sleep(5)
        elif data == 'STATUS_CANCEL':
            print("Активация была отменена.")
            return None
        else:
            print('Ошибка:', data)
            return None

def main():
    activation_id, phone_number = get_number()
    if activation_id:
        print("Номер для регистрации в Telegram:", phone_number)
        input("Зарегистрируйтесь в Telegram и нажмите Enter, когда отправите SMS-код...")
        sms_code = get_sms(activation_id)
        if sms_code:
            print("Полученный код:", sms_code)
        else:
            print("Не удалось получить SMS-код.")
    else:
        print("Не удалось получить номер.")

if __name__ == '__main__':
    main()
