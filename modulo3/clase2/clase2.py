"""
concatenacion
"""
cadena1 = "mi edad es "
cadena2 = 25
resultado = cadena1 + str(cadena2)
print(resultado.upper())

"""
nombre = input("ingresa tu nombre: ")
apellido = input("ingresa tu apellido: ")
edad = int(input("Edad: "))
print("hola mi nombre es " + nombre + " " + apellido)
saludo = f"hola mi nombre es {nombre} {apellido} y tengo {edad} años"
print (saludo)
"""

"""
concatenar con listas
"""
numeros = [1, 2, 3, 4, 5]
resultado = ""
for num in numeros:
    resultado += str(num) + " "
print(resultado)


"""
concatenación con join
"""
palabras = ["Hola", "mundo", "Python"]
frase = " ".join(palabras)
print(frase)
