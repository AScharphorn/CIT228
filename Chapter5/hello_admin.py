print("------------------- Exercise 5-8 --------------------")
users = ["Austin", "Jayden", "Devin", "Kamryn", "Admin"]

for user in users:
    if user == "Admin":
        print(f"Welcome back {user}, would you like a status report?")
    else:
        print(f"Welcome back {user}, it is nice to see you again.")

print()
print("------------------- Exercise 5-9 --------------------")
users = []

if users:
    print(f"Welcome back {user}, it is nice to see you again.")
else:
    print("We need more users!")