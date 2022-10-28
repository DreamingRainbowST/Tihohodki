from telethon.sync import TelegramClient, events
import time
import re
API_ID = 2181066
API_HASH = "8f95f37b847ada4f0150befe9eb27dbe"
BOT_TOKEN = "1556982843:AAGsCaq8XNERyabbQYhEIUpfSfQC9gAc9TA"

client = TelegramClient('Acc', API_ID, API_HASH)
bot = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN)
CHANNEL_ID = "ComputatisTardigrades"
INTERVAL = 60/20
INTERVAL_BIG = 30
BASE = "тихоход"

START = 569001
ADMIN_ID = 1128142884


    
def generator():
    global START
    global BASE
    count = START
    while True:
        temp = str(count)
        if temp[-1] == "1":
            if len(temp) == 1:
                manul = BASE + 'ка'
            elif temp[-2] not in ["1"]:
                manul = BASE + 'ка'
            else: 
                manul = BASE + "ок"
                
        elif temp[-1] in ["2", "3", "4"]:
            if len(temp) == 1:
                manul = BASE + "ки"
            elif temp[-2] not in ["1"]:
                manul = BASE + "ки"
            else: 
                manul = BASE + "ок"
        else:
            manul = BASE + "ок"
        
        count += 1
        yield f"{count-1} {manul}"
with bot:
    try:
        bot.send_message(ADMIN_ID, 'Начал свою работу')
    except:
        pass
    for text in generator():
        count = 0
        bot.send_message(CHANNEL_ID, text)
        time.sleep(3)
        count += 3
        if count >= 60:
            time.sleep(30)
            count = 0
