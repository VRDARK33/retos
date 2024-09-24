""" EJERCICIO:
 * - Crea ejemplos utilizando todos los tipos de operadores de tu lenguaje:
 *   Aritméticos, lógicos, de comparación, asignación, identidad, pertenencia, bits...
 *   (Ten en cuenta que cada lenguaje puede poseer unos diferentes)
 * - Utilizando las operaciones con operadores que tú quieras, crea ejemplos
 *   que representen todos los tipos de estructuras de control que existan
 *   en tu lenguaje:
 *   Condicionales, iterativas, excepciones...
 * - Debes hacer print por consola del resultado de todos los ejemplos.
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea un programa que imprima por consola todos los números comprendidos
 * entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
 *
 * Seguro que al revisar detenidamente las posibilidades has descubierto algo nuevo."""

#operadores aritmeticos

suma = 2 + 2
resta = 5 - 2
multiplicacion = 2 * 2
division = 9 / 2
modulo = 2 % 2
potencia = 2 ** 3
division_entera = 5 // 2

print(f'suma 2 + 2 = {suma}' )
print(f'resta  5 - 2 = {resta}' )
print(f'multiplicacion 2 * 2 = {multiplicacion}' )
print(f'division 9 / 2 = {division}' )
print(f'modulo 10 % 2 = {modulo}' )
print(f'potencia 2 ** 3 = {potencia}' )
print(f'division_entera 5 // 2 = {division_entera}' )


#operadores de asignacion

numero = 23
print(numero) #asignacion
numero += 1
print(numero) # suma y asignacion
numero -= 2
print(numero) # resta y asignacion
numero *= 4
print(numero) # multiplicacion y asignacion
numero /= 2
print(numero) # division y asignacion
numero %= 5
print(numero) # modulo y asignacion
numero **= 2
print(numero) # exponenciacion y asignacion
numero //= 3
print(numero) # division entera y asignacion

#operadores de comparacion 

#igual a 
print(f" 10 igual que 4  {10 == 4 }")
#diferente de 
print(f"10 diferente de 3  {10 != 3}")
#mayor que
print (f"10 es mayor que 3 {10 > 3}")
#menor que 
print(f"10 es menor que 3 {10 < 3}")
#mayor o igual que
print (f"10 es mayor o igual que 9 {10 >= 9}")
#menor o igual que 
print(f"10 es menor o igual que 10 {10 <= 10}")

#operadores logicos

#operado AND   
print(f"5 > 3 and 3==3 {5>3 and 3==3}")

#operado OR 
print(f"5 > 6 or 2 < 4 { 5 > 6 or 2 < 4 }")

#operador NOT 
print(f"not 10 + 3 == 14 {not 10 + 3 == 14}")

#operadores de identidad

#operador is 


numeroNuevo = numero

print(f"b  apunta al mismo objetos en la memoria que a {numero is numeroNuevo}")


#operador is not

d = [1,2,3]
c = d

print(f"b  apunta al mismo objetos en la memoria que a {c is not d}")

#operadores de pertenencia 

#operador in

a = [1,2,3]
b = 2 

print(f'b pertenece a a {b in a}')

#operador not in

a = [1,2,3]
b = 4
print(f'b no pertenece a a {b not in a}')


#operadores bit a bit 

#operador and 

a = 5 # 0101
b = 9 # 1001
      # 0001

print(a&b)

"""
 * DIFICULTAD EXTRA (opcional):
 * Crea un programa que imprima por consola todos los números comprendidos
 * entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
"""

for numeros in range(10, 56):
      if numeros % 2 == 0 and numeros != 16 and  numeros % 3 !=0:
            print(numeros)

