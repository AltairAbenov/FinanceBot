# 📊 Finance Analysis Helper (Telegram Bot)

A Telegram bot for basic stock market analysis.  
The bot retrieves real-time stock data, calculates key metrics, and generates price charts.

---

## 🚀 Features

- 📥 Accepts stock ticker and time period (e.g., `AAPL 1y`)
- 🌐 Fetches market data via Yahoo Finance (yfinance)
- 📈 Calculates:
  - Last price
  - Percentage change
  - High / Low values
- 🖼 Generates price chart
- ⚡ Asynchronous processing (non-blocking API calls)

---

## 🛠 Technologies Used

- Python 3.11+
- aiogram (Telegram Bot framework)
- yfinance (market data API)
- pandas
- matplotlib
- asyncio

---

## 📦 Installation

1. Clone repository:

```bash
git clone https://github.com/your-username/finance-analysis-helper.git
cd finance-analysis-helper
