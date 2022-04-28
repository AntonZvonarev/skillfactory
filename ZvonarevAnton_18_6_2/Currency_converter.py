# Программа для определения стоимости заданного количества одной валюты в доугой выбираемой валюте
# Звонарев Антон, группа QAP-68

import telebot
from config import keys, TOKEN
from extensions import ConvertionException, CryptoConverter

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'help'])
def help(message: telebot.types.Message):
    text = 'Чтобы начать работу введите комманду боту в следующем формате: \n< имя валюты, цену которой Вы хотите узнать> \
    <имя валюты, в которой надо узнать цену первой валюты> \
    <количество первой валюты>\n\n \
    Пример: доллар рубль 10\n\n \
    Увидеть список доступных валют: /values'
    bot.reply_to(message, text)

@bot.message_handler(commands=['values'])
def values(message: telebot.types.Message):
    text = 'Доступные для рассчета валюты:'
    for key in keys.keys():
        text = '\n' .join((text, key,))
    bot.reply_to(message, text)

@bot.message_handler(content_types=['text', ])
def convert(message: telebot.types.Message):
    try:
        values = message.text.split(' ')

        if len(values) != 3:
            raise ConvertionException('Ошибка ввода праметров.')

        quote, base, amount = values
        total_base = CryptoConverter.get_price(quote, base, amount)
    except ConvertionException as e:
        bot.reply_to(message, f'Ошибка пользователя\n{e}.')

    except Exception as e:
        bot.reply_to(message, f'Не удалось обработать комманду\n{e}.')
    else:
        text = f'{amount} {quote} будет стоить {total_base: .2f}  {base}'
        bot.send_message(message.chat.id, text)

bot.polling(non_stop=False)