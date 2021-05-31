import os
from menu import Menu
class Admin:
    def interfaces(self,id,menu,co):
        os.system('cls')
        if id.upper() == 'TESORERO':
            intento=3                #CADA VEZ QUE SE INGRESA MAL EL USUARIO Y/O CONTRASEÑA SE DESCUENTA UN INTENTO
            while intento!=0:
                print('\t--------INTERFAZ TESORERO--------\n')
                user=input('>>>>INGRESE USUARIO: ')
                passw=input('>>>>INGRESE CONTRASEÑA: ')
                salir=False
                if user.lower()=='utesorero' and passw=='ag@74ck':
                    while not salir:
                        os.system('cls')
                        print("-------------------Menu TESORERO-------------------")
                        print(' 1- GASTOS SUELDOS POR EMPLEADO')
                        print(' 2- SALIR')
                        op= input('\n INGRESE UNA OPCION: ')
                        if op in ('1','2'):
                            if op=='1':
                                menu.opcion(int(op),co)
                            if op=='2':
                                menu.opcion(int(5),co)
                                salir=True
                                intento=0
                                os.system('cls')
                        else:
                            os.system('cls')
                            print ("---OPCION NO VALIDA---")
                else:
                    intento-=1
                    if intento!=0:
                        os.system('cls')
                        print('\t--------INTERFAZ TESORERO--------\n')
                        print('xxxxxx USUARIO O CONTRASEÑA INCORRECTOS xxxxxx')
                        print('     xxxxxx INTENTOS RESTANTES {} xxxxxx'.format(intento))
                        input()
                        os.system('cls')
                    else:
                        os.system('cls')
                        print('\t--------INTERFAZ TESORERO--------\n')
                        print('xxxxxx USUARIO O CONTRASEÑA INCORRECTOS xxxxxx')
                        print('>>>>>SE SUPERO LA CANTIDAD DE INTENTOS<<<<<')
                        input()
                        salir=True
                        os.system('cls')
        elif id.upper() == 'GERENTE':
            intento=3
            while intento!=0:
                print('\t--------INTERFAZ GERENTE--------\n')
                user=input('>>>>INGRESE USUARIO: ')
                passw=input('>>>>INGRESE CONTRASEÑA: ')
                salir=False
                if user.lower()=='ugerente' and passw=='ufC77#!1':
                    os.system('cls')
                    while not salir:
                        print("-------------------Menu GERENTE-------------------")
                        print(' 1- MODIFICAR BASICO DE EMPLEADO DE PLANTA')
                        print(' 2- MODIFICAR VIATICO DE EMPLEADO EXTERNO')
                        print(' 3- MODIFICAR VALOR DE PAGO POR HORA EMPL. CONTRATADO')
                        print(' 4- SALIR')
                        op= input('\n INGRESE UNA OPCION: ')
                        if op in ('1','2','3','4'):
                            if op in ('1','2','3'):
                                menu.opcion(int(op)+1,co)
                            if op=='4':
                                menu.opcion(int(5),co)
                                salir=True
                                intento=0
                                os.system('cls')
                        else:
                            os.system('cls')
                            print ("---OPCION NO VALIDA---")
                else:
                    intento-=1
                    if intento!=0:
                        os.system('cls')
                        print('\t--------INTERFAZ GERENTE--------\n')
                        print('xxxxxx USUARIO O CONTRASEÑA INCORRECTOS xxxxxx')
                        print('     xxxxxx INTENTOS RESTANTES {} xxxxxx'.format(intento))
                        input()
                        os.system('cls')
                    else:
                        os.system('cls')
                        print('\t--------INTERFAZ GERENTE--------\n')
                        print('xxxxxx USUARIO O CONTRASEÑA INCORRECTOS xxxxxx')
                        print('>>>>>SE SUPERO LA CANTIDAD DE INTENTOS<<<<<')
                        input()
                        salir=True
                        os.system('cls')