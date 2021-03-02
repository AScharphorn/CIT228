print("---------------- Try it Yourself 9-1 --------------")
class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"Restaurant Name: {self.restaurant_name}")
        print(f"Cuisine Type: {self.cuisine_type}")

    def open_restaurant(self):
        print(f"{self.restaurant_name} is now open and accepting customers!")

restaurant = Restaurant("Subway","Subs and Pizza")

print(f"The name of the restaurant is {restaurant.restaurant_name}")
print(f"The type of food you will see there is {restaurant.cuisine_type}")
print()

restaurant.describe_restaurant()
restaurant.open_restaurant()

print("---------------- Try it Yourself 9-2 --------------")
restaurant1 = Restaurant("Little Ceasars","Pizza")
restaurant2 = Restaurant("Asian Buffet","Asian")
restaurant3 = Restaurant("Dairy Queen","Ice Cream")

restaurant1.describe_restaurant()
print()
restaurant2.describe_restaurant()
print()
restaurant3.describe_restaurant()