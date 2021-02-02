print ("------------- Hands on 1 ---------------------------------------")
favoriteFoods=["Shrimp","Ice Cream","Apple Muffins","Sea Food Stirfry","Beef Enchiladas","Ham Cheese Potato Soup"]
print("Favorite Foods:", (favoriteFoods))
favoriteNumbers=["2","7","11","22","24","44"]
print("Favorite Numbers:", (favoriteNumbers))
favoriteMovies=["Aladin","Game of Thrones","Dragon Heart"]
print("Favorite Movies:", (favoriteMovies))
CombinationList=[favoriteFoods[0], favoriteFoods[-3], favoriteNumbers[1], favoriteNumbers[-3], favoriteMovies[0], favoriteMovies[-1]]
print("Combo List:", (CombinationList))
print("Last Food Item:", (favoriteFoods[-1]))
print("2nd 4th and 6th numbers:", (favoriteNumbers[1], favoriteNumbers[3], favoriteNumbers[5]))
print("All Movies:", (favoriteMovies))
print("First food, first number and first movie:",(favoriteFoods[0], favoriteNumbers[0], favoriteMovies[0]))
print()

print ("------------- Hands on 2 ---------------------------------------")
favoriteMovies.append("How to Train Your Dragon")
print("Added Movie:",(favoriteMovies))
favoriteNumbers.insert(3,"222")
print("Added number at sub 3:",(favoriteNumbers))
favoriteFoods.insert(5,"Pork Steak")
print("Added food at sub 5:",(favoriteFoods))
del favoriteFoods[6]
print("Deleted food[6]:",(favoriteFoods))
removedNumber1= favoriteNumbers.pop()
print("Deleted last number:",(favoriteNumbers))
removedNumber2= favoriteNumbers.pop(2)
print("Deleted number at sub 2:",(favoriteNumbers))
print()

print ("------------- Hands on 3 ---------------------------------------")
favoriteMovies.sort()
print("Sorted list:",(favoriteMovies))
favoriteFoods.sort()
print("Sorted list:",(favoriteFoods))
print("Temp sorted list:",sorted(favoriteNumbers))
print("Unsorted List:",(favoriteNumbers))
favoriteMovies.reverse()
print("Sorted in reverse:",(favoriteMovies))
print()

print ("------------- Chapter 4, Hands on 1 ----------------------------")
print()
print("Food list")
print("-----------------------------")
for food in favoriteFoods:
    print(food)
print()
print("Number list")
print("-----------------------------")
for number in favoriteNumbers:
    print(number)
print()
print("Movie list")
print("-----------------------------")
for movie in favoriteMovies:
    print(movie)
print()
print("Combination list")
print("-----------------------------")
for combo in CombinationList:
    print(combo)
print()

print ("------------- Chapter 4, Exersice 4-1 ---------------------------")
favoriteAnimals=["Wolf", "Fox", "Owl"]
print(favoriteAnimals[0])
print(favoriteAnimals[1])
print(favoriteAnimals[2])
print("----- Animals that are smart hunters -----")
print("The", favoriteAnimals[0], "is an animal that hunts in packs")
print("The", favoriteAnimals[1], "is an animal that is very clever")
print("The", favoriteAnimals[2], "is an animal that is a silent hunter")