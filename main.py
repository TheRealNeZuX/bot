###################################################
#   L               EeEeEeEeE       OOOOOOO       #
#   L               E              O       O      #
#   L               E             O         O     #
#   L               EeEeEeEeE     O         O     #
#   L               E             O         O     #
#   L               E              O       O      #
#   LlLlLlLlLlL     EeEeEeEeE       OOOOOOO       #
###################################################
import aiogram
import config
import downloader
import lang
import buttons
import time

#bot_data
bot=aiogram.Bot(config.TOKEN)
dp=aiogram.Dispatcher(bot)

langu="ru"
BUTTON=buttons.Buttons(langu)

#start
@dp.message_handler(commands="start")
async def start(msg):
    await msg.answer(lang.data[langu]["messages"]["start"], reply_markup=BUTTON.SETTINGSkb)
    if msg.from_user.id not in config.admins:    
        for i in config.admins:
            await bot.send_message(i, f"Пользователь {msg.from_user.first_name} c ID={msg.from_user.id} присоединился, или настолько тупой, что нажал старт ещё раз")
#help
@dp.message_handler(commands="help")
async def help(msg):
    await msg.answer(lang.data[langu]["messages"]["help"]["1"])
    time.sleep(1)
    await msg.answer("/download [url]\n{}".format(lang.data[langu]["messages"]["help"]["2"]))

#download
@dp.message_handler(commands="download")
async def download(msg):
    try:
        await msg.answer(lang.data[langu]["messages"]["download"]["magic"])
        url=msg.text.split("/download ")[1]
        video=downloader.Video(url=url, name=f"{msg.chat.id}.mp4")
        await video.download()
        with open(f"{msg.chat.id}.mp4", "rb") as f:
            await msg.answer_video(f)
        await video.remove()
    except:
        await msg.answer(lang.data[langu]["messages"]["download"]["Error"])
#settings
@dp.message_handler(commands="settings")
async def settings(msg):
    await msg.answer("настройки/settings", reply_markup=BUTTON.SETTINGSinline)

#text
@dp.message_handler(content_types="text")
async def text(msg):
    if :
        match msg.text:
            case "настройки⚙️":
                await settings(msg)
            case "settings⚙️":
                await settings(msg)
            case _&msg.chat.id!=-1001523431192:
                await msg.answer(lang.data[langu]["messages"]["understanding"])

@dp.callback_query_handler(lambda text: text.data=="back")
async def back(msg):
    await msg.message.edit_text("Настройки\nSettings", reply_markup=BUTTON.SETTINGSinline)

@dp.callback_query_handler(lambda text: text.data=="language")
async def language(msg):
    await msg.message.edit_text(f"Язык|Language\nТвой язык - {langu}\nYour lang is {langu}", reply_markup=BUTTON.LANGUAGE)

@dp.callback_query_handler(lambda text: text.data=="RU")
async def RU(msg):
    try:
        global langu
        langu="ru"
        BUTTON.edit(langu)
        await msg.message.edit_text(f"Язык|Language\nТвой язык - {langu}\nYour lang is {langu}", reply_markup=BUTTON.LANGUAGE)
        await msg.answer("Твой язык - Русский🇷🇺")
    except:
        await msg.answer("Русский язык уже стоит")

@dp.callback_query_handler(lambda text: text.data=="EN")
async def RU(msg):
    try:
        global langu
        langu="en"
        BUTTON.edit(langu)
        await msg.message.edit_text(f"Язык|Language\nТвой язык - {langu}\nYour lang is {langu}", reply_markup=BUTTON.LANGUAGE)
        await msg.answer("Your lang is English🇬🇧")
    except:
        await msg.answer("This language already stands")

@dp.callback_query_handler(lambda text: text.data=="donate")
async def language(msg):
    await msg.message.edit_text(f"Ты можешь задонатить мне🤑, или подписаться в Youtube❤️\n\n\n You can give me some money🤑, or subscribe me in Youtube❤️", reply_markup=BUTTON.DONATE)


aiogram.executor.start_polling(dp, skip_updates=False)
