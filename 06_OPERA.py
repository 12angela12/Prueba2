# ****** OPERACIONES ARIMETICAS ******

# SUMA + , RESTA -  , MULTI * ,  DIVI / , DIV ENTERA //,
# RESIDUO O MODULO %, POTENCIA **
# Jerarquia (primero se realizan las oper dentro de (), luego los exponentes, luego multi y div, y por ultimo suma y resta)

number = int(input('digite numero: ')
)  # le pregunta al Us un numero y luego con print comienzan las respuestas
'''print(f'la suma con 2 es:{number + 2}')
print(f'la resta con 2 es:{number - 2}')
print(f'la multiplicación con 2 es:{number * 2}')
print(f'la división con 2 es:{number / 2}')
print(f'la división ENTERA con 2 es:{number // 2}')
print(f'El residuo con 2 es:{number % 2}')
print(f'La potencia con 2 es:{number ** 2}')
'''

# ******  OPERACIONES DE ASIGNACION  ******

contador = 1
print(f'antes de la operación +=  es: {contador}')
contador += 1  # += contador asignacion incremental

contador = 9
print(f'despues de la operación  += es: {contador}')
contador -= 1  # -= contador asignacion decremental

number += 1
print(f'Al usar operador incremental += resultado es : {number}')
number -= 1
print(f'Al usar operador decremental 1= resultado es : {number}')
number *= 2
print(f'Al usar operador  *= resultado es : {number}')
number /= 2
print(f'Al usar operador /= resultado es : {number}')
number //= 2
print(f'Al usar operador // resultado es : {number}')
number %= 3
print(f'Al usar operador %= resultado es : {number}')
number **= 2
print(f'Al usar operador**= resultado es : {number}')
'''



