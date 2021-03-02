print("---------------- Try it Yourself 9-4 --------------")
increment = 0
day_end = "n"
class Restaurant:
    def __init__(self, restaurant_name, cuisine_type, number_served):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(f"Restaurant Name: {self.restaurant_name}")
        print(f"Cuisine Type: {self.cuisine_type}")

    def open_restaurant(self):
        print(f"{self.restaurant_name} is now open and accepting customers!")
    
    def set_number_served(self):
        print(f"{increment} customers have been served.")

    def increment_number_served(self):
        self.number_served += increment
        print(f"{self.number_served} customers have been served total today.")

class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type, number_served, ice_cream_flavors):
        self.ice_cream_flavors = ice_cream_flavors

    def display_flavors(self):
        print(f"Ice Cream Flavors: {self.ice_cream_flavors}")

restaurant = Restaurant("Subway","Subs and Pizza","3")
iceCreamStand = IceCreamStand("Dairy Queen","Ice Cream","4","Vanilla")

restaurant.open_restaurant()
restaurant.describe_restaurant()
print()
print(f"The initial number of customers today was {restaurant.number_served}")
while day_end != "y":
    increment=int(input("How many customers have been served since the last count? "))
    print()
    restaurant.set_number_served()
    print()
    restaurant.increment_number_served()
    print()
    day_end=input("Has the day ended? (y for yes) ")

print()
iceCreamStand.display_flavors()