####################################
#Project Euler
#3. Largest prime factor of 600851475143 (could be better)
#Author: Paula Yuan
#Date: Oct. 22, 2018
##################################
import math
num = 0
sqrt = int(math.sqrt(600851475143))
for count in range(sqrt):
    num = count
    for i in range(2,num):
        if (num % i) != 0:
            if 600851475143 % num == 0:
                print num
        num = num + 1
                
     
