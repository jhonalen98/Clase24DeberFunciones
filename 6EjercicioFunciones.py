# def operaciones_basicas(a, b):
#     suma = a + b
#     resta = a - b
#     return suma, resta

# resultadosuma, resultadoresta = operaciones_basicas(8, 3)
# print(f"Suma: {resultadosuma}, Resta: {resultadoresta}")

def operaciones_basicas(a, b):
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    return suma, resta, multiplicacion

resultadosuma, resultadoresta, resultadomultiplicacion = operaciones_basicas(8, 3)
print(f"Suma: {resultadosuma}, Resta: {resultadoresta}, Multiplicación: {resultadomultiplicacion}")
