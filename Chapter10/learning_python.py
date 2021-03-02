filename="Chapter10/learning_python.txt"

with open(filename) as python:
    info=python.read()
print("----- Output from read() -----")
print(info)

print("----- Output from looping -----")
with open(filename) as python:
    for line in python:
        print(line)

print("----- Output from readlines() -----")
with open (filename) as python:
    info=python.readlines()
print("Origional life=", info)
for line in info:
    print(line)

print("----- Replacing Python with C# -----")
with open(filename) as Python:
    for line in Python:
        print("Origional: ", line)
        print("Modified: ", line.replace("python","C#"))