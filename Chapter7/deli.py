sandwich_orders = ["Pastrami", "Italian", "Vegan", "Pastrami", "Steak", "Pastrami", "Tuna"]
finished_sandwiches = []
print("I am sorry, we ran out of pastrami.")
for sandwich in sandwich_orders:
    if sandwich == 'Pastrami':
        sandwich_orders.remove(sandwich)
for sandwich in sandwich_orders:
    print(f"I made your {sandwich} sandwich")
    finished_sandwiches.append(sandwich)
sandwich_orders.clear()
print("Sandwiches that were made today:")
for sandwich in finished_sandwiches:
    print(sandwich)