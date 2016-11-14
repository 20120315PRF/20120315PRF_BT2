##
## Core.py
## This file executes the workflow for the scrap bot
##

import time
import logging

from configuration.readConfig import readConfigFile
from telegram.generate_telegrams import send_telegram_notifications
from notification_filter import readLastLog
from notification_filter import writeLastLog
from rake import rake_delegate

# Configure log
logging.basicConfig(filename='out.log',format='[%(asctime)s -- %(levelname)s] %(message)s', level=logging.DEBUG)
logging.debug("Start reading config...")

# 1. Read the config file
configuration = readConfigFile('configuration/botconfig.json')
logging.debug("Start reading config... OK")

# 2. Process the delegates one by one
logging.debug("Processing delegates...")
delegateStatus = rake_delegate.executeRakeQuery()
logging.debug("Processing delegates... OK")

# 3. Send telegram alarms
##Current time to compute notifications
currentTime = time.time()
#history = readLastLog()

# 3.1. Send telegram alerts
send_telegram_notifications(configuration.getTelegramToken(), configuration.getListUsers(),
                            currentTime, configuration.getGtm(), delegateStatus,  [])


# 4.Write log of history
#writeLastLog(delegateStatusList, currentTime)

#print(delegateStatusList)