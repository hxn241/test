# Ip scanning test python script

- Script de python que analizá un fichero de ip's dado en un txt en el mismo directorio.
- El script generará archivos txt del contenido devuelto en cada scanning y devolverá una base de datos "ssldb.db" con la tabla "ips" y las columnas siguientes:   index,ip,puerto,SSLv2,SSLv3,TLSv1.0,TLSv1.1,TLSv1.2,TLSv1.3,Fecha.

### Intrucciones:
Instalar o checkear las librerías:
- pip install subprocess
- pip install pandas
- pip install Datetime
- pip install sqlalchemy==1.3.15
- 
También puedes crear un Environment con conda mediante el comando siguiente y el fichero .yml.
- conda env create -f environment_test.yml

Todos los archivos serán creados en el mismo directorio del repo clonado.
El fichero de ip's se tiene que llamar fichero.txt y contener una ip por línea para que funcione correctamente.

 
