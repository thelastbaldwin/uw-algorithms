def doBinarySearch(input_list, searchValue):
  found = False
  first = 0
  top = len(input_list) - 1
  while not Found and first <= top:
    print("here")
    # find the midpoint between first and last
    mid = int((first + top) / 2)
    # if the midpoint = searchValue, update found
    if input_list[mid] == searchValue:
      print("here")
      found = True
      return mid
    # else if searchValue <= midpoint, update last
    elif searchValue < mid:
      top = mid - 1
    # else update first
    else:
      first = mid + 1
  return -1
  
def Main():
  arrayData = [ 2, 8, 15, -2, 31, 4, 1]
  print("doBinarySearch(5) = {}".format(doBinarySearch(arrayData, 5)))
  print("doBinarySearch(31) = {}".format(doBinarySearch(arrayData, 31)))





