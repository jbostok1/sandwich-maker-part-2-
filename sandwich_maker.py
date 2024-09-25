class SandwichMaker:
    def __init__(self, resources):
        self.machine_resources = resources

    #checks if there is enough resources for ingredients
    def check_resources(self, ingredients):
        #checks if there is enough resources
        for item in ingredients:
            if self.machine_resources[item] < ingredients[item]:
                print(f"Sorry, there is not enough {item}.")
                return False
        return True

    #makes sandwich with ingredients
    def make_sandwich(self, sandwich_size, order_ingredients):
        #makes sandwich
        for item in order_ingredients:
            self.machine_resources[item] -= order_ingredients[item]
        print(f"Here is your {sandwich_size} sandwich. Enjoy!")
