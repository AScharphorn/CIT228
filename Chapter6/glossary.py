glossary={
    "Print":"Command that prints text on the screen",
    "For in":"Creates a loop for each item in a list",
    "If":"Creates a conditional statement that does different things depending on specified conditions",
    "Del":"Removes an item from a list",
    "Key":"Value used to access keys in the dictionary in a for loop",
    "Value":"Value used to access values in the dictionary in a for loop",
    "Item":"Value used to access keys and values in the dictionary ina  for loop",
    "Sorted":"Sorts items in a list",
    "Get":"Lets you access the dictionary using the key",
    "lower":"Makes the printed variable lowercased"
}

print("Dictionary:")
#print("\t\n","Print:",glossary["Print"])
#print("\t\n","For in:",glossary["For in"])
#print("\t\n","If:",glossary["If"])
#print("\t\n","Del:",glossary["Del"])
#print("\t\n","Key:",glossary["Key"])

for item in glossary:
    print(f"\t{item}: {glossary[item]}\n")