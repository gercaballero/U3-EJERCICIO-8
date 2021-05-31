from classEmpleado import Empleado
from classEmpPlanta import EmpleadoPlanta
from classEmpContratados import EmpleadoContratado
from classEmpExterno import EmpleadoExterno
from classIGerente import IGerente
from classITesorero import ITesorero
from zope.interface import implementer
import csv
import numpy as np
@implementer(IGerente)
@implementer(ITesorero)
class Coleccion:
    __arreglo=None
    __dimension=0
    __indice=0
    __carga=False
    
    def __init__(self,dimension):
        self.__arreglo=np.empty(dimension,dtype=Empleado)
        self.__dimension=dimension
        self.__indice=0
        self.__carga=False
    
    def agregarEmpleado(self,empleado):
        if isinstance(empleado, Empleado):
            if self.__indice==self.__dimension:
                print('ARREGLO NO PERMITE MAS TALLERES')
            else:
                self.__arreglo[self.__indice]=empleado
                self.__indice+=1  
    
    def test(self,nombre):
        archivo=open(nombre)
        reader=csv.reader(archivo,delimiter=',')
        empleado=None
        for fila in reader:
            if len(fila)==6:
                empleado=EmpleadoPlanta(fila[0], fila[1], fila[2], fila[3], float(fila[4]), int(fila[5]))
            if len(fila)==7:
                empleado=EmpleadoContratado(fila[0], fila[1], fila[2], fila[3], fila[4], fila[5], int(fila[6]))
            if len(fila)==10:
                empleado=EmpleadoExterno(fila[0], fila[1], fila[2],
                                         fila[3], fila[4], fila[5],
                                         fila[6], float(fila[7]),
                                         float(fila[8]), float(fila[9]))
            self.agregarEmpleado(empleado)
        archivo.close()
        
    def buscarIndice(self,dni):
        band=False
        i=0
        while not band and i<self.__dimension:
            if self.__arreglo[i].getDni().upper()==dni.upper() and isinstance(self.__arreglo[i], EmpleadoContratado):
                    band=True
            else:
                i+=1
        if band:
            retorna=i
        else:
            retorna=band
        return retorna

    def gastosSueldoPorEmpleado(self,dni):
        band=False
        i=0
        while not band and i<self.__dimension:
            if self.__arreglo[i].getDni().upper()==dni.upper():
                    band=True
            else:
                i+=1
        if band:
            retorna=self.__arreglo[i].sueldo()
        else:
            retorna=band
        return retorna
    def modificarBasicoEPlanta(self,dni,nuevoBasico):
        band=False
        i=0
        retorna=None
        while not band and i<self.__dimension:
            if self.__arreglo[i].getDni().upper()==dni.upper() and isinstance(self.__arreglo[i], EmpleadoPlanta):
                    band=True
            else:
                i+=1
        if band:
            self.__arreglo[i].setSueldoBasico(nuevoBasico)
        else:
            retorna=band
        return retorna
        
    def modificarViaticoEExterno(self,dni, nuevoViatico):
        band=False
        i=0
        retorna=None
        while not band and i<self.__dimension:
            if self.__arreglo[i].getDni().upper()==dni.upper() and isinstance(self.__arreglo[i], EmpleadoExterno):
                    band=True
            else:
                i+=1
        if band:
            self.__arreglo[i].setMontoViatico(nuevoViatico)
        else:
            retorna=band
        return retorna  
    
    def modificarValorEPorHora(self,dni, nuevoValorHora):
        band=False
        i=0
        retorna=None
        while not band and i<self.__dimension:
            if self.__arreglo[i].getDni().upper()==dni.upper() and isinstance(self.__arreglo[i], EmpleadoContratado):
                    band=True
            else:
                i+=1
        if band:
            self.__arreglo[i].setValorHora(nuevoValorHora)
        else:
            retorna=band
        return retorna  

        