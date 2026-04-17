from aiogram.types import ReplyKeyboardMarkup,KeyboardButton

def admin_buttons():
    return ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text="➕Kino qo'shish"),
                KeyboardButton(text="📊Statistika")
            ],
            [
                KeyboardButton(text="Userlar")
            ]
        ],resize_keyboard=True
    )