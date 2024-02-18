cadena = "Python es genial"
caracter = cadena[7:9]
print(caracter)
caracter2 = cadena[0:10:2]
print(caracter2)
reversa = cadena[::-1]
print(reversa)

lenguajes_de_programacion = 'Python php go c# javascript java'
lista_de_lenguajes = lenguajes_de_programacion.split(' ')
print(lista_de_lenguajes)

print(lista_de_lenguajes[2:4])
print(lista_de_lenguajes[0:4:2])

email = "usuario@gmail.com"
dominio = email[email.index("@") + 1:]
print(dominio)
