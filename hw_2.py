def stringToInt(str):
    num = 0
    power = 0

    for i in range(len(str)-1, -1, -1):
        currentNum = ord(str[i]) - ord('0')
        num += currentNum * 10 ** power
        power = power + 1

    return num


def Main():
  value = "1024"
  convertedValue = stringToInt(value)
  print(type(convertedValue) is int and convertedValue == 1024)

Main()