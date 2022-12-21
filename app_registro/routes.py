from app_registro import app
from flask import render_template,request,redirect
import csv
from datetime import date

@app.route("/")
def index():
    #llama al archivo
    fichero = open("data/movimientos.csv","r")
    #accede a cada registro de arhivo y lo formatea
    csvReader = csv.reader(fichero,delimiter=",",quotechar='"')
    #creo un array datos vacio para cargar los registros del archivo
    datos=[]
    #recorrer el objeto csvReader y cargar cada registro al array datos
    for item in csvReader:
        datos.append(item)
    return render_template("index.html",pageTitle="Listas",lista=datos)


@app.route("/new",methods=["GET","POST"])
def create():
    if request.method == "GET":#esto puede ser POST o GET
        return render_template("new.html",pageTitle="Alta",typeAction="Alta",typeButon="Guardar",dataForm={})   
    else:
        #acceder al archivo y configurarlo para cargar un nuevo registro
        mifichero =  open('data/movimientos.csv','a',newline='')
        #llamamos al metodo writer de escritura y cargamos el formeto para csv
        lectura= csv.writer(mifichero, delimiter=',',quotechar='"')
        
        error = validateForm(request.form)#validamos los datos de formulario

        if error:
            #hay error
            return render_template("new.html",pageTitle="Alta",typeAction="Alta",typeButon="Guardar",msgError=error,dataForm=request.form)
        else: 
            #no hay errores lo registramos
            #registramos los datos recibidos desde el formulario con request.form y lo añadimos con el metodo writerrow
            #acceder al archivo y configurarlo para cargar un nuevo registro
            mifichero =  open('data/movimientos.csv','a',newline='')
            #llamamos al metodo writer de escritura y cargamos el formeto para csv
            lectura= csv.writer(mifichero, delimiter=',',quotechar='"')
            lectura.writerow([request.form['date'],request.form['concept'],request.form['quantity']])    

            #crear id
            fichero = open("data/movimientos.csv","r")
            csvReader = csv.reader(fichero,delimiter=",",quotechar='"')   



            lectura.writerow([request.form['date'],request.form['concept'],request.form['quantity']])
            
            
            




        mifichero.close()

    return redirect('/')


        
   
@app.route("/update/<int:id>")
def edit(id):
    pass





    #return render_template("update.html",pageTitle="Modificación",typeAction="Modificación",typeButon="Editar") 

@app.route("/delete/<int:id>")
def remove(id):
    pass



    #return render_template("delete.html",pageTitle="Eliminar")

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
        


    
        
