# Predefined stock prices
stock_prices = {
    "RELIANCE": 2800,
    "HDFC": 1700,
    "ITC": 450,
    "WIPRO": 400,
    "MSFT": 320,
    "INFOSYS": 1600
}

print("📈 Welcome to the Stock Portfolio Tracker")
print("Available stocks and their prices:")
for stock, price in stock_prices.items():
    print(f"  {stock}: ₹{price}")

# Get input from user
stock_name = input("\nEnter the stock name: ").upper()
quantity = int(input("Enter quantity of shares: "))

# Check and calculate
if stock_name in stock_prices:
    price = stock_prices[stock_name]
    total = price * quantity
    print(f"\nTotal investment in {stock_name}: ₹{total}")

    # Optional save with UTF-8 encoding (to support ₹)
    save = input("Do you want to save this result to a file? (yes/no): ").lower()
    if save == "yes":
        with open("stock_portfolio.txt", "a", encoding="utf-8") as file:
            file.write(f"{stock_name} x {quantity} = ₹{total}\n")
        print("Saved to 'stock_portfolio.txt'")
else:
    print("❌ Stock not found. Please enter a valid stock name.")
