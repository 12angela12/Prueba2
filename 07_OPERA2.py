# ******** OPERACIONES RELACIONALES   O DE COMPARACION ********
# entrega solo dos valores verdadero o falso
# TRUE(1)   FALSE(0)
number = int(input('digite numero: '))
number > 3
print(number > 3)  #pregunta si number es mayor que 3 FALSE
print(number >= 3)  # pregunta si number es mayor o igual que 3  TRUE
print(number < 3)  # pregunta si number es menor que 3  TRUE
print(number <= 3)  # pregunta si number es menor o igual que 3  TRUE
print(number == 3)  # pregunta si es exactamente igual a 3
print(number != 3)  # pregunta si es diferente a 3

#******  OPERACIONES LOGICAS  ********
print('******  Operaciones Lógicas.*****')
# entrega solo dos valores verdadero o falso
# Conjuncion  (and &)
# Disyuncion (or |)
# Negación (not ~)
# or exclusiva (^)

# Conjuncion  (and &)      # valor1 and valor2
print("     Conjunción")
print(False and True)
print((number >= 3) and False)
print(True & True & False)  # cambiar operador and por el simbolo ampersan
print(number > 3 and number < 10)  # numero dentro del rango 3 y 10

# Disyuncion (or |)
print("    Disyunción")
print(False or False)  # el resultado sera False
print(False or True)  # el resultado sera True
print(True or True)  # el resultado sera True
print(number > 3 or number < 10)  # numero dentro del rango 3 y 10
print(number <= 3 or number >= 10)  # numero fuera del rango 3 y 10
print(not (number <= 3 | number >= 10))

# Negación (not )
print("    Negación")
print(not (True))

# or exclusiva (^)
print("   Or Exclusiva")
print(False ^ False)  # el resultado sera False
print(False ^ True)  # el resultado sera True
print(True ^ False)  # el resultado sera True
print(True ^ True)  # el resultado sera False

#    operaciones de CONTENIDO o PERTENENCIA (^)
# in    pregunta su un valor esta dentro de otro

print("   Operador   in")
nombre = 'Angela Martínez'
print('A' in nombre)  # A si esta dentro de nombre
print('Q' in nombre)  # el resultado sera False
