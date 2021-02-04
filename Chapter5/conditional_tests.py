variableList = [2, 7, 13]
isTrue = True
wordList = ["fang", "Fang", "Dream"]

print("-------------------- True Results ----------------------")
if variableList[0] < variableList[1]:
    isTrue = True
else:
    isTrue = False
print(f"{variableList[0]} < {variableList[1]} {isTrue}")

if variableList[1] <= variableList[2]:
    isTrue = True
else:
    isTrue = False
print(f"{variableList[1]} <= {variableList[2]} {isTrue}")

if variableList[0] != variableList[2]:
    isTrue = True
else:
    isTrue = False
print(f"{variableList[0]} != {variableList[2]} {isTrue}")

if wordList[1] == wordList[1]:
    isTrue = True
else:
    isTrue = False
print(f"{wordList[1]} == {wordList[1]} {isTrue}")

if wordList[1].lower() == wordList[0]:
    isTrue = True
else:
    isTrue = False
print(f"{wordList[1].lower()} == {wordList[0]} {isTrue}")

if "Dream" in wordList:
    isTrue = True
else:
    isTrue = False
print(f"Dream in wordList {isTrue}")

if variableList[0] != variableList[1] and variableList[1] != variableList[2]:
    isTrue = True
else:
    isTrue = False
print(f"{variableList[0]} != {variableList[1]} and {variableList[1]} != {variableList[2]} {isTrue}")

if variableList[0] == variableList[0] or variableList[1] != variableList[2]:
    isTrue = True
else:
    isTrue = False
print(f"{variableList[0]} == {variableList[0]} or {variableList[1]} != {variableList[2]} {isTrue}")

print("-------------------- False Results ---------------------")
if variableList[0] > variableList[1]:
    isTrue = True
else:
    isTrue = False
print(f"{variableList[0]} > {variableList[1]} {isTrue}")

if variableList[1] >= variableList[2]:
    isTrue = True
else:
    isTrue = False
print(f"{variableList[1]} >= {variableList[2]} {isTrue}")

if variableList[0] == variableList[2]:
    isTrue = True
else:
    isTrue = False
print(f"{variableList[0]} == {variableList[2]} {isTrue}")

if wordList[1] != wordList[1]:
    isTrue = True
else:
    isTrue = False
print(f"{wordList[1]} != {wordList[1]} {isTrue}")

if wordList[1].upper() == wordList[0]:
    isTrue = True
else:
    isTrue = False
print(f"{wordList[1].upper()} == {wordList[0]} {isTrue}")

if "Dreams" in wordList:
    isTrue = True
else:
    isTrue = False
print(f"Dreams in wordList {isTrue}")