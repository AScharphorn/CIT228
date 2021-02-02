print("----------- Origional List ----------------------")
farmAnimals = ["Dog", "Sheep", "horse", "cow", "chicken", "pig"]
for animal in farmAnimals:
    print(animal)
print("----------- New List ----------------------------")
newFarmAnimals = farmAnimals[:]
newFarmAnimals.append("Rooster")
newFarmAnimals.append("Goat")
newFarmAnimals.append("Llama")
newFarmAnimals.append("Cat")
for animal in newFarmAnimals:
    print(animal)
print()

print("The first 3 items in the new list are:", newFarmAnimals[:3])
print("The middle 3 items in the new list are:", newFarmAnimals[3:6])
print("The last 3 items in the list are:", newFarmAnimals[7:10])