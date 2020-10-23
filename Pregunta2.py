"""
    Escribir un codigo en python que sume y multiplique 
    respectivamente todos los numeros de una lista, ejemplo;
    Numeros=1 2 3 4, suma 10, multiplicacion 24.
"""
# importing module (./myModules/operation.py)
from myModules.operation import *
# creating list
listNumbers = [1, 3, 5, 10]
# instance module
opera = operation(listNumbers)
# print results
print(f'The list is : {listNumbers}')
print(f'Sum : {opera.suma()}')
print(f'Multi : {opera.multi()}')