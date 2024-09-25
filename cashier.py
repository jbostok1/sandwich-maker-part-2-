class Cashier:
    def __init__(self):
        pass

    # Returns the total calculated from coins inserted
    def process_coins(self):
        """Returns the total calculated from coins inserted.
           Hint: include input() function here, e.g. input("how many quarters?: ")"""
        quarters = int (input("how many quarters?: "))
        dimes = int (input("how many dimes?: "))
        nickels = int (input("how many nickels?: "))
        pennies = int (input("how many pennies?: "))
        #calculates how much money was inserted
        total = (quarters * 0.25) + (dimes * 0.10) + (nickels * 0.05) + (pennies * 0.01)
        return total
        

    # Returns True when payment is accepted, or False if money is insufficient
    def transaction_result(self, coins, cost):
        """Return True when the payment is accepted, or False if money is insufficient.
           Hint: use the output of process_coins() function for cost input"""
        
        if coins >= cost:
            change = round(coins -cost,2) #rounds change to 2 decimal places, checks if payment was correct.
            print(f"Here is ${change} in change.")
            return True
        else:
            print("Sorry that's not enough money. Money refunded.")
            return False
