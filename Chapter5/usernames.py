current_users = ["Austin", "Kalob", "Devin", "Kamryn", "Telsa"]
new_users = ["AUSTIN", "Devin", "Emilia", "Steven", "Richard"]
current_users_copy = []

for user in current_users:
    current_users_copy.append(user.lower())

for user in new_users:
    if user.lower() in current_users_copy:
        print(f"Sorry {user}, but that name is already taken and you will need to enter a new username.")
    else:
        print(f"Welcome {user}, that username is available.")