from aiogram import Router, F
from aiogram.types import Message,CallbackQuery
from aiogram.fsm.context import FSMContext
from states.addmovies import AddMovies

router=Router()

@router.message(F.text=="➕Kino qo'shish")
async def start_add_book(msg:Message, state: FSMContext):
    await msg.answer("📝 Kino **nomini** kiriting:")
    await state.set_state(AddMovies.title)

@router.message(AddMovies.title)
async def get_title(msg:Message, state: FSMContext):
    await state.update_data(title=msg.text)
    await msg.answer("Kino videosini jo'nating")
    await state.set_state(AddMovies.file_id)

@router.message(AddMovies.title)
async def get_title(msg:Message, state: FSMContext):
    await state.update_data(title=msg.text)
    await msg.answer("Kino ni jo'nating")
    await state.set_state(AddMovies.file_id)

@router.message(AddMovies.file_id)
async def get_title(msg:Message, state: FSMContext):
    await state.update_data(file_id=msg.video.file_id)
    await msg.answer("Kino code ni jo'nating")
    await state.set_state(AddMovies.code)

@router.message(AddMovies.code)
async def get_code(msg:Message,state:FSMContext,db):
    if not msg.text.isdigit():
        await msg.answer("Iltimos raqam jo'nating\nHarf qabul qilinmaydi")
    movie_code=int(msg.text)
    await state.update_data(code=movie_code)
    data= await state.get_data()
    try:
        await db.add_movies(
            title=data['title'],
            file_id=data['file_id'],
            code=data['code']
        )
        await msg.answer("Kino bazaga qoshildi")
        await state.clear()
    except Exception as e:
        await msg.answer(f"Xatolik yuz berdi:{e}")