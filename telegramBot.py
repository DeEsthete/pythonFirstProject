import requests
from telegram.ext import Updater
from config import TOKEN, GROUP_CHAT_ID


updater = Updater(token=TOKEN, use_context=True)
def sendMessage(bot_message):
    send_text = 'https://api.telegram.org/bot' + TOKEN + '/sendMessage?chat_id=' + GROUP_CHAT_ID + '&parse_mode=Markdown&text=' + bot_message
    response = requests.get(send_text)
    return response.json()

sendMessage('Apchi')

