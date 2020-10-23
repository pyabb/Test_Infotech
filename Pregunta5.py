"""
    Escribir una funcion sum() y una función multip() que sumen y multipliquen
    respectivamente todos los números de una lista.
    Por ejemplo: sum([1,2,3,4]) debería devolver 10 y multip([1,2,3,4]) debería devolver 24.
"""
# importing module
from myModules.utility5 import *
# create list
listNumber = [1, 2, 3, 4]
# print results
print(f'The list is : {listNumber}')
print(f'The sum is : {sum(listNumber)}') # use sum() function
print(f'The multip is : {multip(listNumber)}') # use multip() function