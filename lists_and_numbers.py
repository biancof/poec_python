"""
Some functions on numbers and lists.
"""

# It creates a copy of a list

def copyList(list):
    newList=[] ## copy of list
    for i in list:
        newList.append(i)
    return newList

# It calculates the sum of the values of a list

def sum(list):
    res = list[0]
    for i in list:
        res += i
    return res

# It calculates the minimum value in a list

def min(list):
    listMin = copyList(list)
    listMin.sort()
    return listMin[0]

# It calculates the maximum value in a list

def max(list):
    listMax = copyList(list)
    listMax.sort()
    return listMax[len(listMax) - 1]

# It calculates the average value in a list

def average(list):
    return sum(list) / len(list)

# It verifies if n is a prime number or not
# It is used by getPrimeNumbers() function (see below)

def isPrime(n):
    res = True ## n is a prime number
    if n < 2:
        res = False ## n is not a prime number
    else:
        for i in range(2, n):
            if n % i == 0:
                res = False ## n is not a prime number
    return res

# It gives all prime numbers of a list (list) in a new sorted list (primeNums)

def getPrimeNumbers(list):
    primeNums = []
    for i in list:
        if isPrime(i):
            primeNums.append(i)
    primeNums.sort()
    return primeNums

# It creates a copy of a list with inverted order
# It uses python reverse() function

def invert(list):
    invList = copyList(list)
    invList.reverse()
    return invList

# It creates a copy of a list with inverted order
# It doesn't use python reverse() function
# and it doesn't work yet :-(

def invertDifficult(list):
    invList = copyList(list)
    for i in range(len(invList) - 1, 0, -1):
        n = invList[i - 1]
        invList.append(n)
        invList.remove(n)

# End of functions

# Test code for the functions

list = [4,2,3,1,5] # Sample list

print(f"List of numbers: {list}")                                   # Sample list (original)
print(f"Sum = {sum(list)}")                                         # sum test
print(f"Min = {min(list)}")                                         # min test
print(f"Max = {max(list)}")                                         # max test
print(f"Average = {average(list)}")                                 # average test
print(f"Prime numbers = {getPrimeNumbers(list)}")                   # getPrimeNumbers test
print(f"Inverted list of numbers (easy method): {invert(list)}")    # invert (easy ,ethod) test