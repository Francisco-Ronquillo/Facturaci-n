import os
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
MAGENTA = "\033[95m"
CYAN = "\033[96m"
RESET = "\033[0m" 
class Menu():
    def __init__(self,title="",option=[]):
        self.title=title
        self.option=option

    def menu(self):
        fila=0
        print(self.title)
        for option in self.option:
            fila+=1
            print(f"{fila}){option}")
        option=input('Escoja una opcion 1...'+str(fila)+': ' )
        return option
def limpiarPantalla():
    os.system("cls")

def dibujarCabez(title=''):
    limpiarPantalla()
    print(GREEN,'='*120)
    gotoxy(50,2)
    print(BLUE,title)
    print(GREEN,'='*120)
    


def gotoxy(x,y):
    print("%c[%d;%df"%(0x1B,y,x),end="")

