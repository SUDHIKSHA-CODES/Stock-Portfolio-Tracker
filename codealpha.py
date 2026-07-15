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
    total = stock_prices[stock] * quantity

    print("Stock:", stock)
    print("Price:", stock_prices[stock])
    print("Quantity:", quantity)
    print("Total Investment: $", total)

else:
    print("Stock not available.")
    stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 320,
    "AMZN": 145
}

total_investment = 0

while True:

    stock = input("Enter Stock Name (or EXIT): ").upper()

    if stock == "EXIT":
        break

    if stock not in stock_prices:
        print("Stock not found.")
        continue

    quantity = int(input("Enter Quantity: "))

    investment = stock_prices[stock] * quantity

    total_investment += investment

print("Total Investment Value: $", total_investment)
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 320,
    "AMZN": 145
}

total_investment = 0

file = open("portfolio.txt", "w")

while True:

    stock = input("Enter Stock Name (or EXIT): ").upper()

    if stock == "EXIT":
        break

    if stock not in stock_prices:
        print("Stock not found.")
        continue

    quantity = int(input("Enter Quantity: "))

    investment = stock_prices[stock] * quantity

    total_investment += investment

    file.write(f"{stock} - Quantity: {quantity} - Investment: ${investment}\n")

file.write(f"\nTotal Investment: ${total_investment}")

file.close()

print("Portfolio saved successfully.")
print("Total Investment: $", total_investment)
