from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton
import lang


class Buttons:
    def __init__(self, language):
        #основные кнопки
        self.settings=KeyboardButton(text=lang.data[language]["buttons"]["keyboard"]["settings"])
        self.lang=InlineKeyboardButton(text=lang.data[language]["buttons"]["inline"]["language"], callback_data="language")
        self.donate=InlineKeyboardButton(text=lang.data[language]["buttons"]["inline"]["donate"], callback_data="donate")
        self.back=InlineKeyboardButton(text=lang.data[language]["buttons"]["inline"]["back"], callback_data="back")
        #основные кнопки
        #дополнительные кнопки
        #языки
        self.ru=InlineKeyboardButton("Русский🇷🇺", callback_data="RU")
        self.en=InlineKeyboardButton("English🇬🇧", callback_data="EN")
        #языки
        #донат
        self.yt=InlineKeyboardButton("Youtube❤️", url="https://www.youtube.com/channel/UCso6aUoOmlgmqnVCAVlLLAg", callback_data="yt")
        self.money=InlineKeyboardButton(lang.data[language]["buttons"]["inline"]["money"], url="https://vk.com/public204310665?w=app6471849_-204310665", callback_data="money")
        #донат
        #дополнительные кнопки
        self.SETTINGSkb=ReplyKeyboardMarkup(resize_keyboard=True).add(self.settings)
        self.SETTINGSinline=InlineKeyboardMarkup(row_width=2).add(self.lang, self.donate)
        self.LANGUAGE=InlineKeyboardMarkup(row_width=2).add(self.ru, self.en, self.back)
        self.DONATE=InlineKeyboardMarkup(row_width=2).add(self.yt, self.money, self.back)
        #сборка

    def edit(self, language):
        self.settings=KeyboardButton(lang.data[language]["buttons"]["keyboard"]["settings"])
        self.lang=InlineKeyboardButton(lang.data[language]["buttons"]["inline"]["language"], callback_data="language")
        self.donate=InlineKeyboardButton(lang.data[language]["buttons"]["inline"]["donate"], callback_data="donate")
        self.back=InlineKeyboardButton(lang.data[language]["buttons"]["inline"]["back"], callback_data="back")
        self.money=InlineKeyboardButton(lang.data[language]["buttons"]["inline"]["money"], url="https://vk.com/public204310665?w=app6471849_-204310665", callback_data="money")

        self.SETTINGSkb=ReplyKeyboardMarkup(resize_keyboard=True).add(self.settings)
        self.SETTINGSinline=InlineKeyboardMarkup(row_width=2).add(self.lang, self.donate)        
        self.DONATE=InlineKeyboardMarkup(row_width=2).add(self.yt, self.money, self.back)
        self.LANGUAGE=InlineKeyboardMarkup(row_width=2).add(self.ru, self.en, self.back)
