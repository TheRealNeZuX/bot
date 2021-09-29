import aiogram
import config
import youtube_dl
import os
import time

#bot data
bot=aiogram.Bot(config.TOKEN)
dp=aiogram.Dispatcher(bot)
#text status: 0-text, 1-download


@dp.message_handler(commands=["start"])
async def start(msg):
    await msg.answer("Привет, я бот для скачивания видео с ютуб, напиши мне /help")
    for i in config.AdminID:
        await bot.send_message(i, f"Пользователь {msg.from_user.first_name} присоединился")

@dp.message_handler(commands=["help"])
async def help(msg):
    await msg.answer("Напиши сообщение типа:")
    time.sleep(1)
    await msg.answer("/download https://www.youtube.com/watch?v=vgUOhL0MtfY")
    time.sleep(1)
    await msg.answer("Если видео на скачалось то либо подождите, либо оно весит слишком много(его длина должна быть~10 мин)")

@dp.message_handler(commands=["download"])
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
        await msg.answer("Простите, телеграмм не позволяет отправлять такие тяжёлые видео, но я с удовольствием скачаю видео длиною ~ 10 мин🥶")
    os.remove(path)

@dp.message_handler()
async def txt(msg):
    await msg.answer("Я тебя не понял, напиши /help")

aiogram.executor.start_polling(dp, skip_updates=True)
