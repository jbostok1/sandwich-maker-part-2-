class Cashier:
    def __init__(self):
        pass

    # Process coins
    def process_coins(self):
        # Prompt user for coins
        quarters = int(input("How many quarters?: "))
        dimes = int(input("How many dimes?: "))
        nickels = int(input("How many nickels?: "))
        pennies = int(input("How many pennies?: "))
        total = (quarters * 0.25) + (dimes * 0.10) + (nickels * 0.05) + (pennies * 0.01) # total in dollars
        return total

    def transaction_result(self, coins, cost):
        # Check if enough money is inserted
        if coins >= cost: 
            change = round(coins - cost, 2)
            print(f"Here is ${change} in change.")
            return True
        else:
            print("Sorry, that's not enough money. Money refunded.")
            return False
