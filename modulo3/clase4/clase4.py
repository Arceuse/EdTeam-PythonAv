from datetime import datetime

name = "César"
age = 30
print(f"Mi nombre es {name} y tengo {age} años")
print("Mi nombre es {} y tengo {} años".format(name, age + 10))

sql_insert = "insert into users(name, age) values ( '{}', '{}' )".format(
    name, age)
print(sql_insert)

print("Nombre: : {1}, Edad : {0}".format(age, name))

"""
print con parametros
"""

producto = "Celular Iphone 12"
precio = 599.99

print("Producto : {prod}, Precio : {pre:.3f}".format(
    prod=producto, pre=precio))

"""
formatear numeros
"""
num = 12345.6889
print("{:.2f}".format(num))
print("{:,}".format(num))
print("{:e}".format(num))

"""
formatear fechas
"""
now = datetime.now()
print("Fecha y hora: {: %d/%m/%Y %H:%M:%S }".format(now))

"""
alineación y relleno
"""
number = 42
print("Número : {:s>10}".format(number))
print("Número : {:1<5}".format(number))
