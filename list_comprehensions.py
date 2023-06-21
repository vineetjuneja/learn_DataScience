"""
here's my version if-elif using list comprehension

 [<expression> if <condition> <2nd_expression> else <elif condition> else <3rd_expression> for <iterator> in <the_iterable>]

example: Suppose we need to create a list of multiples of 6 that fulfils the following conditions:
1. for even numbers between 1 to 10 multiply by 6
2. for multiples of 5, multiply by 5
3. for rest of the numbers, multiply by 3.

Please note: this is just for practice; as it gets more complex and less readable for other coders. So better try traditional loops and expressions when it gets too complex :-)

CODE BELOW:
"""

# complex list comprehension
print(
    [i*6 if i%2==0 else i*5 if i%5==0 else i*3 for i in range (1,11)]
)

sum_up = reduce (lambda x,y: x*y, [i for in range(1,11)])
print (sum_up)

# missed import random