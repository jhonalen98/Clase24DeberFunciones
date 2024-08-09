# def funcionexterior():
#     def funcioninterior():
#         print("Esta es la función interior")
#     funcioninterior()
#     print("Esta es la función exterior")
    
# funcionexterior()

def funcionexterior():
    def funcioninterior(nombre):
        print(f"{nombre}, Esta es la función interior")
    funcioninterior("Jhon")
    print("Esta es la función exterior")
    
funcionexterior()
