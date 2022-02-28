import telebot, requests
from bs4 import BeautifulSoup

bot = telebot.TeleBot("BOT_TOKEN") 
tegtext = "By: @Unknown_26_04"

@bot.message_handler(commands=['start','START','Start'])
def start(message):
    bot.send_message(message.chat.id,f"Assalomu Alaykum <a href='tg://user?id={message.from_user.id}'>{message.from_user.first_name}</a>!\n\nUshbu bot orqali ismlarning ma'nosini bilib olishingiz mumkin!\n\nBuning uchun menga ism jo'nating va men sizga uni ma'nosini jo'nataman!",
    parse_mode='html')

@bot.message_handler(content_types=['text'])
def ism(message):
        try:
            url = requests.get(f"https://ismlar.com/search/{message.text}")
            soup = BeautifulSoup(url.text,'lxml')
            mano = soup.find('p',class_='text-size-5').text
            bot.reply_to(message,f"<b>🔎Ism:</b> {message.text}\n\n<b>📑 Ma'nosi:</b> <code>{mano}</code>\n\n{tegtext}",
            parse_mode='html')
        except:
            bot.reply_to(message,f"{message.text} ism mano'si topilmadi.Ismni to'g'ri yozganingizga ishonch xosil qiling!")

bot.polling()
