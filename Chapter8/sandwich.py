items = []
def sandwich(amount):
    counter = 0
    while counter < amount:
        item = input("What would you like to add to your sandwich? ")
        items.append(item)
        counter += 1
    return items

sandwich(3)
sandwich1 = items.copy()
print("The first sandwich is ready")
items.clear()

sandwich(4)
sandwich2 = items.copy()
print("The second sandwich is ready")
items.clear()

sandwich(1)
sandwich3 = items.copy()
print("The third sandwich is ready")
items.clear()

print()
print("The first sandwich has: ")
for item in sandwich1:
    print(item)
    
print("The second sandwich has: ")
for item in sandwich2:
    print(item)

print("The third sandwich has: ")
for item in sandwich3:
    print(item)