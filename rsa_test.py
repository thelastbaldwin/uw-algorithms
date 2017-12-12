import math

def getLargest(list):
    return list[-1]

# returns true if greatest common divisor is 1
def areCoprime(a, b):
    return math.gcd(a, b) == 1

# used for e value
def getCoprimes(max):
    primes = []
    for i in range(2, max):
        if areCoprime(i, max):
            primes.append(i)
    return primes

# count of coprimes between known factors
def phi(p, q):
    return (p - 1) * (q - 1)

# mod value used for both keys
def getMod(p, q):
    return p * q

# return list of all potential d values up to max
def getDValues(e, totient, max):
    dees = []
    for i in range(2, max):
        if areValidConstants(i,e, totient):
            dees.append(i)
    return dees

def areValidConstants(e, d, totient):
    return (d * e) % totient == 1

def encryptRSA(val, e, mod):
    return (val ** e) % mod

def decryptRSA(val, d, mod):
    return (val ** d) % mod

def encryptMessage(message, e, mod):
    encryptedMessage = []

    for m in message:
        encryptedMessage.append(encryptRSA(ord(m), e, mod))

    return encryptedMessage

def decryptMessage(message, d, mod):
    decryptedMessage = []

    for m in message:
        decryptedMessage.append(chr(decryptRSA(m, d, mod)))

    return "".join(decryptedMessage)

p = 31
q = 53

# significantly faster with smaller numbers
# p = 17
# q = 29
mod = getMod(p, q)
totient = phi(p, q)
e = getLargest(getCoprimes(totient))
d = getLargest(getDValues(e, totient, e * 200))
# print(e)
# print(d)

message = "Violet Beauregarde"
secretMessage = encryptMessage(message, e, mod)
decryptedMessage = decryptMessage(secretMessage, d, mod)
print("Original Message: {}".format(message))
print("Secret Message: {}".format(secretMessage))
print("Decrypted Message: {}".format(decryptedMessage))