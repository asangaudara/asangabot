from telegram import *
from telegram.ext import *


bot = Bot("1534183615:AAGwgn4v235bwQm8yoIP0jn-mT1Dv37Vtos")
#print(bot.get_,me())
updater=Updater("1534183615:AAGwgn4v235bwQm8yoIP0jn-mT1Dv37Vtos" ,use_context=True):

dispatcher=updater.dispatcher

def test_function(update:Update,context:CallbackContext)
    bot.send_messaeg(

    	chat_id=update.effective_chat.id,
    	text="Hi I'm Asanga Udara How Are You")


start_value=CommandHandler('motion_detection',test_function)

dispatcher.add_handler(start_value)


updater.start_polling()