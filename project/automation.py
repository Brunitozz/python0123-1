import pandas as pd
import os
import db
import requests
def insertData():
    #obtiene la ruta absoluta
    path_=os.getcwd()+'\dataTienda.csv'
    #conection a bd
    conn=db.Conection('tienda.db')
    cursor=conn.getCursor()
    print(path_)
    df = pd. read_csv (path_, sep = ";") 
    ### logica para insertar 
    for i,fila in df.iterrows():
        print(fila['ORDER_ID'],fila['PRICE_TOTAL'],fila['PRODUCT_ID'],fila['NAME'],fila['NROSERIE'],fila['CANTIDAD'],fila['PRODUCT'],fila['PRICE_UNIT'],fila['CATEGORIA'],fila['STOCK_ACUTAL'],fila['DATE'],fila['USER_ADMIN'],fila['USER_CLIENT'])

def updateDolar():
    url = 'https://api.apis.net.pe/v1/tipo-cambio-sunat' #tipo cambio sunat
    respons=requests.get(url)
    data = respons.json()
    compra_dolar=data['compra']
    venta_dolar=data['venta']
    print(f'la venta del dolar es {compra_dolar} y la venta es {venta_dolar}')
    pass

message="""
    1)Insertar data:
    2)Actualizar data del dolar
"""
print(message)

while True:
    try:
        a=int(input('ingrese la tarea a realizar: '))
        if a==1:
            insertData()
            break
        elif a==2:
            updateDolar()
            break        
        else:
            None
    except Exception as m:
        print('ERROR EN LA EJECUCIÓN', m)