def isInArray(startElement, endElement, elementToFind, elements):
  middle = int((startElement + endElement) / 2)
  midElement = elements[middle]
  if elementToFind == midElement:
    return True

  if startElement >= endElement:
    return False
  if elementToFind > midElement:
    return isInArray(middle + 1, endElement, elementToFind, elements)
  elif elementToFind < midElement:
    return isInArray(startElement, middle - 1, elementToFind, elements)


def Main():
  numbers = [2,8,22,44,56,65,72,101,208,452,801]
  
  # test all cases actually in array
  for number in numbers:
    print(isInArray(0, len(numbers) - 1, number, numbers))

  # test a few bad cases
  print(isInArray(0, len(numbers) - 1, 49, numbers))
  print(isInArray(0, len(numbers) - 1, 1000, numbers))
  print(isInArray(0, len(numbers) - 1, 666, numbers))

Main()
