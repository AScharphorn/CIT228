def count_words(filename):
    """Count the approximate number of words in a file."""
    try:
        with open(filename, encoding='utf-8') as f:
            contents = f.read()
    except FileNotFoundError:
        pass
    else:
        words = contents.split()
        num_words = len(words)
        print(f"The file {filename} has about {num_words} words total.")

def find_words(filename, searchword):
    try:
        with open(filename, encoding='utf-8') as f:
            contents = f.read()
    except FileNotFoundError:
        pass
    else:
        words= contents.count(searchword)
        print(f"The word '{searchword}' occured {words} in the {filename} file.")

filenames = ['Chapter10/the_ones_who_got_me_here.txt', 'Chapter10/my_faith_in_you.txt', 'Chapter10/dont_you_worry_child.txt']
for filename in filenames:
    count_words(filename)
searchword=input("What common word would you like to search for within these files? ")
for filename in filenames:
    find_words(filename,searchword)