"""
    Desarrollar una funcion que me devuelva el n-esimo fibonacci
    Recordar que la serie fibonacci inicia en uno, es decir que 
    fibonacci(1) = 1, ademas que
    el fibonacci(3) = fibonacci(2) + fibonacci(1)

    Nota: Implementarlo de modo iterativo.
"""
# insert n-esimo number to fibonacci
value = input('Insert n-esimo number to search: ')
# restriccion the input valor
while True:
    if value.isdigit():
        value = int(value)
        break
    else:
        value = input('Insert n-esimo number to search: ')

# fibonacci function
def fibonacci(n):
    f1 = f2 = 1
    x = 2

    if n == 1 or n == 2:
        return f1
   
    else:
        while x < n:
            fn = f2 + f1 
            f1 = f2 
            f2 = fn
            x += 1
        return fn

# print the n-esimo fibonacci
print(fibonacci(value))