def reverse_string(input_string):
    """
    Recursively reverses a given string.
    Args:
        input_string (str): The string to reverse.
    Returns:
        str: The reversed string.
    """
    if input_string == "":
        return ""  # Base case: empty string
    remaining_reversed = reverse_string(input_string[1:])
    return remaining_reversed + input_string[0]


# Get user input
user_input = input("Enter a string to reverse: ")

# Reverse the string
reversed_output = reverse_string(user_input)

# Display result
print("Reversed string:", reversed_output)
