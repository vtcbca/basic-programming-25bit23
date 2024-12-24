def is_palindrome(s):
    s = s.lower().replace(" ", "")  # Normalize the string
    if len(s) <= 1:
        return True
    if s[0] != s[-1]:
        return False
    return is_palindrome(s[1:-1])

# Example usage
print(is_palindrome("civic"))  # True
print(is_palindrome("science"))  # False
