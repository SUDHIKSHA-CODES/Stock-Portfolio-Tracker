print("Stock Portfolio Tracker")
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 320,
    "AMZN": 145
}

print("Available Stocks:")

for stock, price in stock_prices.items():
    print(stock, "-", price)
    stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 320,
    "AMZN": 145
}

stock = input("Enter Stock Name: ").upper()
quantity = int(input("Enter Quantity: "))

if stock in stock_prices:
    print("Stock Selected:", stock)
    print("Quantity:", quantity)
else:
    print("Stock not available.")