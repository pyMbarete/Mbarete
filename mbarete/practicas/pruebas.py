#!/usr/bin/env python
# -*- coding: latin-1 -*-
import os,sys
d={
    'img':os.getcwd()+os.path.sep+"media"+os.path.sep,
    'audio':os.getcwd()+os.path.sep+"media"+os.path.sep
    }

class object_prueba(object):
    """esta clase sera heredada a todas las clases de las demas practicas"""
    def __init__(self,logFile=__file__+'.log',flags=['log','error','init'],open_modo='wb'):
        super(object_prueba, self).__init__()
        self.init_pwd=os.getcwd()
        self.log=True
        self.prnt=True
        self.code='utf-8'
        self.logFile=logFile
        self.flags=['']+flags
        self.open_modo=open_modo
        self.info=self.info_system()
    def go_main_pwd(self,pwd='',mkdir='auto.'+__file__,scan=[]):

        if os.path.lexists(pwd):
            if mkdir:
                if not mkdir in os.listdir(pwd): os.mkdir(pwd+mkdir)
            os.chdir(pwd+mkdir)

    def go_back_pwd(self,pwd=''):
        main_pwd='auto.'+__file__
        if not main_pwd in os.listdir(pwd): os.mkdir(pwd+main_pwd)
        os.chdir(pwd+main_pwd)

    def return_system(self,command,join=None,sep=':',prefijo=''):
        os.system(command+" > "+self.info['tmp']+'mbarete_tmp')
        ret = self.getFile(self.info['tmp']+'mbarete_tmp',join=join,sep=sep,prefijo=prefijo)
        os.remove(self.info['tmp']+'mbarete_tmp')
        return ret
    def info_system(self):
        if os.name == 'nt':
            import platform
            info={'OS':'windows','V':os.environ['OS'],'tmp':os.environ['TEMP']+os.sep,'home':os.environ['USERPROFILE']+os.sep}
            info['uname_sysname'] ,info['uname_nodename'] ,info['uname_release'] ,info['uname_version'] ,info['uname_machine'] ,info['uname_processor'] = platform.uname()
        elif os.name == 'posix':
            info=self.getFile('/etc/os-release',join={'OS':'linux','tmp':'/tmp/'},sep='=',prefijo='os_release_')
            info['uname_sysname'] ,info['uname_nodename'] ,info['uname_release'] ,info['uname_version'] ,info['uname_machine'] = os.uname()
            info['V']=info['os_release_ID']
        elif 'ANDROID_ROOT' in os.environ:
            info={'OS':'android','V':os.environ['SHELL'],'tmp':'/tmp/'}
        info['sys_prefix']=sys.prefix
        info['sys_platform']=sys.platform
        info['sys_version_info']=sys.version_info
        info['sys_version']=sys.version.replace('\n',' ')
        return info

    def p(self,*args,end='\n',sep=' ',flush=True,flag=''):
        """
        end='\n'
            Con el parámetro end podemos modificar esto por el valor que queramos.
            print( “Hola”, end = “ @ ”)
            print(“Mundo”)
            El resultado es:
            “Hola @ Mundo”
            No se fue a la siguiente línea.
        sep=' '
            Con el parámetro sep, podemos escribir algo entre esos valores.
            print( “Tengo una”, “ ¿Quieres una ”,  “?”, sep = “Manzana”)
            El resultado sería:
            “Tengo 1 Manzana ¿Quieres una Manzana?”
            Nota: Funciona con variables int y float sin necesidad de convertirlas a String.
        flush=True
            Se recomienda usarlo cuando usamos el comando end. Ya que al usarlo el buffer ya 
            no se vacía (flush), por lo tanto para asegurar que el comando print imprima en 
            cuanto lo llamemos, se recomienda usar el comando flush = True.
            Esto se entiende mejor si contamos elementos pero con un tiempo de espera, así 
            veremos que sin Flush=True, el comando print se actualizará hasta el final.
            import time
            print("Números: ")
            for i in range(8):
                time.sleep(0.5)
                print(i, end=" ",  flush=True)
            Ese código pruébalo con flush=True y flush = False y ahí versa la diferencia.
        """
        if self.prnt and (flag in self.flags):
            print(*args,end=end,sep=sep,flush=flush)
        if self.log:
            valor=''
            for e in [*args]: valor+=str(e)+sep
            valor+=end
            self.setFile(self.logFile,valor=valor.encode(self.code),echo='log' in self.flags,modo='ab')
    def getFile(self,name,full=1,code='',modo='rb',join=None,sep=':',prefijo=''):
        if not code: code=self.code
        file=open(name,modo)
        ret=[]
        for line in file:
            line=line.decode(code)[:-1]
            if line.strip()!='':
                ret += [line if full else line.strip()]
        file.close()
        if join==None:
            return ret if len(ret)>1 else ret[0]
        elif join.__class__ == dict:
            for k in ret:join[prefijo+k.split(sep)[0]]=k[len(k.split(sep)[0])+1:]
            return join
        elif join.__class__ == list:
            return join+ret
    def setFile(self,name,valor=[],echo=1,code='',modo='wb'):
        if not code: code=self.code
        file=open(name,modo)
        if echo: print('Archivo:',name)
        if list == valor.__class__:
            for line in valor:
                if echo: print(line.encode(code))
                file.write(line.encode(code)+b'\n')    
        else:
            if echo: print(valor)
            file.write(valor+b'\n')
        file.close()  
    def auto_info(self):
        info=self.getFile('home/info')

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
    import datetime,time
    salir=lambda: exit()
    print(__name__,datetime.datetime.now())
    pruebas[0]={'titulo':"salir, opcion por defecto",'f':salir}
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

def argvToParametros(prefijo='-'):
    kw=[]
    p = sys.argv
    arg=[]
    kwarg={}
    for i in range(0,len(sys.argv)):
        if prefijo in p[i][0]:
            kw+=[i,i+1]
            kwarg[p[i][1:]]=p[i+1]
        else:
            if not i in kw:
                arg+=[p[i]]
    return (arg,kwarg)

    if 1<len(sys.argv):
        f[sys.argv[1]](*argvToParametros())

if 'main' in __name__:
    #from pruebas import main_pruebas
    pruebas={           
        0:{'titulo':"Nombre del script:",'f':lambda: print(__name__)}
        }
    main_pruebas(pruebas,sys.argv)
            