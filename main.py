import asyncio
import os
from dotenv import load_dotenv
from app.bot.user_router import user_router
from aiogram import Bot, Dispatcher

load_dotenv()

TOKEN = os.getenv("BOT_TOKEN")

if not TOKEN:
    raise ValueError("No BOT_TOKEN found in environment variables(.env)")


async def main():
    bot  = Bot(token=TOKEN)
    dp = Dispatcher()
    
    dp.include_router(user_router)
    
    await dp.start_polling(bot)
    
if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Exit')