def magic_function(list_input):
    list_output = [a[::-1] for a in list_input]

    """list_output = []
    for a in list_input:
    list_output.append(a[::-1])"""
    return list_output


A = ["hello world", "hello python", "1 2 3 4 5 6 7 8"]
B = magic_function(A)
print(B)
