# Ip scanning test python script

- Script de python que analiza y escanea un fichero de ip's dado en un txt llamado fichero.txt con una ip por línea.
- El script generará archivos txt del contenido devuelto en cada escaneo y devolverá una base de datos "ssldb.db" con la tabla "ips" y las columnas siguientes:   ### dbname:
- ssldb
### dbtable: 
- ips
### campos de la tabla: 
- indice: autogenerado incremental (clave primaria)
- ip: tipo string
- puerto: tipo integer
- SSLv2: tipo booleano (1/0)
- SSLv3: tipo booleano (1/0)
- TLSv1.0: tipo booleano (1/0)
- TLSv1.1: tipo booleano (1/0)
- TLSv1.2: tipo booleano (1/0)
- TLSv1.3: tipo booleano (1/0)            
- Fecha: Unixtime


### Intrucciones:
Instalar o checkear las librerías:
- pip install subprocess
- pip install pandas
- pip install Datetime
- pip install sqlalchemy==1.3.15


También puedes crear un Environment con conda mediante el comando siguiente y el fichero .yml.
- conda env create -f environment_test.yml


Todos los archivos serán creados en el mismo directorio del repositorio clonado.
El fichero de ip's se tiene que llamar fichero.txt y contener una ip por línea para que funcione correctamente.

Ejecución:
En terminal de comandos y en el mismo directorio del repositorio ejecutar el siguitente comando:
- python test.py
