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
        print('ingrese los datos que se muestran a continuacion')
        fila['ORDER_ID']=input('numero de orden: ')
        fila['PRICE_TOTAL']=input('precio: ')
        fila['PRODUCT_ID']=input('id del producto: ')
        fila['NAME']=input('nombre del producto: ')
        fila['NROSERIE']=input('numero de serie:')
        fila['CANTIDAD']=input('cantidad: ')
        fila['PRODUCT']=input('producto: ')
        fila['PRICE_UNIT']=input('precio por unidad: ')
        fila['CATEGORIA']=input('categoria: ')
        fila['STOCK_ACUTAL']=input('stock: ')
        fila['DATE']=input('fecha de compra: ')
        fila['USER_ADMIN']=input('nombre del admin: ')
        fila['USER_CLIENT']=input('nombre del cliente: ')
    print(df)
    
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