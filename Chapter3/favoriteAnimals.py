print("----------------------------------------------------------------")
print("Favorite Animals")
print("----------------------------------------------------------------")
print()
favoriteAnimals=["Cat","Wolf","Fox","Owl","Tiger"]
print("Origional list:",favoriteAnimals)
favoriteAnimals.append("Dog")
favoriteAnimals.insert(1,"Leopard")
print(f"List after additions: {favoriteAnimals}")
del favoriteAnimals[1]
favoriteAnimals.pop(5)
favoriteAnimals.remove("Tiger")
print(f"List after deletions: {favoriteAnimals}")
print("List with temporary sort:", sorted(favoriteAnimals))
favoriteAnimals.reverse()
print("List sorted in reverse:", favoriteAnimals)
favoriteAnimals.sort()
print("List sorted in alphabetical order:", favoriteAnimals)
print(f"There are {len(favoriteAnimals)} animals in the final list.")