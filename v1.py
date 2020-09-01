import json
import os
from difflib import SequenceMatcher,get_close_matches           # only for close matches

if os.path.exists("./data.json"):
    data = json.load(open("./data.json"))
else:
    print("Error occured during opening dictionary!!\n")

def meaning(inp):
    inp = inp.lower()
    if inp in data.keys():                  # to handle words in the dictionary
        return data[inp]
    elif inp.title() in data.keys():        # to handle capitalised words like Delhi. Comment this block to see the difference
        return data[inp.title()]
    elif len(get_close_matches(inp,data.keys(),cutoff=0.8)) > 0 and inp != "\end":      # if exact match not foundn
        m = get_close_matches(inp,data.keys(),cutoff=0.8)[0]
        v = input("Did you mean \'%s\' instead? Enter Y for yes : " % m)
        if v == 'Y' or v == 'y':
            return data[m]
        else:
            return "Word not found!"
    else:
        return "Word doesn't exist!"

word = ''

while word != "\end":
    i = 1
    print("Enter '\end' to quit")
    word = input("Enter a word: ")
    wordMeaning = meaning(word)
    if word != "\end" :
        if isinstance(wordMeaning, list):
            for item in wordMeaning:
                print("%s. %s" % (i,item))
                print()
                i+=1
        else:
            print(wordMeaning)
            print()