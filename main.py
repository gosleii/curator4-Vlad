import telebot
import string
import re

from random import choice

bot = telebot.TeleBot('6841632503:AAHPZE7vs8QitaWTbVlc30bntpyXsvRm-3I')


@bot.message_handler(commands=['start', 'help'])
def start_message(message):
    bot.reply_to(message, f'Привет, {message.from_user.first_name}! Ты можешь воспользоваться командой /generate_password [длина пароля], \
        чтобы сгенерировать пароль. На этом пока всё, в дальнейшем бот будет развиваться')


@bot.message_handler(regexp=r'/generate_password (\d+)')
def generate_password(message):
    number = int(re.match(r'/generate_password (\d+)', message.text).group(1))
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join([choice(characters) for _ in range(number)])
    bot.reply_to(message, password)


@bot.edited_message_handler(content_types=['text'])
def edited_message_answer(message):
    bot.reply_to(message, 'Ага, сообщение изменил 😑')


if __name__ == "__main__":
    bot.polling(non_stop=True)