#!/usr/bin/env python
# -*- coding: utf-8 -*-
# archivo generado por Diseño Libre para servidor

#Modulos importados
import socket, glob, json  
import threading
import os,datetime,time
def f1(*a,**k):
    return datetime.datetime.now()
f1()

def f2(*a,**k):
    return str(datetime.datetime.now())
f2()

def f3(*a,**k):
    return datetime.datetime.now()
f3()


funciones={
    'f1':f1,
    'f2':f2,
    'f3':f3
}
pwd=os.getcwd()+'\\media\\servidor'
subProyectos={
    'a':{'pwd':pwd+'\\'+'a','name':'a'},
    'b':{'pwd':pwd+'\\'+'b','name':'b'},
    'c':{'pwd':pwd+'\\'+'c','name':'c'},
    'd':{'pwd':pwd+'\\'+'d','name':'d'}
    }
#api=servidor(pwd, funciones,subProyectos,puerto=666)
#api.servidor_HTTP_python()

def command(admin,G,info,ec,geo):
    print(info['subProyecto'])
    print('Info:',info['info'])
    print('Widgest:',info['widget'])
    print('Comandos',info['command']) 
    G.command[info['command']['manager']]=lambda : admin.transicion(G,admin.manager)


print(__name__)
if 'main' in __name__:
    import sys
    pruebas={           
        0:{'titulo':":",'f':print("")},
        1:{'titulo':"servidor_CHAT_socket_python",'f':servidor_CHAT_socket_python},
        2:{'titulo':"cliente_CHAT_socket_python",'f':cliente_CHAT_socket_python},
        3:{'titulo':"salir",'f':lambda : p(('hello',21,True))},
        4:{'titulo':"salir",'f':lambda : p(('hello',21,True),console=0)},
        5:{'titulo':"salir",'f':exit}
        }
    def f(num):
        print('######################################################################')
        print("PRUEBA Inicianda: "+pruebas[num]['titulo'])
        print('######################################################################'+'\n')

        #llamamos a la funcion
        pruebas[num]['f']()

        #esperamos que termine
        
        #Aviso de que la funcion termino.
        print('\n'+"PRUEBA Terminada...")
        print('\n')
    if len(sys.argv)>1:
        f(int(sys.argv[1]))
        exit()        
    num=1
    while num > 0:
        num=0
        for prueba in pruebas:
            print(str(prueba)+'. '+pruebas[prueba]['titulo'])
        inpu=input('Ingrese el numero de la siguiente prueba: ').split(' ')
        num=int(inpu[0] if inpu[0] != '' else 0)
        if num > 0:
            f(num)
        else:
            exit()
