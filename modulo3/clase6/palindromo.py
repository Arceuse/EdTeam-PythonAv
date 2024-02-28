"""
palindromos:
radar
atar a la rata
"""


def palindromo(str_input):
    str_original = str_input.replace(" ", "")
    str_reverso = str_input[::-1].replace(" ", "")

    if (str_original == str_reverso):
        print("es un palindromo")
    else:
        print("no es un palindromo")


if __name__ == "__main__":
    str_input = input("Ingrese una frase: ")
    palindromo(str_input)
