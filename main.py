import config
import cybersport
from bot import BotHandler as bot_handler

bot = bot_handler(config.token)


def main():
    is_first = True
    message_id = 0

    while True:
        last_update = bot.get_last_update()
        bot_info = bot.get_me()
        bot_name = bot_info['username']

        try:
            last_chat_id = last_update['message']['chat']['id']
            last_chat_text = last_update['message']['text']
            last_message_id = last_update['message']['message_id']

            if is_first or message_id != last_message_id:
                is_first = False
                message_id = last_message_id

                if last_chat_text == "/get_matches" or last_chat_text == "/get_matches@"+bot_name:
                    response_message = cybersport.get_matches_info()
                    bot.send_message(last_chat_id, response_message)
        except KeyError:
            continue


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        exit()
