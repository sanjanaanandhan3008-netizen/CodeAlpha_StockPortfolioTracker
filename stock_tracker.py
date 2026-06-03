stocks = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOG": 140
}

stock_name = input("Enter stock name (AAPL/TSLA/GOOG): ").upper()
quantity = int(input("Enter quantity: "))

if stock_name in stocks:
    total_value = stocks[stock_name] * quantity
    print("Total Investment Value: $", total_value)
else:
    print("Stock not found!")
    