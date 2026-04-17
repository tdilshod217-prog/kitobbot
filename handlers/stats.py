from aiogram import F,Router
from aiogram.types import Message
import datetime

router=Router()

@router.message(F.text == "📊Statistika")
async def stats(msg: Message, db):
    data = await db.get_bot_stats()
    current_time = datetime.datetime.now().strftime("%H:%M:%S")
    # 2. Asosiy xabarni shakllantiramiz
    stats_msg = (
        "<b>📊 BOT STATISTIKASI</b>\n"
        "━━━━━━━━━━━━━━━\n\n"
        f"👥 <b>A'zolar:</b> <code>{data['users']} ta</code>\n"
        f"📚 <b>Kinolar:</b> <code>{data['movie']} ta</code>\n"
        f"🕒 Yangilangan vaqt: {current_time}"
    )
    
    await msg.answer(stats_msg, parse_mode="HTML")