def is_palindrome(input_string):
    # Remove spaces and convert to lowercase for case-insensitive comparison
    new_string = input_string.replace(" ", "").lower()
    
    # Compare the string with its reversed version
    return new_string == new_string[::-1]

# Test cases
print(is_palindrome("racecar"))  # True
print(is_palindrome("hello"))  # False
print(is_palindrome("A man a plan a canal Panama"))  # True
