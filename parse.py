def IntToString(val):
  output = ""
  isNegative = val < 0

  if isNegative:
    output = "-" + output
    val = -val


  factor = 1
  # calculate the factor necessary
  # to grab the first digit of the value.
  while val / factor > 10:
    factor = factor * 10

  # process whole part
  while factor >= 1:
    # grab the first digit of the value.
    digit = (val / factor)

    # concatenate the digit to the 
    # string. make sure to integerize
    # the digit because it's really
    # a fractional number.
    output = output + str(int(digit))

    # reduce the value by the
    # digit * the factor. This will
    # get the remainder out.
    val = val - int(digit) * factor

    # reduce the factor
    factor = factor / 10

  # process fractional part (0.1465)
  # digits = 6
  # output = output + "."
  # while val != 0.0 and digits > 0:
  #   # push the first fractional digit
  #   # to the left of the decimal.
  #   val = val * 10
  #   digit = int(val)
  #   output = output + str(digit)
  #   val = val - digit

  #   # only display up to 6 digits
  #   digits = digit - 1

  return output

def parseInt(char):
  return ord(char) - ord('0')

def StringToInt(inputString):
  value = 0
  isNegative = inputString[0] == "-"

  # for each character
  for s in inputString:
    if s != "-":
      # else convert inputChar to numberValue using ascii
      value = value * 10
      value = value + parseInt(s)
      # and value = value * 10 + numberValue

  value = -value if isNegative else value
  return value

def IntToStringTest(number):
  result = IntToString(number)
  print("{} to string = {}".format(number, result))

def StringToIntTest(string):
  result = StringToInt(string)
  print("{} to int = {}".format(string, result))

IntToStringTest(0)
IntToStringTest(-1023)
IntToStringTest(41)
IntToStringTest(18293)
IntToStringTest(41.234)
IntToStringTest(425.923522)
IntToStringTest(4321.1465)

StringToIntTest("-1023")
StringToIntTest("42")
StringToIntTest("512")
