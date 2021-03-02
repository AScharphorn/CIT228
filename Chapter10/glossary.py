import json

def menu():
    selection = int(input("1-create file\n2-read file\n3-add to file\n4-quit"))
    while selection != 1 and selection != 2 and selection != 3 and selection != 4:
        print("You made an invalid selection, please try again")
        selection = int(input("1-create file\n2-read file\n3-add to file\n4-quit"))
    return selection

def create(glossary):
    overwrite=input("You are about to create a new file, existing data will be overwritten (q to quit).")
    if overwrite != "q":
        with open("Chapter10/glossary.json", "w") as write_file:
            json.dump(glossary, write_file, indent=4, sort_keys=True)
            print("glossary.json has been created")

def read():
    try:
        with open("glossary.json") as read_file:
            Dictionary = json.load(read_file)
    except FileNotFoundError:
        print("The file does not exist or cannot be found")
        print("Please make a different menu selection")
    else:
        print(Dictionary)
    
def get_term():
    term=input("Please enter a new term: ")
    return term

def get_definition():
    definition=input("Please enter the definition of the new term: ")
    return definition

def append(term, definition):
    if term == "" or definition == "":
        print("You have not entered a term of definition, please select another menu option")
    else:
        new_item = (f"{term}:{definition}")
        with open("Chapter10/glossary.json") as add_file:
            Dictionary = json.load(add_file)
            Dictionary.update(new_item)
            add_file.seek(0)
            json.dump(Dictionary, add_file, indent=4, sort_keys=True)
            print("Data has been added to glossary.json")


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

selection = 0
term = ""
definition = ""
while selection != 4:
    menu()
    if selection == 1:
        create(glossary)
    if selection == 2:
        read()
    if selection == 3:
        get_term()
        get_definition()
        append(term, definition)