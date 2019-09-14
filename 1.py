####################################
#Project Euler
#1. Sum of all multiples of 3 or 5 below 1000
#Author: Paula Yuan
#Date: Oct. 22, 2018
##################################
acc = 0
acc2 = 0
acc3 = 0
for count in range(0, 1000, 3):
    acc = acc + count
for count in range(0, 1000, 5):
    acc2 = acc2 + count
for count in range(0, 1000, 15):
    acc3 = acc3 + count
print acc+acc2-acc3

