from Adafruit_IO import Client
from telegram.ext import Updater,MessageHandler,Filters

def demo1(bot,update):
  chat_id = bot.message.chat_id
  path= 'https://previews.123rf.com/images/murika/murika1511/murika151100069/48123160-bright-glowing-incandescent-light-bulb-on-a-white-background.jpg'
  bot.message.reply_text('Light Turned ON')
  update.bot.sendPhoto(chat_id=chat_id,photo=path)
def demo2(bot,update):
  chat_id = bot.message.chat_id
  path= 'https://previews.123rf.com/images/ericmilos/ericmilos0912/ericmilos091200136/6109526-3d-render-of-light-bulb-on-white.jpg'
  bot.message.reply_text('Light Turned OFF')
  update.bot.sendPhoto(chat_id=chat_id,photo=path)
def demo3(bot,update):
  chat_id = bot.message.chat_id
  path= 'https://thumbs.dreamstime.com/b/spinning-gray-ceiling-fan-picture-summer-134473260.jpg'
  bot.message.reply_text('Fan Turned ON')
  update.bot.sendPhoto(chat_id=chat_id,photo=path)
def demo4(bot,update):
  chat_id = bot.message.chat_id
  path= 'https://images-na.ssl-images-amazon.com/images/I/412QHDSQB1L._SL1000_.jpg'
  bot.message.reply_text('Fan Turned OFF')
  update.bot.sendPhoto(chat_id=chat_id,photo=path)
def func1(bot,update):
  a=bot.message.text.lower()
  a = a.split()
  if 'on'in a:
    if 'light' in a:
       demo1(bot,update)
       aio.send('light', 1)
    elif 'fan' in a:
       demo3(bot,update)
       aio.send('fan', 1)
  elif 'off'in a:
     if 'light' in a:
       demo2(bot,update)
       aio.send('light', 0)
     elif 'fan' in a:
       demo4(bot,update)
       aio.send('fan', 0)
  else:
    bot.message.reply_text('invalid text')

aio = Client('harsh_thummar', 'aio_yTGF69Rxg7HXChvpbYQSed48fvoc')
BOT_TOKEN = '1946645481:AAHtWnIjIbO6w7gz8SryKB3ya8KePDBqJT0'
u = Updater(BOT_TOKEN,use_context=True)
dp = u.dispatcher
dp.add_handler(MessageHandler(Filters.text,func1))
u.start_polling()
u.idle()
