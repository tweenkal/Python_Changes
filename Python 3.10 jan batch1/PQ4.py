def list_nouns(nouns):
    """
    Create a grammatically correct sentence from a list of nouns.
    """
    result = []

    for word in nouns:
        if word[0].lower() in "aeiou":
            result.append("an " + word)
        else:
            result.append("a " + word)

    if len(result) == 2:
        sentence = result[0] + " and " + result[1]
    else:
        sentence = ", ".join(result[:-1]) + " and " + result[-1]

    return sentence.capitalize() + "."


print(list_nouns(["orange", "apple", "pear"]))
print(list_nouns(["keyboard", "mouse"]))
print(list_nouns(["car", "plane", "truck", "boat", "apple"]))
