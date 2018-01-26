# -*- coding: utf-8 -*-

import config
import cybersport
import utils

import telebot
from telebot import types

bot = telebot.TeleBot(config.token)


@bot.message_handler(commands=['get_matches'])
def command_get_matches(message):
    response_message = utils.replace_time_with_local(cybersport.get_matches_info())
    bot.send_message(message.chat.id, response_message)


@bot.inline_handler(func=lambda query: query.query == "get")
def query_text(query):
    matches_list = types.InlineQueryResultArticle(
        id='1', title="Матчи Dota 2",
        description="Список будущих матчей",
        input_message_content=types.InputTextMessageContent(message_text=cybersport.get_matches_info())
    )
    bot.answer_inline_query(query.id, [matches_list])


if __name__ == '__main__':
    bot.polling(none_stop=True)
