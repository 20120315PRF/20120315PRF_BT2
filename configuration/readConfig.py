import json
import os.path
import logging

## Class that mantains the configuration
class Configuration:

    ## Config parameters parsed here
    _gtm = 0
    _telegramToken = None
    _listUsers = None

    def __init__(self):
        self._telegramToken = ""
        self._listUsers = []
        self._gtm = 0

    def getTelegramToken(self):
        if self._telegramToken is not None:
            return self._telegramToken
        else:
            return ""

    # Get the list of users
    def getListUsers(self):
        if self._listUsers is not None:
            return self._listUsers
        else:
            return []

    # Get GTM offset
    def getGtm(self):
        if not self._gtm is None:
            return self._gtm
        else:
            return 0

##Function that return a configuration object
def readConfigFile(filename):

    if not os.path.exists(filename):
        logging.error("Configuration file %s does not exists", filename)
        raise Exception("config.json file does not exists")

    configFile = open(filename, 'r')
    fileContent = configFile.read()
    configFile.close()

    objectJson = json.loads(fileContent)

    #extract the from file
    configuration = Configuration()
    configuration._telegramToken = objectJson['telegram']['token']
    objectJson['telegram'].pop('token', None)

    # Process users to notify
    listUsers = objectJson['telegram']['listUsers']
    configuration._listUsers = objectJson['telegram']['listUsers']
    # GTM offset
    if 'GTM' in objectJson:
        configuration._gtm = objectJson['GTM']

    return configuration

