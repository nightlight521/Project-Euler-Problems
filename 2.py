####################################
#Project Euler
#2. Sum of even Fibonacci numbers below 4 million
#Author: Paula Yuan
#Date: Oct. 22, 2018
##################################
n1 = 0
n2 = 1
nth = 0
acc = 0
while nth < 3000000:
    nth = n1 + n2
    n1 = n2
    n2 = nth
    if nth%2 == 0:
        acc = acc + nth
    print nth
print acc
