def two_sum(numbers, target_sum):
    """
    Return indices of two numbers in 'numbers' that add up to 'target_sum'.
    """
    number_to_index = {}
    for current_index, current_number in enumerate(numbers):
        required_number = target_sum - current_number

        if required_number in number_to_index:
            return [number_to_index[required_number], current_index]

        number_to_index[current_number] = current_index


numbers = [2, 7, 11, 15]
target_sum = 9
print(two_sum(numbers, target_sum))  # Output: [0, 1]

numbers = [3, 2, 3, 1, 4]
target_sum = 7
print(two_sum(numbers, target_sum))  # Output: [0, 4]
