from aiogram import types

button1 = types.KeyboardButton(text='start')
button2 = types.KeyboardButton(text='info')
button3 = types.KeyboardButton(text='Покажи лису')

keyboard1 = [
    [button1, button2],
    [button3]
]

keyboard2 = [
    [button3],
]

kb1 = types.ReplyKeyboardMarkup(keyboard=keyboard1, resize_keyboard=True)
kb2 = types.ReplyKeyboardMarkup(keyboard=keyboard2, resize_keyboard=True)