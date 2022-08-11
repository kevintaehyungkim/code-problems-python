

### Find the nth number in the fib sequence ###
'''
The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence, 
such that each number is the sum of the two preceding ones, starting from 0 and 1. 
That is,

F(0) = 0,   F(1) = 1
F(N) = F(N - 1) + F(N - 2), for N > 1.
Given N, calculate F(N).
'''
def fib(self, N):
    a, b = 0, 1
	for i in range(N): a, b = b, a + b
	return a



### The Fizz Buzz problem ###
# time O(n)
# space O(1)
def fizzBuzz(n):
    res = []
    for i in range (1,n+1):
        if i % 15 == 0:
            res.append("FizzBuzz")
        elif i % 3 == 0:
            res.append("Fizz")
        elif i % 5 == 0:
            res.append("Buzz")
        else:
            res.append(str(i))
    return res



### Reverse Bits ###
def reverseBits(self, n):
    bit_str = '{0:032b}'.format(n)
    reverse_str = bit_str[::-1]
    return int(reverse_str, 2)


########################
### BASIC CALCULATOR ###
########################

# given a string, evaluate it as a math expression and return the result
#
# assumptions:
#   you do not need to validate the input, you can assume it will always be valid
#   all characters in the string will be a digit or an operator
#   allowed operators are +, -, *, /
#   all numbers in the expression are integers >= 0
#   you will never encounter division by 0
#
# correct order of operations should be followed:
#   1. multiplication and division
#   2. addition and subtraction
#
# examples:
#   "1+7"       -> 8
#   "8+2-6+2"   -> 6
#   "8/4+3"     -> 5
#   "1+2*3"     -> 7 

def calculate(string):
num = 0
stack = []
sign = '+'

for i in range(len(string)):
    s = string[i]
    if i == len(string)-1 or not s.isdigit():
        if sign == '-':
            stack.append(-num)
        elif sign == '+':
            stack.append(num)
        elif sign == '*':
            stack.append(stack.pop()*num)
        else:
            stack.append(float(stack.pop())/num)
        sign = s
        num = 0
    else:
    	num = 10*num + int(s)
    
return sum(stack)



"""
I think the first q was like printing a tree that has a and b as nodes
sanjay gupta (Founder, CEO Genentech)
and the parents can be either | or +
sanjay gupta (Founder, CEO Genentech)
and basically if it's a|b then you get set(a, b)
sanjay gupta (Founder, CEO Genentech)
and if it's + you get set(ab)
sanjay gupta (Founder, CEO Genentech)
and then you recursively build it
sanjay gupta (Founder, CEO Genentech)
and then after she asked me to construct the tree given a string like
sanjay gupta (Founder, CEO Genentech)
Arno Chang
(a | (a + b | (a + b))) or something



they gave me relatively easier questions involving trees and data structures





design a system for
a set of recipes
and a set of ingredients
and the recipes could be made up of raw ingredients and also of compound ingredients
and yeah I made some objects and did some tree shit
and basically had to return what could be made and so forth
and then the follow up was like adding stock to each ingredient



last question was a variation of largest island matrix
except it was like largest land mass that could have water inside it
so basically you have to first take out all the water that touches the edges
and then the largest landmass with the land remaining kinda
I did it in some 3 pass janky way where
I filled in the land masses
and then did largest land mass LOL
but the dude liked me and we kinda clicked so I guess it was fine







"""