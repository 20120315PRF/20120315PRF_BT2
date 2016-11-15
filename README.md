# Delegate Telegram Bot v1

Telegram bot that generates notifications to subscribed telegram users, giving information about the delegate node. This bot is executed every 15 minutes, checking the node status with Lisk Rake and notifying subscribed users which are configured on the configuration file.

# Pre-requisites
To use this bot, you will need the next features:
  - Lisk node (of course) running on **Unix** System
  - Lisk Rake **must be installed and running** on node machine
  - Python 2.7 installed
  - Telegram user to be notificated

# How to install
Open a terminal on your machine and go to the rake's path. Then, download the bot.

```sh
$ cd lisk-rake
$ git clone https://github.com/20120315PRF/20120315PRF_BT2.git
```

Create and subscribe to the bot. Check the next link to create a bot. 

TODO: write here how to create a bot on telegram

Copy the API Key on the config file. 

blablablablabla TODO: complete the configuration
```sh
$ cd 20120315PRF_BT2/telegram
$ python telegram_bot_register.py
```


Test that the bot is working

```sh
$ cd 20120315PRF_BT2
$ python core.py
```

If it's all right, you can schedule the execution by executing the next command:

```sh
$ */15 * * * * /path/to/command TODO: write the correct command here
```
