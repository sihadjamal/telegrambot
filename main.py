import logging
import requests
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# Enable logging (optional but recommended)
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

logger = logging.getLogger(__name__)

# Function to fetch Quote of the Day from a free API
def get_quote_of_the_day():
    try:
        response = requests.get("https://quotes.rest/qod?language=en")
        data = response.json()
        quote = data['contents']['quotes'][0]['quote']
        author = data['contents']['quotes'][0]['author']
        return f'"{quote}"\n— {author}'
    except Exception as e:
        logger.error(f"Error fetching quote: {e}")
        return "Sorry, I couldn't retrieve the quote at the moment."

# Command handler for /quote
async def quote(update: Update, context: ContextTypes.DEFAULT_TYPE):
    quote_text = get_quote_of_the_day()
    await update.message.reply_text(quote_text)

# Main function to run the bot
async def main():
    # Replace 'YOUR_BOT_TOKEN' with your actual bot token
    app = ApplicationBuilder().token("7888772610:AAFL3Le8_6CQxqCHs4bfWlDU9KJ2m8GNb6U").build()

    app.add_handler(CommandHandler("quote", quote))

    print("Bot is running...")
    await app.run_polling()

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
