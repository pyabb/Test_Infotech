"""
    Generar un codigo en python que sume 10 numeros aleatorios de la siguiente forma:
    Los 5 más bajos y los 5 más altos
"""
# importing module (./myModules/numbers.py)
import random
from myModules.numbers import *
# create empty list
numberList = []

# create ten random numbers
for x in range(10):
    numberList.append(random.randint(1,101)) # push in numberList
print(f'The ten numbers are:\n\n{numberList}') # print list

# sort ascending
numberList.sort()
low = numbers(numberList) # instance
print(f'\nThe sum of the five SMALLEST numbers is : {low.sumNumbers()}') # print result

# sort descending
numberList.reverse()
high = numbers(numberList) # isntance
print(f'\nThe sum of the five LARGEST numbers is : {high.sumNumbers()}') # print result

