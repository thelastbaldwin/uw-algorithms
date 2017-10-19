import math

def base62toBase10(numToConvert):
    base62Lookup = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    convertedNumber = 0
    currentBase = 0

    for i in range(len(numToConvert)-1, -1, -1):
        currentLetterValue = base62Lookup.find(numToConvert[i])
        convertedNumber += currentLetterValue * 62 ** currentBase
        # convertedNumber = convertedNumber * 62 + currentLetterValue
        currentBase += 1

    return convertedNumber

print(base62toBase10("LpuPe81bc2w"))