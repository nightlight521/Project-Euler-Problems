####################################
#Project Euler
#4. Largest palindromic number as product of 2 3-digit numbers
#Author: Paula Yuan
#Date: Oct. 22, 2018
##################################
import math

def isPalindrome(num):
    last = len(num) - 1
    i = 0
    while i < last:    
        if num[i] != num[last]:
            return False
        last = last - 1
        i = i + 1
    return True

def largestPalindrome():
    largest = 0
    for i in range(100, 1000):
        for j in range(i, 1000):
            product = i * j
            if isPalindrome(str(product)) and product > largest:
                largest = product
    return largest


def listMax(l):
    partialMax = l[0]
    for i in range(len(l)):
        if l[i] > partialMax:
            partialMax = l[i]
    return partialMax 


def listSum(l):
    listSum = 0
    for i in range(len(l)):
        listSum = listSum + l[i]
    return listSum
