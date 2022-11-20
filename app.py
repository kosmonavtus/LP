from telegram.ext import Updater, CommandHandler

def greet_user(update, context):
    update.message.reply_text('ТЫ ПИДОР')


def main():
    mybot = Updater('5621425346:AAHKZKfz5sYdQyLNF8UZUvhgmIGnK_ZfMF8')

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler('start', greet_user))

    mybot.start_polling()
    mybot.idle()


main()