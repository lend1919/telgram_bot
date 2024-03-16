from aiogram import types, F,Router
from aiogram.filters.command import Command
# import sys
# sys.path.insert(1,"less3/keyboards")
# sys.path.insert(1,"less3/utils")

from less3.keyboards.keyboard import kb1, kb2
from less3.utils.func import fox, quote, emoji

router = Router()

#Хэндлер на команду /start
@router.message(Command('start'))
async def cmd_start(message: types.Message):
    name = message.chat.first_name
    await message.answer(f'Привет, {name}', reply_markup=kb1)

#Хэндлер на команду /stop
@router.message(Command('stop'))
async def cmd_stop(message: types.Message):
    name = message.chat.first_name
    await message.answer(f'Пока, {name}')

@router.message(F.text.lower() == 'инфо')
@router.message(F.text.lower() == 'info')
@router.message(Command('info'))
async def cmd_info(message: types.Message):
    name = message.chat.first_name
    await message.answer(f'бот понимает и отвичает на следуюшие слова (привет,\nпока,\nлиса,\nfox,\nquote,\nцитаты из аниме,\nquotes from anime,\nэмодзи,\nemoji)')

#Хэндлер на команду /fox
@router.message(Command('fox'))
@router.message(Command('лиса'))
@router.message(F.text.lower() == 'покажи лису')
async def cmd_fox(message: types.Message):
    name = message.chat.first_name
    img_fox = fox()
    await message.answer(f'Держи лису, {name}')
    await message.answer_photo(photo=img_fox)
  
@router.message(Command('quote'))
@router.message(Command('цитаты'))
@router.message(F.text.lower() == 'Цитаты ')
async def cmd_quote(message: types.Message):
    result = quote()
    character = result["character"]
    quote_text = result["quote"]
    anime_name = result["anime"]
    await message.answer(f"Anime - {anime_name},\ncharacter - {character},\nQuote - {quote_text}")
    
@router.message(Command('emoji'))
@router.message(Command('эмодзи'))
async def cmd_emoji(message: types.Message):
    name = message.chat.first_name
    result = emoji()

    for code in result.get('htmlCode'):
        await message.answer(code,parse_mode="html")
    # await bot.send_photo(message.from_user.id, photo=img_fox)

# @router.message(Command("брось кость"))
# async def cmd_dice(message: types.Message):

# Отправка сообщения с опис

#Хендлер на сообщения
@router.message(F.text)
async def msg_echo(message: types.Message):
    msg_user = message.text.lower()
    name = message.chat.first_name
    if 'привет' in msg_user:
        await message.answer(f'Ну-привет, {name}')
    elif 'start' in msg_user:
        await message.answer(f'start, {name}')
    elif 'пока' == msg_user:
        await message.answer(f'Пока-пока, {name}')
    elif 'брось кость' in msg_user:
        await message.answer_dice(emoji="🎲")
    elif 'лиса' in msg_user or  "fox" in msg_user:
        await message.answer(f'Смотри что у меня есть, {name}', reply_markup=kb2)
    elif 'цитаты из аниме' in msg_user or  "quotes from anime" in msg_user or  'цитаты' in msg_user  or  'quote' in msg_user :
    # elif F.text.lower() in ('quote', 'цитаты', 'цитаты из аниме',"quotes from anime"):
        result = quote()
        character = result["character"]
        quote_text = result["quote"]
        anime_name = result["anime"]
        await message.answer(f"Anime - {anime_name},\ncharacter - {character},\nQuote - {quote_text}")
    elif 'emoji' in msg_user or  "эмодзи" in msg_user:
            result = emoji()
            for code in result.get('htmlCode'):
                await message.answer(code,parse_mode="html")
    else:
        await message.answer(f'Я не знаю такого слова!!!!')