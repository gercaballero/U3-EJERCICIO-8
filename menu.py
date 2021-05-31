import os
from classColeccion import Coleccion
class Menu:
    __switcher=None
    def __init__(self):
        self.__switcher = { 1:self.opcion1,
                            2:self.opcion2,
                            3:self.opcion3,
                            4:self.opcion4,
                            5:self.salir
                         }
    def getSwitcher(self):
        return self.__switcher
    def opcion(self,op,co):
        func= self.__switcher.get(op, lambda: print("Opción no válida"))
        func(co)

    def salir(self,co):
        print('Salida del programa')

    def opcion1(self,co):
        os.system('cls')
        print('---------GASTO SUELDO DE EMPLEADO---------')
        dni=input('INGRESE EL DNI DEL EMPLEADO:')
        band=False
        while not band and dni!=0:
            indice=co.gastosSueldoPorEmpleado(dni)
            if indice!=False:
                os.system('cls')
                print('---------GASTO SUELDO DE EMPLEADO---------')
                print('\nEL GASTO DE SUELDO DEL EMPLEADO CON DNI {} ES: {}'.format(dni,indice))
                band=True
            else:
                os.system('cls')
                print('---------GASTO SUELDO DE EMPLEADO---------')
                print('DNI NO SE ENCUENTRA. REINTENTE')
                dni=input('INGRESE EL DNI DEL EMPLEADO (0 para finalizar):')
        input()
        os.system('cls')
        
    def opcion2(self,co):
        band=False
        print('---------MODIFICAR SUELDO BASICO---------')
        dni=input('INGRESE EL DNI DEL EMPLEADO:')
        if dni!=0:
            sueldo=int(input('INGRESE NUEVO SUELDO BASICO: '))
        while not band and dni!=0:
            indice=co.modificarBasicoEPlanta(dni,sueldo)
            if indice!=False:
                os.system('cls')
                print('---------MODIFICAR SUELDO BASICO---------')
                print('<<<SUELDO DE EMPLEADO CON DNI {} MOFICIADO A {} PESOS'.format(dni,sueldo))
                band=True
            else:
                os.system('cls')
                print('---------MODIFICAR SUELDO BASICO---------')
                print('~DNI NO ENCONTRADO~\n')
                dni=input('INGRESE EL DNI DEL EMPLEADO (0 para finalizar):')
                if dni!=0:
                    sueldo=int(input('INGRESE NUEVO SUELDO BASICO: '))
        input()
        os.system('cls')
    def opcion3(self,co):
        band=False
        print('---------MODIFICAR MONTO VIATICO---------')
        dni=input('INGRESE EL DNI DEL EMPLEADO:')
        if dni!=0:
            sueldo=int(input('INGRESE NUEVO MONTO VIATICO: '))
        while not band and dni!=0:
            indice=co.modificarViaticoEExterno(dni,sueldo)
            if indice!=False:
                os.system('cls')
                print('---------MODIFICAR MONTO VIATICO---------')
                print('<<<MONTO VIATICO DE EMPLEADO CON DNI {} MOFICIADO A {} PESOS'.format(dni,sueldo))
                band=True
            else:
                os.system('cls')
                print('---------MODIFICAR MONTO VIATICO---------')
                print('~DNI NO ENCONTRADO~\n')
                dni=input('INGRESE EL DNI DEL EMPLEADO (0 para finalizar):')
                if dni!=0:
                    sueldo=int(input('INGRESE NUEVO MONTO VIATICO: '))
        input()
        os.system('cls')
        
    def opcion4(self,co):
        band=False
        print('---------MODIFICAR VALOR POR HORA---------')
        dni=input('INGRESE EL DNI DEL EMPLEADO:')
        sueldo=int(input('INGRESE NUEVO MONTO VIATICO: '))
        while not band and dni!=0:
            indice=co.modificarValorEPorHora(dni,sueldo)
            if indice!=False:
                os.system('cls')
                print('---------MODIFICAR VALOR POR HORA---------')
                print('<<<MONTO VIATICO DE EMPLEADO CON DNI {} MOFICIADO A {} PESOS'.format(dni,sueldo))
                band=True
            else:
                os.system('cls')
                print('---------MODIFICAR VALOR POR HORA---------')
                print('~DNI NO ENCONTRADO~\n')
                dni=input('INGRESE EL DNI DEL EMPLEADO (0 para finalizar):')
                if dni!=0:
                    sueldo=int(input('INGRESE NUEVO MONTO VIATICO: '))
        input()
        os.system('cls')