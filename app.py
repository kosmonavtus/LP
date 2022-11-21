from telegram.ext import Updater, CommandHandler

def greet_user(update, context):
    update.message.reply_text('играет музыка из бара "голубая устрица" ')


def main():
    mybot = Updater(token)

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler('start', greet_user))

    mybot.start_polling()
    mybot.idle()


main()