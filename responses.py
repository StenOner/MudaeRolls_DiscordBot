import requests, time, os
from dotenv import load_dotenv

load_dotenv()

URL_BASE = 'https://discord.com/api/v9/channels/{}/messages'
USER_TOKEN = os.getenv('USER_TOKEN')

def handle_response(channel_id: int, user_message: str) -> str:
    p_user_message = user_message.lower()
    [command, command_message] = p_user_message.split(' ', 1) if ' ' in user_message else [user_message, None]
    headers = {
        'Authorization': USER_TOKEN,
    }
    json = {
        'content': f'${command}',
    }
    match command:
        case 'cc':
            return str(command_message)
        case 'tu' | 'rolls' | 'daily' | 'dk' | 'vote':
            requests.post(URL_BASE.format(channel_id), json=json, headers=headers, timeout=2.50)
            return ''
        case 'wa' | 'ha' | 'ma':
            try:
                times_to_roll = int(command_message)
            except Exception as ex:
                times_to_roll = 1
                print(ex)
            else:
                if times_to_roll > 10:
                    times_to_roll = 10
            for _ in range(times_to_roll):
                requests.post(URL_BASE.format(channel_id), json=json, headers=headers, timeout=2.50)
                time.sleep(0.5)
            return ''
        case _:
            return '`Unknown command`'