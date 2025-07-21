import json

# Load portfolio from file
def load_portfolio(filename):
    try:
        with open(filename, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

# Save portfolio to file
def save_portfolio(portfolio, filename):
    with open(filename, 'w') as file:
        json.dump(portfolio, file)

# Display portfolio
def display_portfolio(portfolio):
    total_value = 0
    print("\nYour Portfolio:")
    for stock, data in portfolio.items():
        value = data['shares'] * data['price']
        print(f"{stock}: {data['shares']} shares @ ₹{data['price']} = ₹{value}")
        total_value += value
    print(f"\nTotal Portfolio Value: ₹{total_value}\n")

# Main tracker logic
def main():
    filename = "portfolio.json"
    portfolio = load_portfolio(filename)

    while True:
        print("\nOptions: 1. Add Stock  2. Update Price  3. View Portfolio  4. Exit")
        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            stock = input("Enter stock name: ")
            shares = int(input("Enter number of shares: "))
            price = float(input("Enter current price: ₹"))
            portfolio[stock] = {"shares": shares, "price": price}
            save_portfolio(portfolio, filename)
            print("Stock added successfully!")

        elif choice == '2':
            stock = input("Enter stock name to update: ")
            if stock in portfolio:
                new_price = float(input(f"Enter new price for {stock}: ₹"))
                portfolio[stock]['price'] = new_price
                save_portfolio(portfolio, filename)
                print(f"{stock} price updated!")
            else:
                print("Stock not found in portfolio.")

        elif choice == '3':
            display_portfolio(portfolio)

        elif choice == '4':
            print("Exiting... Happy investing!")
            break

        else:
            print("Invalid choice. Try again!")

if __name__ == "__main__":
    main()

