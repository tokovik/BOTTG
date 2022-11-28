import dotenv
import os
from telegram import ReplyKeyboardMarkup
from telegram.ext import CommandHandler, Updater

dotenv.load_dotenv()
secret_token = os.getenv('TOKEN')

def my_func():
    updater = Updater(token=secret_token)
    


if __name__ == '__main__':
    # my_func()
    print(secret_token)
