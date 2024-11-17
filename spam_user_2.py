from telethon import TelegramClient

api_id = '28841939'
api_hash = '9f77eaf56b839c64c25fecb77bf53fc8'
phone_number = '+998945822808'

client = TelegramClient('session_name', api_id, api_hash)

async def main():
    await client.start(phone=phone_number)
    
    username = '@Usz_701'
    while True:
      await client.send_message(username, 'SARDOR GEY!')

    

with client:
    client.loop.run_until_complete(main())
