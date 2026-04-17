from aiogram.types import InlineKeyboardMarkup,InlineKeyboardButton
from aiogram.types import InlineKeyboardMarkup

def users_inline(users):
    keyboard = []

    for user in users:
        keyboard.append([
            InlineKeyboardButton(
                text=f"{user['username']} ({user['role']})",
                callback_data=f"user_{user['telegram_id']}"
            )
        ])

    return InlineKeyboardMarkup(inline_keyboard=keyboard)

def role_inline(telegram_id):
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="👑 Admin",
                    callback_data=f"setrole_admin_{telegram_id}" #"setrole_admin_1716549072"
                ),
                InlineKeyboardButton(
                    text="👤 User",
                    callback_data=f"setrole_user_{telegram_id}"
                )
            ]
        ]
    )