from aiogram import F ,Router
from aiogram.types import Message


router=Router()

@router.message(F.text.isdigit()) 
async def search_handler(msg: Message, db):
    movie_code = int(msg.text)
    result = await db.search_movie(movie_code)

    if result is None:
        return await msg.answer(f"❌ {movie_code} kodi bo'yicha kino topilmadi")
    
    await msg.answer_video(
        video=result["file_id"],
        caption=f"🎬 {result['title']}\n\nKodi: {result['code']}"
    )