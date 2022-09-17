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

"""
    #############  FUNCIONES UTILES #############
    PARA DIFERENTES TIPOS DE PROYECTOS, FUNCIONES PARA PRUEBAS, MANEJO DE DATOS, VALIDACIONES, ETC,ETC
"""


def getFile(f,full=1):
    file=open(f)
    ret=[]
    for line in file:
        #print(line.strip())
        if str(line.strip())!='':
            ret += [str(line if full else line.strip())]
    file.close()
    return ret if len(ret)>1 else ret[0]
def setFile(f,valor,echo=1):
    if echo:
        print('Archivo:',f)
    file=open(f,"wb")
    if list == valor__class__:
        for line in valor:
            if echo:
                #line.encode()
                print(line.encode('latin-1'))
            file.write(line.encode('latin-1')+b'\n')    
    else:
        file.write(valor)
    file.close()
def okString(string,para='Clave'):
    myStr=string.strip()
    notKey=['`','ñ','_',"'",'à','è','ì','ò','ù','.','']
    yesKey=["'",'nh','',"'",'a','e','i','o','u','' ,'']
    notUtf8=['`','ñ','_',"'",'','','','','','','','','','','','','','','']
    if para=="Clave":
        for char in notKey:
            myStr=myStr.replace(char,'')

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
    escala = {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'a':10,'b':11,'c':12,'d':13,'e':14,'f':15}
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
    ############# CLASES PRINCIPALES DEL MODULO MBARETE  ########################
        def __get__(self, instance, cls):
        # Retorna un método si se llama en una instancia
        print(self,instance,cls)
        return self if instance is None else MethodType(self, instance)

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
            self.dirCRUD=self.ubi.pwd+self.ubi.s+ficheroCRUD
            self.ficheroCRUD=ficheroCRUD
        else:
            self.dirCRUD=self.ubi.pwd+self.ubi.s+nombre.replace(' ','_')+"_CRUD_.sql"
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
        load=open(self.ubi.pwd+self.ubi.s+'preload.py','w')
        load.write(r'proyectos={}'+'\n')
        for subP in subProyectos:
            if self.cargarScript in self.ubi.listaDeFicheros(self.ubi.pwd+self.ubi.s+subP,ignorar=self.archivosInternos): 
                load.write('from .'+subP+' import '+self.cargarScript[:-3]+' as '+subP+'\n')
            elif subP+'.py' in self.ubi.listaDeFicheros(self.ubi.pwd+self.ubi.s+subP,ignorar=self.archivosInternos): 
                load.write('from .'+subP+' import '+subP+' as '+subP+'\n')
            load.write("proyectos['"+subP+"']="+subP+'\n')
        load.write("def command(admin,G,manager):"+'\n')
        for subP in subProyectos:
            load.write("    G.command[manager+'_transicion_"+subP+"']=lambda : admin.transicion(G,'"+subP+"')"+'\n')
        load.close()
        #from diseñoLibre.preload import proyectos
    def getWidget(self,subProyecto,widgets,info):
        w=widgets
        info['pwd']=self.ubi.pwd+self.ubi.s+subProyecto
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
class deco(object):
    def __init__(self, flag='ignore',msj=''):
        self.flag = flag
        self.msj = msj
    def __call__(self, original_func):
        decorator_self = self
        if decorator_self.flag=='geo':
            def wrappee(*args, **kwargs):
                ret = []
                for a in [*args]:
                    if (list == a.__class__) and (len(a)<3):
                        ret += [[float(c) for c in a]+[0.0 for c in range(3-len(a))]]
                    else:
                        ret += [a]
                ret=tuple(ret)
                f_return= original_func(*ret,**kwargs)
                return f_return
            return wrappee
            
        elif decorator_self.flag=='tiempo':
            def wrappee(*args, **kwargs):
                T0=time.time()
                f_return= original_func(*args,**kwargs)
                print(decorator_self.msj,time.time()-T0)
                return f_return
            return wrappee
            
        else:
            def wrappee(*args, **kwargs):
                print('#'*30+'\n'+'#'*30)
                print('En decorador:', decorator_self.flag)
                print("Funcion Ignorada:",original_func.__name__)
                print('#'*30+'\n'+'#'*30)
            return args,kwargs
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

