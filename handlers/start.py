from aiogram import Router, F, Bot, types
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.filters import CommandStart
from keyboard.reply import admin_buttons
from filters.filter import RoleFilter

router = Router()

router=Router()
@router.message(CommandStart(),RoleFilter("admin"))
async def admin_start(msg:Message):
    await msg.answer("Assalomu Alaykum admin xush kelibsz",reply_markup=admin_buttons())

@router.message(CommandStart())
async def start_handler(msg:Message,db):
    username=msg.from_user.username
    telegram_id=msg.from_user.id
    await db.add_user(username,telegram_id)
    await msg.answer("Kino botimizga xush kelibsiz\nKino kodini yozing!")