# <QUESTION 1>

# Given a list of items, return a dictionary mapping items to the amount
# of times they appear in the list

# Note: the order of this dictionary does not matter

# <EXAMPLES>

# one(['apple', 'banana', 'orange', 'orange', 'apple', 'apple']) → {'apple':3, 'orange':2, 'banana':1}
# one(['tic', 'tac', 'toe']) → {'tic':1, 'tac':1, 'toe':1}
    
def one(items):
    thisdict = {}
    for x in items:
        if x in thisdict.keys():
            thisdict[x] += 1
        else:
            thisdict[x] = 1

    return thisdict

# <QUESTION 2>

# Given two numbers, a & b, and an operator, evaluate the operation between a & b
# using the given operator

# The operator will be a string, and will only be +, -, *, or /. 

# <EXAMPLES>

# two(2, 4, '+') → 6
# two(7, 3, '-') → 4
# two(3, 1.5, '*') → 4.5
# two(-5, 2, '/') → -2.5

def two(a, b, operator):
    numberA = float(a)
    numberB = float(b)
    result = 0

    if operator == '+':
        result = numberA + numberB
    elif operator == '-':
        result = numberA - numberB
    elif operator == '*':
        result = numberA * numberB
    elif operator == '/':
        result = numberA/numberB
    if result % 1 == 0:
        return int(result)
    else:
        return result

        
# <QUESTION 3>

# Given a positive integer, return the next integer below it that has an
# integer square root (is the square of another integer)

# If the number has a square root, just return the number

# <EXAMPLES>

# three(7) → 4          # 4 is the square of 2
# three(64) → 64        # 64 is the square of 8 already
# three(32) → 25

# <HINT>

# We can use `x ** 0.5` to get the square root of `x`

def three(num):
    squareRoot = num ** 0.5
    while squareRoot % 1 != 0:
        num -= 1
        squareRoot = num ** 0.5
    return num


# <QUESTION 4>

# Given two integers, return the greatest common factor of the two numbers

# <EXAMPLES>

# four(32, 24) → 8
# four(18, 11) → 1
# four(10, 50) → 10

def four(a, b):
    cf = max(a,b)
    while a % cf != 0 or b % cf != 0:
        cf -= 1
    return cf



# <QUESTION 5>

# Given a string, return a string where each letter is the previous letter in the alphabet
# in comparison to the original string

# For a or A, use z or Z respectively

# Ignore characters that aren't in the alphabet, such as whitespace or numbers

# <EXAMPLES>

# five('wxyz') → 'vwxy'
# five('abc') → 'zab'
# five('aAbB') → 'zZaA'
# five('hello world') → 'gdkkn vnqkc'
# five('54321') → '54321'

def five(string):
    result = ''
    for char in string:
        if char.isalpha():

            if char == 'a':
                char = 'z'
            elif char == 'A':
                char = 'Z'
            else:
                char = chr(ord(char) - 1 )
            result +=char
        elif char == " ":
            result += char
        else: 
            result += char
    return result

print (five('hello world'))
