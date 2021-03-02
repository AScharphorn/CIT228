rivers={
    "Danube":["Germany","Austria","Slovakia","Hungary", "Coratia", "Serbia","Romania","Bulgaria", "Moldova", "Ukraine"],
    "Amazon":["Brazil","Bolivia","Peru","Ecuador","Colombia","Venezuela","Guyana", "Suriname", "French Guiana"],
    "Mississippi":"United States"
}

for key, value in rivers.items():
    if type(value)==list:
        print(f"The {key.title()} river flows through: ")
        for v in value:
            print (f" {v}")
    else:
        print(f"The {key.title()} river flows though {value.title()}")