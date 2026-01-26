"""
Flatten a nested list into a single-level list using recursion.
"""
def flatten_list(nested_list):
    """Recursively flatten a nested list."""
    flat_result = []
    for element in nested_list:
        if isinstance(element, list):
            flat_result.extend(flatten_list(element))
        else:
            flat_result.append(element)
    return flat_result

user_input = input("Enter a nested list (e.g., [1, [2, [3, 4], 5], [6, 7]]): ")
nested_list = eval(user_input)
flat_list = flatten_list(nested_list)
print(flat_list)
