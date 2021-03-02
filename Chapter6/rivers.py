rivers={
    "Danube":"['Germany', 'Austria', 'Slovakia', 'Hungary', 'Coratia', 'Serbia', 'Romania', 'Bulgaria', 'Moldova', 'Ukraine'",
    "Amazon":"['Brazil', 'Bolivia', 'Peru', 'Ecuador', 'Colombia', 'Venezuela', 'Guyana', 'Suriname', 'French Guiana']",
    "Mississippi":"United Stats"
}

print("----------------- Rivers and Countries ---------------")
for item in rivers:
    print(f"The {item} river flows through {rivers[item]}")

print("\n----------------- Rivers -----------------")
for item in rivers:
    print(item)

print("\n----------------- Countries -----------------")
for item in rivers:
    print(rivers[item])