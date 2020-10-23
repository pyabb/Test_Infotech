"""
    Crear una funcion que determine si dado una serie de parentesis,
    estas se encuentran en pares, es decir,
    abierto '(' y cerrado ')'.
    Ejm:
    Entrada: '(()()())()()(())'
    Salida: True

    Entrada: '(()('
    Salida: False
"""
# verify function
def verify(_string):
    # use count() function to search quantity especific of a character
    x = _string.count('(')
    y = _string.count(')')
    # conditional sentence.
    # If the number of characteres '(' is equal ')'
    print(x)
    print(y)
    if x == y:
        return True
    else:
        return False

# insert parenthesis for keyboard
param = str(input('Insert the quantity of parenthesis : \n'))
# print result
print(verify(param))