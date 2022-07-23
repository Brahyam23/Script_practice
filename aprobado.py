import sys

def validar_numero(num):
    if 0 <= num <=10:
        return True
    else:
        return False

if len(sys.argv) == 3:
    num1 = int(sys.argv[1])
    num2 = int(sys.argv[2])

    if validar_numero(num1) and validar_numero(num2):
        
        if num1 >= 7 and num2 >=7:
            print("Promocionado")
        
        elif num1 >= 4 and num2 >=4:
            print("Aprobado, debe rendir final")
        
        elif num1 < 4 and num2 < 4:
            print("Desaprobó ambos parciales, debe recursar")
        
        elif num1 < 4 or num2 < 4:
            if num1 < 4:
                print("Desaprobado, debe recuperar el primer parcial")
            else:
                print("Desaprobado, debe recuperar el segundo parcial")
else:
    print("Debes ingresar unicamente 2 valores")