import io
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

def build_price_chart(hist, ticker: str) -> bytes:
    close = hist["Close"]
    
    plt.figure()
    plt.plot(close.index, close.values)
    plt.title(f"{ticker.upper()} Close")
    plt.xlabel("Date")
    plt.ylabel("Price")
    plt.grid(True)
    
    ax = plt.gca()
    locator = mdates.AutoDateLocator(minticks=4, maxticks=8)
    ax.xaxis.set_major_locator(locator)
    ax.xaxis.set_major_formatter(mdates.ConciseDateFormatter(locator))
    
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    
    buf = io.BytesIO()
    plt.savefig(buf, format="png", dpi=160)
    plt.close()
    buf.seek(0)
    
    return buf.read()
