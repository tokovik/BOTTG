import requests
import dotenv
import os
from telegram import ReplyKeyboardMarkup
from telegram.ext import CommandHandler, Updater

dotenv.load_dotenv()
secret_token = os.getenv('TOKEN')

def wake_up(update, context):
    chat = update.effective_chat
    name = update.message.chat.first_name
    buttons = ReplyKeyboardMarkup([['hello', 'help']],
                                  resize_keyboard=True)
    context.bot.send_message(
        chat_id=chat.id,
        text=f'Привет, {name}',
        reply_markup=buttons
    )

def help_me(update, context):
    chat = update.effective_chat
    context.bot.send_message(
        chat_id=chat.id,
        text='Вы вызвали справку, как пользоваться системой'
    )


def get_new_image():
    URL = 'https://api.thecatapi.com/v1/images/search'
    try:
        response = requests.get(URL)
    except Exception as error:
        new_url = 'https://api.thedogapi.com/v1/images/search'
        response = requests.get(new_url)

    response = response.json()
    random_cat = response[0].get('url')
    return random_cat


def hello(update, context):
    chat = update.effective_chat
    context.bot.send_photo(chat.id, get_new_image())


def my_func():
    updater = Updater(token=secret_token)
    updater.dispatcher.add_handler(CommandHandler('/start', wake_up))
    updater.dispatcher.add_handler(CommandHandler('/help', help_me))
    updater.dispatcher.add_handler(CommandHandler('/hello', hello))
    
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    my_func()
