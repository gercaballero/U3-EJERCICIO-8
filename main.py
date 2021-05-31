from classColeccion import Coleccion
from menu import Menu
import os
from classAdmin import Admin
if __name__=='__main__':
    co=Coleccion(10)
    co.test('planta.csv')      #CARGA EMPLEADOS DE PLANTA
    co.test('contratados.csv')  #CARGA EMPLEADOS CONTRATADOS
    co.test('externos.csv')     #CARGA EMPLEADOS EXTERNOS
    menu= Menu()
    admin=Admin()               #CLASE ADMIN CON MENUS DE TESORERO Y GERENTE
    salir=False
    os.system('cls')
    while not salir:
        print('\t---<--<---INTERFAZ GENERAL--->-->---\n')
        ad=input('>>>INGRESAR COMO (TESORERO/GERENTE/SALIR): ')
        if ad.upper() in ('TESORERO','GERENTE'):
            admin.interfaces(ad,menu,co)    #ENVIA QUE TIPO DE USUARIO CON EL MENU Y LA COLECCION
        elif ad.upper() =='SALIR':
            os.system('cls')
            print('\n\t~~~~ SALIENDO DEL PROGRAMA ~~~~ ')
            input()
            salir=True
            os.system('cls')
        else:
            os.system('cls')
            print('\t ------OPCION INCORRECTA------\n')