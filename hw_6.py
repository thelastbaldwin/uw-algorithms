def strCompare(str1, str2, caseInsensitive=False):
    if len(str1) != len(str2):
        return False

    # distance between capital and lowercase letters
    # http://www.asciitable.com/
    caseDist = 32 if caseInsensitive else 0

    for i, char in enumerate(str1):
        dist = abs(ord(char) - ord(str2[i]))
        if dist not in (0, caseDist):
            return False

    return True

print(strCompare("hello", "hello", False) == True)
print(strCompare("hello", "hello", True) == True)
print(strCompare("hello", "HELLO", False) == False)
print(strCompare("hello", "HELLO", True) == True)
print(strCompare("hElLo", "HeLlO", True) == True)
print(strCompare("hell", "HELLO", True) == False)