# Aplicación web ingresos-gastos
-Programa hecho en python con el framework Flask, Hello Word


# En su entorno de python ejecutar el comando
pip install -r requirements.txt
las libreria utilizada flask https://flask.palletsprojects.com/en/2.2.x/

# Ejecucion del programa
-inicializar el servidor de flask,agregando estos comandos a la terminal

en mac: export ```FLASK_APP=hello.py```
en windows: set ```FLASK_APP=hello.py```

## Comando para ejecutar el servidor:
```
flask --app hello run
```
## Comando para actualizar el servidor con cambios de codigo en tiempo real
```
flask --app hello --debug run
```
## Comando especial para lanzar el servidor en un puerto diferente

-Esto se utiliza en el caso que el puerto 5000 este ocupado
```
flask --app hello run -p 5001
```
## Comando para lanzar en modo debug y con puerto cambiado
```
flask --app hello --debug run -p 5001
```