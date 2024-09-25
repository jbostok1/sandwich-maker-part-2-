
class SandwichMaker:
    def __init__(self, resources):
        self.machine_resources = resources

    def check_resources(self, ingredients):
        """Returns True when order can be made, False if ingredients are insufficient."""
        for item in ingredients:
            if self.machine_resources[item] < ingredients[item]:
                print(f"Sorry there is not enough {item}.")
                return False
        return True
        

    def make_sandwich(self, sandwich_size, order_ingredients):
        """Deduct the required ingredients from the resources."""
        for item in order_ingredients:
            self.machine_resources[item] -= order_ingredients[item]
        print(f"Here is your {sandwich_size} sandwich. Enjoy!")
        print("Your sandwich is ready! ")
