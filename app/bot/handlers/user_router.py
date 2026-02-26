import asyncio
from aiogram import Router, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, BufferedInputFile
from app.bot.parsing import parse_query
from app.services.market_data import fetch_history, fetch_currency
from app.services.analytics import make_summary
from app.services.charts import build_price_chart

user_router = Router()

@user_router.message(CommandStart())
async def start_handler(message: Message):
    await message.answer("<b>👋 Hi! I'm a stock analysis bot.</b> \n\n"
                         "<b>📌 Enter the ticker and period:</b>\n"
                         "<b>For example:</b> <em>AAPL 1y</em>\n\n"
                         "<b>If you don't specify a period, I'll use 6mo by default.</b>\n\n"
                         "<b>🕒 Available periods:</b>\n"
                         "<em>1d, 5d, 7d, 30d, 1mo, 3mo, 6mo, 1y, 2y, 5y</em>\n\n"
                         "<b>Try it 👇</b>",
                         parse_mode="HTML")
    
@user_router.message(F.text)
async def ticker_handler(message: Message):
    try:
        ticker, period = parse_query(message.text)
    except ValueError:
        await message.answer('Incorrect format. Try again.')
        return
    
    status = await message.answer("<b>Accepted ✅</b>\n"
                         f"<b>Ticker:</b> {ticker}\n"  
                         f"<b>Period:</b> {period}\n"
                         "<b>Processing... 🕐</b>",
                         parse_mode="HTML")
    
    hist = await asyncio.to_thread(fetch_history, ticker, period)
    
    if hist is None:
        await status.edit_text("❌ Failed to retrieve data.")
        return
    
    summary = make_summary(hist)
    currency = await asyncio.to_thread(fetch_currency, ticker)
    
    await status.edit_text(
        f"<b>{ticker.upper()}</b> for <b>{period}</b>\n\n"
        f"Price: <b>{summary['last']:.2f} {currency}</b>\n"
        f"Change: <b>{summary['change_percent']:.2f}%</b>\n"
        f"High: <b>{summary['high']:.2f} {currency}</b>\n"
        f"Low: <b>{summary['low']:.2f} {currency}</b>",
        parse_mode = "HTML"
    )
    
    chart_bytes = await asyncio.to_thread(build_price_chart, hist, ticker)
    photo = BufferedInputFile(chart_bytes, filename=f"{ticker}.png")
    await message.answer_photo(photo, caption=f"<b>{ticker.upper()}</b> - Chart for the <b>{period}</b> period",
                               parse_mode="HTML")

