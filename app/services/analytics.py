def make_summary(hist):
    close = hist["Close"]
    last = float(close.iloc[-1])
    first = float(close.iloc[0])
    change_percent = (last - first) / first * 100
    
    high = float(hist["High"].max())
    low = float(hist["Low"].min())
    
    return {
        "first": first,
        "last": last,
        "change_percent": change_percent,
        "high": high,
        "low": low
    }