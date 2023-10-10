import telebot
from telebot import types
token = '6582646182:AAEd-GYp7SuHlfK8V_vbRhzmbwcHCIDr198'

bot = telebot.TeleBot(token)
account_sid = 'AC70d6f507c0d4623a371c543281abcc3f'

# Define a password that users need to enter to start the chat
password = 'love'

# Dictionary to keep track of users who have entered the chat
authenticated_users = {}
user_menus = {}  # Dictionary to store user menus

@bot.message_handler(commands=['start'])
def start_message(message):
    if message.chat.id in authenticated_users:
        # User is already authenticated, continue chatting
        keyboard = telebot.types.ReplyKeyboardMarkup(row_width=3, resize_keyboard=True)
        keyboard.row('Test', 'Bye', 'Bot')
        keyboard.row('Start', 'Contact', 'Settings')
        bot.send_message(message.chat.id, 'Hello again!', reply_markup=keyboard)
    else:
        # User is not authenticated, request the password
        bot.send_message(message.chat.id, 'Please enter the password to start the chat:')



@bot.message_handler(func=lambda message: message.text == password)
def authenticate_user(message):
    # Password is correct, add the user to the authenticated users list
    authenticated_users[message.chat.id] = True
    keyboard = telebot.types.ReplyKeyboardMarkup(True)
    keyboard.row('Test', 'Bye', 'Bot', 'Start', 'Contact')
    bot.send_message(message.chat.id, 'Authentication successful! Hello!', reply_markup=keyboard)


@bot.message_handler(func=lambda message: message.text == 'Test' and message.chat.id in authenticated_users)
def start1_message(message):
    markup = telebot.types.InlineKeyboardMarkup()
    
    markup.add(telebot.types.InlineKeyboardButton(text='Three', callback_data=3))
    markup.add(telebot.types.InlineKeyboardButton(text='Four', callback_data=4))
    markup.add(telebot.types.InlineKeyboardButton(text='Five', callback_data=5))
    bot.send_message(message.chat.id, text="How much is 2 plus 2?", reply_markup=markup)
# menu text on bot
@bot.message_handler(func=lambda message: message.text == 'Bot' and message.chat.id in authenticated_users)
def start2_message(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton(text='Menu 1', callback_data='menu1'))
    markup.add(types.InlineKeyboardButton(text='Menu 2', callback_data='menu2'))
    bot.send_message(message.chat.id, text="Please choose a menu:", reply_markup=markup)

@bot.callback_query_handler(func=lambda call: True)
def callback_handler(call):
    if call.data == 'menu1':
        submenu_markup = types.InlineKeyboardMarkup()
        submenu_markup.add(types.InlineKeyboardButton(text='Submenu 1 Option 1', callback_data='submenu1_option1'))
        submenu_markup.add(types.InlineKeyboardButton(text='Submenu 1 Option 2', callback_data='submenu1_option2'))
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="You selected Menu 1. Please choose an option from the submenu:",
                              reply_markup=submenu_markup)
    elif call.data == 'menu2':
        submenu_markup = types.InlineKeyboardMarkup()
        submenu_markup.add(types.InlineKeyboardButton(text='Submenu 2 Option 1', callback_data='submenu2_option1'))
        submenu_markup.add(types.InlineKeyboardButton(text='Submenu 2 Option 2', callback_data='submenu2_option2'))
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="You selected Menu 2. Please choose an option from the submenu:",
                              reply_markup=submenu_markup)
    elif call.data == 'submenu1_option1':
        submenu1_option1_markup = types.InlineKeyboardMarkup()
        submenu1_option1_markup.add(types.InlineKeyboardButton(text='Submenu 1.1 Option 1', callback_data='submenu1_option1_1'))
        submenu1_option1_markup.add(types.InlineKeyboardButton(text='Submenu 1.1 Option 2', callback_data='submenu1_option1_2'))
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="You selected Submenu 1 Option 1. Please choose an option from the submenu:",
                              reply_markup=submenu1_option1_markup)
    elif call.data == 'submenu1_option2':
        submenu1_option2_markup = types.InlineKeyboardMarkup()
        submenu1_option2_markup.add(types.InlineKeyboardButton(text='Submenu 1.2 Option 1', callback_data='submenu1_option2_1'))
        submenu1_option2_markup.add(types.InlineKeyboardButton(text='Submenu 1.2 Option 2', callback_data='submenu1_option2_2'))
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="You selected Submenu 1 Option 2. Please choose an option from the submenu:",
                              reply_markup=submenu1_option2_markup)
    elif call.data == 'submenu2_option1':
        submenu2_option1_markup = types.InlineKeyboardMarkup()
        submenu2_option1_markup.add(types.InlineKeyboardButton(text='Submenu 2.1 Option 1', callback_data='submenu2_option1_1'))
        submenu2_option1_markup.add(types.InlineKeyboardButton(text='Submenu 2.1 Option 2', callback_data='submenu2_option1_2'))
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="You selected Submenu 2 Option 1. Please choose an option from the submenu:",
                              reply_markup=submenu2_option1_markup)
    elif call.data == 'submenu2_option2':
        submenu2_option2_markup = types.InlineKeyboardMarkup()
        submenu2_option2_markup.add(types.InlineKeyboardButton(text='Submenu 2.2 Option 1', callback_data='submenu2_option2_1'))
        submenu2_option2_markup.add(types.InlineKeyboardButton(text='Submenu 2.2 Option 2', callback_data='submenu2_option2_2'))
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="You selected Submenu 2 Option 2. Please choose an option from the submenu:",
                              reply_markup=submenu2_option2_markup)
    elif call.data == 'submenu1_option1_1':
        submenu1_option1_1_markup = types.InlineKeyboardMarkup()
        submenu1_option1_1_markup.add(types.InlineKeyboardButton(text='Submenu 1.1.1 Option 1', callback_data='submenu1_option1_1_1'))
        submenu1_option1_1_markup.add(types.InlineKeyboardButton(text='Submenu 1.1.1 Option 2', callback_data='submenu1_option1_1_2'))
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="You selected Submenu 1.1 Option 1. Please choose an option from the submenu:",
                              reply_markup=submenu1_option1_1_markup)
    elif call.data == 'submenu1_option1_2':
        submenu1_option1_2_markup = types.InlineKeyboardMarkup()
        submenu1_option1_2_markup.add(types.InlineKeyboardButton(text='Submenu 1.1.2 Option 1', callback_data='submenu1_option1_2_1'))
        submenu1_option1_2_markup.add(types.InlineKeyboardButton(text='Submenu 1.1.2 Option 2', callback_data='submenu1_option1_2_2'))
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="You selected Submenu 1.1 Option 2. Please choose an option from the submenu:",
                              reply_markup=submenu1_option1_2_markup)
    elif call.data == 'submenu1_option2_1':
        submenu1_option2_1_markup = types.InlineKeyboardMarkup()
        submenu1_option2_1_markup.add(types.InlineKeyboardButton(text='Submenu 1.2.1 Option 1', callback_data='submenu1_option2_1_1'))
        submenu1_option2_1_markup.add(types.InlineKeyboardButton(text='Submenu 1.2.1 Option 2', callback_data='submenu1_option2_1_2'))
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="You selected Submenu 1.2 Option 1. Please choose an option from the submenu:",
                              reply_markup=submenu1_option2_1_markup)
    elif call.data == 'submenu1_option2_2':
        submenu1_option2_2_markup = types.InlineKeyboardMarkup()
        submenu1_option2_2_markup.add(types.InlineKeyboardButton(text='Submenu 1.2.2 Option 1', callback_data='submenu1_option2_2_1'))
        submenu1_option2_2_markup.add(types.InlineKeyboardButton(text='Submenu 1.2.2 Option 2', callback_data='submenu1_option2_2_2'))
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="You selected Submenu 1.2 Option 2. Please choose an option from the submenu:",
                              reply_markup=submenu1_option2_2_markup)
    elif call.data == 'submenu2_option1_1':
        submenu2_option1_1_markup = types.InlineKeyboardMarkup()
        submenu2_option1_1_markup.add(types.InlineKeyboardButton(text='Submenu 2.1.1 Option 1', callback_data='submenu2_option1_1_1'))
        submenu2_option1_1_markup.add(types.InlineKeyboardButton(text='Submenu 2.1.1 Option 2', callback_data='submenu2_option1_1_2'))
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="You selected Submenu 2.1 Option 1. Please choose an option from the submenu:",
                              reply_markup=submenu2_option1_1_markup)
    elif call.data == 'submenu2_option1_2':
        submenu2_option1_2_markup = types.InlineKeyboardMarkup()
        submenu2_option1_2_markup.add(types.InlineKeyboardButton(text='Submenu 2.1.2 Option 1', callback_data='submenu2_option1_2_1'))
        submenu2_option1_2_markup.add(types.InlineKeyboardButton(text='Submenu 2.1.2 Option 2', callback_data='submenu2_option1_2_2'))
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="You selected Submenu 2.1 Option 2. Please choose an option from the submenu:",
                              reply_markup=submenu2_option1_2_markup)
    elif call.data == 'submenu2_option2_1':
        bot.send_message(call.message.chat.id, text="You selected Submenu 2.2 Option 1")
    elif call.data == 'submenu2_option2_2':
        bot.send_message(call.message.chat.id, text="You selected Submenu 2.2 Option 2")
    elif call.data == 'submenu2_option1_1_1':
        bot.send_message(call.message.chat.id, text="You selected Submenu 2.1.1 Option 1")
    elif call.data == 'submenu2_option1_1_2':
        bot.send_message(call.message.chat.id, text="You selected Submenu 2.1.1 Option 2")
    elif call.data == 'submenu2_option1_2_1':
        bot.send_message(call.message.chat.id, text="You selected Submenu 2.1.2 Option 1")
    elif call.data == 'submenu2_option1_2_2':
        bot.send_message(call.message.chat.id, text="You selected Submenu 2.1.2 Option 2")
    elif call.data == 'submenu1_option2_1_1':
        bot.send_message(call.message.chat.id, text="You selected Submenu 1.2.1 Option 1")
    elif call.data == 'submenu1_option2_1_2':
        bot.send_message(call.message.chat.id, text="You selected Submenu 1.2.1 Option 2")
    elif call.data == 'submenu1_option2_2_1':
        bot.send_message(call.message.chat.id, text="You selected Submenu 1.2.2 Option 1")
    elif call.data == 'submenu1_option2_2_2':
        bot.send_message(call.message.chat.id, text="You selected Submenu 1.2.2 Option 2")
    elif call.data == 'submenu1_option1_1_1':
            bot.send_message(call.message.chat.id, text="You selected Submenu 1.1.1 Option 1")
    elif call.data == 'submenu1_option1_1_1':
        bot.send_message(call.message.chat.id, text="You selected Submenu 1.1.2 Option 2")

@bot.message_handler(func=lambda message: message.text == 'Start' and message.chat.id in authenticated_users)
def exchange_command(message):
    keyboard = telebot.types.InlineKeyboardMarkup()
    keyboard.row(
        telebot.types.InlineKeyboardButton('USD', callback_data='get-USD')
    )
    keyboard.row(
        telebot.types.InlineKeyboardButton('EUR', callback_data='get-EUR'),
        telebot.types.InlineKeyboardButton('RUR', callback_data='get-RUR')
    )
    bot.send_message(message.chat.id, 'Click on the currency of choice:', reply_markup=keyboard)
    
@bot.message_handler(func=lambda message: message.text.lower() == 'bye' and message.chat.id in authenticated_users)
def send_text(message):
    bot.send_message(message.chat.id, 'Goodbye!')




@bot.callback_query_handler(func=lambda call: True)
def iq_callback(query):
    data = query.data
    if data.startswith('get-'):
        get_ex_callback(query)


def get_ex_callback(query):
    bot.answer_callback_query(query.id)
    send_exchange_result(query.message, query.data[4:])


def send_exchange_result(message, ex_code):
    bot.send_chat_action(message.chat.id, 'typing')


bot.polling()
