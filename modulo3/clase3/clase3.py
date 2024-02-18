texto = """
lorem lorem2 lorem imput lorem imput lorem imput
lorem imput lorem imput lorem imput lorem imput
lorem imput lorem imput lorem imput lorem imput
lorem imput lorem imput lorem imput lorem imput
lorem imput lorem imput lorem imput lorem imput
lorem imput lorem imput lorem imput lorem imput
lorem imput lorem imput lorem imput lorem imput
lorem imput lorem imput lorem imput lorem imput
lorem imput lorem imput lorem imput lorem2 imput
"""

texto = texto.replace("lorem", "python", 1)

palabra_busqueda = input("Ingresa palabra a buscar: ")
index = texto.find(palabra_busqueda)

if (index != -1):
    print(f"{palabra_busqueda} se encontro en el indice {index}")

    total_encontrados = texto.count(palabra_busqueda)
    print(f"{palabra_busqueda} aparece {total_encontrados} veces")
else:
    print("No se encontro la palabra")

print(texto)
