# Condicional   if
'''
numero = int(input('Sr usuario, digite un numero:'))
# if('condicion')  # argumento dentro del paréctesis
# if(numero>50): # siempre termina con los dos puntos
if(numero > 50):
  print('VERDADERO')
  print('SI ESTA CORRECTO')
  print('EXCELENTE')
else:
  print('FALSO')
  print('NO ESTA CORRECTO')
  print('QUE MAL')
print('la instrucción IF terminó')
print('FIN')
'''
adivinar = 42
numero = int(input('Sr usuario, digite un numero:'))
if(numero > adivinar):
  print('Bájele el volumen')
elif (numero < adivinar):
  print('Súbale el volumen')
else:
  print("VERDADERO")
  print('la instrucción IF terminó')
# IF anidado if dentro de otro if    else if = elif

