import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def wordDefinition(word):
    word = word.lower()

    if word in data:
        return data[word]
    elif word.title() in data:
        return data[word.title()]
    elif word.upper() in data:
        return data[word.upper()]
    elif len(get_close_matches(word, data.keys())) > 0:
        yes_or_no = input("Did you mean '%s'? If Yes press 'Y', else press any other key: " %get_close_matches(word, data.keys())[0])
        if  yes_or_no == "Y" or yes_or_no == "Yes" or yes_or_no == "YES" or yes_or_no == "y" or yes_or_no == "yes":
            return data[get_close_matches(word, data.keys())[0]]
        else:
            word = input("Kindly provide the word you meant: ")
            return wordDefinition(word)
    else:
        return "\nNo such word!"

word = input("Kindly provide a word: ")
output = wordDefinition(word)

if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)

