import re

"""
sintaxis para lograr hacer busquedas basadas en patrones
"""

"""
expresiones regulares
"""
cadena = "vamos a aprender expresiones regulares con python"
busqueda = re.search("aprender", cadena)
print(busqueda)


"""
busqueda de fecha en base a un patron
"""
texto = ("la fecha de vencimiento es 2023-12-31 y"
         "la fecha de inicio fue 2023-01-15")
patron_fecha = r'\d{4}-\d{2}-\d{2}'
fechas_encontradas = re.findall(patron_fecha, texto)
print(fechas_encontradas)


"""
remplazo de texto basado en patrones
"""
texto = "el número de telegono es 001-376-1234"
patron_numero = r'\d{3}-\d{3}-\d{4}'
nuevo_texto = re.sub(patron_numero, "####", texto)
print(nuevo_texto)

"""
extracción de urls de un html
"""
html = "<p>enlace uno <a href='http://www.google.com'>Enlace 1</a></p>"
patron_url = r"<a href='(.*?)'>(.*?)</a>"
enlaces = re.findall(patron_url, html)
for enlace in enlaces:
    url, texto = enlace
    print(f"URL: {url}, texto: {texto}")
