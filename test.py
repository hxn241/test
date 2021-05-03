#!/usr/bin/env python
# coding: utf-8

# In[1]:


import subprocess
import pandas as pd
import datetime
def ip_scan(fichero): # creamos una función que desempeñará todo.
    
    with open(fichero) as f: #abrimos el fichero y nos guardamos todas las lineas en una variable.
        lines = f.readlines()
    cont=0
    df = pd.DataFrame(index = list(range(100)),columns=['ip','protocol','puerto']) # definimos dataframe
    
    for i,k in enumerate(lines): # bucle en el archivo de ips fichero.txt.

        string_443 ="nmap -p 8443-8443 {}".format(k)
        string_8443 = "nmap -p 8443-8443 {}".format(k)
        result_443_ip= subprocess.getoutput(string_443)
        result_8443_ip= subprocess.getoutput(string_8443)
        file = open("ip_scan_{}.txt".format(k), "w") 
        file.write(result_443_ip) 
        file.write(result_8443_ip)
        file.close()
                                            # asignamos la salida de cada comando a una variable y lo devolvemos en un txt con el resultado.

        scan_443 = "sslscan {}:{} grep -F Preferred".format(k,443)
        scan_8443 = "sslscan {}:{} grep -F Preferred".format(k,8443)

        result443 = subprocess.getoutput(scan_443)
        result8443 = subprocess.getoutput(scan_8443)
        
                                            # volvemos a asignar el output a una variable, luego hacemos loop y buscamos sobre ellas la línea
                                            # Preferred, que es lo que estamos buscando.
                                            # se ha hecho solo sobre la preferred.
        cont+=1
        for item1 in result443.split("\n"): # leemos linea a linea por cada archivo de puertos diferente 
                                            #y buscarmos el término "preferred" y asignamos la parte que nos interesa a un DF.

            if "Preferred" in item1:
                #print(item1.split(' ')[1])
                k=k.replace('\n',"")
                df['ip'].loc[cont] = k
                df['protocol'].loc[cont] = item1.split(' ')[1]
                df['puerto'].loc[cont] = 443
                cont+=1

        for item2 in result8443.split("\n"):

            if "Preferred" in item2:
                #print(item2.split(' ')[1])
                k=k.replace('\n',"")
                df['ip'].loc[cont] = k
                df['protocol'].loc[cont] = item2.split(' ')[1]
                df['puerto'].loc[cont] = 8443
                cont+=1
                                            # Tenemos que quedarnos con los datos limpios para ello usamos libreria como str.split para separar 
                                            # y quedarnos la parte que queremos.
                                        
    
                                            #clean and adapt the dataframe
                                            # creamos columnas, limpiamos y dejamos el dataframe tal cual el ejercicio(limpieza y dtypes)
    df.dropna(inplace=True)
    df['protocol'][3] = df['protocol'][3][5:12]
    df['protocol'][6] = df['protocol'][6][5:12]
    df['SSLv2'] = False
    df['SSLv3'] = False
    df ['TLSv1.0'] = False
    df ['TLSv1.1'] = False
    df ['TLSv1.2'] = False
    df['TLSv1.3'] = False
    df['Fecha'] = datetime.datetime.now()
    date=datetime.datetime.now().date()
    date=pd.to_datetime(date)
    df['Fecha']=pd.to_datetime(date)
    df=df.reset_index().reset_index()
    df.drop(['index'],axis=1,inplace=True)
    df.rename(columns={'level_0':'index'},inplace=True)
    
    for i,x in enumerate(df['protocol']):     # asignamos True a los protocolos que tenga cada ip en la columna correspondiente.
        if x  in df:
            df[x][i]=True
    df.drop(['protocol'],inplace=True,axis=1)
    
                                                #dataframe to SQLalchemy(sqlite3) Libreria para pasar de Dataframe a crear la base de datos.
    from sqlalchemy import create_engine
    engine = create_engine('sqlite:///ssldb.db', echo=True)
    sqlite_connection = engine.connect()
    sqlite_table = "ips"
    df.to_sql(sqlite_table, sqlite_connection, if_exists='fail')
    sqlite_connection.close()
    return df


# In[2]:


df = ip_scan('fichero.txt')

