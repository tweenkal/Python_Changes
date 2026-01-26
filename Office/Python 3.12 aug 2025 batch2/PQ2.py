"""
Run-Length Encoding (RLE) Compression
Accepts a string from the user and compresses it by replacing consecutive
repeating characters with the character followed by its count.
"""
input_string = input("Enter a string to compress: ")

compressed_result = ""
repeat_count = 1

for current_index in range(1, len(input_string)):
    current_char = input_string[current_index]
    previous_char = input_string[current_index - 1]

    if current_char == previous_char:
        repeat_count += 1
    else:
        compressed_result += previous_char + str(repeat_count)
        repeat_count = 1

compressed_result += input_string[-1] + str(repeat_count)
print("Compressed string:", compressed_result)
