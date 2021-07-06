#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Modulos importados
import sqlite3
import time
import os
from tkinter import *
import threading

global variables, tablas, BBDD, RESET
#Declaracion de las funciones
def limpiar():
    """Limpia la pantalla"""
    if os.name == "posix":
        os.system("clear")
    elif os.name == ("ce", "nt", "dos"):
        os.system("cls")   
def CrearTabla(nombre,columnas):
    #Comprueba si las tablas "HashtagList,RegistroList,MisVariables" existen, en caso de no existir alguno la creara
    #cursor.execute("""CREATE TABLE IF NOT EXISTS  ( TEXT, TEXT)""")
    """
    CrearTabla("Nombre_de_la_tabla",["primer_campo TEXT","segundo_campo TEXT","tercero_campo TEXT","cuarto_campo TEXT"])
    CREATE TABLE IF NOT EXISTS nombre (variable TEXT, valor TEXT)
    """
    comandoSQL="CREATE TABLE IF NOT EXISTS "+str(nombre)+" "
    colum="("
    for col in range(0,(len(columnas)-1),1):
        colum=colum+str(columnas[col])+", "
    colum=colum+str(columnas[-1])+")"
    comandoSQL=comandoSQL+colum
    con = sqlite3.connect(BBDD)
    cursor = con.cursor()
    cursor.execute(comandoSQL)
    cursor.close()
def VerTabla(tabla):
    print("Lista de",tablas[tabla][0])
    con = sqlite3.connect(BBDD)
    cursor = con.cursor()
    cursor.execute("SELECT * FROM '%s'"%(tablas[tabla][0]))
    resultado = cursor.fetchall()
    for i in resultado:
        print(i[0:])
    cursor.close()
    print("------------------")
def CargarTabla(nombre,columnas,valores):
    """insert into '%s' ('%s','%s') values ('%s','%s')"%(tablas[tabla][0],tablas[tabla][1],tablas[tabla][2],infoHashtag[0], infoHashtag[1])"""
    comandoSQL="insert into "+str(nombre)+" "
    colum="("
    val="("
    for col in range(0,(len(columnas)-1),1):
        colum=colum+str(columnas[col].split(' ')[0])+","
        val=val+"'"+str(valores[col])+"',"
    colum=colum+str(columnas[-1])+")"
    val=val+"'"+str(valores[-1])+"')"
    comandoSQL=comandoSQL+colum+" values "+val
    con = sqlite3.connect(BBDD)
    cursor = con.cursor()
    cursor.execute(comandoSQL)
    con.commit()
    cursor.close()
#variables 
def agregar(tabla,info):
    """agregara los valores a la tabla correspondiente"""
    con = sqlite3.connect(BBDD)
    cursor = con.cursor()
    cursor.execute("SELECT * FROM '%s'"%(tablas[tabla][0]))
    resultado = cursor.fetchall()
    if tablas[tabla][0] == "MisVariables":
        infoHashtag=info.split(";")
        cursor.execute("SELECT * FROM %s WHERE %s='%s'"%(tablas[tabla][0],tablas[tabla][1],infoHashtag[0]))
    else:
        infoHashtag=[str(variables[tabla][2]),info]
        for libre in range(0,len(resultado),1):
            resultado[libre]=resultado[libre][0]
        if len(resultado)<variables[tabla][2]:
            for buscando in range(0,variables[tabla][2],1):
                if str(buscando) in resultado:
                    pass
                else:
                    infoHashtag[0]=str(buscando)
        cursor.execute("SELECT * FROM %s WHERE %s='%s'"%(tablas[tabla][0],tablas[tabla][2],infoHashtag[1]))
    x = cursor.fetchall()
    if 0 < len(x):
        #print("ERROR:El valor",infoHashtag[0],"ya esta agregado en la tabla,",tablas[tabla][0])
        cursor.close()
        return 1
    else:
        if tablas[tabla][0] == "MisVariables":
            if len(resultado)==variables[tabla][2]:
                variables[tabla][2]=variables[tabla][2]+1
        cursor.execute("insert into '%s' ('%s','%s') values ('%s','%s')"%(tablas[tabla][0], tablas[tabla][1], tablas[tabla][2], infoHashtag[0], infoHashtag[1]))
        con.commit()
        #print("OK:El valor",infoHashtag[0],"fue agregado en la tabla,",tablas[tabla][0])
        cursor.close()
        return 0
def eliminar(tabla,info):
    """Elimina un contacto de la Agenda"""
    infoHashtag=[str(variables[tabla][1]),info]
    con = sqlite3.connect(BBDD)
    cursor = con.cursor()
    cursor.execute("DELETE FROM %s WHERE %s='%s'"%(tablas[tabla][0],tablas[tabla][1],infoHashtag[1]))
    con.commit()
    cursor.close()
    #print("Eliminado",infoHashtag[1],"de",tablas[tabla][0])
def modificar(tabla,info):
    """Modificar el Hashtag en LA TABLA """
    global tablas
    con = sqlite3.connect(BBDD)
    cursor = con.cursor()
    if tablas[tabla][0] == "MisVariables":
        infoHashtag=info.split(";")
    else:
        infoHashtag=[str(variables[tabla][2]),info]
        cursor.execute("SELECT * FROM %s WHERE %s='%s'"%(tablas[tabla][0],tablas[tabla][2],infoHashtag[1]))
        x = cursor.fetchall()
        infoHashtag=[str(x[0][0]),infoHashtag[1]]
    cursor.execute("DELETE FROM %s WHERE %s='%s'"%(tablas[tabla][0],tablas[tabla][2],infoHashtag[1]))
    cursor.execute("insert into '%s' ('%s','%s') values ('%s','%s')"%(tablas[tabla][0],tablas[tabla][1],tablas[tabla][2],infoHashtag[0], infoHashtag[1]))
    con.commit()
    cursor.close()
    #print("Modificado",infoHashtag[infoIndex],"de",tablas[tabla][0])
def actualizarVariables():
    global variables
    for var in range(0,len(variables),1):
        if 1==agregar(5,variables[var][0]+";0"):
            con = sqlite3.connect(BBDD)
            cursor = con.cursor()
            cursor.execute("SELECT * FROM %s WHERE %s = '%s'" %(tablas[5][0],tablas[5][1],variables[var][0]))
            resultado = cursor.fetchall()
            for i in resultado:
                if variables[var][1]=="int":
                    variables[var][2]=int(float(i[1]))
                elif variables[var][1]=="str":
                    variables[var][2]=str(i[1])
                elif variables[var][1]=="float":
                    variables[var][2]=float(i[1])
            cursor.close()
        else:            
            if variables[var][1]=="int":
                variables[var][2]=int(float(variables[var][2]))
            elif variables[var][1]=="str":
                variables[var][2]=str(variables[var][2])
            elif variables[var][1]=="float":
                variables[var][2]=float(variables[var][2])
def guardarVariables():
    global variables
    for var in range(0,len(variables),1):
        variables[var][2]=str(variables[var][2])
        modificar(5,variables[var][0]+";"+variables[var][2])
    actualizarVariables()
"""FUNCIONES PARA HACER PRUEBAS"""


"""
RESET=False
BBDD="cajero.db"
tablas=[["Clientes","RUC TEXT","RazonSocial TEXT","NombresApellidos TEXT","Direccion TEXT","Telefono TEXT","saldo TEXT"],
        ["Inventario","COD TEXT","nombre TEXT","precioVenta TEXT","precioCompra TEXT","origen TEXT","imagen TEXT","etiquetas TEXT","stock TEXT"],
        ["MisVariables","variable TEXT","tipo TEXT","valor TEXT"],
        ["LibroDiario","NumeroFactura TEXT","Cliente TEXT","CodigoProducto TEXT","Unidades TEXT","Precios TEXT","Fecha TEXT","TotalCaja TEXT"]]
variables=[["TotalCaja","int","0"],["ultimaFactura","int","0"],["Clima","str","31 Nublado 59 humedad"]]

bbdd=BBDD_SQLite(RESET,BBDD,tablas,variables)

#CargarTabla(tablas[1][0],tablas[1][1:],valores)
valores=["7750097003424","espirulina","50000","45000","Bolivia","null","Natural,Anticancerigena,Antiviral,antiinflamtorio","24"]
bbdd.Modificar(tablas[1][0],tablas[1][1:],valores)

#bbdd.CrearTabla(tablas[3][0],tablas[3][1:])

#bbdd.ModificarTabla(tablas[0][0],tablas[0][1:],["123","123-1","Lucas mathias Villalba Diaz","sanlorenzo florida","0991753962","0"])

limpiar()
print(variables)
bbdd.VerTablas()
actualizarVariables()
guardarVariables()
print(variables)
VerTabla(0)
VerTabla(1)
        fecha tiempo,momento
        audio mp3,wav,ogg,opus
        imagen jpg,gif,png,foto,
        office word,doc,ppt,opd,exel,calc
        programacion desarrollo web,aplicacion,app
        libro pdf,word
        video mp4,pelicula,wmv,DVD
"""
