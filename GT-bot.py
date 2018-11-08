from googletrans import Translator
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
# configure the bot 
update = Updater('487419783:AAE4wEp4nO901cWoRYV9aptO9yMc5GoAIQ8')

def start_method(bot, update):
    chat_id = update.message.chat_id
    bot.sendMessage(chat_id, "Translate bot  C0d3r >> @Evmo83 \n send me Your Text to I Translate that !")
    
def translate_method(bot, update):
    chat_id = update.message.chat_id
    user_text = update.message.text
    lang = Translator().detect(user_text).lang
    if lang == 'fa':
        transed = Translator().translate(user_text, dest='en').text
        bot.sendMessage(chat_id, transed)
    elif lang == 'en':
        transed = Translator().translate(user_text, dest='fa').text
        bot.sendMessage(chat_id, transed)
        
# adding handlers
start = CommandHandler("start", start_method)
tran = MessageHandler(Filters.text, translate_method)
update.dispatcher.add_handler(start)
update.dispatcher.add_handler(tran)
# configuring Shell >>
update.start_polling()
update.idle()
