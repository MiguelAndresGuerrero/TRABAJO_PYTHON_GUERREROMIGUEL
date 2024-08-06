import json
def abrirArchivo():
    with open(r"info.json","r") as openfile:
        return json.load(openfile)
    
def guardarArchivo(data):
    with open(r"info.json", "w") as outfile:
        json.dump(data, outfile, indetnt=4)

print("Bienvenido Usuario")

def menu(productos):
    for producto in producto:
        print("""
              ===============================================
                                    MENU
              ===============================================
              1. 
              """)