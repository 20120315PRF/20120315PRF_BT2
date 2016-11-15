#!/usr/bin/env python

##
## Core.py
## This file executes the workflow for the scrap bot
##

import time
import logging

from configuration.readConfig import read_config_file
from telegram.generate_telegrams import send_telegram_notifications
#from notification_filter import read_last_log
#from notification_filter import write_last_log
from rake import rake_delegate

# Configure log
logging.basicConfig(filename='out.log',format='[%(asctime)s -- %(levelname)s] %(message)s', level=logging.DEBUG)
logging.debug("Start reading config...")

# 1. Read the config file
configuration = read_config_file('configuration/botconfig.json')
logging.debug("Start reading config... OK")

# 2. Process the delegates one by one
logging.debug("Processing delegates...")
delegateStatus = rake_delegate.execute_rake_query_mock()
logging.debug("Processing delegates... OK")

# 3. Send telegram alarms
##Current time to compute notifications
current_time = time.time()
#history = read_last_log()

# 3.1. Send telegram alerts
send_telegram_notifications(configuration.get_telegram_token(), configuration.get_list_users(),
                            current_time, configuration.get_gtm(), delegateStatus,  [])

# 4.Write log of history
#write_last_log(delegateStatusList, currentTime)