import json
import os.path
import logging

## Class that mantains the configuration
class Configuration:

    ## Config parameters parsed here
    _gtm = 0
    _telegram_token = None
    _list_users = None

    def __init__(self):
        self._telegram_token = ""
        self._list_users = []
        self._gtm = 0

    def get_telegram_token(self):
        if self._telegram_token is not None:
            return self._telegram_token
        else:
            return ""

    # Get the list of users
    def get_list_users(self):
        if self._list_users is not None:
            return self._list_users
        else:
            return []

    # Get GTM offset
    def get_gtm(self):
        if not self._gtm is None:
            return self._gtm
        else:
            return 0

##Function that return a configuration object
def read_config_file(filename):

    if not os.path.exists(filename):
        logging.error("Configuration file %s does not exists", filename)
        raise Exception("config.json file does not exists")

    config_file = open(filename, 'r')
    file_content = config_file.read()
    config_file.close()

    object_json = json.loads(file_content)

    #extract the from file
    configuration = Configuration()
    configuration._telegram_token = object_json['telegram']['token']
    object_json['telegram'].pop('token', None)

    # Process users to notify
    list_users = object_json['telegram']['listUsers']
    configuration._list_users = object_json['telegram']['listUsers']
    # GTM offset
    if 'GTM' in object_json:
        configuration._gtm = object_json['GTM']

    return configuration

