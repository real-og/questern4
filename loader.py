from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.contrib.fsm_storage.redis import RedisStorage2
import logging
import os


logging.basicConfig(level=logging.WARNING)
ADMIN_IDS = str(os.environ.get('ADMIN_IDS')).split(',')
BOT_TOKEN = str(os.environ.get('BOT_TOKEN'))
SHEET_LINK = str(os.environ.get('SHEET_LINK'))


# storage = RedisStorage2(db=1)
storage = MemoryStorage()

bot = Bot(token=BOT_TOKEN, parse_mode="HTML")
dp = Dispatcher(bot, storage=storage)