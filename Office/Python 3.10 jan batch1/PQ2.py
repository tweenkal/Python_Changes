def reverse_only_letters(var):
    """
    Reverse only alphabetic characters in the string,
    keeping all non-alphabetic characters in the same position.
    """
    chars = list(var)
    left = 0
    right = len(chars) - 1

    while left < right:
        if not chars[left].isalpha():
            left += 1
        elif not chars[right].isalpha():
            right -= 1
        else:
            chars[left], chars[right] = chars[right], chars[left]
            left += 1
            right -= 1

    return "".join(chars)

print(reverse_only_letters("a-bC-dEf-ghIj"))
# Output: j-Ih-gfE-dCba

print(reverse_only_letters("Test1ng-Leet=code-Q!"))
# Output: Qedo1ct-eeLg=ntse-T!
