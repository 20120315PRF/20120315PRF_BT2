##
# Generate telegram messages and send to the user
##
import telebot
import notification_filter
from datetime import datetime, timedelta

#Singleton telegram bot
class TelegramBot:

    __telegram_bot = None

    def __init__(self):
        self.__telegram_bot = None

    def get_bot(self, apiKey):
        if self.__telegram_bot is None:
            self.__telegram_bot = telebot.TeleBot(apiKey)
        return self.__telegram_bot

    ## Return the bot with the api key given
    def set_api_key(self, apiKey):
        self.__telegram_bot = None
        return self.get_bot(apiKey)

#Instance for telegram bot
telegramBot = TelegramBot()

## Sends a message to the user
def __send_telegram_message(apiKey, user, msg):
     bot = telegramBot.get_bot(apiKey)
     bot.send_message(int(user), str(msg) )

# Generate email message for a given delegate
def __generate_message_for_telegram( delegate, user, currentTime, history):
    ## Delegate status
    if delegate['status'] is None:
        delegate['status'] = 'Not found'
    msg = "\nDelegate " + delegate['name'] + "\n Forging?=" + delegate['status'] + "\n\t"
    msg = msg + "Position: " + delegate['position'] + "\tUptime: " + delegate['uptime']
    return msg


## Generates a UTC Time
def generate_utc_time():
    now = datetime.utcnow()
    return str(now).split('.')[0]

## Generates GTM time with offset
def generate_gtm_time(offset):
    now = datetime.utcnow() + timedelta(hours=offset)
    return str(now).split('.')[0]

## For each user of telegram, send message with notifications
def send_telegram_notifications (apiKey, userList, currentTime, gtmOffset, delegateStatus, history):

    for user in userList:
        #Cast to str
        userDir = str(user)
        msg = __generate_message_for_telegram( delegateStatus , userDir, currentTime, history)

        ### Send notification only if msgContent is available
        msg_content = "" + msg
        if msg_content != "":
            msg_content = "[ (GTM+" + str(gtmOffset) + ") " + generate_gtm_time(gtmOffset) + ' ]\n' + msg_content
            try:
                __send_telegram_message(apiKey, user, msg_content)
            except:
                print("Cant send message for the user " + str(user))

