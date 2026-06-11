# Welccome To project Api Bot
# In this file, we created a chatbot so 
# that we can communicate with the API.

# imports
import telebot
import bot_token
import api

bot = telebot.TeleBot(bot_token.TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "به بات Arlo Movies خوش آمدید...")
    markup = telebot.types.InlineKeyboardMarkup(row_width=2)
    btn_1 = telebot.types.InlineKeyboardButton(text="جستجو با 🆔", callback_data="get_movie_by_id")
    btn_2 = telebot.types.InlineKeyboardButton(text="جستجو با اسم فیلم", callback_data="get_movie_by_name")
    btn_3 = telebot.types.InlineKeyboardButton(text="ارتباط با ما", callback_data="communication")
    
    markup.add(btn_1, btn_2, btn_3)
    bot.send_message(message.chat.id, "شما چه کمکی میخواهید؟", reply_markup=markup)

@bot.message_handler(commands=['help'])
def help(message):
    bot.reply_to(message, text="در صورت نیاز با پشتیبانی تماس بگیرید.")


@bot.message_handler(commands=['menu'])
def show_menu(messagae):
    markup = telebot.types.InlineKeyboardMarkup(row_width=2)
    btn_1 = telebot.types.InlineKeyboardButton(text="جستجو با 🆔", callback_data="get_movie_by_id")
    btn_2 = telebot.types.InlineKeyboardButton(text="جستجو با اسم فیلم", callback_data="get_movie_by_name")
    btn_3 = telebot.types.InlineKeyboardButton(text="ارتباط با ما", callback_data="communication")
    
    markup.add(btn_1, btn_2, btn_3)
    bot.send_message(messagae.chat.id, "شما چه کمکی میخواهید؟", reply_markup=markup)


@bot.callback_query_handler(func=lambda call:True)
def callback_query(call):
    if call.data == "get_movie_by_id":
        question = bot.send_message(call.message.chat.id, text="آیدی 🎬 بگو:")
        bot.register_next_step_handler(question, get_movie_by_id)
    
    elif call.data == "get_movie_by_name":
        question = bot.send_message(call.message.chat.id, text="اسم 🎬 بگو:")
        bot.register_next_step_handler(question, get_movie_by_moviename)

    elif call.data == "communication":
        markup = telebot.types.ReplyKeyboardMarkup(row_width=3, resize_keyboard=True)
        btn_4 = telebot.types.KeyboardButton(text="شماره تماس")
        btn_5 = telebot.types.KeyboardButton(text="ایمیل")
        markup.add(btn_4, btn_5)
        question = bot.send_message(call.message.chat.id, text="نحوه ارتباط با ما:", reply_markup=markup)
        bot.register_next_step_handler(question, communication)

def get_movie_by_id(message):
    movie_id = int(message.text)
    movie_info = api.get_info_movie_byid(movie_id)
    if movie_info == "Error":
        bot.reply_to(message, text="آیدی فیلم پیدا نشد.")
    else:
        title, country, year, imdb_rating = movie_info
        movie_info = f"Title: {title}\nCountry: {country}\nYear: {year}\nImdb Rating: {imdb_rating}"
        bot.reply_to(message, text=movie_info)
    show_menu(message)

def get_movie_by_moviename(message):

    movie_name = message.text
    movie_info = api.get_info_movie_moviename(movie_name)
    if movie_info == "Error":
        bot.reply_to(message, text="اسم فیلمو پیدا نکردم.")
    else:
        title, country, year, imdb_rating = movie_info
        movie = f"Title: {title}\nCountry: {country}\nYear: {year}\nImdb Rating: {imdb_rating}"
        bot.reply_to(message, movie)
    show_menu(message)

def communication(message):
    if message.text == "شماره تماس":
        number = "09382104800"
        info = f"Number Phone: {number}"
        bot.send_message(message.chat.id, text=info, reply_markup=telebot.types.ReplyKeyboardRemove())
    
    elif message.text == "ایمیل":
        email = "imthemhmd@gmail.com"
        info = f"Email: {email}"
        bot.send_message(message.chat.id, text=info, reply_markup=telebot.types.ReplyKeyboardRemove())
     
    show_menu(message)



if __name__ == "__main__":
    bot.infinity_polling()