import logging
from transliterate import to_cyrillic,to_latin
from aiogram import Bot,Dispatcher,executor,types
from checkWord import checkWord
from imlo import translit
from transliterate import to_latin, to_cyrillic

API_TOKEN='5866856954:AAHqweTaSVRYJXEQyX5OU7pqaUe-GcNAsw0'
logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands="start")
async def send_welcome(message:types.Message):
    await message.reply('Assalomu Alaykum Imlo botiga Xush kelibsiz!')
    await message.answer("Botdan foydalanish uchun so'z yuboring")

@dp.message_handler(commands='help')
async def help_user(message:types.Message):
    await message.reply("Botdan foydalanish uchun so'z yuboring")

@dp.message_handler()
async def checkImlo(message:types.Message):
    # matn = message.text
        word = message.text
        word2=message.text.isascii()

        if word2:
            result = checkWord(to_cyrillic(word))
            if result['available']:
                 response=f'✅ {word.capitalize()}'
            else:
                 response=f'❌ {word.capitalize()}\n'
                 for text in result['matches']:
                   response+= f'✅ {text.capitalize()}\n'
            await message.answer(translit(response))
        else:
            result = checkWord(word)
            if result['available']:
              response = f'✅ {word.capitalize()}'
            else:
              response = f'❌ {word.capitalize()}\n'
              for text in result['matches']:
                 response += f'✅ {text.capitalize()}\n'
            await message.answer(response)


if __name__=='__main__':
    executor.start_polling(dp, skip_updates=True)


# def translit(message):
#     msg = message.text
#     javob = lambda msg: to_cyrillic(msg) if msg.isascii() else to_latin(msg)
#     return javob


# bot.polling()