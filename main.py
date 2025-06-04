from telegram.ext import Updater, CommandHandler

def start(update, context):
    update.message.reply_text('Hello!')

def main():
    updater = Updater("7888772610:AAFL3Le8_6CQxqCHs4bfWlDU9KJ2m8GNb6U", use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
