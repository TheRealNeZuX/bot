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
import youtube_dl
import os
import time
import json

#bot data
bot=aiogram.Bot(config.TOKEN)
dp=aiogram.Dispatcher(bot)
disable=False

#start
@dp.message_handler(commands="start")
async def start(msg):
    global disable
    await msg.answer("Привет, я бот для скачивания видео с ютуб, напиши мне /help")
    data=json.load(open("data.json", "r"))
    if msg.from_user.id not in data["UserID"]:
        data["UserID"].append(msg.from_user.id)
        with open("data.json", "w") as f:
            json.dump(data, f)
        for i in data["AdminID"]:
            await bot.send_message(i, f"User {msg.from_user.first_name} started", disable_notification=disable)

#help
@dp.message_handler(commands="help")
async def help(msg):
    await msg.answer("Напиши сообщение типа:")
    time.sleep(1)
    await msg.answer("/download https://www.youtube.com/watch?v=vgUOhL0MtfY")
    time.sleep(1)
    await msg.answer("Если видео не скачалось то либо подождите, либо оно весит слишком много(его длина должна быть~10 мин)")

#download
@dp.message_handler(commands="download")
async def text(msg):
    url=msg.text.split("/download ")[1]
    name=msg.from_user.id
    path = os.path.join(os.path.abspath(os.path.dirname(__file__)), f'{name}.mp4')
    opts={'outtmpl': path}
    with youtube_dl.YoutubeDL(opts) as ydl:
        await msg.answer("Ждите🔮")  
        ydl.download([url]) 
    try:
        with open(path, "rb") as f:
            await msg.answer_video(f) 
    except:
        await msg.answer("Простите, telegram не позволяет отправлять такие тяжёлые видео, но я с удовольствием скачаю видео длиною ~ 10 мин🥶")
    os.remove(path)

#notification
@dp.message_handler(commands="notification")
async def notification(msg):
    turn=msg.text.split("/notification ")[1]
    global disable
    if msg.from_user.id in json.load(open("data.json","r"))["AdminID"]:
        if turn=="off":
            disable=True
            await msg.answer("Уведомления отключены")
        else:
            disable=False
            await msg.answer("Уведомления включены")

#usersID
@dp.message_handler(commands="users")
async def users(msg):
    if msg.from_user.id in json.load(open("data.json","r"))["AdminID"]:
        data=json.load(open("data.json", "r"))
        data="  ".join(map(str, data["UserID"]))
        await msg.answer(data)

#text
@dp.message_handler(content_types=aiogram.types.ContentTypes.TEXT)
async def txt(msg):
    await msg.answer("Я тебя не понял, напиши /help")


#sticker
@dp.message_handler(content_types=aiogram.types.ContentTypes.STICKER)
async def stiker(msg):
    await msg.answer(f"🆔:\n{msg.sticker.file_id}")


#circle
aiogram.executor.start_polling(dp, skip_updates=True)
