ALLOWED_PERIODS = {"1d", "5d", "7d", "30d", "1mo", "3mo", "6mo", "1y", "2y", "5y"}

def parse_query(text: str):
    text = text.strip()
    
    if not text:
        raise ValueError("Empty input")
    
    parts = text.split()
    
    if len(parts) == 1:
        ticker = parts[0].upper()
        period = "6mo"
        
    elif len(parts) == 2:
        ticker = parts[0].upper()
        period = parts[1].lower()
        
        if period not in ALLOWED_PERIODS:
            raise ValueError("Invalid period")
        
    else:
        raise ValueError("Too many arguments")
    
    return ticker, period