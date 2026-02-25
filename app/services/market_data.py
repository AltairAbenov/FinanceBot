import yfinance as yf

def fetch_history(ticker: str, period: str):
    t = yf.Ticker(ticker.lower())
    hist = t.history(period=period, 
                     interval="1d",
                     start=None,
                     auto_adjust=True,
                     actions=False
                     )
    if hist is None or hist.empty:
        return None
    return hist

def fetch_currency(ticker: str):
    t = yf.Ticker(ticker)
    info = t.info
    return info.get("currency", "")