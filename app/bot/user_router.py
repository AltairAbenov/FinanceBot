from aiogram import Router, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from app.bot.parsing import parse_query

user_router = Router()

@user_router.message(CommandStart())
async def start_handler(message: Message):
    await message.answer("<b>👋  Привет! Я бот для анализа акций.</b> \n\n"
                         "<b>📌  Напиши тикер и период:</b>\n"
                         "<b>Например:</b> <em>AAPL 1y</em>\n\n"
                         "<b>Если не укажешь период - я возьму 6mo по умолчанию.</b>\n\n"
                         "<b>🕒  Доступные периоды:</b>\n"
                         "<em>1d,  5d,  7d,  30d,  1mo,  3mo,  6mo,  1y,  2y,  5y</em>\n\n"
                         "<b>Попробуй  👇</b>",
                         parse_mode="HTML")
    
@user_router.message(Command("help"))
async def help_cmd(message: Message):
    await message.answer('Хелпа')
    
@user_router.message(F.text)
async def ticker_handler(message: Message):
    try:
        ticker, period = parse_query(message.text)
    except ValueError:
        await message.answer('Неправильный формат. Попробуй еще раз.')
        return
    await message.answer("<b>Принято ✅</b>\n"
                         f"<b>Тикер:</b> {ticker}\n"  
                         f"<b>Период:</b> {period}\n"
                         "<b>Обрабатываю... 🕐</b>",
                         parse_mode="HTML")

