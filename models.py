import csv
from config import *
import os

def select_all():
    """
    devolvera una lista con todos los registros del 
    fichero MOVIMIENTOS_FILE
    """
    fichero = open(MOVIMIENTOS_FILE,"r")
    csvReader = csv.reader(fichero,delimiter=",",quotechar='"')
    datos=[]
    for item in csvReader:
        datos.append(item)
    fichero.close()

    return datos    

def select_by(id):
    """
    devolvera un registro con el id de la entrada o vacio si no lo encuentra  en el fichero MOVIMIENTOS_FILE
    """
    mifichero =  open(MOVIMIENTOS_FILE,'r')
    lectura= csv.reader(mifichero, delimiter=',',quotechar='"')
    registro_buscado=[]
    for registro in lectura:
        if registro[0] == str(id):
            registro_buscado = registro

    diccionario = dict()

    nombres = ["id", "date", "concept", "quantity"]

    for i in range(len(nombres)):
        diccionario[nombres[i]]=registro_buscado[i]



    '''
    diccionario["id"] = registro_buscado[0]#id
    diccionario["date"] = registro_buscado[1]#date
    diccionario["concept"] = registro_buscado[2]#concept
    diccionario["quantity"] = registro_buscado[3]#quantity
    '''


    mifichero.close()
       
    return diccionario   

def delete_by(id):
    """
    borrará el registro cuyo id coincide con el de la entrada en el fichero MOVIMIENTOS_FILE
    """
    fichero_old =  open(MOVIMIENTOS_FILE,'r')#acceder al csv de registros
    fichero = open(MOVIMIENTOS_FILE_NEW,'w',newline="")#acceder a un archivo auxiliar

    csvReader= csv.reader(fichero_old, delimiter=',',quotechar='"')
    csvWriter = csv.writer( fichero , delimiter=',',quotechar='"')

    for registro in csvReader:
        if registro[0] != str(id):#mientras el id sea distinto del proporcionado para borrar que escriba en fichero
            csvWriter.writerow(registro)

    fichero_old.close()
    fichero.close()    

    os.remove(MOVIMIENTOS_FILE)#funcion remove que recibe la ruta del archivo a eliminar
    os.rename(MOVIMIENTOS_FILE_NEW,MOVIMIENTOS_FILE)#funcion para renombrar que recibe
    

def insert(registro_form):
    """
    crear un nuevo registro, siempre y cuando sea compatible con el fichero,
    asignara al registro un id unico(acumulativo)
    """
               
    mifichero =  open(MOVIMIENTOS_FILE,'a',newline='')
    lectura= csv.writer(mifichero, delimiter=',',quotechar='"')
    
    #crear id
    fichero = open(LAST_ID_FILE,"r")
    registro = fichero.read()
    if registro == "":
        new_id=1
    else:    
        new_id = int(registro)+1
    
    fichero.close()

    ficheroG =  open(LAST_ID_FILE,'w')
    ficheroG.write(str(new_id))
    ficheroG.close()

    lectura.writerow( [str(new_id)]+registro_form)    

    mifichero.close()


def update_by(id,registro_modificado):
    fichero_old =  open(MOVIMIENTOS_FILE,'r')#acceder al csv de registros
    fichero = open(MOVIMIENTOS_FILE_NEW,'w',newline="")#acceder a un archivo auxiliar

    csvReader= csv.reader(fichero_old, delimiter=',',quotechar='"')
    csvWriter = csv.writer( fichero , delimiter=',',quotechar='"')

    for registro in csvReader:
        if registro[0] != str(id):#mientras el id sea distinto del proporcionado para borrar que escriba en fichero
            csvWriter.writerow(registro)
        else:
            csvWriter.writerow([str(id)] + registro_modificado)
    fichero_old.close()
    fichero.close()    

    os.remove(MOVIMIENTOS_FILE)#funcion remove que recibe la ruta del archivo a eliminar
    os.rename(MOVIMIENTOS_FILE_NEW,MOVIMIENTOS_FILE)

