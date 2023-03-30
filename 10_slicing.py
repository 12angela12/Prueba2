nombre = "Cesar Quintero"
#     INDEXING
print(nombre[0])  # posicion indice de la letra C
print(nombre[4])  # posicion indice de la letra r
#     SLICING
# Cesar Quintero
# 1,2,3,4,5,6,7,8,9,10,11,12,13
# C e s a r Q i n t  e  r  o

print(nombre[1:4])  # recortando cadena de caracteres
print(nombre[2:7])
print(nombre[7:12])
print(nombre[0:18])  # NO genera lio un numero mayor
print(nombre[0:])
print(nombre[0::2])  # MAS USADA caracter por caracter de 2en2
print(nombre[0:13])
print(nombre[0:13:2])  # imprime Cesar Q caracteres seguidos
print(nombre[0:13:3])  # imprime CsrQ  es decir de 2 en 2

print("conteo regresivo")
print(nombre[-1:-9:-1])
print(nombre[-1::-1])
