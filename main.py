import telegram
import datetime
import pytz
from telegram.ext import Updater, CommandHandler

TOKEN = "YOUR_TOKEN"


def start(update, context):
    user = update.message.from_user
    now = datetime.datetime.now()
    timezone = pytz.timezone("YOUR_TIMEZONE")
    now = timezone.localize(now)
    text = "Welcome!!\n\nYou requested your information on {} at {}.\n\nHere is the information that you have requested:\n\nHave a great day <3\n\nContact me here: https://wa.me/962791466699".format(now.strftime("%m/%d/%Y"), now.strftime("%I:%M %p"))
                                                                                                                                                                                                          
    context.bot.send_message(chat_id=update.effective_chat.id, text=text)
    text = ""
    if user.first_name:
        text += "First Name: {}\n".format(user.first_name)
    if user.last_name:
        text += "Last Name: {}\n".format(user.last_name)
    if user.language_code:
        text += "Language: {}\n".format(user.language_code)
    if user.id:
        text += "Chat ID: {}\n".format(user.id)
    context.bot.send_message(chat_id=update.effective_chat.id, text=text)

updater = Updater(TOKEN, use_context=True)

updater.dispatcher.add_handler(CommandHandler('start', start))

updater.start_polling()
updater.idle()
