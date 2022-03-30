#!/usr/bin/env python
# -*- coding: latin-1 -*-
import os
d={
    'img':os.getcwd()+os.path.sep+"media"+os.path.sep,
    'audio':os.getcwd()+os.path.sep+"media"+os.path.sep
    }
def funciones():
    import time
    """
        practica con decoradores
        la funcion 'decorador' se ejecutara automaticamente cada ves que ejecutemos las funciones decoradas con esta funcion
        la funcion 'decorador' recive como parametro la funcion 'funcion_parametro' que fue decorada, junto con sus argumentos de posicion *vars y los argumentos con palabras claves **vars_claves
        la funcion 'decorador' retornara otra funcion 'funcionInterior', esta funcion interna ejecuta su propio codigo, y dentro de esta funcion intarna ejecutamos la funcion_parametro 
    """
    def decorador(funcion_parametro):
        def funcionInterior(*args,**kwargs):
            print("Funcion:",funcion_parametro.__name__)
            print("Entradas:",*args,**kwargs)
            ret=funcion_parametro(*args,**kwargs)
            print("Salidas:",ret,'\n')
            return ret
        return funcionInterior
    """ 
        la funcion 'decoradorPlus' recive la funcion decoradoa con sos respectivos 
        argumentos, aparte tambien recive un parametro asignada a la clave arg como 
        cualquier funcion normal. De acuerdo al valor de 'arg' decorara la funcion decorada con una funcion interna de 'decoradorPlus'     
    """
    def decoradorPlus(arg=""):
        def decoradortiempo(funcion):
            def funcionInterior(*args,**kwargs):
                inicio=time.time()
                print("Funcion:",funcion.__name__)
                ret=funcion(*args,**kwargs)
                print("Tiempo de Ejecucion:",time.time()-inicio)
                return ret
            return funcionInterior
        def decoradorSimple(funcion):
            def funcionInterior(*args,**kwargs):
                print("Funcion:",funcion.__name__)
                print("Entradas:",*args,**kwargs)
                ret=funcion(*args,**kwargs)
                print("Salidas:",ret)
                return ret
            return funcionInterior

        if arg=="tiempo":
            return decoradortiempo
        else:
            return decoradorSimple
    """
        la funcion 'testFuncion' recive como argumento posicional, una 
        funcion, el valor que debe retornar dicha funcion, seguido de 
        los argumentos que recive dicha funcion
    """
    def testFuncion(funcion,retorna,*test_args):
        test=True
        if retorna!=funcion(*test_args):
            test=False
        return test
    """
        decoramos la funcion 'resta', con la funcion 'decoradorPlus' sin pasarle la clave opcional 'arg'
    """
    @decoradorPlus()
    def resta(a,b):
        return (a-b)

    """
        decoramos la funcion 'suma', con la funcion 'decoradorPlus' y le pasamos la clave opcional 'arg' igual a "tiempo"
    """
    @decoradorPlus(arg='tiempo')
    def suma(a,b):
        return (a+b)

    print(testFuncion(resta,40,50,10))
    print(testFuncion(suma,40,50,10))

def ahorcado(pwd=d['img']+"palabras.txt"):
    import random
    vidas='******'
    letrasCantadas=''
    file=open(pwd,'r')
    secretos=[line[:-1] for line in file]
    file.close()
    secreto=secretos[random.randrange(0,len(secretos))].upper()
    letra_inicio=random.randrange(0,len(secreto))
    palabra='_ '*len(secreto)
    letra=secreto[letra_inicio]
    while True:
        if (letra in secreto) and (letra not in letrasCantadas):
            letrasCantadas+=letra
            for x in range(len(secreto)):
                if  secreto[x]==letra:
                    palabra=palabra[:2*x]+letra[0]+palabra[2*x+1:]
        elif letra in letrasCantadas:
            print("La letra '"+letra+"', ya fue Cantada...")
            vidas=vidas[:-1]
        else:
            letrasCantadas+=letra
            vidas=vidas[:-1]
        print('\n\nPalabra Secreta:    '+palabra)
        print('Vidas:  '+vidas+', te quedan '+str(len(vidas))+' vidas.')
        print('Letras Cantadas:  '+letrasCantadas)
        if vidas:
            if [l for l in secreto if l not in letrasCantadas]:
                letra=input('Siguiente Letra: <<< ')[0].upper()
            else:
                if input("Muchas Felicidades Lograste Descubrir la palabra secreta "+secreto.upper()+". \n¿Si queres volver a jugar ingresa cualquier letra, sino es asi presiona enter? :<<<"):
                    secreto=secretos[random.randrange(0,len(secretos))]
                    letra_inicio=random.randrange(0,len(secreto))
                    palabra='_ '*len(secreto)
                    letra=secreto[letra_inicio]
                    letrasCantadas=''
                    vidas='******'
                else:
                    break
        else:
            print("Te quedaste sin vidas JAJAJA. \nLa palabra Secreta es: "+secreto)
            break

def manipularArchivos(pwd=d['img'],f='',ret=0):
    bi=b''
    if not f:
        file=f
    else:
        file='subiendo'
    binario=open(file,'rb')
    for b in binario:
        bi+=b
    binario.close()
    print(bi[:1024])
    print(bi[-1024:])
def capturarNumerosMagicos(pwd=d['img'],f='',ret=0):
    bi={}
    miDir=os.listdir(pwd)
    muestra=100
    contador=0
    for file in miDir:
        bi[contador]={'name':file,'inicio':b''}
        binario=open(pwd+'\\'+file,'rb')
        for inicio in binario:
            bi[contador]['inicio']+=inicio
        binario.close()
        bi[contador]['fin']=bi[contador]['inicio'][-muestra:]
        bi[contador]['inicio']=bi[contador]['inicio'][:muestra]
        print('name',bi[contador]['name'])
        print('inicio',bi[contador]['inicio'])
        print('fin',bi[contador]['fin'])
        contador+=1


def git_admin():

    """
    //Segmento de windows CMD
    SET /p sigue=Hacer "git add -A" s/n?:
    if "%sigue%"=="n" (goto :fin)
    if "%sigue%"=="N" (goto :fin)
    echo Ejecutando: git add -A
    git add -A

    #segmento de Linux Bash

    """
def main_pruebas(pruebas,argv):
    import datetime
    salir=lambda: exit()
    print(__name__,datetime.datetime.now())
    pruebas[len(pruebas)]={'titulo':"salir, opcion por defecto",'f':salir}
    def f(num):
        print("PRUEBA Iniciada: "+pruebas[num]['titulo'])
        #llamamos a la funcion Decorada y esperamos que termine
        pruebas[num]['f']()
        #Aviso de que la funcion termino.
        input('\n'+"PRUEBA Terminada...")
    if len(argv)>1:
        f(int(argv[1]))
        exit()        
    num=1
    while num > 0:
        num=0
        print('######################################################################')
        for prueba in pruebas:
            print(prueba,'.',pruebas[prueba]['titulo'],'>>> def '+pruebas[prueba]['f'].__name__+'():')
        i=input('Ingrese el numero de la siguiente prueba: ').strip()
        num=0 if i=='' else int(float(i))
        f(num)
        print('######################################################################'+'\n\n')



if 'main' in __name__:
    import sys
    #from ..setup import main_pruebas
    pruebas={           
        0:{'titulo':"Nombre del script:",'f':lambda: print(__name__)}
        }
    main_pruebas(pruebas,sys.argv)
            