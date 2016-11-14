##
# Generate telegram messages and send to the user
##
import telebot
import notification_filter
from datetime import datetime, timedelta

#Singleton telegram bot
class TelegramBot:

    __telegramBot = None

    def __init__(self):
        self.__telegramBot = None

    def getBot(self, apiKey):
        if self.__telegramBot is None:
            self.__telegramBot = telebot.TeleBot(apiKey)
        return self.__telegramBot

    ## Return the bot with the api key given
    def setApiKey(self, apiKey):
        self.__telegramBot = None
        return self.getBot(apiKey)

#Instance for telegram bot
telegramBot = TelegramBot()

## Sends a message to the user
def __sendTelegramMessage(apiKey, user, msg):
     bot = telegramBot.getBot(apiKey)
     bot.send_message(int(user), str(msg) )

# Generate email message for a given delegate
def __generateMessageForTelegram( delegate, user, currentTime, history):
    ## Delegate status
    if delegate['status'] is None:
        delegate['status'] = 'Not found'
    msg = "\nDelegate " + delegate['name'] + "\n Forging?=" + delegate['status'] + "\n\t"
    msg = msg + "Position: " + delegate['position'] + "\tUptime: " + delegate['uptime']
    return msg


## Generates a UTC Time
def generateUtcTime():
    now = datetime.utcnow()
    return str(now).split('.')[0]

## Generates GTM time with offset
def generateGtmTime(offset):
    now = datetime.utcnow() + timedelta(hours=offset)
    return str(now).split('.')[0]

## For each user of telegram, send message with notifications
def send_telegram_notifications (apiKey, userList, currentTime, gtmOffset, delegateStatus, history):

    for user in userList:
        #Cast to str
        userDir = str(user)
        msg = __generateMessageForTelegram( delegateStatus , userDir, currentTime, history)

        ### Send notification only if msgContent is available
        msgContent = "" + msg
        if msgContent != "":
            msgContent = "[ (GTM+" + str(gtmOffset) + ") " + generateGtmTime(gtmOffset) + ' ]\n' + msgContent
            try:
                __sendTelegramMessage(apiKey, user, msgContent)
            except:
                print("Cant send message for the user " + str(user))

