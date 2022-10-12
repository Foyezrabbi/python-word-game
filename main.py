import json
import difflib
from difflib import get_close_matches

data = json.load(open("data.json"))


def translate(word):
    word = word.lower()

    if word in data:
        return data[word]

    elif len(get_close_matches(word, data.keys())) > 0:
        yn = input("did you mean %s instead? Enter y if yes or N for No: " % get_close_matches(word, data.keys())[0])
        if "y" in yn.lower():
            return data[get_close_matches(word, data.keys())[0]]
        elif "n" in yn.lower():
            return "Word Doesnt Exist"
        else:
            return "We didnt understand you entry!"
    else:
        return "Word Doesnt Exist"


user_word = "rainn"
output = translate(user_word)

if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)
