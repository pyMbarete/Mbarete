#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Modulos importados
import sqlite3  #mini gestor de base de datos, muy util para pruebas y almacenar datos de nuestro programa
import time     #para hacer calculos de tiempo
import datetime #para abotener y manipular datos de fechas
import os       #libreria con todo los necesario para comunicar nuestro programa con el sistema
import math 
from tkinter import *   #libreria base, para las clases de interfaces de escritorio
import tkinter.colorchooser as colorchooser #modulo de la libreria tkinter para seleccionar color 
import threading    #para poder ejecutar procesos en segundo plano, estos proceso afectan al hilo principal, variables, funciones, etc,etc.
import socket
import urllib
import requests

#se identaran las siguentes clases en variables globales
#la variables globales permiten acceder a las propiedades y metodos, de estos objetos desde cualquier lugar 
global variables, tablas, BBDD, RESET, ventana

#FUNCIONES UTILES 
#PARA DIFERENTES TIPOS DE PROYECTOS, FUNCIONES PARA PRUEBAS, MANEJO DE DATOS, VALIDACIONES, ETC,ETC
def okString(string,para='Clave'):
    myStr=string.strip()
    notKey=['`','ñ','_',"'",'à','è','ì','ò','ù','.','']
    yesKey=["'",'nh','',"'",'a','e','i','o','u','' ,'']
    notUtf8=['`','ñ','_',"'",'','','','','','','','','','','','','','','']
    if para=="Clave":
        for char in notKey:
            myStr=myStr.replace(char,'')
def ordenar(myDict,orden=1,ordenarCampo=""):
    lenString=0
    campo=ordenarCampo if (ordenarCampo in myDict[[key for key in myDict][0]]) else [key for key in myDict[[key for key in myDict][0]]][0]
    relaciones=[[clave,myDict[clave][campo]] for clave in myDict ]
    typesIn=['str','int','float']
    typeString=str(type(relaciones[0][1]))[8:].replace("'>",'')
    if typeString in typesIn:
        relaciones=[[elemento[0],elemento[1].lower().strip() if typeString=='str' else elemento[1]] for elemento in relaciones]
        menor=relaciones[0]
        posicionMenor=0
        ordenado={}
        recorrer=range(0,len(relaciones),1)
        for check in recorrer:
            menor=relaciones[0]
            posicionMenor=0
            for x in range(0,len(relaciones),1):
                if (menor[1] > relaciones[x][1]) and orden==1:
                    menor=relaciones[x]
                    posicionMenor=x
                if (menor[1] < relaciones[x][1]) and orden==0:
                    menor=relaciones[x]
                    posicionMenor=x
            relaciones.pop(posicionMenor)
            ordenado.setdefault(menor[0],myDict[menor[0]])
        return ordenado
    else:
        return myDict
def buscador(myDictionary,buscar=" ",exacta=0,campoClave="",clavesString=[" "],clavesList="",returnKeys=[]):
    """
        ESTA FUNCION AUN DEBE OPTIMIZARCE...
        la funcion retornara un diccionario con los elementos que si coincidan con la busqueda

        myDictionary dict : diccionario que sera revisado para encontrar las coincidencias

        buscar str : este elemento puede ignorarse en caso de ser necesario. Sino debera ingresar: buscar='palabraParaBuscar -palabraParaDescartar'
            obs:
                si no se le asigna ningun string a 'buscar', la funcion retornara la variable 'myDictionary' completa, solo seran aplicados los cambios de 'returnKeys' y 'campoClave'
                Puede pasarle mas de una palabra para buscar, solo debe pasarlos separados y sin el signo negativo al inicio
                Tambien puede pasarle mas de una palabraParaDescartar, solo deben tener un negativo al comienzo y deben estar separados.
                Se pueden pasar solo palabrasParaDescartar y varias a la ves

        exacta int : 1 o 0 para hacer la busqueda de forma excata o no.
            Si exacta es igual a 0, Se aplicara:
                if 'PaLaB'.lower() in 'PALABRA'.lower(): obs: Esto sera True, ya que 'PaLaB'.lower() si 'pertenece' a 'PALABRA'.lower() 
            Si exacta es igual a 1, Se aplicara:
                if 'PaLaB' == 'PALABRA':      Obs: esto sera False, ya que 'PaLaB' no es exactamente igual a 'PALABRA' 
        
        campoClave str : la funcion tomara el valor asignado a la clave 'campoClave' de cada elemento de 'myDictionary', luego en el nuevo diccionario que retornara esta funcion, se identificara a cada elemento con el valor que contenga 'campoClave' en 'myDictionary'.
            Un ejemplo para ver como se aplica 'campoClave', por que ni yo entiendi lo que escribi jeje. Para ver como afecta 'campoClave' a 'para_retornar_final' debes cambiar "id" por "barCode" que serian codigos de Barra o "proveedorID":
                campoClave='id'
                para_retornar_inicial={
                    0:{'id':10025,'proveedorID':16,'barCode':6549849464,'name':'Producto 5001','list':['stock','precios','proveedor','sucursal']},
                    1:{'id':46887,'proveedorID':28,'barCode'9878954:,'name':'Producto 8000','list':['stock','precios','proveedor','sucursal']},
                    2:{'id':89795,'proveedorID':6,'barCode':456548984984,'name':'Producto 30003','list':['stock','precios','proveedor','sucursal']}
                    }
                para_retornar_final={}
                if campoClave in [ clave for clave in para_retornar_inicial[0] ]:
                    for clave_inicial in para_retornar_inicial:
                        clave_final = para_retornar_inicial[clave_inicial][campoClave]
                        para_retornar_final[clave_final] = para_retornar_inicial[clave_inicial]
                else:
                    para_retornar_final = para_retornar_inicial
                print(para_retornar_final)
                
        clavesString list : lista de las claves que estan en 'myDictionary', y deben tomarse esos valores como Strings para hacer la busqueda

        clavesList list : lista de las claves que estan en 'myDictionary', y deben tomarse esos valores como Listas y aplicar la busqueda en cada elemnto de esta lista

        returnKeys list : la funcion retornara un diccionario, y cada uno de los elementos tambien sera un dicionario que solo tendra las claves que esten en 'returnKeys'

    """
    search=buscar.strip()    
    omitir=[]
    filtrar=[]
    for x in search.split(" "):
        if ("-" in x):
            omitir+=[x.replace("-",'')]
        else:
            filtrar+=[x.replace("+",'')]
    ret={}
    lista=[]
    myDict=myDictionary
    if filtrar:
        for search in filtrar:
            ret={}
            if exacta:
                for clave in [palabra for palabra in myDict]:
                    if ([etiqu for etiqu in myDict[clave][clavesList] if (search.lower()==etiqu.lower())] if clavesList else False) :
                        lista+=[myDict[clave]]
                    else:
                        for check in [str(myDict[clave][claveString]).lower().split(' ') for claveString in clavesString]:
                            if (search.lower() in check):
                                lista+=[myDict[clave]]
            else:
                for clave in [palabra for palabra in myDict]:
                    if ([etiqu for etiqu in myDict[clave][clavesList] if (search.lower()==etiqu.lower()[0:len(search.lower())])] if clavesList else False) :
                        lista+=[myDict[clave]]
                    elif ([check for check in [str(myDict[clave][claveString]).lower().split(' ') for claveString in clavesString] if (search.lower() in [ checking.lower()[0:len(search)] for checking in check])]):
                        lista+=[myDict[clave]]
            for ok in lista:
                pasar={}
                for key in [keyword for keyword in ok]:
                    pasar.setdefault(str(key),ok[key])
                ret.setdefault(str(ok[campoClave if (campoClave in [clave for clave in ok]) else [clave for clave in ok][0]]),pasar)
            myDict=ret
    if omitir:
        for search in omitir:
            ret={}
            if exacta:
                for clave in [palabra for palabra in myDict]:
                    if not ([etiqu for etiqu in myDict[clave][clavesList] if (search.lower()==etiqu.lower())] if clavesList else False) :
                        lista+=[myDict[clave]]
                    elif not ([check for check in [str(myDict[clave][claveString]).lower().split(' ') for claveString in clavesString] if (search.lower() in check)]):
                        lista+=[myDict[clave]]
            else:
                for clave in [palabra for palabra in myDict]:
                    if not ([etiqu for etiqu in myDict[clave][clavesList] if (search.lower()==etiqu.lower()[0:len(search.lower())])] if clavesList else False) :
                        lista+=[myDict[clave]]
                    elif not ([check for check in [str(myDict[clave][claveString]).lower().split(' ') for claveString in clavesString] if (search.lower() in [ checking.lower()[0:len(search)] for checking in check])]):
                        lista+=[myDict[clave]]
            for ok in lista:
                pasar={}
                for key in [keyword for keyword in ok]:
                    pasar.setdefault(key,ok[key])
                ret.setdefault(str(ok[campoClave if (campoClave in [clave for clave in ok]) else [clave for clave in ok][0]]),pasar)
            myDict=ret
    if returnKeys:
        ret={}
        lista=[ myDict[clave] for clave in [palabra for palabra in myDict]]
        for ok in lista:
            pasar={}
            for key in returnKeys:
                pasar.setdefault(key,ok[key])
            ret.setdefault(ok[campoClave if (campoClave in [clave for clave in ok]) else [clave for clave in ok][0]],pasar)
    return ret
def strToUnicode(strng):
    unicod=""
    for x in str(strng):
        unicod += r" "+str(ord(x))
    return unicod.strip()
def unicodeToStr(unicod):
    strng=""
    if unicod.strip()=="":
        return unicod
    else:
        for x in unicod.split(" "):
            strng += str(chr(int(x)))
        return strng.strip()
def strToVar(strng,type_class=None):
    divisorDate=str(datetime.date.today())[4]
    string=str(strng).strip()
    start=["{","(","[","'",'"']
    stop= ["}",")","]","'",'"']
    formato=type_class
    nivel=0
    try:
        if "-" in string:
            ret=float(string[1:])
            formato="negativo"
        if ("." in string) and ("-" not in string):
            ret=float(string)
            formato="float"
        if "." not in string and ("-" not in string):
            ret=int(float(string))
            formato="int"
    except Exception as e:
        formato=type_class
    if not formato:
        try:
            if (divisorDate in string):
                if (":" in string) and ( ":"==string.split(" ")[1][2]) and ( ":"==string.split(" ")[1][5]) and ( "."==string.split(" ")[1][8]):
                    formato="time"
                elif (-1 < int(string.split(divisorDate)[0])) and (-1 < int(string.split(divisorDate)[1])) and (-1 < int(string.split(divisorDate)[2])):
                    formato="date"
        except Exception as e:
            formato=type_class
    if string=="":
        return string
    elif formato == "date":
        #retorna datetime.date(int dia, int mes, int año) 
        ret=datetime.date(int(string.split("-")[0]),int(string.split("-")[1]),int(string.split("-")[2]))
        return ret
    elif formato == "time":
        #retorna datetime(año,mes,dia,hora,minutos,segundos,milisegundos) 
        ret=datetime.datetime(int(string[0:4]),int(string[5:7]),int(string[8:10]),int(string[11:13]),int(string[14:16]),int(string[17:19]),int(string[20:]))
        return ret
    elif (string[0]=="{") and (string[-1]=="}"):
        #retorna dict
        ret ={}
        string=string[1:-1]
        comasDivisores=[-1]
        dosPuntos=[]
        comilla=0
        for x in range(0,len(string),1):
            if string[x] in start:
                if string[x] not in ['"',"'"]:
                    nivel += 1
                if string[x]==comilla:
                    nivel -= 1
                    comilla = 0
                elif (string[x] in ['"',"'"]) and (comilla not in ['"',"'"]):
                    nivel += 1
                    comilla=string[x]
            elif string[x] in stop:
                nivel -= 1
            if (string[x]==",") and (nivel==0):
                comasDivisores.append(x)
            if (string[x]==":") and (nivel==0):
                dosPuntos.append(x)
        for x in range(1,len(comasDivisores),1):
            ret.setdefault(strToVar(string[comasDivisores[x-1]+1:dosPuntos[x-1]]),strToVar(string[dosPuntos[x-1]+1:comasDivisores[x]]))
        ret.setdefault(strToVar(string[comasDivisores[-1]+1:dosPuntos[-1]]),strToVar(string[dosPuntos[-1]+1:]))
        return ret
    elif (string[0]=="[") and (string[-1]=="]"):
        ret =[]
        string=string[1:-1]
        comasDivisores=[-1]
        comilla=0
        for x in range(0,len(string),1):
            if string[x] in start:
                if string[x] not in ['"',"'"]:
                    nivel += 1
                if string[x]==comilla:
                    nivel -= 1
                    comilla = 0
                elif (string[x] in ['"',"'"]) and (comilla not in ['"',"'"]):
                    nivel += 1
                    comilla=string[x]
            elif string[x] in stop:
                nivel -= 1
            if (string[x]==",") and (nivel==0):
                comasDivisores.append(x)
        for x in range(1,len(comasDivisores),1):
            ret.append(strToVar(string[comasDivisores[x-1]+1:comasDivisores[x]]))
        ret.append(strToVar(string[comasDivisores[-1]+1:]))
        return ret
    elif (string[0]=="(") and (string[-1]==")"):
        #retornatupla
        ret =[]
        string=string[1:-1]
        comasDivisores=[-1]
        for x in range(0,len(string),1):
            if string[x] in start:
                nivel += 1
            if string[x] in stop:
                nivel -= 1
            if (string[x]==",") and (nivel==0):
                comasDivisores.append(x)
        for x in range(1,len(comasDivisores),1):
            ret.append(strToVar(string[comasDivisores[x-1]+1:comasDivisores[x]]))
        ret.append(strToVar(string[comasDivisores[-1]+1:]))
        return tuple(ret)
    elif (string=="True") or (string=="False"):
        return True if string=="True" else False
    elif  (formato=="negativo"):    
        return -1*float(string.replace('-',''))
        
    elif  (formato=="float"):        
        #retornamos un float
        return float(string)
    elif formato=="int":
        #retornamos un int
        return int(float(string))
    elif ((formato!="int") and (formato!="float") and (formato!="date") and (formato!="negativo")):
        #retornamos un str
        if (string[0] in start) and (string[-1] in stop):
            return string[1:-1]
        else:
            return string
    else:
        print("NO HAY FORMATO")
        return string
def escalarHex(h="#ffffff",factor=1.0):
    escala={'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'a':10,'b':11,'c':12,'d':13,'e':14,'f':15}
    #separamos el codigo de color #RRGGBB, en tres numeros enteros que equivalen a rojo -> RR, verde -> GG, azul -> BB.
    RR=float((escala[h[1:3][0]])*16+(escala[h[1:3][1]])) #convertimos los dos primeros digitos del numero hexagesimal a numero entero, corresponde al ROJO
    GG=float((escala[h[3:5][0]])*16+(escala[h[3:5][1]])) #convertimos el tercer y cuarto digito del numero hexagesimal a numero entero, corresponde al VERDE
    BB=float((escala[h[5:][0]])*16+(escala[h[5:][1]])) #convertimos el quinto y sexto digito del numero hexagesimal a numero entero, corresponde al AZUL
    RR= int(RR*factor if RR*factor <=255.0 else RR ) #escalamos el rojo
    GG= int(GG*factor if GG*factor <=255.0 else GG ) #escalamos el verde
    BB= int(BB*factor if BB*factor <=255.0 else BB ) #escalamos el azul
    #generamas el string que seria el nuevo codigo de color #RRGGBB
    ret='#' #todos los codigos de color deben comenzar con el signo numeral '#'
    ret+=("" if RR>15 else "0")+str(hex(RR))[2:]
    ret+=("" if GG>15 else "0")+str(hex(GG))[2:]
    ret+=("" if BB>15 else "0")+str(hex(BB))[2:]
    #print(ret)
    return ret[0:7]
def gradient(poligono=[],x=0,y=0,height=0,width=0,rotacion=0,color1='#ffffff',color2='#000000'):
    limite=height if rotacion==0 else width
    if poligono:
        print("No Degradamos Poligonos")
    else:
        poligono=[[100,0],[150,50],[50,50],[100,0]]

    escala={'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'a':10,'b':11,'c':12,'d':13,'e':14,'f':15}
    r1=float((escala[color1[1:3][0]])*16+(escala[color1[1:3][1]]))
    g1=float((escala[color1[3:5][0]])*16+(escala[color1[3:5][1]]))
    b1=float((escala[color1[5:][0]])*16+(escala[color1[5:][1]]))
    r2=float((escala[color2[1:3][0]])*16+(escala[color2[1:3][1]]))
    g2=float((escala[color2[3:5][0]])*16+(escala[color2[3:5][1]]))
    b2=float((escala[color2[5:][0]])*16+(escala[color2[5:][1]]))
    
    r=(r2-r1)/limite
    g=(g2-g1)/limite
    b=(b2-b1)/limite
    lines=[]
    for i in range(limite):
        RR=int(r1+(r*i))
        GG=int(g1+(g*i))
        BB=int(b1+(b*i))
        color='#'+("" if RR>15 else "0")+str(hex(RR))[2:]+("" if GG>15 else "0")+str(hex(GG))[2:]+("" if BB>15 else "0")+str(hex(BB))[2:]
        lines +=[[x+(i if rotacion==0 else 0),y+(i if rotacion!=0 else 0),x+(i if rotacion==0 else height),y+(height if rotacion==0 else i),color]]
        #,tags=("gradient",)
    return lines

def buscarFunciones(myFile):
    if myFile in os.listdir():
        os.remove(myFile)
    print(os.path.basename(__file__))
    myScript=os.path.basename(__file__)
    buscar=open(myScript)
    ret=["Funciones={"]
    for linea in [line.strip() if (("def " in line.strip()[0:4]) and (":" in line.strip()[-1])) else "self" for line in buscar]:
        start=0
        stop=0
        for c in range(0,len(linea),1):
            if "("==linea[c]:
                start=c
            elif ")"==linea[c]:
                stop=c+1
        if ("self" not in linea) and ("=" not in linea):
            ret.append("'"+linea[4:start]+"':["+linea[4:start]+','+linea[start:stop]+"]")
            ret.append(',')
    ret[-1]="}"
    buscar.close()
    func=open(myFile,"w")
    for string in ret:
        func.write(string)
    func.close()
    import dictFunciones.Funciones as retorna
    print(retorna)
    return retorna
def myFuncion(inputType,nameWitget,comando):
    if comando=="pruebaClickDerecho":
        print("pruebaClickDerecho")
    elif comando=="pruebaClickIzquierdo":
        print("pruebaClickIzquierdo")
    elif comando=="pruebaClickRueda":
        print("pruebaClickRueda")
""" 
    Clases para deferentes tipos de proyectos
    cesar escobar ieee ras una 
"""

class mbarete(object):
    """ 
        Esta clase sera para combinar las demas clases en este modulo, 
        funciones para poder tener una estructura escalable, y facil de desarrollar para proyectos mas complejos
    """
    def __init__(self, pwd='',baseName='',ficheroCRUD='',nombre="Proyecto Mbarete",reset=0,gitignore=[],gitBranch='master',defaultCommand=[],campoAutoincrement='id',cargarScript='mbarete.py',archivosInternos=['__pycache__','__init__.py','media','bibliografia','preload.py'],formato=[''],fullDir=1,renombrarArchivos=0,ignorar=[]):
        super(mbarete, self).__init__()
        self.reset=reset
        self.ubi=directorio(pwd=pwd,baseName=baseName,formato=formato,fullDir=fullDir,renombrarArchivos=renombrarArchivos,ignorar=ignorar)
        self.archivosInternos=archivosInternos
        self.nombre=nombre
        if ficheroCRUD:
            self.dirCRUD=self.ubi.pwd+os.path.sep+ficheroCRUD
            self.ficheroCRUD=ficheroCRUD
        else:
            self.dirCRUD=self.ubi.pwd+os.path.sep+nombre.replace(' ','_')+"_CRUD_.sql"
            self.ficheroCRUD=nombre.replace(' ','_')+"_CRUD_.sql"
        self.campoAutoincrement=campoAutoincrement
        self.cargarScript=cargarScript
        self.info={}
        self.subProyectoActivo=''
        self.manager=''
        self.subtransicionInicio='Inicio'
        self.defaultCommand=defaultCommand
        self.gitBranch=gitBranch
        self.gitignore=gitignore
    def start(self,G):
        for subProyecto in self.info:
            self.info[subProyecto]
        
        gitignore=open('.gitignore','w')
        for ig in self.gitignore:
            gitignore.write('*'+ig+'*'+'\n')
        gitignore.close()
        self.transicion(G,self.manager)
        G.loop()
    def getInicio(self):
        #esta funcion genera el menu de inicio del proyecto
        ret={}
        for subProyecto in self.info:
            ret[subProyecto]={
                'inputType':'Button',
                'command':'transicion_'+subProyecto,
                'text':self.info[subProyecto]['info']['text']
            }
        return ret
    def transicion(self,G,entra):
        if self.subProyectoActivo:
            for ocultar in self.info[self.subProyectoActivo]['widget']:
                G.widgets[self.info[self.subProyectoActivo]['widget'][ocultar]]['visible']=0
        for mostrar in self.info[entra]['widget']:
            #print(mostrar,self.info[entra]['etiquetas'][mostrar],self.info[entra]['subtransicion']['aceptar'],sum([1 if (aceptar in self.info[entra]['etiquetas'][mostrar]) else 0 for aceptar in self.info[entra]['subtransicion']['aceptar']]),sum([1 if (ignorar in self.info[entra]['etiquetas'][mostrar]) else 0 for ignorar in self.info[entra]['subtransicion']['ignorar']]))
            if sum([1 if (aceptar in self.info[entra]['etiquetas'][mostrar]) else 0 for aceptar in self.info[entra]['subtransicion']['aceptar']]) > 0 and sum([1 if (ignorar in self.info[entra]['etiquetas'][mostrar]) else 0 for ignorar in self.info[entra]['subtransicion']['ignorar']])==0:
                G.widgets[self.info[entra]['widget'][mostrar]]['visible']=1
        G.title(self.info[entra]['subtransicion']['aceptar'][0]+' - '+self.info[entra]['info']['text']+' - '+self.nombre)
        G.update()
        G.atrb['transicion']=entra
        self.subProyectoActivo=entra 
    def subtransicion(self,G,entra,etiquetas):
        e=etiquetas.strip()
        ignorar=[]
        aceptar=[]
        for x in e.split(" "):
            if ("-" in x):
                ignorar+=[x.replace("-",'').strip()]
            else:
                aceptar+=[x.replace("+",'').strip()]
        self.info[entra]['subtransicion']={'aceptar':aceptar+['default'],'ignorar':ignorar}
        G.atrb['subtransicion']=self.info[entra]['subtransicion']
        self.transicion(G,entra)
    def preload(self):
        subProyectos=self.ubi.listaDeCarpetas(self.ubi.pwd,ignorar=self.archivosInternos)
        load=open(self.ubi.pwd+os.path.sep+'preload.py','w')
        load.write(r'proyectos={}'+'\n')
        for subP in subProyectos:
            if self.cargarScript in self.ubi.listaDeFicheros(self.ubi.pwd+os.path.sep+subP,ignorar=self.archivosInternos): 
                load.write('from .'+subP+' import '+self.cargarScript[:-3]+' as '+subP+'\n')
            elif subP+'.py' in self.ubi.listaDeFicheros(self.ubi.pwd+os.path.sep+subP,ignorar=self.archivosInternos): 
                load.write('from .'+subP+' import '+subP+' as '+subP+'\n')
            load.write("proyectos['"+subP+"']="+subP+'\n')
        load.write("def command(admin,G,manager):"+'\n')
        for subP in subProyectos:
            load.write("    G.command[manager+'_transicion_"+subP+"']=lambda : admin.transicion(G,'"+subP+"')"+'\n')
        load.close()
        #from diseñoLibre.preload import proyectos
    def getWidget(self,subProyecto,widgets,info):
        w=widgets
        info['pwd']=self.ubi.pwd+os.path.sep+subProyecto
        metadata={'subProyecto':subProyecto,'command':{},'widget':{},'info':info,'etiquetas':{},'subtransicion':{'aceptar':[self.subtransicionInicio,'default'],'ignorar':[]}}
        for widget in w:
            metadata['widget'][w[widget]['name']]=subProyecto+'_'+w[widget]['name']
            metadata['etiquetas'][w[widget]['name']] = w[widget]['etiquetas']
            w[widget]['subProyecto']=subProyecto
            w[widget]['name']=subProyecto+'_'+w[widget]['name']
            w[widget]['visible']=0
            if 'crearTabla' in w[widget]:
                if w[widget]['crearTabla']:
                    for i in self.defaultCommand: 
                        w[widget]['inputs'][i]=self.defaultCommand[i]
                
            for i in w[widget]['inputs']:
                if (w[widget]['inputs'][i]['inputType'] in ['Button','Checkbutton']) and ('command' in w[widget]['inputs'][i]):
                    if w[widget]['inputs'][i]['command'] in self.defaultCommand:
                        metadata['command'][w[widget]['inputs'][i]['command']] = w[widget]['inputs'][i]['command']
                    else:
                        metadata['command'][w[widget]['inputs'][i]['command']] = subProyecto+'_'+w[widget]['inputs'][i]['command']
                        w[widget]['inputs'][i]['command']=subProyecto+'_'+w[widget]['inputs'][i]['command']
        self.info[subProyecto]=metadata
        return w
class git(object):
    """docstring for git"""
    def __init__(self, branch='',userName=''):
        super(git, self).__init__()
        self.branch=''
        self.userName=''
        self.userEmail=''
        self.commit=''
        self.userGithub=''
        self.repoGithub=''
        self.branchGithub=''
        self.gitignore=''
        self.commitGithub=''

class microservicio(object):
    """ 
        Clase para poder tener microservicios y nodos con contenedores docker o postman.
        Crear y administrar Microservicios en una red local por lo menos
        Esta clase no fue estudiada a fundo, osea que esta en desuso 
        El objetivo es tener una formade conectarse a nuestro proyecto desde distintas maquinas
        Definiendo una maquina Servidor, para luego este poder ser accedido desde otras maquinas 

    """
    def __init__(self,wan_url='https://8.8.8.8'):
        super(microservicio, self).__init__()
        self.lan_ip=self.get_lan_ip()
        self.wan_ip=self.get_wan_ip(wan_url)
    def get_lan_ip(self):
        s=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        try:
            s.connect(('10.255.255.255',1))
            ip=s.getsockname()
        except:
            ip='127.0.0.1'
        finally:
            s.close()
        return ip

    def get_wan_ip(self, wan_url):
        wan_ip = urllib.request.urlopen(wan_url).read().decode('utf8')
        return wan_ip
class calculadora(object):
    """
        En el plano, las coordenadas cartesianas se denominan abscisa y ordenada. 
        La abscisa es la coordenada horizontal y se representa habitualmente por la letra X, 
        mientras que la ordenada es la coordenada vertical y se representa por la Y.
        a continuacion informacion de algunas librerias importantes
        LIBRERIA MATH
            import math
            Traducido de https://www.w3schools.com/python/module_math.asp
            Python tiene un módulo incorporado que puede usar para tareas matemáticas.
            El módulo de matemáticas tiene un conjunto de métodos y constantes.
            Constantes matemáticas
                math.e Devuelve el número de Euler (2.7182 ...)
                math.inf Devuelve un infinito positivo en coma flotante
                math.nan Devuelve un valor NaN (no un número) de coma flotante
                math.pi Devuelve PI (3.1415 ...)
                math.tau Devuelve tau (6.2831 ...)
            Descripción del método
                math.acos () Devuelve el arco coseno de un número
                math.acosh () Devuelve el coseno hiperbólico inverso de un número
                math.asin () Devuelve el arco seno de un número
                math.asinh () Devuelve el seno hiperbólico inverso de un número
                math.atan () Devuelve el arco tangente de un número en radianes
                math.atan2 () Devuelve el arco tangente de y / x en radianes
                math.atanh () Devuelve la tangente hiperbólica inversa de un número
                math.ceil () Redondea un número al entero más cercano
                math.comb () Devuelve el número de formas de elegir k elementos de n elementos sin repetición ni orden
                math.copysign () Devuelve un flotante que consta del valor del primer parámetro y el signo del segundo parámetro
                math.cos () Devuelve el coseno de un número
                math.cosh () Devuelve el coseno hiperbólico de un número
                math.degrees () Convierte un ángulo de radianes a grados
                math.dist () Devuelve la distancia euclidiana entre dos puntos (pyq), donde pyq son las coordenadas de ese punto
                math.erf () Devuelve la función de error de un número
                math.erfc () Devuelve la función de error complementaria de un número
                math.exp () Devuelve E elevado a la potencia de x
                math.expm1 () Devuelve Ex - 1
                math.fabs () Devuelve el valor absoluto de un número
                math.factorial () Devuelve el factorial de un número
                math.floor () Redondea un número hacia abajo al entero más cercano
                math.fmod () Devuelve el resto de x / y
                math.frexp () Devuelve la mantisa y el exponente de un número especificado
                math.fsum () Devuelve la suma de todos los elementos en cualquier iterable (tuplas, matrices, listas, etc.)
                math.gamma () Devuelve la función gamma en x
                math.gcd () Devuelve el máximo común divisor de dos enteros
                math.hypot () Devuelve la norma euclidiana
                math.isclose () Comprueba si dos valores están cerca uno del otro, o no
                math.isfinite () Comprueba si un número es finito o no
                math.isinf () Comprueba si un número es infinito o no
                math.isnan () Comprueba si un valor es NaN (no un número) o no
                math.isqrt () Redondea un número de raíz cuadrada hacia abajo al entero más cercano
                math.ldexp () Devuelve el inverso de math.frexp () que es x * (2 ** i) de los números dados x e i
                math.lgamma () Devuelve el valor log gamma de x
                math.log () Devuelve el logaritmo natural de un número o el logaritmo de un número en base
                math.log10 () Devuelve el logaritmo en base 10 de x
                math.log1p () Devuelve el logaritmo natural de 1 + x
                math.log2 () Devuelve el logaritmo en base 2 de x
                math.perm () Devuelve el número de formas de elegir k elementos de n elementos con orden y sin repetición
                math.pow () Devuelve el valor de x elevado a y
                math.prod () Devuelve el producto de todos los elementos en un iterable
                math.radians () Convierte un valor de grado en radianes
                math.remainder () Devuelve el valor más cercano que puede hacer que el numerador sea completamente divisible por el denominador
                math.sin () Devuelve el seno de un número
                math.sinh () Devuelve el seno hiperbólico de un número
                math.sqrt () Devuelve la raíz cuadrada de un número
                math.tan () Devuelve la tangente de un número
                math.tanh () Devuelve la tangente hiperbólica de un número
                math.trunc () Devuelve las partes enteras truncadas de un número
        LIBRERIA STATISTICS
            import statistics
            TRADUCIDI DE https://www.w3schools.com/python/module_statistics.asp
            Python tiene un módulo incorporado que puede usar para calcular estadísticas matemáticas de datos numéricos.
            El módulo de estadísticas era nuevo en Python 3.4.
            Descripción del método
                statistics.harmonic_mean () Calcula la media armónica (ubicación central) de los datos dados
                statistics.mean () Calcula la media (promedio) de los datos dados
                statistics.median () Calcula la mediana (valor medio) de los datos dados
                statistics.median_grouped () Calcula la mediana de datos continuos agrupados
                statistics.median_high () Calcula la mediana alta de los datos dados
                statistics.median_low () Calcula la mediana baja de los datos dados
                statistics.mode () Calcula el modo (tendencia central) de los datos numéricos o nominales dados
                statistics.pstdev () Calcula la desviación estándar de una población completa
                statistics.stdev () Calcula la desviación estándar de una muestra de datos
                statistics.pvariance () Calcula la varianza de una población completa
                statistics.variance () Calcula la varianza a partir de una muestra de datos
    """
    def __init__(self, ec={},constantes={},extras={},config={'angulos':'radianes'}):
        super(calculadora, self).__init__()
        self.error=0.0000001
        self.masInf=999999999999.9
        self.menosInf=-999999999999.9
        self.alfa=0.0
        self.factoresDeEscala=[1.0,1.0]
        self.trasladarOrigen=[0.0,0.0]
        self.escalarOrigen=[0.0,0.0]
        self.rotarOrigen=[0.0,0.0]
        self.historial={}
        self.ec={}
        self.ecuaciones=[]
        self.constantes={'e':math.e,'pi':math.pi,'g':9.8182}
        self.extras=extras
        self.operadores=['w(','sen(','cos(','tg(','log(','ln(','lambert(','dy(','sec(','cosec(','cotag(','arcsen(','arccos(','arctg(','round(','floor(','ceil(','signo(','abs(']
        self.simbolos=['*','(',')','/','+','-','.','%']
    def update(self, ec={},constantes={},extras={}):
        if constantes:
            for C in constantes:
                self.constantes[C]=constantes[C]
    def setEcuacion(self, nombre, string='', variable='x',constantes={},extras={}):
        if constantes:
            self.update(constantes=constantes)
        self.ec[nombre]=self.strToMath(string=string, variable=variable)
        self.ecuaciones=[ecu for ecu in self.ec]
        print("Se agrego Exitosamente: '",nombre,"':",self.ec[nombre](variable,p=1))
    def inversa(self,ordenada,f=None,error=None):
        ordenada=float(ordenada)
        mayor=0.0
        menor=0.0
        abscisa=0.0
        while f(mayor)<ordenada:
            mayor += 10.0
        while f(menor)>ordenada:
            menor -= 1.0
        while ((ordenada-f(abscisa))**(2))**(1/2) > error:
            if ordenada<f((mayor+menor)/2.0):
                mayor=(mayor+menor)/2.0
            elif ordenada>f((mayor+menor)/2.0):
                menor=(mayor+menor)/2.0
            abscisa=(mayor+menor)/2.0   
        return abscisa
    def strToMath(self,string='',variable='x',dy=0,p=0,c=None,decimales=4,signo=None,v=0,composicion=0):
        
        if not v:
            print('validando',string,composicion)
            v=1
        composicion += 1
        nivel=0
        esSuma=0
        signoSuma=[0]
        esProducto=0
        signoProducto=[0]
        esDivision=0
        signoDivision=[0]
        esExponente=0
        signoExponente=[0]
        esResto=0
        signoResto=[0]
        operador=1
        monomio=1
        parentesis=1
        string=string.strip()
        for x in range(0,len(string),1):
            if string[x]=='(':
                nivel += 1
            if string[x]==')':
                nivel -= 1
            if string[x] in '-+' and nivel==0:
                if x>0:
                    monomio=0
            if string[x] in '-+*/%' and nivel==0:
                if x>0:
                    parentesis=0
        if monomio:
            if string[0] in '+' and nivel==0:
                sig= 1.0
                string=string[1:]
            elif string[0] in '-' and nivel==0:
                sig=-1.0
                string=string[1:]
            else:
                sig= 1.0
            string=string.strip()
        else:
            sig=1.0

        if parentesis:        
            if ('(' in string[0]) and (')' in string[-1]):
                string=string[1:-1]
            string=string.strip()
                
        monomio=1
        parentesis=1
        string=string.strip()
        for x in range(0,len(string),1):
            if string[x]=='(':
                nivel += 1
            if string[x]==')':
                nivel -= 1
            if string[x] in '-+' and nivel==0:
                if x>0:
                    monomio=0
            if string[x] in '-+*/%' and nivel==0:
                if x>0:
                    parentesis=0
        if monomio:
            if string[0] in '+' and nivel==0:
                sig= 1.0*sig
                string=string[1:]
            elif string[0] in '-' and nivel==0:
                sig=-1.0*sig
                string=string[1:]
            string=string.strip()

        if parentesis:        
            if ('(' in string[0]) and (')' in string[-1]):
                string=string[1:-1]
            string=string.strip()
        for x in range(0,len(string),1):
            if string[x]=='(':
                nivel += 1
            if string[x]==')':
                nivel -= 1
            if string[x] in '-+' and nivel==0:
                if x>0:
                    esSuma=1
                    signoSuma += [x]
                if not monomio:
                    operador=0
            if (string[x] == '*') and ( '*' != string[x+1]) and ( '*' != string[x-1]) and nivel==0:
                esProducto=1
                signoProducto += [x]
                operador=0
            if string[x] in '/' and nivel==0:
                esDivision=1
                signoDivision += [x]
                operador=0
            if (string[x] == '*') and ( '*' == string[x+1]) and nivel==0:
                esExponente=1
                signoExponente += [x]
                operador=0
            if (string[x] == '%') and nivel==0:
                esResto=1
                signoResto += [x]
                operador=0

        if operador:
            x=0
            coincide=[op for op in self.operadores+self.ecuaciones if op in (string if len(op)<len(string) else '')]
            if coincide:
                comas=[0]
                for x in range(0,len(string),1):
                    if string[x]=='(':
                        nivel += 1
                    if string[x]==')':
                        nivel -= 1
                    if string[x] in ',' and nivel==0:
                        comas += [x]
                if string[:len('w(')] in 'w(' and nivel==0:
                    pass
                if string[:len('dy(')] in 'dy(' and nivel==0:
                    pass
                if string[:len('log(')] in 'log(' and nivel==0:
                    #math.log(x,base)
                    print('log',string)
                    parteReal=self.strToMath(string=string[len('log'):comas[1]],dy=dy,p=p,decimales=decimales,v=v,composicion=composicion)
                    if len(comas)==1:
                        base=self.strToMath(string='10.0',dy=dy,p=p,decimales=decimales,v=v,composicion=composicion)
                    else:
                        base=self.strToMath(string=string[comas[1]+1:-1],dy=dy,p=p,decimales=decimales,v=v,composicion=composicion)
                    def logaritmoNatural(x,dy=dy,p=p,decimales=decimales,signo=sig,mostrarSigno=0,parteReal=parteReal,base=base):
                        if mostrarSigno:
                            s='+' if signo>0.0 else '-'
                        else:
                            s=''
                        if dy:
                            if p:
                                numerador='(('+parteReal(x,p=p,dy=1,decimales=decimales,mostrarSigno=1)+'/'+parteReal(x,p=p,dy=0,decimales=decimales,mostrarSigno=1)+')-('+parteReal(x,p=p,dy=1,decimales=decimales,mostrarSigno=1)+'/'+parteReal(x,p=p,dy=0,decimales=decimales,mostrarSigno=1)+'))'
                                return s+'('+numerador+'/'+parteReal(x,p=p,dy=0,decimales=decimales,mostrarSigno=1)+')'
                            else:
                                numerador=signo*((parteReal(x,p=p,dy=1,decimales=decimales,mostrarSigno=1)/parteReal(x,p=p,dy=0,decimales=decimales,mostrarSigno=1))-(base(x,p=p,dy=1,decimales=decimales,mostrarSigno=1)/base(x,p=p,dy=0,decimales=decimales,mostrarSigno=1)))
                                return numerador/((math.log(base(x,p=p,dy=1,decimales=decimales,mostrarSigno=1)))**2)
                        else:
                            if p:
                                return s+'ln('+parteReal(x,p=p,decimales=decimales,mostrarSigno=1)+','+base(x,p=p,decimales=decimales,mostrarSigno=1)+')'
                            else:
                                return signo*math.log(parteReal(x),base(x))
                    return logaritmoNatural
                if string[:len('ln(')] in 'ln(' and nivel==0:
                    #math.log(x,base)
                    print('ln',string)
                    parteReal=self.strToMath(string=string[len('ln'):],dy=dy,p=p,decimales=decimales,v=v,composicion=composicion)
                    def logaritmoNatural(x,dy=dy,p=p,decimales=decimales,signo=sig,mostrarSigno=0,parteReal=parteReal):
                        if mostrarSigno:
                            s='+' if signo>0.0 else '-'
                        else:
                            s=''
                        if dy:
                            if p:
                                return s+'('+parteReal(x,p=p,dy=1,decimales=decimales,mostrarSigno=1)+'/'+parteReal(x,p=p,dy=0,decimales=decimales,mostrarSigno=1)+')'
                            else:
                                return signo*(parteReal(x,p=p,dy=1,decimales=decimales,mostrarSigno=1)/parteReal(x,p=p,dy=0,decimales=decimales,mostrarSigno=1))
                        else:
                            if p:
                                return s+'ln('+parteReal(x,p=p,decimales=decimales,mostrarSigno=1)+')'
                            else:
                                return signo*math.log(parteReal(x))
                    return logaritmoNatural
                if string[:len('abs(')] in 'abs(' and nivel==0:
                    #math.fabs(-66.43)
                    print('abs',string)
                    valor=self.strToMath(string=string[len(''):],dy=dy,p=p,decimales=decimales,v=v,composicion=composicion)
                    def valorAbsoluto(x,dy=dy,p=p,decimales=decimales,signo=sig,mostrarSigno=0,u=valor):
                        if mostrarSigno:
                            s='+' if signo>0.0 else '-'
                        else:
                            s=''
                        if dy:
                            if p:
                                return s+'(('+valor(x,p=p,dy=0,decimales=decimales,mostrarSigno=1)+'/abs('+valor(x,p=p,dy=0,decimales=decimales,mostrarSigno=1)+'))*('+valor(x,p=p,dy=1,decimales=decimales,mostrarSigno=1)+'))'
                            else:
                                return signo*((valor(x,p=p,dy=0,decimales=decimales)/math.fabs(valor(x,p=p,dy=0,decimales=decimales)))*valor(x,p=p,dy=1,decimales=decimales)) 
                        else:
                            if p:
                                return s+'abs('+valor(x,p=p,decimales=decimales,mostrarSigno=1)+')'
                            else:
                                return signo*math.fabs(valor(x))
                    return valorAbsoluto
                if string[:len('tg(')] in 'tg(' and nivel==0:
                    #math.tan()
                    print('tg',string)
                    radian=self.strToMath(string=string[len('tg'):],dy=dy,p=p,decimales=decimales,v=v,composicion=composicion)
                    def tangente(x,dy=dy,p=p,decimales=decimales,signo=sig,mostrarSigno=0,radian=radian):
                        if mostrarSigno:
                            s='+' if signo>0.0 else '-'
                        else:
                            s=''
                        if dy:
                            if p:
                                return s+'((1+tg('+radian(x,dy=0,p=p,decimales=decimales,mostrarSigno=1)+')**2)*('+radian(x,dy=dy,p=p,decimales=decimales,mostrarSigno=1)+'))'
                            else:
                                return signo*(1+math.tan(radian(x))**2)*radian(x,dy=dy)
                        else:
                            if p:
                                return s+'tg('+radian(x,dy=dy,p=p,decimales=decimales,mostrarSigno=1)+')'
                            else:
                                return signo*math.tan(radian(x))
                    return tangente
                if string[:len('sen(')] in 'sen(' and nivel==0:
                    #math.sin()
                    print('sen',string)
                    radian=self.strToMath(string=string[len('sen'):],dy=dy,p=p,decimales=decimales,v=v,composicion=composicion)
                    def seno(x,dy=dy,p=p,decimales=decimales,signo=sig,mostrarSigno=0,radian=radian):
                        if mostrarSigno:
                            s='+' if signo>0.0 else '-'
                        else:
                            s=''
                        if dy:
                            if p:
                                return s+'cos('+radian(x,dy=0,p=p,decimales=decimales,mostrarSigno=1)+')*('+radian(x,dy=dy,p=p,decimales=decimales,mostrarSigno=1)+')'
                            else:
                                return signo*math.cos(radian(x))*radian(x,dy=dy)
                        else:
                            if p:
                                return s+'sen('+radian(x,dy=dy,p=p,decimales=decimales,mostrarSigno=1)+')'
                            else:
                                return signo*math.sin(radian(x))
                    return seno
                if string[:len('cos(')] in 'cos(' and nivel==0:
                    #math.cos()
                    print('cos',string)
                    radian=self.strToMath(string=string[len('cos'):],dy=dy,p=p,decimales=decimales,v=v,composicion=composicion)
                    def coseno(x,dy=dy,p=p,decimales=decimales,signo=sig,mostrarSigno=0,radian=radian):
                        if mostrarSigno:
                            s='+' if signo>0.0 else '-'
                        else:
                            s=''
                        if dy:
                            if p:
                                s=('-' if signo>0.0 else '+') if mostrarSigno else ''
                                return s+'sen('+radian(x,dy=0,p=p,decimales=decimales,mostrarSigno=1)+')*('+radian(x,dy=dy,p=p,decimales=decimales,mostrarSigno=1)+')'
                            else:
                                return -1*signo*math.sin(radian(x))*radian(x,dy=dy,p=p,decimales=decimales,mostrarSigno=1)
                        else:
                            if p:
                                return s+'cos('+radian(x,dy=dy,p=p,decimales=decimales,mostrarSigno=1)+')'
                            else:
                                return signo*math.cos(radian(x))
                    return coseno
                if string[:len('arcsen(')] in 'arcsen(' and nivel==0:
                    #math.asin()
                    pass
                if string[:len('arccos(')] in 'arccos(' and nivel==0:
                    #math.acos()
                    pass
                if string[:len('arctg(')] in 'arctg(' and nivel==0:
                    #math.atan()
                    pass
                if string[:len('signo(')] in 'signo(' and nivel==0:
                    pass
                if string[:len('entero(')] in 'entero(' and nivel==0:
                    pass
                if string[:len('decimal(')] in 'decimal(' and nivel==0:
                    pass
                if string[:len('round(')] in 'round(' and nivel==0:
                    print('round',string)
                    redondeo=self.strToMath(string=string[len('round'):],dy=dy,p=p,decimales=decimales,v=v,composicion=composicion)
                    def redondear(x,dy=dy,p=p,decimales=decimales,signo=sig,mostrarSigno=0,redondeo=redondeo):
                        if mostrarSigno:
                            s='+' if signo>=0.0 else '-'
                        else:
                            s=''
                        if dy:
                            if p:
                                return '0.0'
                            else:
                                return 0.0
                        else:
                            if p:
                                return s+'round('+defecto(x,p=p,decimales=decimales,mostrarSigno=1)+')'
                            else:
                                return signo*math.round(defecto(x))
                    return redondear
                if string[:len('floor(')] in 'floor(' and nivel==0:
                    print('floor',string)
                    defecto=self.strToMath(string=string[len('floor'):],dy=dy,p=p,decimales=decimales,v=v,composicion=composicion)
                    def redondearHaciaAbajo(x,dy=dy,p=p,decimales=decimales,signo=sig,mostrarSigno=0,defecto=defecto):
                        if mostrarSigno:
                            s='+' if signo>0.0 else '-'
                        else:
                            s=''
                        if dy:
                            if p:
                                return '0.0'
                            else:
                                return 0.0
                        else:
                            if p:
                                return s+'floor('+defecto(x,p=p,decimales=decimales,mostrarSigno=1)+')'
                            else:
                                return signo*math.floor(defecto(x))
                    return redondearHaciaAbajo
                if string[:len('ceil(')] in 'ceil(' and nivel==0:
                    print('ceil',string)
                    exceso=self.strToMath(string=string[len('ceil'):],dy=dy,p=p,decimales=decimales,v=v,composicion=composicion)
                    def redondearHaciaArriba(x,dy=dy,p=p,decimales=decimales,signo=sig,mostrarSigno=0,exceso=exceso):
                        if mostrarSigno:
                            s='+' if signo>0.0 else '-'
                        else:
                            s=''
                        if dy:
                            if p:
                                return '0.0'
                            else:
                                return 0.0
                        else:
                            if p:
                                return s+'ceil('+exceso(x,p=p,decimales=decimales,mostrarSigno=1)+')'
                            else:
                                return signo*math.ceil(exceso(x))
                    return redondearHaciaArriba
                if [op for op in self.ecuaciones if op in (string if len(op)<len(string) else '')] and nivel==0:
                    miEcuacion=''
                    for op in self.ecuaciones:
                        if op in (string[:len(op)] if len(op)<len(string) else ''):
                            miEcuacion=op
                    print(miEcuacion,string)
                    myF=self.ec[miEcuacion]
                    ecuacionInterna=self.strToMath(string=string[len(miEcuacion):],dy=dy,p=p,decimales=decimales,v=v,composicion=composicion)
                    def f(x,dy=dy,p=p,decimales=decimales,signo=sig,mostrarSigno=0,miEcuacion=miEcuacion,myF=myF,ecuacionInterna=ecuacionInterna):
                        #f(x,dy=dy,p=p,decimales=decimales,mostrarSigno=0)
                        if mostrarSigno:
                            s='+' if signo>0.0 else '-'
                        else:
                            s=''
                        if dy:
                            if p:
                                return s+'('+myF(ecuacionInterna(x,p=p,dy=0,decimales=decimales,mostrarSigno=1),p=p,dy=1,decimales=decimales,mostrarSigno=0)+')*('+ecuacionInterna(x,p=p,dy=0,decimales=decimales,mostrarSigno=1)+')'
                            else:
                                ret = myF(ecuacionInterna(x,p=p,dy=0,decimales=decimales,mostrarSigno=1),p=p,dy=1,decimales=decimales,mostrarSigno=0)*ecuacionInterna(x,p=p,dy=0,decimales=decimales,mostrarSigno=1)
                                return signo*ret
                        else:
                            if p:
                                return s+myF('('+ecuacionInterna(x,p=p,decimales=decimales,mostrarSigno=0)+')',p=p,decimales=decimales)
                            else:
                                return signo*myF(ecuacionInterna(x))
                    return f
                else:
                    esConstante=1
                """
                if string[:len('')] in '' and nivel==0:
                    print('',string)
                    =strToMath(string=string[len(''):],dy=dy,p=p,decimales=decimales,v=v)
                    def op(x,dy=dy,p=p,decimales=decimales,signo=sig,mostrarSigno=0):
                        #f(x,dy=dy,p=p,decimales=decimales,mostrarSigno=0)
                        if mostrarSigno:
                            s='+' if signo>0.0 else '-'
                        else:
                            s=''
                        if dy:
                            if p:
                                return s
                            else:
                                ret = 
                                return signo*ret
                        else:
                            if p:
                                return s
                            else:
                                return signo*
                    return op
                """
            else:
                c=None
                if string in self.constantes:
                    c=self.constantes[string]
                elif sum([1 for l in string if ((48<=ord(l) and ord(l)<=57) or (ord(l)==46))])==len(string):
                    c=float(string)
                if c:
                    print('constante',c)
                    def constante(x,dy=dy,p=p,c=c,decimales=decimales,signo=sig,mostrarSigno=0):
                        if mostrarSigno:
                            s='+' if signo>0.0 else '-'
                        else:
                            s=''
                        if dy:
                            if p:
                                return '0.0'
                            else:
                                return 0
                        else:
                            if p:
                                c=str(c)
                                #[:decimales if len(c)>decimales else None]
                                return s+c
                            else:
                                return c*signo
                    return constante
                if string==variable:
                    print('variable',string,sig)
                    def variable(x,dy=dy,p=p,decimales=decimales,signo=sig,mostrarSigno=0):
                        if mostrarSigno:
                            s='+' if signo>=0.0 else '-'
                        else:
                            s=''
                        if dy:
                            if p:
                                return '1.0'
                            else:
                                return 1.0
                        else:
                            if p:
                                return s+str(x)[:decimales]
                            else:
                                return x*signo
                    return variable
            
        else:
            #parentecis,exponente/radicales,multiplicacion/division,suma/resta
            if esSuma:
                print('suma',string,signoSuma)
                if len(signoSuma)==1:
                    sumandos=[self.strToMath(string=string[1:],dy=dy,p=p,decimales=decimales,v=v,composicion=composicion)]
                else:
                    sumandos=[]
                    for sumando in range(0,len(signoSuma)-1,1):
                        sumandos+=[self.strToMath(string=string[signoSuma[sumando]:signoSuma[sumando+1]],dy=dy,p=p,decimales=decimales,v=v,composicion=composicion)]
                    sumandos+=[self.strToMath(string=string[signoSuma[-1]:],dy=dy,p=p,decimales=decimales,v=v,composicion=composicion)]
                def suma(x,dy=dy,p=p,decimales=decimales,sumandos=sumandos,signo=sig,mostrarSigno=0):
                    if mostrarSigno:
                        s='+' if signo>0.0 else '-'
                    else:
                        s=''
                    if dy:
                        if p:
                            ret = s
                            for sumando in sumandos:
                                ret += sumando(x,p=p,dy=dy,decimales=decimales,mostrarSigno=1)
                            return ret
                        else:
                            return signo*sum([sumando(x,dy=dy) for sumando in sumandos])
                    else:
                        if p:
                            ret = ''
                            for sumando in sumandos:
                                ret += sumando(x,p=p,decimales=decimales,mostrarSigno=1)
                            return ret
                        else:
                            ret = 0.0
                            for sumando in sumandos:
                                ret += sumando(x)
                            return signo*ret
                return suma
            elif esDivision:
                print('division',string,signoDivision)
                signoDivision+=[]
                numerador=self.strToMath(string=string[0:signoDivision[1]],dy=dy,p=p,decimales=decimales,v=v,composicion=composicion)
                denominador=self.strToMath(string=string[signoDivision[1]+1:],dy=dy,p=p,decimales=decimales,v=v,composicion=composicion)
                def division(x,dy=dy,p=p,decimales=decimales,numerador=numerador,denominador=denominador,signo=sig,mostrarSigno=0):
                    if mostrarSigno:
                        s='+' if signo>0.0 else '-'
                    else:
                        s=''
                    if dy:
                        if p:
                            return s+'(('+numerador(x,p=p,dy=1,decimales=decimales)+')*('+denominador(x,p=p,dy=0,decimales=decimales)+')-('+numerador(x,p=p,dy=0,decimales=decimales)+')*('+denominador(x,p=p,dy=1,decimales=decimales)+'))/(('+denominador(x,p=p,dy=0,decimales=decimales)+')**2)'
                        else:
                            return signo*((numerador(x,p=p,dy=1,decimales=decimales)*denominador(x,p=p,dy=0,decimales=decimales))-(numerador(x,p=p,dy=0,decimales=decimales)*denominador(x,p=p,dy=1,decimales=decimales)))/(denominador(x,p=p,dy=0,decimales=decimales)**2)
                    else:
                        if p:
                            return s+'('+numerador(x,p=p,dy=0,decimales=decimales)+')/('+denominador(x,p=p,dy=0,decimales=decimales)+')'
                        else:
                            return signo*numerador(x,dy=0,decimales=decimales)/denominador(x,dy=0,decimales=decimales)
                return division
            elif esResto:
                print('resto',string,signoResto)
                signoResto+=[]
                numerador=self.strToMath(string=string[0:signoResto[1]],dy=dy,p=p,decimales=decimales,v=v,composicion=composicion)
                denominador=self.strToMath(string=string[signoResto[1]+1:],dy=dy,p=p,decimales=decimales,v=v,composicion=composicion)
                def restoPorDefecto(x,dy=dy,p=p,decimales=decimales,numerador=numerador,denominador=denominador,signo=sig,mostrarSigno=0):
                    if mostrarSigno:
                        s='+' if signo>0.0 else '-'
                    else:
                        s=''
                    if dy:
                        if p:
                            return ''
                        else:
                            return None
                    else:
                        if p:
                            return s+'('+numerador(x,p=p,dy=0,decimales=decimales)+'%'+denominador(x,p=p,dy=0,decimales=decimales)+')'
                        else:
                            return signo*numerador(x,dy=0,decimales=decimales)%denominador(x,dy=0,decimales=decimales)
                return restoPorDefecto
            elif esProducto:
                print('producto',string,signoProducto)
                factores=[]
                for factor in range(0,len(signoProducto)-1,1):
                    factores+=[self.strToMath(string=string[signoProducto[factor]+(1 if 0<factor else 0 ):signoProducto[factor+1]],dy=dy,p=p,decimales=decimales,v=v,composicion=composicion)]
                factores+=[self.strToMath(string=string[signoProducto[-1]+1:],dy=dy,p=p,decimales=decimales,v=v,composicion=composicion)]
                def producto(x,dy=dy,p=p,decimales=decimales,signo=sig,factores=factores,mostrarSigno=0):
                    if mostrarSigno:
                        s='+' if signo>0.0 else '-'
                    else:
                        s=''
                    if dy:
                        if p:
                            ret=s+'('
                            factor='('
                            for derivar in range(0,len(factores),1):
                                factor=factores[derivar](x,dy=1,p=p,decimales=decimales)
                                for escalar in range(0,len(factores),1):
                                    if not (derivar == escalar):
                                        factor += '*'+factores[escalar](x,dy=0,p=p,decimales=decimales)
                                ret += factor+')+'
                            return ret[:-1]+')'
                        else:
                            ret=0.0
                            factor=1.0
                            for derivar in range(0,len(factores),1):
                                factor=factores[derivar](x,dy=1,p=p,decimales=decimales)
                                for escalar in range(0,len(factores),1):
                                    if not (derivar == escalar):
                                        factor*=factores[escalar](x,dy=0,p=p,decimales=decimales)
                                ret += factor
                            return signo*ret
                    else:
                        if p:
                            ret = s+'('+factores[0](x,dy=0,p=p,decimales=decimales)
                            for factor in factores[1:]:
                                ret += '*'+factor(x,dy=0,p=p,decimales=decimales)
                            return ret+')'
                        else:
                            ret = 1.0
                            for factor in factores:
                                ret *= factor(x,dy=0,p=0)
                            return signo*ret
                return producto
            elif esExponente:
                print('exponente',string,signoExponente)
                signoExponente+=[]
                base=self.strToMath(string=string[0:signoExponente[1]],dy=dy,p=p,decimales=decimales,v=v,composicion=composicion)
                exponente=self.strToMath(string=string[signoExponente[1]+2:],dy=dy,p=p,decimales=decimales,v=v,composicion=composicion)
                def potencia(x,dy=dy,p=p,decimales=decimales,signo=sig,base=base,exponente=exponente,mostrarSigno=0):
                    if mostrarSigno:
                        s='+' if signo>0.0 else '-'
                    else:
                        s=''
                    if dy:
                        if p:
                            return s+'((('+exponente(x,dy=0,p=p,decimales=decimales)+'*('+base(x,dy=0,p=p,decimales=decimales)+'**('+exponente(x,dy=0,p=p,decimales=decimales)+'-1))*'+base(x,dy=1,p=p,decimales=decimales)+') + ('+exponente(x,dy=1,p=p,decimales=decimales)+'*('+base(x,dy=0,p=p,decimales=decimales)+'**'+exponente(x,dy=0,p=p,decimales=decimales)+')*ln('+base(x,dy=0,p=p,decimales=decimales)+'))))'
                        else:
                            ret = exponente(x,dy=0,p=p,decimales=decimales)*(base(x,dy=0,p=p,decimales=decimales)**(exponente(x,dy=0,p=p,decimales=decimales)-1))*base(x,dy=1,p=p,decimales=decimales) + exponente(x,dy=1,p=p,decimales=decimales)*(base(x,dy=0,p=p,decimales=decimales)**exponente(x,dy=0,p=p,decimales=decimales))*math.log(base(x,dy=0,p=p,decimales=decimales))
                            return signo*ret
                    else:
                        if p:
                            return s+base(x,p=p,decimales=decimales)+'**('+exponente(x,p=p,decimales=decimales,mostrarSigno=1)+')'
                        else:
                            return signo*base(x)**exponente(x)
                return potencia
              
    def escalar(self, o=None,factor=None):
        if not o:
            o=self.escalarOrigen
        if not factor:
            factor=self.factoresDeEscala
        def ecuacionEscalada(abscisa,factor=factor,o=o,f=self.f,extras=self.extras):
            ordenada=factor[0]*(f(((abscisa-o[0])/factor[0])+o[0],extras=extras)-o[1])+o[1]
            return ordenada
        self.extras['string'] = '('+str(factor[0])+'*('+self.extras['string'].replace('x','(((x-('+str(o[0])+'))/'+str(factor[0])+')'+str(o[0])+')')+'-('+str(o[1])+'))+('+o[1]+'))'
        self.escalarOrigen=o 
        self.factoresDeEscala=factor
        self.f = ecuacionEscalada
        self.historial[len(self.historial)] = {'escalar':{'o':o,'factor':factor}} 
    def trasladar(self, o=None):
        if not o:
            o=self.trasladarOrigen
        def ecuacionTrasladada(abscisa,o=o,f=self.f,extras=self.extras):
            ordenada=f(abscisa+o[0],extras=extras)-o[1]
            return ordenada
        self.extras['string'] = '('+self.extras['string'].replace('x','(x+'+str(o[0])+')')+'-('+str(o[1])+'))'
        self.f = ecuacionTrasladada
        self.trasladarOrigen=o
        self.historial[len(self.historial)] = {'trasladar':{'o':o}} 
    def rotar(self, o=None,alfa=None):
        if not o:
            o=self.rotarOrigen
        if not alfa:
            alfa=self.alfa
        #sobre  el punto 'o', rotara el angulo 'alfa', en sentido antiorario 
        self.extras['alfa']=alfa
        def ecuacionRotada(abscisa,alfa=alfa,o=o,f=self.f,extras=self.extras):
            abscisa = self.inversa(abscisa,f= lambda abscisa : (abscisa-o[0])*math.cos(alfa)-(f(abscisa,extras=extras)-o[1])*math.sin(alfa)+o[0])
            ordenada = (abscisa-o[0])*math.sen(alfa)+(f(abscisa,extras=extras)-o[1])*math.cos(alfa)+o[1]
            return ordenada
        #self.extras['string'] = '(((x-('+str(o[0])+'))*('+str(math.sin(alfa))+'))+(('+self.extras['string']+'-('+str(o[1])+'))*('+str(math.cos(alfa))+'))+('+str(o[1])+'))'
        self.f = ecuacionRotada
        self.alfa=alfa
        self.rotarOrigen=o
        self.historial[len(self.historial)] = {'rotar':{'o':o,'alfa':alfa}}
    def deshacer(self):
        print('deshacer')
        
    def rehacer(self):
        print('rehacer')
class directorio(object):
    #pwd= es la ruta completa donde se ejecutara la clase,'C:\rutacompleta\carpetadelprograma'
    #baseName= solo el nombre de la carpeta donde se ejecutara la clase,'carpetadelprograma'
    #formato= retornara solo estos formatos en la lista de archivos dentro de la carpeta 'baseName' y las sub-carpetas, ['video','audio','imagen,'script','documento']
    #fullDir=guardara la ruta absoluta de cada uno de los ficheros, dentro de la lista de ficheros y sub-carpetas
    #renombrarArchivos= En los nombres de los archivos, cambiara los caracteres que no pertenecen a UTF-8. Esto evitara muchos errores de lectura y escritura
    def __init__(self,pwd='',baseName='',formato=[''],fullDir=1,renombrarArchivos=0,ignorar=[]):
        super(directorio, self).__init__()
        self.s=os.path.sep
        if baseName:
            self.baseName=baseName
            self.pwd= pwd if pwd else (os.getcwd()+self.s+self.baseName)
        else:
            self.baseName=os.getcwd().split(self.s)[-1]
            self.pwd=os.getcwd()

        self.prefijos=['N','U']
        self.ID=0
        self.index={}
        self.full=fullDir
        self.renombrarArchivos=renombrarArchivos
        self.ignorar=ignorar
        self.formatos=self.formato(formato)
        #print(self.pwd,self.baseName,self.ignorar)
        #print('Formatos:',self.formatos)
        self.directorio=self.carpetas(self.pwd,self.baseName)
        self.tabla(self.directorio,0,self.pwd)
        if self.renombrarArchivos:
            self.habilitar()
    def tabla(self,d,nivel,pwd):
        tab="    "
        print(tab*nivel+self.s+d['baseName'])
        for carpeta in d['SubCarpetas']:
            if not carpeta in self.ignorar:
                self.tabla(d['SubCarpetas'][carpeta], nivel+1, pwd+self.s+d['SubCarpetas'][carpeta]['baseName'])

        for f in d['ficheros']:
            if not d['ficheros'][f]['name'] in self.ignorar:
                self.index[self.ID]=d['ficheros'][f]
                self.ID += 1    
    def formato(self,formato):
        formatos=[]
        if 'video' in [f.lower() for f in formato]:
            formatos += ['.mp4','.avi','.webm','.mkv','.rmvb','.vob','.wmv']
        if 'audio' in [f.lower() for f in formato]:
            formatos += ['.mp3','.wav','.ogg','.m4a','.wav','.aud']
        if 'imagen' in [f.lower() for f in formato]:
            formatos += ['.jpeg','.jpg','.png','.ico','.bmp','.gif']
        if 'script' in [f.lower() for f in formato]:
            formatos += ['.sl','.ino','.c','.h','.xml','.java','.php','.html','.cmd','.cpp','.py','.js','.css','.txt']
        if 'documento' in [f.lower() for f in formato]:
            formatos += ['.pdf','.doc','.docx','.csv','.txt']
        if formatos:
            return formatos
        else:
            ['']
    def strToClave(self,nombre):
        clave=nombre
        filtro=[
            ('ú','u'),
            ('á','a'),
            ('é','e'),
            ('í','i'),
            ('ó','o'),
            ('ú','u'),
            ('_',''),
            ('-',''),
            ('¡',''),
            ('!',''),
            ('  ',' '),
            (' ',''),
            ('@',''),
            ('|',''),
            ('º',''),
            ('!',''),
            ('·',''),
            ('$',''),
            ('%',''),
            ('&',''),
            ('/',''),
            ('(',''),
            (')',''),
            ('¬',''),
            ('~',''),
            ('¡',''),
            ('´',''),
            ('ç',''),
            ('`',''),
            ('-',''),
            ('+',''),
            ('-',''),
            ('*',''),
            ('[',''),
            (']',''),
            ('{',''),
            ('}',''),
            ('"',''),
            ('<',''),
            ('>',''),
            ('=',''),
            ('?',''),
            ('¿','')
            ]
        for change in filtro:
            clave=clave.replace(change[0],change[1])
        return clave
    def carpetas(self,pwd,baseName):
        dirs = self.listaDeCarpetas(pwd,validar=1)
        ret = [archivo for archivo in os.listdir(pwd)  if ((os.path.isfile(pwd+self.s+archivo)) and (not archivo in self.ignorar))]
        fichero = {}
        for archivo in ret:    
            extencion=['.'+archivo.split('.')[-1].lower()]
            if (not self.formatos) or (extencion in self.formatos):
                #fichero={
                #    'name':nombre del fichero,
                #    'pwd':ruta absoluta o relativa al fichero,
                #    'tags':una lista con las etiquetas del fichero
                #    }
                palabras=archivo[:-len(extencion[0])].lower().split(' ')
                carpetasPadre=pwd[len(self.pwd):].lower().split(self.s)
                fichero[self.strToClave(archivo)] = {
                    'name':archivo,
                    'pwd':pwd[0 if self.full else len(self.pwd):]+self.s+archivo,
                    'tags':carpetasPadre+ palabras+extencion
                }
        sub={}
        if dirs:
            for file in dirs:
                sub[self.strToClave(file)]=self.carpetas(pwd+self.s+file,file)
        return {'baseName':baseName,'SubCarpetas':sub,'ficheros':fichero}
    def listaDeCarpetas(self,pwd,ignorar=[],validar=0):
        if not pwd:
            pwd=self.pwd
        dirs=[]
        for archivo in os.listdir(pwd):
            if (not archivo in self.ignorar) and (not archivo in ignorar):
                if archivo[0] in self.prefijos:
                    if self.renombrarArchivos:
                        os.rename(pwd+self.s+archivo,pwd+self.s+' '+archivo)
                        archivo=' '+archivo
                try:
                    if (not os.path.isfile(pwd+self.s+archivo)):
                        dirs+=[archivo]
                        if validar:
                            try:
                                os.listdir(pwd+self.s+archivo)
                            except:
                                dirs=dirs[:-1]
                except Exception as e:
                    raise e
        #return [carpeta for carpeta in os.listdir(pwd) if ((not (os.path.isfile(pwd+s+carpeta)) and (not carpeta in ignorar) ) )]
        return dirs 
    def listaDeFicheros(self,pwd,ignorar=[]):
        return  [fichero for fichero in os.listdir(pwd) if ((os.path.isfile(pwd+self.s+fichero)) and (not fichero in ignorar) )]
    def habilitar(self):
        filtro=[
            ('à','a'),
            ('è','e'),
            ('ì','i'),
            ('ò','o'),
            ('ù','u'),
            ('á','a'),
            ('é','e'),
            ('í','i'),
            ('ó','o'),
            ('ú','u'),
            ('Ò','O'),
            ('À','A'),
            ('È','E'),
            ('Ì','I'),
            ('Ù','U'),
            ('Ú','U'),
            ('Ó','O'),
            ('Í','I'),
            ('É','E'),
            ('Á','A')
        ]
        for f in self.index:
            pasar=self.index[f]['name']
            for letra in filtro:
                pasar=pasar.replace(letra[0],letra[1])
            ok=pasar
            for letra in pasar:
                if ord(letra) > 256:
                    ok=ok.replace(letra,'_')
            if ok[0] in self.prefijos:
                ok = ' '+ok 
            if ok != self.index[f]['name']: 
                if not os.path.isfile(str(self.index[f]['pwd'].replace(self.index[f]['name'],ok))):
                    os.rename(str(self.index[f]['pwd']),str(self.index[f]['pwd'].replace(self.index[f]['name'],ok)))
            self.index[f]['pwd']=self.index[f]['pwd'].replace(self.index[f]['name'],ok)
            self.index[f]['name']=ok      
class audio(object):
    """
    import pyAudio,wave
    pu:(guarani), traduccion:sonido
    clase que puede reproducir canales de sonido en segundo plano,
    se puede hacer sonar diferentes canales a la vez, identando diferentes objetos de esta clase,
    un objeto de este clase es como tener un canal de sonido para reproducir un sonido a la ves,
    si desea reproducir mas de un sonido a la ves, debera identar varios objetos de esta clase.
    ejemplo:
    canal_DO=audio("Flauta DO.wav","DO",pedal=0,tecla='A')
    canal_RE=audio("Flauta RE.wav","RE",pedal=0,tecla='S')
    canal_MI=audio("Flauta MI.wav","MI",pedal=0,tecla='D')

    """
    def __init__(self, archivo,nota,pedal,tecla=''):
        super(audio, self).__init__()
        import pyaudio  #maneja los puertos de audio, requiere 'portAudio' en el sistema
        import wave     #para manipular los ficheros de sonido, por defecto archivos .wav
        self.tecla=tecla #en caso de activar con alguna tecla
        self.archivo=archivo #archivo en formato .wav para reproducir
        self.nota=nota #en caso de que sea un instrumento
        self.pedal=0 #es para que el sonido siga, despues de darle .off(), util si quere que el sonido siga despues de soltar el sensor  
        self.wav = wave.open(self.archivo, 'rb')
        self.Audio=pyaudio.PyAudio()
        self.stream=None
        self.presionado=0
    def activo(self):
        if self.stream:
            return self.stream.is_active()
        else:
            return 0
    def callback(self,in_data, frame_count, time_info, status):
        data = self.wav.readframes(frame_count)
        return (data, pyaudio.paContinue)
    def play(self):
        self.wav = wave.open(self.archivo, 'rb')
        self.stream = self.Audio.open(format=self.Audio.get_format_from_width(self.wav.getsampwidth()),
            channels=self.wav.getnchannels(),
            rate=self.wav.getframerate(),
            output=True,
            stream_callback=self.callback)
        self.stream.start_stream()
    def stop(self):
        try:
            if self.stream.is_active():
                self.stream.stop_stream()
            self.stream.close()
            self.wav.close()
        except:
            print(self.nota,"ya esta cerrado")
        
    def terminate(self):
        self.stop()
        self.Audio.terminate()
    def On(self):
        self.presionado=1
        self.stop()
        self.play()
    def Off(self):
        self.presionado=0
        if self.stream.is_active() and self.pedal:
            self.stop()
    def wait(self):
        while self.stream.is_active():
            time.sleep(0.1)
class CRUD(object):
    """
    import sqlite3, os  
    La clase para administrar la base de datos 
        estructura del diccionario de tablas:
            tablas={
                'nombreTabla':{'campoID':['campoID','campo1','campo2','campo3','campo4','campo5']}
            }
    """
    def __init__(self, tabla, campoAutoincrement='id', dirCRUD="myMbareteCRUD.sql", reset=0):
        """
        bb='Mbarete.sql' nombre de la base de datos y del archivo que sera el contenedor del gestor de base de datos Sqlite3
        reset=1 borrara el archivo con el nombre 'miBaseDeDatos.sql' que le pases como parametro en dirCRUD='miBaseDeDatos.sql', 'Mbarete.sql' es el archivo que se crea por defecto si no se asigna un nombre diferente a 'dirCRUD'
        reset=0 no eliminara el archivo 'Mbarete.sql' y ejecutara los comandos SQL  en el archivo, si hacemos cambios en la estructura de una tabla en la base de datos debemois resetar el archivo para poder
        """
        self.campoAutoincrement=campoAutoincrement if (' ' in campoAutoincrement) else campoAutoincrement+' integer not null primary key autoincrement'
        self.reset=reset
        self.dirCRUD=dirCRUD
        if not '.' in self.dirCRUD.split(os.path.sep)[-1]:
            self.extencionCRUD='.sql'
        else:
            self.extencionCRUD='.'+(self.dirCRUD.split(os.path.sep)[-1]).split('.')[-1]

        self.tablas=tabla
        if self.reset:
            if (os.path.exists(self.dirCRUD)):
                os.remove(self.dirCRUD)
            for tabl in self.tablas:
                self.CrearTabla(tabl,self.tablas[tabl])
    def CrearTabla(self,nombreTabla,columnas,autoincrement=0,dirCRUD=''):
        if not dirCRUD:
            dirCRUD=self.dirCRUD
        # nombre_tabla="miTabla"
        # columnas=["primer_campo TEXT","segundo_campo TEXT","tercer_campo TEXT","cuarto_campo TEXT"]
        # Comprueba si la tabla "nombre_tabla" existe, en caso de no existir la creara
        # cursor.execute("""CREATE TABLE IF NOT EXISTS  ( TEXT, TEXT)""")
        """
        CrearTabla("Nombre_de_la_tabla",["primer_campo TEXT","segundo_campo TEXT","tercero_campo TEXT","cuarto_campo TEXT"])
        CREATE TABLE IF NOT EXISTS nombre_de_la_tabla (variable TEXT, valor TEXT)
        """
        if self.reset == False:
            self.tablas.setdefault(nombreTabla,[self.campoAutoincrement]+columnas if autoincrement else columnas)
        self.comandoSQL="CREATE TABLE IF NOT EXISTS "+str(nombreTabla)+" "
        self.colum="("
        for col in range(0,(len(columnas)-1),1):
            self.colum += str(columnas[col])+", "
        self.colum += str(columnas[-1])+")"
        self.comandoSQL += self.colum
        self.con = sqlite3.connect(dirCRUD)
        self.cursor = self.con.cursor()
        self.cursor.execute(self.comandoSQL)
        self.con.commit()
        self.cursor.close()
    def SelectAll(self,nombreTabla,typeSalida="dict",campoClave="id",dirCRUD=''):
        if not dirCRUD:
            dirCRUD=self.dirCRUD
        campos=[key.split(' ')[0] for key in self.tablas[nombreTabla]]
        noModificar=[self.tablas[nombreTabla].index(self.campoAutoincrement)] if (self.campoAutoincrement in self.tablas[nombreTabla]) else []
        self.con = sqlite3.connect(dirCRUD)
        self.cursor = self.con.cursor()
        self.cursor.execute("SELECT * FROM '%s'"%(nombreTabla))
        self.con.commit()
        if typeSalida=="list":
            ret=[campos]+[[strToVar(unicodeToStr(fila[n]))  if (not n in noModificar) else fila[n] for n in range(0,len(fila),1)] for fila in self.cursor.fetchall()]
        elif typeSalida=="dict":
            ret={}
            for registro in [[strToVar(unicodeToStr(fila[n]))  if (not n in noModificar) else fila[n] for n in range(0,len(fila),1)] for fila in self.cursor.fetchall()]:
                pasar={}
                for clave in campos:
                    pasar.setdefault(clave,registro[campos.index(clave)])
                ret.setdefault(registro[campos.index(campoClave if (campoClave in campos) else campos[0])],pasar)
        else:
            ret=[campos]+[[strToVar(unicodeToStr(fila[n]))  if (not n in noModificar) else fila[n] for n in range(0,len(fila),1)] for fila in self.cursor.fetchall()]
        self.cursor.close()
        return ret
    def Cargar(self,nombreTabla,columnas,valores,dirCRUD=''):
        if not dirCRUD:
            dirCRUD=self.dirCRUD
        """insert into '%s' ('%s','%s') values ('%s','%s')"%(tablas[tabla][0],tablas[tabla][1],tablas[tabla][2],infoHashtag[0], infoHashtag[1])"""
        self.comandoSQL="insert into "+str(nombreTabla)+" "
        self.colum="("
        self.val="("
        for col in range(0,(len(columnas)-1),1):
            self.colum=self.colum+str(columnas[col].split(' ')[0])+","
            self.val=self.val+"'"+strToUnicode(valores[col])+"',"
        self.colum=self.colum+str(columnas[-1].split(' ')[0])+")"
        self.val=self.val+"'"+strToUnicode(valores[-1])+"')"
        self.comandoSQL=self.comandoSQL+self.colum+" values "+self.val
        self.con = sqlite3.connect(dirCRUD)
        self.cursor = self.con.cursor()
        self.cursor.execute(self.comandoSQL)
        self.con.commit()
        self.cursor.close() 
    def Modificar(self,nombreTabla,columnas,valores,dirCRUD=''):
        if not dirCRUD:
            dirCRUD=self.dirCRUD
        """ sin terminar """
        self.comandoSQL="insert into "+str(nombreTabla)+" "
        self.colum="("
        self.val="("
        for col in range(0,(len(columnas)-1),1):
            self.colum=self.colum+str(columnas[col].split(' ')[0])+","
            self.val=self.val+"'"+strToUnicode(valores[col])+"',"
        self.colum=self.colum+str(columnas[-1].split(' ')[0])+")"
        self.val=self.val+"'"+strToUnicode(valores[-1])+"')"
        self.comandoSQL=self.comandoSQL+self.colum+" values "+self.val
        self.con = sqlite3.connect(dirCRUD)
        self.cursor = self.con.cursor()
        self.cursor.execute("DELETE FROM %s WHERE %s='%s'"%(nombreTabla,columnas[0].split(' ')[0],strToUnicode(valores[0])))
        self.con.commit()
        self.cursor.execute(self.comandoSQL)
        self.con.commit()
        self.cursor.close()
    def Elimina(self,nombreTabla,columnas,valores,dirCRUD=''):
        if not dirCRUD:
            dirCRUD=self.dirCRUD
        """ """
        self.con = sqlite3.connect(dirCRUD)
        self.cursor = self.con.cursor()
        self.cursor.execute("DELETE FROM %s WHERE %s='%s'"%(nombreTabla,columnas[0].split(' ')[0],strToUnicode(valores[0])))
        self.con.commit()
        self.cursor.close()
    def exportarTablas(self,tabla=[],formato="shell",campoClave="",file="",dirCRUD=''):
        if not dirCRUD:
            dirCRUD=self.dirCRUD
        """ guardara las tablas que estan guardadas en la base de datos en formato ["shell","csv","py","js"] """
        ret={}
        self.con = sqlite3.connect(dirCRUD)
        self.cursor = self.con.cursor()
        if tabla:
            for clave in tabla:
                ret.setdefault(clave,[[campo.split(" ")[0] for campo in self.tablas[clave]]])
                noModificar=[self.tablas[clave].index(self.campoAutoincrement)] if (self.campoAutoincrement in self.tablas[clave]) else []
                self.cursor.execute("SELECT * FROM '%s'"%(clave))
                self.resultado = self.cursor.fetchall()
                self.con.commit()
                for i in range(0,len(self.resultado),1):
                    registro=list(self.resultado[i][0:])
                    self.resultado[i]=[strToVar(unicodeToStr(registro[n]))  if (not n in noModificar) else registro[n] for n in range(0,len(registro),1)]
                ret[clave]+=self.resultado
        else:
            for tabl in self.tablas:
                ret.setdefault(tabl,[[campo.split(" ")[0] for campo in self.tablas[tabl]]])
                noModificar=[self.tablas[tabl].index(self.campoAutoincrement)] if (self.campoAutoincrement in self.tablas[tabl]) else []
                self.cursor.execute("SELECT * FROM '%s'"%(tabl))
                self.resultado = self.cursor.fetchall()
                self.con.commit()
                for i in range(0,len(self.resultado),1):
                    registro=list(self.resultado[i][0:])
                    self.resultado[i]=[strToVar(unicodeToStr(registro[n]))  if (not n in noModificar) else registro[n] for n in range(0,len(registro),1)]
                ret[tabl]+=self.resultado
        self.cursor.close()
        if formato.lower() in "shell consola":
            f='en consola'
            for clave in ret:
                print('Nombre de la tabla:',clave,'\n','Numero de Registros:',len(ret[clave]))
                for i in ret[clave]:
                    print(" ",i)
        elif formato.lower() in ".csv":
            f=(file if file else self.dirCRUD[:-len(self.extencionCRUD)])+".csv"
            file=open(f,"w")
            for clave in ret:
                file.write('Nombre de la tabla:'+";"+str(clave)+'\n')
                file.write('Numero de Registros:'+";"+str(len(ret[clave]))+'\n')
                for i in ret[clave]:
                    registro=""
                    for x in i:
                        registro+=';'+str(x) 
                    file.write(" "+";"+str(registro)+""+'\n')
                file.write('\n'+'\n'+'\n'+'\n'+'\n')
        elif formato.lower() in ".py":
            f=(file if file else self.dirCRUD[:-len(self.extencionCRUD)])+".py"
            file=open(f,"w")
            file.write(str(r'#!/usr/bin/env python'+'\n'))
            file.write(str(r'# -*- coding: latin-1 -*-'+'\n'))
            for clave in ret:
                campos=[campo.split(" ")[0] for campo in self.tablas[clave]]
                myClave=campoClave if campoClave in campos else campos[0]
                if 1<len(ret[clave]):
                    file.write(str(clave)+'={\n')
                    for reg in range(1,len(ret[clave]),1):
                        file.write("    '"+str(ret[clave][reg][campos.index(myClave)])+"':{\n")
                        for x in range(0,len(ret[clave][reg])-1,1):
                            file.write("        '"+str(campos[x])+"':"+( '"'+ret[clave][reg][x]+'"' if "str" in str(type(ret[clave][reg][x])) else str(ret[clave][reg][x]) )+",\n")
                        file.write("        '"+str(campos[-1])+"':"+( '"'+ret[clave][reg][-1]+'"' if "str" in str(type(ret[clave][reg][-1])) else str(ret[clave][reg][-1]) )+"\n")
                        file.write("    }\n" if len(ret[clave][1:])==reg else "    },\n" )
                    file.write('}\n'+'\n')
            file.close()
        print("Fue exportado Exitosamente ,",f)
    def command(self,comandoSQL,ret=0,dirCRUD=''):
        if not dirCRUD:
            dirCRUD=self.dirCRUD
        self.con = sqlite3.connect(dirCRUD)
        self.cursor = self.con.cursor()
        self.cursor.execute(comandoSQL)
        self.con.commit()
        rtrn=self.cursor.fetchall()
        self.cursor.close()
        if ret:
            return rtrn
class GUI(object):
    """
        Clase de una GUI basado en Tkinter para crear y editar una GUI SIMPLE, 
        y posiblemente se pueda exportar una version .html con la logica en javascript 
        en un .js y sus estilos en un .css 
    """
    #titulo="Mbarete Proyect",
    #bbdd={},
    #comandos={},
    #tablas={},
    #reset=0,
    #dirCRUD='',
    #pwd=''
    #el paramatro recibido en 'bbdd={}' debe ser un gestor de bases de datos de la clase CRUD, en otras palabras debe ser un objeto de la clase 'CRUD', y eso debe declararse antes de inicializar esta clase para poder pasarle a 'GUI'
    def __init__(self,titulo="Mbarete Proyect",bbdd={},comandos={},tablas={},reset=0,dirCRUD='',pwd='', campoAutoincrement='id'):
        if pwd:
            self.pwd=pwd
        else:
            self.pwd=os.getcwd()
        self.tablas={
            'atributos':["clave TEXT","valor TEXT"],
            'inputType':["clave TEXT","valor TEXT"],
            'Vars':["clave TEXT","valor TEXT"]
            }
        if tablas:
            for clave in tablas:
                self.tablas.setdefault(clave,tablas[clave])
        if dirCRUD:
            self.dirCRUD=dirCRUD
        else:
            self.dirCRUD=self.pwd+os.path.sep+titulo.replace(' ','_')+"_CRUD_.sql"
        if bbdd:
            self.Sql=bbdd
            self.dirCRUD=self.Sql.dirCRUD
        else:
            self.Sql=CRUD(self.tablas, campoAutoincrement='id', dirCRUD=self.dirCRUD, reset=reset)
        self.variablesEnSql=[]
        self.gitignore=[]
        self.menus={}
        self.Vars={}
        if reset:
            from mbarete import myVars as externo
            self.INPUTS_CONFIG=self.crearVariable("inputType",externo.inputsDefault)
            self.atrb=self.crearVariable("atributos",externo.atributos)
            del (externo)
            for tabla in self.tablas:
                if not tabla in self.Sql.tablas:
                    self.Sql.CrearTabla(tabla,self.tablas[tabla])
                    #print(tabla)
            #print(self.Sql.tablas)
        else:
            self.INPUTS_CONFIG=self.recuperarVariable("inputType")
            self.atrb=self.recuperarVariable("atributos")
        self.atrb['bbdd']=self.dirCRUD
        self.atrb['campoAutoincrement']=self.Sql.campoAutoincrement
        
        #lista de los widgetType que son creados automaticamente por y para esta clase al momento de declara un objeto de esta clase
        self.defaultWidgets=['Tk','myFrame','scrollCanvas','myCanvas','scrollbar','panel','Frame']
        #widgets que seran conectados automaticamente a variables de tipo IntVar(),StringVar(),DoubleVar(),BooleanVar()
        self.widgetConectadoaVars=['Radiobutton','Checkbutton','Entry']
        #Contendra todos los widgets tkinter, canvas, ttk, etc.
        #Cada elemento del diccionario, contendra el widget y todas las informaciones adicionales para poder configurar y manipular el widget
        self.widgets={}
        self.widgets.setdefault('tk',
            {
                'widget':Tk(),
                'inputType':'Tk'
                }
            )
        self.title(titulo)
        #Enlazamos la funcion 'self.onkey(self,event)' al evento "<Key>" que es cada ves que se presiona una tecla y el Widget 'tk' este en uso o en Foco, o sea esten usando el programa
        self.widgets['tk']['widget'].bind("<Key>",self.onkey)
        #Enlazamos una Funcion anonima 'lambda' al evento "<MouseWheel>", este evento se activa a mover la rueda del raton
        self.widgets['tk']['widget'].bind("<MouseWheel>",lambda event: self.widgets['canvas']['widget'].yview_scroll(int(-1*(event.delta/120)), "units"))
        #cada ves que presionen alguna tecla del raton se ejecutara la funcion 'self.onclick(self,event)'
        self.widgets['tk']['widget'].bind("<Button>",self.onclick)
        #cada ves se modifique algo en 'tk' se ejecutara la funcion 'self.onclick(self,event)'. Tamaño o posicion de la ventana o algun evento .config en el widget 'tk' que seria la ventana.
        self.widgets['tk']['widget'].bind("<Configure>",self.responsive)
        self.widgets.setdefault('f',{
                'widget':Frame(self.widgets['tk']['widget']),
                'inputType':'myFrame',
                'padre':'tk'
                })
        #canvas para usar como area de Scroll
        self.widgets.setdefault('canvas',{
                'widget':Canvas(self.widgets['f']['widget']),
                'inputType':'myCanvas',
                'padre':'f'
                })
        #barra de Scroll Vertical
        self.widgets.setdefault('yscrollbar',{
                'widget':Scrollbar(self.widgets['f']['widget'], orient='vertical',command=self.widgets['canvas']['widget'].yview),
                'inputType':'scrollbar',
                'padre':'f'
                })
        #barra de Scroll Horizontal
        self.widgets.setdefault('xscrollbar',{
                'widget':Scrollbar(self.widgets['f']['widget'], orient='horizontal',command=self.widgets['canvas']['widget'].xview),
                'inputType':'scrollbar',
                'padre':'f'
                })
        #Frame Scrolleado con el widget 'canvas' ya que 'myFrame' pertenece a 'canvas' y 'canvas' a su ves esta siendo controlado con Scrollbar en X y en Y
        self.widgets.setdefault('myFrame',{
                'widget':Frame(self.widgets['canvas']['widget'],width=self.atrb['ancho'],height=self.atrb['alto'],bg=self.atrb['fondo']),
                'inputType':'myFrame'
                })
        self.widgets['myFrame']['widget'].bind("<Configure>",lambda event: self.widgets['canvas']['widget'].configure(scrollregion=self.widgets['canvas']['widget'].bbox("all")))        
        self.widgets['canvas']['widget'].create_window((0, 0),window=self.widgets['myFrame']['widget'],anchor="nw")
        self.widgets['canvas']['widget'].configure(yscrollcommand=self.widgets['yscrollbar']['widget'].set,xscrollcommand=self.widgets['xscrollbar']['widget'].set)
        self.widgets['xscrollbar']['widget'].pack(side='bottom', fill='x')
        self.widgets['yscrollbar']['widget'].pack(side='right', fill='y')
        self.widgets['f']['widget'].pack(expand=1, fill='both')
        self.widgets['canvas']['widget'].pack(side="left" , fill="both", expand=True)
        self.widgets['tk']['widget'].geometry("%sx%s+%s+%s"%(str(self.atrb['ancho']),str(self.atrb['alto']),str(self.atrb['Xexterior']),str(self.atrb['Yexterior'])))
        self.widgets['tk']['widget'].update()
        #print(buscarFunciones("dictFunciones.py"))
        self.clickDerecho=[
            [0,500,0,500,"pruebaClickDerecho"]
            ]
        self.clickIzquierdo=[
            [0,500,0,500,"pruebaClickIzquierdo"]
            ]
        self.clickRueda=[
            [0,500,0,500,"pruebaClickRueda"]
            ]

        self.defaultCommand={
            'GUI_destroy':{'inputType':'Button','command':'GUI_destroy','text':'Salir'},
            'GUI_Aceptar':{'inputType':'Button','command':'GUI_Aceptar','text':'ACEPTAR'},
            'GUI_Guardar':{'inputType':'Button','command':'GUI_Guardar','text':'GUARDAR'},
            'GUI_Borrar':{'inputType':'Button','command':'GUI_Borrar','text':'BORRAR'},
            'GUI_Leer':{'inputType':'Button','command':'GUI_Leer','text':'Leer'},
            'GUI_Exportar_PY':{'inputType':'Button','command':'GUI_Exportar_PY','text':'Exportar a '+self.atrb['titulo']+'.py'},
            'GUI_Exportar_CSV':{'inputType':'Button','command':'GUI_Exportar_CSV','text':'Exportar a '+self.atrb['titulo']+'.csv'}
            }
        self.command={
            'pruebaClickDerecho':[myFuncion,(self.atrb['titulo'],self.atrb['bbdd'],"pruebaClickDerecho")],
            'pruebaClickIzquierdo':[myFuncion,(self.atrb['titulo'],self.atrb['bbdd'],"pruebaClickIzquierdo")],
            'pruebaClickRueda':[myFuncion,(self.atrb['titulo'],self.atrb['bbdd'],"pruebaClickRueda")],
            'GUI_destroy':lambda : self.widgets['tk']['widget'].destroy(),
            'GUI_Aceptar':lambda : print('Aceptar ',self.atrb['frameActivo']),
            'GUI_Guardar':lambda : self.comandoGuardar(),
            'GUI_Borrar':lambda : print('Borrar ',self.widgets['tk']['text']),
            'GUI_Leer':lambda : self.comandoLeer(),
            'GUI_Exportar_PY':lambda : self.comandoExportar(campoClave='id',file='',formato='.py',tabla=[]),
            'GUI_Exportar_CSV':lambda : self.comandoExportar(campoClave='id',file='',formato='.csv',tabla=[])
            }
        if comandos:
            for clave in comandos:
                self.command.setdefault(clave,comandos[clave])
    def title(self,titulo):
        self.atrb['titulo']=titulo
        self.widgets['tk']['widget'].title(self.atrb['titulo'])
    def loop(self):
        self.update()
        self.widgets['tk']['widget'].update()
        self.widgets['tk']['widget'].mainloop()
    def updateVar(self,name,arg2,mod):
        #print(name,arg2,mod)
        nombreSinPadre=name.replace(self.widgets[name]['padre']+'_','')
        if self.widgets[name]['inputType'] in ['Radiobutton']:
            ok_name=nombreSinPadre.replace('_'+nombreSinPadre.split('_')[-1],'')
        else:
            ok_name=nombreSinPadre
        self.widgets[self.widgets[name]['padre']]['value'][ok_name]=self.Vars[name].get()    
    def setVar(self,name,values={}):
        myVars=[]
        if self.widgets[name]['inputType'] in ['Frame','panel']:
            for w in self.widgets:
                if (self.widgets[w]['inputType'] not in self.defaultWidgets):
                    if (self.widgets[w]['padre'] == name) and (self.widgets[w]['inputType'] in self.widgetConectadoaVars):
                        myVars += [w]
            for buscar in [w for w in myVars if (self.widgets[w]['inputType'] in ['Radiobutton'])]:    
                    if buscar in self.Vars:
                        for v in values:
                            if str(name+'_'+v) in buscar:
                                self.Vars[buscar].set(values[v])
            for v in values:
                if str(name+'_'+v) in self.Vars:
                    self.Vars[name+'_'+v].set(values[v])
            if not values:
                for v in myVars:
                    if v in self.Vars:
                        self.Vars[v].set(self.INPUTS_CONFIG[self.widgets[v]['inputType']]['value'])
    def onkey(self,event):
        #print(event)
        pass
    def onclick(self,event):
        for w in self.widgets:
            if self.widgets[w]['widget']==event.widget:
                name = w
            if 'canvas' in self.widgets[w]:
                if self.widgets[w]['canvas']==event.widget:
                    name = w
        if name=='canvas':
            xReal=event.x
            yReal=event.y
        else:
            hijo=name
            padre=self.widgets[name]['padre']
            while padre!='tk':
                if 'padre' in self.widgets[hijo]['padre']:
                    padre=self.widgets[hijo]['padre']
                if self.widgets[hijo]['inputType'] in self.defaultWidgets:
                    padre='tk'
                else:
                    hijo=padre           
            #print('name:',name,'hijo:',hijo,'padre:',padre)
            xReal=int(self.widgets[hijo]['xPlace']+event.x)
            yReal=int(self.widgets[hijo]['yPlace']+event.y)
        #print(xReal,yReal)
        #print(event.x,event.y,event.state,event.num,event.widget)
        if 1==int(event.num):
            for area in self.clickIzquierdo:
                if ((area[1]>=event.x) and (area[0]<=event.x)) and ((area[3]>=event.y) and (area[2]<=event.y)):
                    threading.Thread(target=self.command[area[-1]][0],args=self.command[area[-1]][1]).start()
        elif 2==int(event.num):
            for area in self.clickRueda:
                if ((area[1]>=event.x) and (area[0]<=event.x)) and ((area[3]>=event.y) and (area[2]<=event.y)):
                    threading.Thread(target=self.command[area[-1]][0],args=self.command[area[-1]][1]).start()
        elif 3==int(event.num):
            for area in self.clickDerecho:
                if ((area[1]>=event.x) and (area[0]<=event.x)) and ((area[3]>=event.y) and (area[2]<=event.y)):
                    threading.Thread(target=self.command[area[-1]][0],args=self.command[area[-1]][1]).start()
    def responsive(self,event):
        self.widgets['tk']['widget'].update()
        if (self.atrb['alto'] != self.widgets['tk']['widget'].winfo_height()) or (self.atrb['ancho']!= self.widgets['tk']['widget'].winfo_width()):
            self.atrb['alto'] = self.widgets['tk']['widget'].winfo_height()
            self.atrb['ancho']= self.widgets['tk']['widget'].winfo_width()
            self.update()
    def recuperarVariable(self,nombreVariable):
        #funcion que recupera variables de una tabla y los retorna como una variable original de este clase
        ret={}
        dictReturn=self.Sql.SelectAll(nombreVariable,typeSalida='dict',campoClave='clave')
        if nombreVariable in self.tablas:
            for clave in dictReturn:
                ret.setdefault(dictReturn[clave]['clave'],dictReturn[clave]['valor'])
        return ret
    def crearVariable(self,nombreVariable,variables):
        #nombreVariable: nombre de la variable en el programa
        #variables: variable tipo diccionario sera guardada en una tabla, y el nombre de la tabla sera 'nombreVariable'
        self.tablas.setdefault(nombreVariable,["clave TEXT","valor TEXT"])
        self.variablesEnSql+=[nombreVariable]
        self.Sql.CrearTabla(nombreVariable,self.tablas[nombreVariable])
        for clave in variables:
            self.Sql.Cargar(nombreVariable,self.tablas[nombreVariable],[clave, variables[clave] ])
        ret={}
        dictReturn=self.Sql.SelectAll(nombreVariable,typeSalida='dict',campoClave='clave')
        for clave in dictReturn:
            ret.setdefault(dictReturn[clave]['clave'],dictReturn[clave]['valor'])
        return ret
    def guardarVariable(self,nombreVariable,variables):
        for clave in variables:
            self.Sql.Cargar(nombreVariable,self.tablas[nombreVariable],[clave, variables[clave]]) 
    def update(self):
        self.widgets['tk']['widget'].geometry("%sx%s"%(str(self.atrb['ancho']),str(self.atrb['alto'])))
        #print("update")
        #self.widgets['myFrame']['widget'].config(width = self.atrb['ancho'], height = self.atrb['alto'])
        #self.widgets['canvas']['widget'].config(width = self.atrb['ancho'], height = self.atrb['alto'])
        self.margenSuperior=0
        self.margenInferior=0
        self.margenIzquierdo=0
        self.margenDerecho=0
        espasioAlfinal=100
        altoTotal=0
        anchoTotal=0
        sandwishSuperior=[]
        sandwishInferior=[]
        sandwishDerecho=[]
        sandwishIzquierdo=[]
        #actualizamos los parametros 'command' de los widgets
        for w in self.widgets:
            if self.widgets[w]['inputType']=='Button':            
                self.widgets[w]['widget'].config(
                    command=self.command[self.widgets[w]['command']],
                    text=self.widgets[w]['text'],
                    width=self.widgets[w]['width'] if self.widgets[w]['width'] else None,
                    bg=self.widgets[w]['bgColor'],
                    fg=self.widgets[w]['fontColor'],
                    font=(self.widgets[w]['fontType'],self.widgets[w]['fontSize'])
                    )
            elif self.widgets[w]['inputType'] in ['Label','Checkbutton','Radiobutton']:
                self.widgets[w]['widget'].config(
                    text=self.widgets[w]['text'],
                    bg=self.widgets[w]['bgColor'],
                    fg=self.widgets[w]['fontColor'],
                    font=(self.widgets[w]['fontType'],self.widgets[w]['fontSize'])
                    )
            elif self.widgets[w]['inputType'] in ['Entry']:
                self.widgets[w]['widget'].config(
                    bg=self.widgets[w]['bgColor'],
                    width=self.widgets[w]['width'] if self.widgets[w]['width'] else None,  
                    fg=self.widgets[w]['fontColor'],
                    insertbackground=self.widgets[w]['fontColor'],
                    font=(self.widgets[w]['fontType'],self.widgets[w]['fontSize'])
                    )
                #self.widgets[w]['padre']+self.widgets[w]['']
                #[self.widgets[w]['name']+'_LabelCanvas']
                if self.widgets[w]['name']+'_LabelCanvas' in self.widgets[self.widgets[w]['padre']]['inputs']:
                    self.widgets[self.widgets[w]['padre']]['inputs'][self.widgets[w]['name']+'_LabelCanvas']['xPlace']=self.widgets[w]['xPlace']
                    self.widgets[self.widgets[w]['padre']]['inputs'][self.widgets[w]['name']+'_LabelCanvas']['yPlace']=self.widgets[w]['yPlace']
                    self.widgets[self.widgets[w]['padre']]['inputs'][self.widgets[w]['name']+'_LabelCanvas']['ancho']=self.anchoWidget(self.widgets[w])
                    self.widgets[self.widgets[w]['padre']]['inputs'][self.widgets[w]['name']+'_LabelCanvas']['alto']=self.altoWidget(self.widgets[w])*0.5
                    self.widgets[self.widgets[w]['padre']]['inputs'][self.widgets[w]['name']+'_LabelCanvas']['fontSize']=int(self.widgets[w]['fontSize']*0.7)
                    self.widgets[self.widgets[w]['padre']]['inputs'][self.widgets[w]['name']+'_LabelCanvas']['fontType']=self.widgets[w]['fontType']
                    self.widgets[self.widgets[w]['padre']]['inputs'][self.widgets[w]['name']+'_LabelCanvas']['fontColor']=self.widgets[w]['fontColor']
                    self.widgets[self.widgets[w]['padre']]['inputs'][self.widgets[w]['name']+'_LabelCanvas']['bgColor']=self.widgets[w]['bgColor']
                    self.widgets[self.widgets[w]['padre']]['inputs'][self.widgets[w]['name']+'_LabelCanvas']['text']=self.widgets[w]['text']
                            
        #calculamos espacios de los margenes que necesitaremos para ubicar en ellos los paneles laterales, superiores, inferiores
        for myWidget in self.widgets:
            if self.widgets[myWidget]['inputType']=='panel' and self.widgets[myWidget]['visible']:
                self.margenDerecho +=  ((11-self.widgets[myWidget]['fontSize'])+(self.widgets[myWidget]['width']+1)*(self.widgets[myWidget]['fontSize']-1)+(self.widgets[myWidget]['width']*self.atrb['fontSizeToCorrectorAncho'][self.widgets[myWidget]['fontType']][self.widgets[myWidget]['fontSize']])) if ('e'==self.widgets[myWidget]['anchor'][0]) else 0 
                self.margenIzquierdo +=  ((11-self.widgets[myWidget]['fontSize'])+(self.widgets[myWidget]['width']+1)*(self.widgets[myWidget]['fontSize']-1)+(self.widgets[myWidget]['width']*self.atrb['fontSizeToCorrectorAncho'][self.widgets[myWidget]['fontType']][self.widgets[myWidget]['fontSize']])+self.atrb['scrollVerticalAncho']) if ('o'==self.widgets[myWidget]['anchor'][0]) else 0 
                self.margenSuperior += (self.atrb['fontSizeToAlto'][self.widgets[myWidget]['fontType']][self.widgets[myWidget]['fontSize']]) if ('n'==self.widgets[myWidget]['anchor'][0]) else 0 
                self.margenInferior += self.atrb['scrollHorizontalAlto']+(self.atrb['fontSizeToAlto'][self.widgets[myWidget]['fontType']][self.widgets[myWidget]['fontSize']]) if ('s'==self.widgets[myWidget]['anchor'][0]) else 0

        for myWidget in self.widgets:
            if self.widgets[myWidget]['inputType'] in ['Frame','panel']:
                if self.widgets[myWidget]['visible']:
                    #menus[myWidget]={'anchor':self.widgets[myWidget]['anchor'],'':self.widgets[myWidget]['']}
                    #hallamos el espacio total en X y Y que ocuaran todos los widget dentro del 'frame' o 'panel'
                    ySuma,xSuma=0,0
                    for w in self.widgets:
                        if (self.widgets[w]['inputType'] not in self.defaultWidgets):
                            if (self.widgets[w]['padre'] == myWidget):
                                posicionfinalenY=self.widgets[w]['yPlace']+self.widgets[w]['alto']+self.atrb['scrollHorizontalAlto']+self.margenSuperior + espasioAlfinal
                                ySuma = posicionfinalenY if posicionfinalenY > ySuma else ySuma

                                posicionfinalenX=self.widgets[w]['xPlace']+self.widgets[w]['ancho']+self.atrb['scrollVerticalAncho']+self.margenIzquierdo
                                xSuma = posicionfinalenX if posicionfinalenX > xSuma else xSuma
                    
                    if self.widgets[myWidget]['inputType'] in ['Frame']:
                        self.widgets[myWidget]['ancho'] =(self.atrb['ancho'])-self.margenIzquierdo-self.margenDerecho
                        self.widgets[myWidget]['alto'] = ySuma
                        self.widgets[myWidget]['yPlace'] = self.margenSuperior
                        self.widgets[myWidget]['xPlace'] = self.margenIzquierdo 
                        self.atrb['frameActivo']=myWidget

                        if ySuma>altoTotal:
                            altoTotal=ySuma
                            #print(self.margenSuperior,self.margenInferior,self.margenIzquierdo,self.margenDerecho)
                            #print(ySuma,self.atrb['alto'])
                        if self.widgets['myFrame']['widget'].winfo_height()<altoTotal:
                            self.widgets['myFrame']['widget'].config(width=self.atrb['ancho'],height=altoTotal,bg=self.widgets[myWidget]['bgColor'])
                        if self.widgets['myFrame']['widget'].winfo_height()>self.widgets[myWidget]['alto']:
                            self.widgets['myFrame']['widget'].config(width=self.atrb['ancho'],height=self.atrb['alto'],bg=self.widgets[myWidget]['bgColor'])

                    if self.widgets[myWidget]['inputType'] in ['panel']:
                        self.widgets[myWidget]['ancho'] = ((11-self.widgets[myWidget]['fontSize'])+(self.widgets[myWidget]['width']+1)*(self.widgets[myWidget]['fontSize']-1)+(self.widgets[myWidget]['width']*self.atrb['fontSizeToCorrectorAncho'][self.widgets[myWidget]['fontType']][self.widgets[myWidget]['fontSize']])) if (('e'==self.widgets[myWidget]['anchor'][0]) or ('o'==self.widgets[myWidget]['anchor'][0])) else (self.atrb['ancho']-self.atrb['scrollVerticalAncho'])
                        self.widgets[myWidget]['alto'] = self.atrb['alto']-self.margenInferior-self.margenSuperior-self.atrb['scrollHorizontalAlto'] if (('e'==self.widgets[myWidget]['anchor'][0]) or ('o'==self.widgets[myWidget]['anchor'][0])) else (self.atrb['fontSizeToAlto'][self.widgets[myWidget]['fontType']][self.widgets[myWidget]['fontSize']])
                        self.widgets[myWidget]['yPlace']= self.margenSuperior if (('e'==self.widgets[myWidget]['anchor'][0]) or ('o'==self.widgets[myWidget]['anchor'][0])) else (self.atrb['alto']-self.widgets[myWidget]['alto']-self.atrb['scrollHorizontalAlto']-sum([self.widgets[ocupa]['alto'] for ocupa in sandwishInferior]) if ('s'==self.widgets[myWidget]['anchor'][0]) else sum([self.widgets[ocupa]['alto'] for ocupa in sandwishSuperior]))
                        self.widgets[myWidget]['xPlace']= 0 if (('n'==self.widgets[myWidget]['anchor'][0]) or ('s'==self.widgets[myWidget]['anchor'][0])) else (self.atrb['ancho']-self.widgets[myWidget]['ancho']-self.atrb['scrollVerticalAncho']-sum([self.widgets[ocupa]['ancho'] for ocupa in sandwishDerecho]) if ('e'==self.widgets[myWidget]['anchor'][0]) else sum([self.widgets[ocupa]['ancho'] for ocupa in sandwishIzquierdo]))
                        if ('n'==self.widgets[myWidget]['anchor'][0]):
                            sandwishSuperior += [myWidget]
                        elif ('s'==self.widgets[myWidget]['anchor'][0]): 
                            sandwishInferior += [myWidget]
                        elif ('e'==self.widgets[myWidget]['anchor'][0]): 
                            sandwishDerecho += [myWidget]
                        elif ('o'==self.widgets[myWidget]['anchor'][0]): 
                            sandwishIzquierdo += [myWidget]
                    if (self.widgets[myWidget]['ancho']!=self.widgets[myWidget]['widget'].winfo_width()) or (self.widgets[myWidget]['alto']!=self.widgets[myWidget]['widget'].winfo_height()) or (not (self.widgets[myWidget]['widget'].place_info())):
                        self.widgets[myWidget]['widget'].config(width=self.widgets[myWidget]['ancho'],height=self.widgets[myWidget]['alto'],bg=self.widgets[myWidget]['bgColor'])
                        self.widgets[myWidget]['canvas'].config(width=self.widgets[myWidget]['ancho'],height=self.widgets[myWidget]['alto'],bg=self.widgets[myWidget]['bgColor'])
                        if not (self.widgets[myWidget]['widget'].place_info()):
                            self.widgets[myWidget]['canvas'].place(x=0, y=0)
                        #gradient(poligono=[],x=0,y=0,height=0,width=0,rotacion=0,color1='#ffffff',color2='#000000')
                        if self.widgets[myWidget]['degradado']:
                            for line in gradient(width=self.widgets[myWidget]['ancho'],height=self.widgets[myWidget]['alto'],color1=self.widgets[myWidget]['bgColor'],color2=escalarHex(h=self.widgets[myWidget]['bgColor'],factor=0.05)):
                                self.widgets[myWidget]['canvas'].create_line(line[0],line[1],line[2],line[3],fill=line[4])
                        for w in self.widgets[myWidget]['inputs']:
                            if self.widgets[myWidget]['inputs'][w]['inputType'] in ['LabelCanvas']:
                                self.widgets[myWidget]['canvas'].create_text(
                                    self.widgets[myWidget]['inputs'][w]['xPlace']+(self.widgets[myWidget]['inputs'][w]['ancho']/2),
                                    self.widgets[myWidget]['inputs'][w]['yPlace']-(self.widgets[myWidget]['inputs'][w]['alto']/2),
                                    fill=self.widgets[myWidget]['inputs'][w]['fontColor'],
                                    font=(self.widgets[myWidget]['inputs'][w]['fontType'],self.widgets[myWidget]['inputs'][w]['fontSize']), 
                                    text=self.widgets[myWidget]['inputs'][w]['text']
                                )
                    self.widgets[myWidget]['widget'].place(x=self.widgets[myWidget]['xPlace'],y=self.widgets[myWidget]['yPlace'])
                        
                        
                    #self.widgets[myWidget]['canvas'].config(width=self.widgets[myWidget]['ancho'],height=self.widgets[myWidget]['alto'],bg=self.widgets[myWidget]['bgColor'])
                    #self.widgets[myWidget]['canvas'].place(x=0, y=0)
                else:
                    self.widgets[myWidget]['widget'].place_forget()
                    print(myWidget,'place_forget')
                
        for myWidget in self.widgets:
            if (self.widgets[myWidget]['inputType'] not in self.defaultWidgets):
                self.widgets[myWidget]['widget'].place(x=self.widgets[myWidget]['xPlace'],y=self.widgets[myWidget]['yPlace'])
        self.widgets['tk']['widget'].update()
        #self.widgets['canvas']['widget'].config(scrollregion=(0,0,self.widgets['canvas']['ancho'],self.widgets['canvas']['alto']))#self.widgets['canvas']['widget'].config(width = self.atrb['ancho'], height = self.atrb['alto'], scrollregion=(0,0,anchoTotal,altoTotal))
        #self.widgets['tk']['widget'].geometry("%sx%s+%s+%s"%(str(self.atrb['ancho']),str(self.atrb['alto']),str(self.atrb['Xexterior']),str(self.atrb['Yexterior'])))
    def anchoWidget(self,w):
        return int( (11-w['fontSize']) + ((w['width']+1)*(w['fontSize']-1)) + (w['width']*self.atrb['fontSizeToCorrectorAncho'][w['fontType']][w['fontSize']]) )
    def altoWidget(self,w):
        return self.atrb['fontSizeToAlto'][w['fontType']][w['fontSize']]
    def comandoGuardar(self):
            if self.widgets[self.atrb['frameActivo']]['crearTabla']:
                print(self.atrb['frameActivo'],self.tablas[self.atrb['frameActivo']][1:],[self.widgets[self.atrb['frameActivo']]['value'][v.split(' ')[0]] for v in self.tablas[self.atrb['frameActivo']][1:]] )
                self.Sql.Cargar(self.atrb['frameActivo'],self.tablas[self.atrb['frameActivo']][1:],[self.widgets[self.atrb['frameActivo']]['value'][v.split(' ')[0]] for v in self.tablas[self.atrb['frameActivo']][1:]] ,dirCRUD=self.pwd+os.path.sep+self.atrb['transicion']+os.path.sep+self.atrb['transicion']+self.Sql.extencionCRUD)
                self.setVar(self.atrb['frameActivo'])
    def comandoLeer(self,campoClave='id'):
                if self.widgets[self.atrb['frameActivo']]['crearTabla']:
                    if [1 for ok in self.atrb['subtransicion']['aceptar'] if (ok in self.widgets[self.atrb['frameActivo']]['etiquetas'])]:
                        print(self.Sql.SelectAll(self.atrb['frameActivo'],typeSalida='dict',campoClave=campoClave,dirCRUD=self.pwd+os.path.sep+self.atrb['transicion']+os.path.sep+self.atrb['transicion']+self.Sql.extencionCRUD))
                        #self.setVar(w)
    def comandoExportar(self,campoClave='id',file='',formato='',tabla=[]):
        if self.widgets[self.atrb['frameActivo']]['crearTabla']:
            self.Sql.exportarTablas(
                tabla=[self.atrb['frameActivo']],
                formato=formato,
                campoClave=campoClave,
                file=self.pwd+os.path.sep+self.atrb['transicion']+os.path.sep+self.atrb['titulo'],
                dirCRUD=self.pwd+os.path.sep+self.atrb['transicion']+os.path.sep+self.atrb['transicion']+self.Sql.extencionCRUD
                )
            #self.setVar(w)
    def SetWidget(self,atributos={}):
        myCommand={
            "Aceptar":[myFuncion,(atributos['inputType'], atributos['name'], "Aceptar")],
            "Aplicar":[myFuncion,(atributos['inputType'], atributos['name'], "Aplicar")],
            "Modificar":[myFuncion,(atributos['inputType'], atributos['name'], "Modificar")],
            "Guardar":[myFuncion,(atributos['inputType'], atributos['name'], "Guardar")],
            "Siguiente":[myFuncion,(atributos['inputType'], atributos['name'], "Siguiente")],
            "Anterior":[myFuncion,(atributos['inputType'], atributos['name'], "Anterior")],
            "Ignorar":[myFuncion,(atributos['inputType'], atributos['name'], "Ignorar")],
            "Cancelar":[myFuncion,(atributos['inputType'], atributos['name'], "Cancelar")],
            "Salir":[myFuncion,(atributos['inputType'], atributos['name'], "Salir")],
            "Validar":[myFuncion,(atributos['inputType'], atributos['name'], "Validar")]
        }
        #Combinamos el conjunto de datos que resive esta funcion en el parametro 'atributos', con el conjunto de datos que ya tenemos Predefenidos en 'myVars.py'
        myWidget= self.INPUTS_CONFIG[atributos['inputType']]
        if myWidget != 'None':
            #print('linea 1273',atributos['inputType'],myWidget)
            for clave in [clave for clave in atributos]:
                if clave in [key for key in myWidget]:
                    myWidget[clave]=atributos[clave]
                else:
                    myWidget.setdefault(clave,atributos[clave])
            
            if 'padre' in myWidget:
                if not myWidget['padre']:
                    myWidget['padre']='myFrame'
            else:
                myWidget['padre']='myFrame'
        else:
           myWidget={'inputType':'' }

        """
            esta parte del codigo genera el 'Frame Tkinter' los inputs y outputs dentro de este
            A cada 'Frame  Tkinter' se le asignara un widget padre que le heredara el comportamiento deseado,
            los widget padre solo son 'tk' y 'myFrame', estos widget son declarados en la funcion __init__ de esta clase,
            COMPORTAMIENTOS:
            'tk' es el objeto Tk() de tkinter, y sus hijos se comportaran de forma ESTATICA dentro del programa, los hijos de 'tk' no se mueven o desplazan dentro de la ventana del Programa, o sea no seran controlados por las 'barras de desplazamiento'(Scrollbar)
            'myFrame' es el Frame() de tkinter, pero esta 'posicionado' dentro de un 'Canvas()' que este a su ves es controlado por las 'barras de desplazamiento'(Scrollbar), y los hijos de 'myFrame' tambien seran controlados por las 'barras de desplazamiento'(Scrollbar)
            POSICIONAMIENTO:
            'tk' sera el padre del 'Frame Tkinter' si le pasamos inputType='panel', y los hijos de 'Frame Tkinter' seran posicionados con .place(x=posicion real en pantalla,y=posicion real en pantalla)
            'myframe' sera el padre del 'Frame Tkinter' si le pasamos inputType='Frame', como 'myFrame' puede tener una dimencion deferente de 'tk', este debe posicionar los widgets dentro del 'Frame Tkinter' calculando su posicion dentro 'myFrame'
        """
        if myWidget['inputType'] in ['Frame','panel']:
            if myWidget['inputType']=='Frame':
                myWidget['widget']=Frame(
                    self.widgets['myFrame']['widget'], 
                    width=myWidget['ancho'], 
                    height=myWidget['alto'],
                    bd=0,
                    highlightthickness=0
                    )
                myWidget['padre']='myFrame'

            if myWidget['inputType']=='panel':
                myWidget['widget']=Frame(
                    self.widgets['tk']['widget'], 
                    width=myWidget['ancho'], 
                    height=myWidget['alto'],
                    bg=myWidget['bgColor']
                    )
                myWidget['padre']='tk'
            
            myWidget['canvas']=Canvas(myWidget['widget'],bd=0,highlightthickness=0)
            myWidget['value']={}
            self.widgets.setdefault(myWidget['name'],myWidget)
            if 'inputs'in myWidget:
                inputs={}
                x,y=0,0
                saltoX,saltoY=0,0
                if 'text' in myWidget:
                    inputs[myWidget['name']+'_Label']={
                        'inputType':'Label',
                        'padre':myWidget['name'],
                        'name':myWidget['name']+'_Label',
                        'xPlace':x,
                        'yPlace':y,
                        'ancho':self.anchoWidget(myWidget),
                        'alto':self.altoWidget(myWidget)*0.3+2,
                        'fontSize':int(myWidget['fontSize']),
                        'fontType':myWidget['fontType'],
                        'fontColor':myWidget['fontColor'],
                        'bgColor':myWidget['bgColor'],
                        'text':myWidget['text']}
                    self.SetWidget(atributos=inputs[myWidget['name']+'_Label'])
                for btn in myWidget['inputs']:
                    if saltoX>0:
                        x += saltoX
                        saltoX=0    
                    else:
                        x += self.anchoWidget(myWidget) if (('n'==myWidget['anchor'][0]) or ('s'==myWidget['anchor'][0])) else 0
                    if saltoY>0:
                        y += saltoY
                        saltoY=0    
                    else:
                        y += self.altoWidget(myWidget)+self.atrb['espacioVerticalEntreWidgets']
                    myWidget['inputs'][btn].setdefault('name',myWidget['name']+'_'+btn)
                    myWidget['inputs'][btn].setdefault('padre',myWidget['name'])
                    myWidget['inputs'][btn].setdefault('width',myWidget['width'])
                    myWidget['inputs'][btn].setdefault('fontSize',myWidget['fontSize'])
                    myWidget['inputs'][btn].setdefault('fontType',myWidget['fontType'])
                    myWidget['inputs'][btn].setdefault('fontColor',(escalarHex(h=myWidget['fontColor'],factor=1.0/0.9) if myWidget['inputs'][btn]['inputType']=='Entry' else myWidget['fontColor']))
                    myWidget['inputs'][btn].setdefault('bgColor',(escalarHex(h=myWidget['bgColor'],factor=0.9) if myWidget['inputs'][btn]['inputType']=='Entry' else myWidget['bgColor']))
                    myWidget['inputs'][btn].setdefault('fgColor',myWidget['fgColor'])
                    myWidget['inputs'][btn].setdefault('xPlace',x)
                    if myWidget['inputs'][btn]['inputType'] in ['Entry']:
                        myWidget['inputs'][btn].setdefault('yPlace',y+(self.altoWidget(myWidget['inputs'][btn]) if 'text' in myWidget['inputs'][btn] else 0))
                    else:
                        myWidget['inputs'][btn].setdefault('yPlace',y)

                    if myWidget['inputs'][btn]['inputType'] in ['Radiobutton']:
                        myWidget['inputs'][btn]['alto']=self.altoWidget(myWidget['inputs'][btn])*(len(myWidget['inputs'][btn]['radios'])+1)
                        saltoY=myWidget['inputs'][btn]['alto']
                    if myWidget['inputs'][btn]['inputType'] in ['Entry']:
                        myWidget['inputs'][btn]['alto']=self.altoWidget(myWidget['inputs'][btn])*2
                        saltoY=myWidget['inputs'][btn]['alto']
                    
                    self.SetWidget(atributos=myWidget['inputs'][btn])
                    if myWidget['inputs'][btn]['inputType']=='Entry' and ('text' in myWidget['inputs'][btn]) :
                        inputs[myWidget['name']+'_'+btn+'_LabelCanvas']={
                            'inputType':'LabelCanvas',
                            'padre':myWidget['name'],
                            'name':myWidget['name']+'_'+btn+'_LabelCanvas',
                            'xPlace':x,
                            'yPlace':y,
                            'ancho':self.anchoWidget(myWidget),
                            'alto':self.altoWidget(myWidget)*0.3+10,
                            'fontSize':int(myWidget['fontSize']*0.7),
                            'fontType':myWidget['fontType'],
                            'fontColor':myWidget['fontColor'],
                            'bgColor':myWidget['bgColor'],
                            'text':myWidget['inputs'][btn]['text']}
                        #self.SetWidget(atributos=inputs[myWidget['name']+'_'+btn+'_LabelCanvas'])
            self.widgets[myWidget['name']]['inputs']=myWidget['inputs']
            for i in inputs:
                self.widgets[myWidget['name']]['inputs'][i]=inputs[i]
            
        elif myWidget['inputType']=='formIn':
            self.widgets.setdefault(myWidget['name'],myWidget)

        elif myWidget['inputType']=='formOut':
            self.widgets.setdefault(myWidget['name'],myWidget)

        elif myWidget['inputType']=='Button':
            myWidget['widget']=Button(
                self.widgets[myWidget['padre']]['widget'],
                text=myWidget['text'],
                width=myWidget['width'] if myWidget['width'] else None,
                bg=myWidget['bgColor'],
                fg=myWidget['fontColor'],
                font=(myWidget['fontType'],myWidget['fontSize']),
                command=self.command[myWidget['command']]
                )
            myWidget['ancho']=self.anchoWidget(myWidget)
            myWidget['alto']=self.altoWidget(myWidget)
            self.widgets.setdefault(myWidget['name'],myWidget)
        elif myWidget['inputType']=='Label':
            myWidget['widget']=Label(
                self.widgets[myWidget['padre']]['widget'], 
                text=myWidget['text'],
                bg=myWidget['bgColor'],
                fg=myWidget['fontColor'],
                font=(myWidget['fontType'],myWidget['fontSize']))
            myWidget['ancho']=self.anchoWidget(myWidget)
            myWidget['alto']=self.altoWidget(myWidget)
            self.widgets.setdefault(myWidget['name'],myWidget)

        elif myWidget['inputType']=='LabelCanvas':
            self.widgets[myWidget['padre']]['canvas'].create_text(myWidget['xPlace']+(myWidget['ancho']/2),myWidget['yPlace']+(myWidget['alto']/2),fill=myWidget['fontColor'],font=(myWidget['fontType'],myWidget['fontSize']), text=myWidget['text'])
            

        elif myWidget['inputType']=='Entry':
            if not 'value' in myWidget:
                myWidget['value']=''
            if myWidget['typeSalida'] in ['str','correo','date','nombre']:
                self.Vars[myWidget['name']]=StringVar(value=str(myWidget['value']),name=myWidget['name'])
            elif myWidget['typeSalida'] in ['int','edad']:
                self.Vars[myWidget['name']]=IntVar(value=int(float(myWidget['value'])),name=myWidget['name'])
            elif myWidget['typeSalida'] in ['float','moneda','magnitud']:
                self.Vars[myWidget['name']]=DoubleVar(value=float(myWidget['value']),name=myWidget['name'])
            elif myWidget['typeSalida'] in ['Boolean','bool']:
                self.Vars[myWidget['name']]=BooleanVar(value=bool(myWidget['value']),name=myWidget['name'])
            else:
                self.Vars[myWidget['name']]=StringVar(value=str(myWidget['value']),name=myWidget['name'])

            myWidget['widget']=Entry(
                self.widgets[myWidget['padre']]['widget'], 
                textvariable=self.Vars[myWidget['name']],
                width=myWidget['width'] if myWidget['width'] else None,  
                fg=myWidget['fontColor'],
                insertbackground=myWidget['fontColor'],
                bg=myWidget['bgColor'],
                font=(myWidget['fontType'],myWidget['fontSize'])
                )
            self.Vars[myWidget['name']].trace('w',lambda name,arg2,mod : self.updateVar(name,arg2,mod))
            self.widgets.setdefault(myWidget['name'],myWidget)
            self.updateVar(myWidget['name'],' ','w')
            
        elif myWidget['inputType']=='Checkbutton':
            if not 'value' in myWidget:
                myWidget['value']=''
            self.Vars[myWidget['name']]=BooleanVar(value=bool(myWidget['value']),name=myWidget['name'])
            
            myWidget['widget']=Checkbutton(
                self.widgets[myWidget['padre']]['widget'], 
                text=myWidget['text'],
                bg=myWidget['bgColor'],
                fg=myWidget['fontColor'], 
                variable=self.Vars[myWidget['name']],
                font=(myWidget['fontType'],myWidget['fontSize'])
                )

            self.Vars[myWidget['name']].trace('w',lambda name,arg2,mod : self.updateVar(name,arg2,mod))

            myWidget['ancho']=self.anchoWidget(myWidget)
            myWidget['alto']=self.altoWidget(myWidget)
            self.widgets.setdefault(myWidget['name'],myWidget)
            self.updateVar(myWidget['name'],' ','w')

        elif myWidget['inputType']=='Radiobutton':
            p=myWidget['name']+'_'+[k for k in myWidget['radios']][0]
            #print([k for k in myWidget['radios']][0],p)
            self.Vars[p]=StringVar(value=str(myWidget['value']),name=p)
            x , y = 0 , 0
            if 'text' in myWidget:
                self.SetWidget(atributos={
                    'inputType':'Label',
                    'padre':myWidget['padre'],
                    'name':myWidget['name']+'_Label',
                    'xPlace':myWidget['xPlace']+x,
                    'yPlace':myWidget['yPlace']+y,
                    'ancho':self.anchoWidget(myWidget),
                    'alto':self.altoWidget(myWidget),
                    'fontSize':myWidget['fontSize'],
                    'fontType':myWidget['fontType'],
                    'fontColor':myWidget['fontColor'],
                    'bgColor':myWidget['bgColor'],
                    'text':myWidget['text']})
            x=self.atrb['fontSizeToAlto'][myWidget['fontType']][myWidget['fontSize']]
            if 'radios' in myWidget:
                for r in myWidget['radios']:
                    y += (self.atrb['fontSizeToAlto'][myWidget['fontType']][myWidget['fontSize']])
                    myWidget['radios'][r]['inputType']=myWidget['inputType']
                    myWidget['radios'][r]['padre']=myWidget['padre']
                    myWidget['radios'][r]['name']=myWidget['name']+'_'+str(r)
                    myWidget['radios'][r]['xPlace']=myWidget['xPlace']+x
                    myWidget['radios'][r]['yPlace']=myWidget['yPlace']+y
                    myWidget['radios'][r]['bgColor']=myWidget['bgColor']
                    myWidget['radios'][r]['fontColor']=myWidget['fontColor']
                    myWidget['radios'][r]['fontType']=myWidget['fontType']
                    myWidget['radios'][r]['fontSize']=myWidget['fontSize']
                    myWidget['radios'][r]['ancho']=self.anchoWidget(myWidget)
                    myWidget['radios'][r]['alto']=self.altoWidget(myWidget)
                    myWidget['radios'][r]['widget']=Radiobutton(
                        self.widgets[myWidget['padre']]['widget'], 
                        text=myWidget['radios'][r]['text'],
                        bg=myWidget['radios'][r]['bgColor'],
                        fg=myWidget['radios'][r]['fontColor'], 
                        variable=self.Vars[p],
                        value=r,
                        font=(myWidget['radios'][r]['fontType'],myWidget['radios'][r]['fontSize']))
                    if 'command' in myWidget['radios'][r]:
                        myWidget['radios'][r]['widget'].config(command=self.command[myWidget['radios'][r]['command']])
                    self.widgets.setdefault(myWidget['radios'][r]['name'],myWidget['radios'][r])
            self.Vars[p].trace('w',lambda name,arg2,mod : self.updateVar(name,arg2,mod))

            #myWidget['ancho']=((11-myWidget['fontSize'])+(myWidget['width']+1)*(myWidget['fontSize']-1)+(myWidget['width']*self.atrb['fontSizeToCorrectorAncho'][myWidget['fontType']][myWidget['fontSize']]))
            #myWidget['alto']=(self.atrb['fontSizeToAlto'][myWidget['fontType']][myWidget['fontSize']])
            #self.widgets.setdefault(myWidget['name'],myWidget)
            self.updateVar(p,' ','w')
        self.INPUTS_CONFIG=self.recuperarVariable("inputType")
        #print(myWidget['name'],self.widgets[myWidget['name']]['name'])
        if 'crearTabla' in myWidget:
            if (myWidget['crearTabla']) and (not myWidget['name'] in self.tablas):
                campos = [i for i in myWidget['inputs'] if (myWidget['inputs'][i]['inputType'] in self.widgetConectadoaVars) ]
                self.tablas[myWidget['name']]=[self.Sql.campoAutoincrement]+[campos[0]+' text not null UNIQUE']+campos[1:]
                print(myWidget['name'],self.tablas[myWidget['name']])
                self.Sql.CrearTabla(myWidget['name'],self.tablas[myWidget['name']],dirCRUD=self.pwd+os.path.sep+myWidget['subProyecto']+os.path.sep+myWidget['subProyecto']+self.Sql.extencionCRUD)

        del myWidget
class geometria(object):
    """docstring for geometria"""
    def __init__(self):
        super(geometria, self).__init__()
    def corrector(f):
        def corregido(*arg,**kwargs):
            ret = []
            for a in [*arg]:
                if ("list" in type(a)) and (len(a)<3):
                    ret += [[float(c) for c in a]+[0.0 for c in range(3-len(a))]]
                else:
                    ret += [a]
            ret=tuple(ret)
            f_return= f(*ret,**kwargs)
            return f_return
        return corregido
    @corrector
    def colineales(self,A,B,C,decimales=4):
        AB=self.resta(B,A)
        AC=self.resta(C,A)
        if int((AB[0]/AB[1])*(10**decimales))==int((AC[0]/AC[1])*(10**decimales)):
            return True
        else:
            return False
    @corrector
    def modulo(self,A):
        return (((A[0])**2)+((A[1])**2)+((A[2])**2))**(1/2)
    @corrector
    def vectorUnitario(self,A):
        m=self.modulo(A)
        return [A[0]/m,A[1]/m,A[2]/m]
    def hypotenusa(self,catOp,catAd):
        return (((catAd)**(2))+((catOp)**(2)))**(1/2)
    @corrector
    def dist(self,A,B):
        #calcula la dsitancia entre A y B
        return (((A[0]-B[0])**2)+((A[1]-B[1])**2)+((A[2]-B[2])**2))**(1/2)
    @corrector
    def coseno(self,A,B):
        #retorna el valor del coseno del angulo formado entre los vectores A y B
        divisor=(((((A[0])**2)+((A[1])**2)+((A[2])**2))**(1/2))*((((B[0])**2)+((B[1])**2)+((B[2])**2))**(1/2)))
        if divisor!=0.0:
            return ((A[0]*B[0]+A[1]*B[1]+A[2]*B[2])/divisor)
        else:
            return 3.1416/2
    @corrector
    def angRad(self,A,B):
        return math.acos(self.coseno(A,B))
    @corrector
    def ang(self,A,B):
        return math.degrees(math.acos(self.coseno(A,B)))
    @corrector
    def resta(self,A,B):
        #retorna el vector AB o A-B considerando el punto A como el nuevo origen
        return [B[0]-A[0],B[1]-A[1],B[2]-A[2]]
    @corrector
    def suma(self,A,B):
        #retorna el vector A+B.
        return [B[0]+A[0],B[1]+A[1],B[2]+A[2]]
    @corrector
    def medio(self,A,B):
        #retorna el vector A+B.
        return [(B[0]+A[0])/2,(B[1]+A[1])/2,(B[2]+A[2])/2]
    @corrector
    def alt(self,A,B,C):
        #retorna el punto de origen del segmento que define la altura del triangulo A,B,C. Considerando al lado BC como la base del triangulo.
        ab=self.dist(A,B)
        bc=self.dist(B,C)
        BA=self.resta(B,A)
        BC=self.resta(B,C)
        cosB=self.coseno(BA,BC)
        x=((BC[0]/bc)*(cosB*ab))+B[0]
        y=((BC[1]/bc)*(cosB*ab))+B[1]
        z=((BC[2]/bc)*(cosB*ab))+B[2]
        return  [x,y,z]
    @corrector
    def rotar(self,rad,P):
        #sobre el origen, rotar el angulo dado en sentido antiorario el punto P 
        x=P[0]*math.cos(rad)-P[1]*math.sin(rad)
        y=P[0]*math.sin(rad)+P[1]*math.cos(rad)
        return x,y
    @corrector
    def trasladar(self,O,P):
        #trasladar el punto P, al nuevo origen O
        x=P[0]+O[0]
        y=P[1]+O[1]
        z=P[2]+O[2]
        return x, y ,z
