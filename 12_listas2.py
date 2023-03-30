num = [99,34,25,56,72]  # llamado arreglo
print(num)
num[1]= 88  # mutable cambio el 34 por el 88
print(num)
#num = [99,88,25,56,72]  
print('    FUNCIOn   INSERT')
num.insert(1,77) # [99,77,88,25,56,72]
print(num)

print('    FUNCIOn   APPEND') # adicionar a lista
num.append(100)
print(num)  # [99,77,88,25,56,72,100]
num2= [9,8,7]
print(num)

print('    FUNCIOn   EXTEND') # fusion de listas
num.extend(num2)
print(num)

print('    FUNCIOn   REMOVE') # eliminar elemento
# [99,77,88,25,56,72,100,9,8,7]
num.remove(100) # borra el valor señalado 100
print(num)
num.pop(0) # borra la posicion 0, 99
num.pop() # borra la ultima posicion

print('    FUNCIOn   DEL') # 
del num[0]
print(num) # [77,88,25,56,72,100,9,8,7]

print(num)