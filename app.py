from chat_bot import bot_reply
from time import sleep
import os
# from chat_bot import bot_reply

import logging

from telegram import Update
import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)

def echo(update: Update, context: CallbackContext) -> None:
    """Reply the user's message."""
    print(update)
    context.bot.send_message(chat_id=update.message.chat.id,text=bot_reply(update.message.text),reply_to_message_id=update.message.message_id)


def main():
    """Start the bot."""
    # Create the Updater and pass it your bot's token.
    # Make sure to set use_context=True to use the new context based callbacks
    # Post version 12 this will no longer be necessary
    updater = Updater("1299217256:AAEvZr48ixCv-Kt-zpvbPT2BRKhB4wt3uyM", use_context=True)

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    # on noncommand i.e message - echo the message on Telegram
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()
