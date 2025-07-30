# Simple Stock Tracker using dictionary, input/output, basic arithmetic, and file handling
# Predefined stock prices
stock_prices = {
    "AAPL": 195.20,
    "GOOGL": 2835.55,
    "MSFT": 420.35,
    "TSLA": 280.10,
    "AMZN": 145.75
}

# File name to store user stock data
file_name = "stock_data.txt"

# Function to add stock entry
def add_stock():
    symbol = input("Enter stock symbol (e.g., AAPL): ").upper()
    if symbol not in stock_prices:
        print("Invalid stock symbol. Please use one of:", ", ".join(stock_prices.keys()))
        return
    try:
        quantity = int(input("Enter number of shares: "))
    except ValueError:
        print("Invalid quantity. Please enter a number.")
        return

    # Save to file
    with open(file_name, "a") as file:
        file.write(f"{symbol},{quantity}\n")
    print(f"{quantity} shares of {symbol} added.\n")

# Function to calculate total investment
def calculate_investment():
    total = 0
    print("\nYour Stock Holdings:")
    try:
        with open(file_name, "r") as file:
            for line in file:
                symbol, quantity = line.strip().split(",")
                quantity = int(quantity)
                price = stock_prices.get(symbol, 0)
                investment = quantity * price
                total += investment
                print(f"{symbol}: {quantity} shares × ${price:.2f} = ${investment:.2f}")
        print(f"\nTotal Investment: ${total:.2f}\n")
    except FileNotFoundError:
        print("No stock data found. Please add stocks first.\n")

# Main menu loop
def main():
    while True:
        print("=== Stock Tracker Menu ===")
        print("1. Add Stock Entry")
        print("2. View Total Investment")
        print("3. Exit")
        choice = input("Enter your choice (1-3): ")

        if choice == "1":
            add_stock()
        elif choice == "2":
            calculate_investment()
        elif choice == "3":
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.\n")

# Run the program
if __name__ == "__main__":
    main()