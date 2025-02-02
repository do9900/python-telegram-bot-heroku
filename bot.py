# Imports Packages
import logging
import os
import sys

# Imports Modules
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from telegram.parsemode import ParseMode
# Start Project
PORT = int(os.environ.get('PORT', 5000))

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)
TOKEN = '1765966528:AAFyQC9yHoScAQBgtxwLU4EHx1auQOw_I1g'


# Define a few command handlers. These usually take the two arguments bot and
# context. Error handlers also receive the raised TelegramError object in error.

# def me(update, context):
#     print(context)
#     context.bot.send_message(update.message.chat_id, text='Your information:\n{}'.format(update.effective_user))



def start(update, context):
    """Send a message when the command /start is issued."""
    USER = update.effective_user.first_name
    print("USER: ",USER)
    sys.stdout.flush()
    if len(context.args) > 0:
        key = context.args[0]
        SITE = 'CRIPTOMONEDA SITE'
        URL_SITE = 'https://www.urlcriptomoneda.com/{}/'.format(key)
        context.bot.send_message(
            chat_id=update.effective_chat.id,
            text=
            "Bienvenido, {0}. Este mensaje es para confirmar tu acceso a \
             nuestra plataforma <b>{1}</b>. Abre el link para completar el acceso: \
            <a href='{2}'>{2}</a>.<pre>\n</pre>\
            Importante: <pre>\n</pre>\
            - <b>¡No le envíes a nadie este enlace, será bajo tu responsabilidad!</b><pre>\n</pre> \
            - Recuerda que el enlace expira en 3 minutos.".format(USER,SITE, URL_SITE),
            parse_mode=ParseMode.HTML,
        )
    else:
        update.message.reply_text('¡Bienvenido, {}'.format(USER))

def site(update, context):
    URL_SITE = 'https://www.urlcriptomoneda.com/'
    context.bot.send_message(
            chat_id=update.effective_chat.id,
            text=
            "Nuestro sitio es \
            <a href='{0}'>\
            {0}</a>.".format(URL_SITE),
            parse_mode=ParseMode.HTML,
        )

def help(update, context):
    print("HELP!")
    sys.stdout.flush()
    """Send a message when the command /help is issued."""
    context.bot.send_message(update.message.chat_id, text='¡Lo siento!, seguimos en desarrollo.')
    # update.message.reply_text('Help!')

def echo(update, context):
    """Echo the user message."""
    update.message.reply_text(update.message.text)

def error(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)

def main():
    """Start the bot."""
    # Create the Updater and pass it your bot's token.
    # Make sure to set use_context=True to use the new context based callbacks
    # Post version 12 this will no longer be necessary
    updater = Updater(TOKEN, use_context=True)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    # dp.add_handler(CommandHandler("validation", validation))
    dp.add_handler(CommandHandler("sitio", site))
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))
    # dp.add_handler(CommandHandler("me", me))

    # on noncommand i.e message - echo the message on Telegram
    dp.add_handler(MessageHandler(Filters.text, echo))

    # log all errors
    dp.add_error_handler(error)

    # Start the Bot
    # updater.start_polling()
    updater.start_webhook(listen="0.0.0.0",
                          port=int(PORT),
                          url_path=TOKEN)
    updater.bot.setWebhook('https://bot-telegram031.herokuapp.com/' + TOKEN)

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()
    
# UNCOMMENT
# if __name__ == '__main__':
#     main()

#  web: python3 bot.py