import data
from sandwich_maker import SandwichMaker
from cashier import Cashier

# Make an instance of other classes here
resources = data.resources
recipes = data.recipes
sandwich_maker_instance = SandwichMaker(resources)
cashier_instance = Cashier()

# Function to print welcome message
def print_welcome_message():
    print("=" * 40)
    print("🍞 Welcome to the Ultimate Sandwich Maker 🥪")
    print("=" * 40)
    print("")

# Function to print the menu
def print_menu():
    print("Here are our available sandwich sizes and prices:")
    print("-" * 40)
    for sandwich_name in recipes:
        print(f"{sandwich_name.capitalize():<10} | ${recipes[sandwich_name]['cost']:<5}")
    print("-" * 40)
    print("")

def main():
    working = True

    # Print welcome message
    print_welcome_message()

    while working:
        # Display menu
        print_menu()

        # Get user's sandwich size choice
        choice = input("👉 What size sandwich would you like to order? (small, medium, large): ").lower().strip()

        # Exit condition
        if choice == "exit":
            working = False
            print("\nThank you for using the sandwich maker. Goodbye!")
            print("=" * 40)
            break

        # Check if the selected sandwich size is available
        if choice in recipes:
            sandwich_ingredients = recipes[choice]["ingredients"]
            sandwich_cost = recipes[choice]["cost"]

            # Check if enough ingredients are available to make the sandwich
            if sandwich_maker_instance.check_resources(sandwich_ingredients):
                # Process coins and get the total amount
                print("\nPlease insert coins to proceed.")
                coins = cashier_instance.process_coins()

                # Check if the payment is sufficient
                if cashier_instance.transaction_result(coins, sandwich_cost):
                    # Make the sandwich
                    sandwich_maker_instance.make_sandwich(choice, sandwich_ingredients)
                    print("-" * 40)
                else:
                    # Insufficient funds
                    print("\n🚫 Sorry, that's not enough money, you have been refunded.")
                    print("-" * 40)
            else:
                # Not enough ingredients
                print("\n🚫 Sorry, we don't have enough ingredients.")
                print("-" * 40)
        else:
            # Invalid choice of sandwich size
            print("\n🚫 Sorry, we don't have that sandwich size available.")
            print("-" * 40)

if __name__ == "__main__":
    main()
