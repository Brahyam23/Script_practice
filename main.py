import sys

print(sys.argv) #Argument value:Para mostrar valores agregados, siempre 
# los toma en formato de lista

# Como se llama el archivo que se acaba de ejecutar?
# print( sys.argv[0]) Al ser una LISTA, el nombre del archivo que se ejecutó
# siempre va a estar en el índice 0

if len(sys.argv) == 3:
    print(f"Estas ejecutando: {sys.argv[0]}")
    cadena = sys.argv[1]
    cantidad_repeticion = int(sys.argv[2])
    print( cadena * cantidad_repeticion )
else:
    print("Cantidad de argumentos inválidos")