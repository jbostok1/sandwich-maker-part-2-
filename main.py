import data
from sandwich_maker import SandwichMaker
from cashier import Cashier

# Make an instance of other classes here
resources = data.resources
recipes = data.recipes
sandwich_maker_instance = SandwichMaker(resources)
cashier_instance = Cashier()

def main():
    working = True

    while working:
        # get user input and display available sandwiches
        print("Welcome to the sandwich maker!")
        print("Here are our available sandwiches:")

        # Display the sandwich options directly (small, medium, large)
        for sandwich_name in recipes:
            print(f"{sandwich_name} - ${recipes[sandwich_name]['cost']}")

        # Get user sandwich choice (small, medium, or large)
        choice = input("What size would you like to order (small, medium, large)? ").lower()
        
        if choice == "exit":
            working = False
            break

        # check if sandwich size is available
        if choice in recipes:
            sandwich_ingredients = recipes[choice]["ingredients"]
            sandwich_cost = recipes[choice]["cost"]

            # Check if ingredients are available
            if sandwich_maker_instance.check_resources(sandwich_ingredients):
                coins = cashier_instance.process_coins()  # Get the total amount of coins
                if cashier_instance.transaction_result(coins, sandwich_cost):
                    sandwich_maker_instance.make_sandwich(choice, sandwich_ingredients)
                else:
                    print("Sorry, that's not enough money. Money refunded.")
            else:
                print("Sorry, we don't have enough ingredients.")
        else:
            print("Sorry, we don't have that sandwich.")

if __name__ == "__main__":
    main()
