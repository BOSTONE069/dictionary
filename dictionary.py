import json
from difflib import get_close_matches # this is the import library in python for geetin the close matches of the different words in the dictionary
data = json.load(open("data.json")) # THIS LOAD THE JSON FILE AND CONVERTS IT INTO PYTHON

def translate(word):
    word = word.lower() # this is to enable the display in forma of lower case
    if word in data:
        return data[word]
    elif word.title() in data: # this is to enable the display in form of title case
        return data[word.title()]
    elif word.upper() in data: # this is to enable the display in forma of upper case
        return data[word.upper()]
    elif len(get_close_matches(word , data.keys())) > 0: # this part of the code helps in finding the close matches in the user suggetsion in the dictionaries
        print("did you mean %s instead" %get_close_matches(word , data.keys())[0])
        decide = input("press y for yes of n for no")
        if decide == "y":
            return data[get_close_matches(word , data.keys())[0]]
        elif decide == "n":
            return("Your word could not be found")
        else:
            return("You have entered the wrong word please write again")
    else:
        print("You have entered the wrong word please write again")

word = input("Enter the word you want to search")
output = translate(word)
if type(output) == list: # this is to enable display in form of list
    for item in output:
        print(item)
else:
    print(output)
