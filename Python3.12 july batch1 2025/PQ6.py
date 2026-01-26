def rotate_consonant_simple(char):
    """
    Rotate consonant to next consonant using ASCII values.
    Vowels and non-letters remain unchanged.
    """
    vowels = "aeiouAEIOU"
    if not char.isalpha() or char in vowels:
        return char  # Return vowels and non-letters unchanged

    # Get ASCII code
    next_char = chr(ord(char) + 1)

    # Loop until we find the next consonant
    while next_char in vowels or not next_char.isalpha():
        next_char = chr(ord(next_char) + 1)
        # Wrap around z->b or Z->B
        if char.islower() and next_char > 'z':
            next_char = 'b'
        elif char.isupper() and next_char > 'Z':
            next_char = 'B'

    return next_char

def rotate_string_simple(input_string):
    """
    Rotate all consonants in the string using simpler ASCII logic.
    """
    return "".join(rotate_consonant_simple(c) for c in input_string)

# Example usage
s = "Hello-World!"
rotated = rotate_string_simple(s)
print("Original:", s)
print("Rotated :", rotated)
