# y = 10
# def modificar_global():
#     global y
#     y = 20
#     print(f"Variable global y modificada dentro de la función: {y}")
# modificar_global()
# print(f"Variable global y fuera de la función: {y}")

nuevaVariable = 10
def modificar_global():
    global nuevaVariable
    nuevaVariable = 25
    print(f"Variable global y modificada dentro de la función: {nuevaVariable}")
modificar_global()
print(f"Variable global y fuera de la función: {nuevaVariable}")