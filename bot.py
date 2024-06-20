import telebot
from config import TOKEN
from extensions import APIException, CurrencyConverter

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    text = "Welcome to the currency converter bot!\n" \
           "To use, send a message in the format: \n" \
           "<currency_from> <currency_to> <amount>\n" \
           "Example: usd eur 100\n" \
           "Available commands:\n" \
           "/start or /help - Instructions\n" \
           "/values - List of available currencies"
    bot.reply_to(message, text)

@bot.message_handler(commands=['values'])
def send_values(message):
    text = "Available currencies:\nUSD, EUR, RUB"
    bot.reply_to(message, text)

@bot.message_handler(content_types=['text'])
def handle_conversion(message):
    try:
        values = message.text.split()
        if len(values) != 3:
            raise APIException("Invalid number of parameters. Use the format: <currency_from> <currency_to> <amount>")

        base, quote, amount = values
        total_amount = CurrencyConverter.get_price(base, quote, amount)
        text = f"The price of {amount} {base.upper()} in {quote.upper()} is {total_amount:.2f}"
        bot.reply_to(message, text)
    except APIException as e:
        bot.reply_to(message, f"Error: {e}")
    except Exception as e:
        bot.reply_to(message, f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    bot.polling()
