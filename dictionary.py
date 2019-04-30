import json
from difflib import get_close_matches

data = json.load(open('data.json'))


def display(lst):
    count = 1
    for item in lst:
        print(str(count) + ": " + item)
        count += 1


def cont():
    print("Do you want to continue using the Dictionary? Y or N")
    action = str.upper(input())
    if action == "Y":
        definition()
    elif action == "N":
        quit()
    else:
        print("Please enter Y or N")
        cont()


def definition():
    print("Please enter a word: ")
    word = str.lower(input())
    recommended = get_close_matches(word, data.keys(), cutoff=0.8)
    if word in data:
        display(data[word])
        print()
        cont()

    elif word.title() in data:
        display(data[word.title()])
        print()
        cont()

    elif word.upper() in data:
        display(data[word.upper()])
        print()
        cont()

    elif len(recommended) > 0:
        print("No results found, perhaps you should try: ", ", ".join(recommended))
        definition()
    else:
        print("Word not found in dictionary")
        cont()


if __name__ == "__main__":
    definition()
