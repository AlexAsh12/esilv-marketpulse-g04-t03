def index_by_date(prices):
    
    return {
        row["date"]: row
        for row in prices
    }

