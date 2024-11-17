import requests
import time
time.sleep(3)

bot_token = ''

user_id = '1334136217'
message_text = 'test'

url = f'https://api.telegram.org/bot{bot_token}/sendMessage'


params = {
    'chat_id': user_id,
    'text': message_text
}

for i in range(1000):
    response = requests.get(url, params=params)

    if response.status_code == 200:
        print(f'Сообщение {i + 1} отправлено успешно!')
    else:
        print(f'Ошибка при отправке сообщения {i + 1}:', response.text)


    # time.sleep(1)
