from app_registro import app
from flask import render_template,request,redirect
import csv
from datetime import date
from config import *
import os #modulo para renombrar y eliminar archivos
from models import delete_by, insert, select_all, select_by, update_by


@app.route("/")
def index():
    
    datos = select_all()
    
    return render_template("index.html",pageTitle="Listas",lista=datos)


@app.route("/new",methods=["GET","POST"])
def create():
    if request.method == "GET":#esto puede ser POST o GET
        return render_template("new.html",pageTitle="Alta",typeAction="Alta",typeButon="Guardar",dataForm={},urlform="/new")   
    else:

        error = validateForm(request.form)#validamos los datos de formulario

        if error:
            #hay error
            return render_template("new.html",pageTitle="Alta",typeAction="Alta",typeButon="Guardar",msgError=error,dataForm=request.form)
        else: 

           insert([request.form['date'],
                   request.form['concept'],
                   request.form['quantity']])    

        

    return redirect('/')


        
   
@app.route("/update/<int:id>",methods=["GET","POST"])
def edit(id):
    if request.method =="GET":

        registro = select_by(id)
        print("aqui",type(registro))

        return render_template("update.html",pageTitle="Modificación",typeAction="Modificación",typeButon="Editar",dataForm=registro,urlform="/update/"+str(id)) 
    else:
        error = validateForm(request.form)#validamos los datos de formulario

        if error:
            #hay error
            return render_template("update.html",pageTitle="Modificación",typeAction="Modificación",typeButon="Editar",msgError=error,dataForm=request.form)
        else: 

            update_by(id,[request.form['date'],
                   request.form['concept'],
                   request.form['quantity']])  
           
           
    return redirect("/") 
      


@app.route("/delete/<int:id>", methods=["GET","POST"])
def remove(id):

    #1-consultar en data/movimientos.csv y recuperar el registro con id de la peticion
    #2-devolver al formulario html para borrar que los campos no sean modificables
    #3-tendria un boton para confirmar el borrado, si da accion a este boton borrar el registro dado
    if request.method == "GET":

        registro_buscado = select_by(id)

        if len(registro_buscado) > 0:
            return render_template("delete.html",pageTitle="Eliminar",registros=registro_buscado)
        else:
            return redirect("/")
    else:

        delete_by(id)


    return redirect("/")     
        




#crear una funcion para validar formulario de registro donde controlemos lo siguiente:
#1-que la fecha no sea mayor a la actual
#2-que el concepto no vaya vacio
#3-que la cantidad sea distinto de 0 y de vacio

def validateForm(requestForm):
    hoy = date.today().isoformat()
    errores=[]
    if requestForm['date'] > hoy:
        errores.append("fecha invalida: La fecha introducida es a futuro")
    if requestForm['concept'] == "":
        errores.append("concepto vacio: Introduce un concepto para el registro")
    if requestForm['quantity'] == "" or float(requestForm['quantity']) == 0.0:
        errores.append("cantidad vacio o cero: Introduce una cantidad positiva o negativa")   
    return errores


    
        
