# http://nikovit.ru/blog/pishem-bota-peresylki-soobshcheniy-iz-vk-v-telegram-na-python/

import os
import sys
import vk_api
import telebot
import configparser
import logging
from telebot.types import InputMediaPhoto

config_path = os.path.join(sys.path[0], 'settings.ini')
config = configparser.ConfigParser()
config.read(config_path)

COUNT     = config.get('VK', 'COUNT')
DOMAIN    = config.get('VK', 'DOMAIN')
BOT_TOKEN = config.get('Telegram', 'BOT_TOKEN')
CHANNEL   = config.get('Telegram', 'CHANNEL')

bot = telebot.TeleBot(BOT_TOKEN)