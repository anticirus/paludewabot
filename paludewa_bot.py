import asyncio
import schedule
import time
from telegram import Bot, InlineKeyboardButton, InlineKeyboardMarkup

TOKEN = "8089607954:AAHpoSMpa7Gc_t-vyA2d4sl3Aqg9X-gshMQ"
GROUP_CHAT_ID = -1002533964008  # Ganti dengan chat_id grup kamu
bot = Bot(token=TOKEN)

async def kirim_promo():
    keyboard = [
        [InlineKeyboardButton("💥 LP GACOR", url="https://example.com/lpgacor"),
         InlineKeyboardButton("🎯 RTP ANTI RUNGKAT", url="https://example.com/rtp")],
        [InlineKeyboardButton("📝 DAFTAR AKUN VVIP", url="https://example.com/vvip")],
        [InlineKeyboardButton("ℹ️ INFO UPTODATE", url="https://example.com/info"),
         InlineKeyboardButton("🔗 LINK ANTI NAWALA", url="https://example.com/nawala")],
        [InlineKeyboardButton("⚡ LINK GACOR", url="https://example.com/gacor")],
        [InlineKeyboardButton("👩‍💼 ADMIN BEATRICE", url="https://t.me/adminusername")],
        [InlineKeyboardButton("💬 LIVECHAT 24 JAM", url="https://example.com/livechat")],
        [InlineKeyboardButton("📘 FACEBOOK GRUP OFFICIAL", url="https://facebook.com/")],
        [InlineKeyboardButton("🆕 INFO TERBARU KAMI", url="https://example.com/newinfo")],
        [InlineKeyboardButton("🎁 BONUS HARIAN 30%", url="https://example.com/bonus")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    text = """
💥 GARUDAHOKI SITUS TERGACOR ANTI RUNGKAD!!! 💥

🔗 LINK DAFTAR: https://garudahoki-20.com

🔥 BONUS GARUDAHOKI 🔥
❌ KALAH CLAIM 100K  
❌ BONUS NEW MEMBER 100%  
❌ GARANSI KEKALAHAN 100%  
❌ DEPOSIT HARIAN 30%  

💵 Min Depo = 10.000  
💸 Min WD = 50.000  

🔥 AYO DAFTAR DAN DEPOSIT, RASAKAN SENSASI GACORNYA!
"""

    await bot.send_message(chat_id=GROUP_CHAT_ID, text=text, reply_markup=reply_markup)

def job():
    asyncio.run(kirim_promo())

# Jadwal tiap 3 jam
schedule.every(3).hours.do(job)

print("Bot aktif. Pesan akan dikirim tiap 3 jam.")

while True:
    schedule.run_pending()
    time.sleep(1)