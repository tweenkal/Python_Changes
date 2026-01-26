def clean_string(s):
    """Return lowercase letters of a string, ignoring non-letters."""
    return ''.join(filter(str.isalpha, s.lower()))


def are_anagrams(str1, str2):
    """Return True if two strings are anagrams, ignoring case and spaces."""
    str1_clean = clean_string(str1)
    str2_clean = clean_string(str2)

    return sorted(str1_clean) == sorted(str2_clean)


string1 = "Listen"
string2 = "Silent"

print(are_anagrams(string1, string2)) 
