def check_palindrome(word):
    length = len(word)
    if word[0] != word[length-1]:
        return False
    elif word[1] != word[length-2]:
        return False
    else:
        return True

print(check_palindrome('cow'))
print(check_palindrome('radar'))
