import re
import time
from components import gotoxy
class Validar():
    def letras(text,fila,columna):
        while True:
            gotoxy(fila,columna);cadena=input(text)
            if cadena.isalpha() and not re.search(r"[^a-zA-Z0-9]",cadena):
                return cadena
            else:
                gotoxy(fila+len(text),columna);print(' '*20)
                gotoxy(fila+len(text),columna);print('Solo letras')
                time.sleep(2)
                gotoxy(fila+len(text),columna);print(' '*20)

    def Dni(text,fila,columna):
        while True:
            gotoxy(fila,columna);cedula=input(text)
            if len(cedula)==10 and cedula.isdigit:
                coeficientes = [2, 1, 2, 1, 2, 1, 2, 1, 2]
                suma = 0
                
                for i in range(9):
                    digito = int(cedula[i]) * coeficientes[i]
                    if digito > 9:
                        digito -= 9
                    suma += digito
            
                total = suma % 10
                if total != 0:
                    total = 10 - total                
                if total == int(cedula[9]):
                    return cedula
                else:
                    gotoxy(len(text),columna);print(' '*22)
                    gotoxy(len(text),columna);print('No es una cedula real')
                    time.sleep(2)
                    gotoxy(len(text),columna);print(' '*22)
                    
            else:
                    gotoxy(len(text),columna);print(' '*22)
                    gotoxy(len(text),columna);print('No es una cedula real')
                    time.sleep(2)
                    gotoxy(len(text),columna);print(' '*22)
                    
    def numerosEnteros(text,fila,columna):
        while True:
            try:
                gotoxy(fila,columna);number=float(input(text))
                if number.is_integer():
                    number=int(number)
                    return number
                else:
                    print('Solo numeros enteros')        
            except ValueError:
                gotoxy(fila+len(text),columna);print(' '*20)
                gotoxy(fila+len(text),columna);print('Solo numeros')
                time.sleep(2)
                gotoxy(fila+len(text),columna);print(' '*20)
    def numerosDecimales(text,fila,columna):
        while True:
            try:
                gotoxy(fila,columna);number=float(input(text))
                number_fort=round(number,2)
                return number_fort
            except ValueError:
                gotoxy(fila+len(text),columna);print(' '*20)
                gotoxy(fila+len(text),columna);print('Solo numeros')
                time.sleep(2)
                gotoxy(fila+len(text),columna);print(' '*20)
        
