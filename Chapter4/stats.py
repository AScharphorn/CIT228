import random
number = random.randrange(10,100)
numbers = list(range(0, number))
print(numbers)
print("The largest number:", max(numbers))
print("The smallest number:", min(numbers))
print("The total of all numbers:", sum(numbers))
print("The average number:", sum(numbers)/len(numbers))
print()

squares = []
for value in range(1, 11):
     square = value ** 2
     squares.append(square)
print(squares) 

cubes = [value**3 for value in range(1, 11)]
print(cubes) 