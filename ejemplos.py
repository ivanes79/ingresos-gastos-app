'''

with open('data/movmiento.txt',"r") as resultado:
    leer = resultado.read()# solo 'read' lo lee todo
    print(leer)

result = open("data/movimiento.txt","r")
lectura = result.readlines()
print(lectura)

import csv

datos = []
mifichero = open("data/movimiento.txt","r")
mifichero = csv.reader(mifichero,delimiter=",",quotechar='"')

for registros in mifichero:
    datos.append(registros)
    print(registros)

print("esto es datos:",datos)
mifichero.close()# siempre que se abra un fichero se tiene que cerrar

mifichero = open('data/movimientos.txt','a',newline='')
lectura=csv.writer(mifichero,delimiter=',',quotechar='"')
lectura.writerow(['20/12/2022''compra de turrones',300])
mifichero.close()
'''
from datetime import date


