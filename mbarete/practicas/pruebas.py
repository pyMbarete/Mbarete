#!/usr/bin/env python
# -*- coding: latin-1 -*-
import os,sys
d={
    'img':os.getcwd()+os.path.sep+"media"+os.path.sep,
    'audio':os.getcwd()+os.path.sep+"media"+os.path.sep
    }
def arboldearchivos(pwd=''):
    ret=[]
    if not pwd:
        pwd = os.getcwd()
    for check in os.listdir(pwd):
        if os.path.isfile(pwd+os.path.sep+check):
            ret += [pwd+os.path.sep+check]
        else:
            ret += arboldearchivos(pwd+os.path.sep+check)
    return ret


class object_prueba(object):
    """esta clase sera heredada a todas las clases de las demas practicas"""
    def __init__(self,pwd=os.getcwd(),logFile=__file__+'.log',flags=['error','init'],open_modo='wb',code='utf-8',home='home',ignore=[],**kwargs):
        super(object_prueba, self).__init__()
        self.pwd= pwd #ruta absoluta de donde se esta ejecutando el servidor
        self.historial_pwd=[0,[self.pwd]]
        self.log=True
        self.prnt=True
        self.code=code
        self.logFile=logFile
        self.flags=['']+flags
        self.open_modo=open_modo
        self.info=self.info_system()
        self.home=home
        self.ignore= ignore+['__pycache__',self.home,self.info['file']]

    def go_pwd(self,pwd='',mkdir='auto.'+__file__,scan=[]):
        equivalente={
            'practicas':'pwd_practicas',
            'consolas':'pwd_consolas',
            'repo':'git_repo_path'
        }
        pwd = self.info[equivalente[pwd]] if pwd in equivalente else pwd
        if os.path.lexists(pwd):
            if mkdir:
                if not mkdir in os.listdir(pwd): os.mkdir(pwd+os.sep+mkdir)
            os.chdir(pwd+os.sep+mkdir)
            self.historial_pwd[0]+=1
            self.historial_pwd[1]+=[pwd+os.sep+mkdir]
        self.p(os.getcwd())
    def back_pwd(self,pwd=''):
        self.p(os.getcwd())
    def return_system(self,command,join=None,sep=':',prefijo=''):
        os.system(command+" > "+self.info['tmp']+'mbarete_tmp')
        ret = self.getFile(self.info['tmp']+'mbarete_tmp',join=join,sep=sep,prefijo=prefijo)
        os.remove(self.info['tmp']+'mbarete_tmp')
        return ret
    def join(self,*arg): 
        return {k:ret[k] for ret in [*arg] for k in ret}

    def info_system(self):
        ignorar='.auto.'
        info={
            'file':'info'+ignorar,
            'pwd_practicas':'mbarete/practicas/',
            'pwd_consolas':'mbarete/consolas/',
            'prefijo':'cross_',
            'ignorar':ignorar
            }
        if os.name == 'nt':
            import platform
            info=self.join(info,{'OS':'windows','V':os.environ['OS'],'tmp':os.environ['TEMP']+os.sep,'home':os.environ['USERPROFILE']+os.sep})
            info['uname_sysname'] ,info['uname_nodename'] ,info['uname_release'] ,info['uname_version'] ,info['uname_machine'] ,info['uname_processor'] = platform.uname()
            info['uname_version']='"'+info['uname_version']+'"'
        elif os.name == 'posix':
            info=self.getFile('/etc/os-release',join=self.join(info,{'OS':'linux','tmp':'/tmp/'}),sep='=',prefijo='OS_',buscar=['VERSION','ID','ID_LIKE','PRETTY_NAME'])
            info['uname_sysname'] ,info['uname_nodename'] ,info['uname_release'] ,info['uname_version'] ,info['uname_machine'] = os.uname()
            info['V']='"'+info['OS_ID']+', '+info['OS_PRETTY_NAME'][1:-1]+'"'
            info['uname_version']='"'+info['uname_version']+'"'
        elif 'ANDROID_ROOT' in os.environ:
            info=join(info,{'OS':'android','V':os.environ['SHELL'],'tmp':'/tmp/'})
        t='temp_mbarete.'
        myTMP=[file[len(t):]for file in os.listdir(info['tmp']) if t in file[:len(t)]]
        buscar=[info['prefijo']+b for b in ['git_repo_path','git_repo_name','git_branch','pwd_consolas','pwd_practicas']]
        self.mis_repos={ repo.split('.git.')[0]:self.getFile(info['tmp']+t+repo,join={},buscar=buscar) for repo in myTMP if '.git.'+info['file'] in repo }
        info['sys_prefix']='"'+sys.prefix+'"'
        info['sys_platform']=sys.platform
        info['sys_version']='"'+sys.version.replace('\n',' ')+'"'
        return info
    def media_me(self,pwd,ret='media'):
        media={}
        total = 0
        num_archivos = 0
        formato = '%d-%m-%y %H:%M:%S'
        home=[]
        for ruta, directorios, archivos in os.walk(pwd, topdown=True):
            ruta='' if ruta==pwd else ruta.replace(self.pwd+os.sep,'')
            self.p(ruta,not ruta.split(os.sep)[0] in self.ignore,flag='init')
            if not ruta.split(os.sep)[0] in self.ignore:
                if not ruta in home: home+=[ruta]
                for elemento in archivos:
                    num_archivos += 1
                    archivo = ruta+os.sep+elemento if ruta else elemento
                    self.p(archivo,flag='init')
                    estado = os.stat(pwd+os.sep+archivo)
                    tamanho = estado.st_size
                    name=self.name+self.sepUser+str(num_archivos)
                    media[name]={'path':os.sep+archivo,'name':elemento,'size':tamanho}
                    ult_acceso = self.dt.fromtimestamp(estado.st_atime)
                    modificado = self.dt.fromtimestamp(estado.st_mtime)
                    ult_acceso = ult_acceso.strftime(formato)
                    modificado = modificado.strftime(formato)
                    total += tamanho
                    media[name]['modificado']=modificado
                    media[name]['ult_acceso']=ult_acceso
        home=[d.replace(pwd,'') for d in home if d]
        home.sort(reverse=False,key=lambda x: len(x.strip(os.sep)))
        if ret=='media':
            media['media_me']={'num_archivos':num_archivos,'peso_total_kb':round(total/1024, 1),'name':self.name,'address':(self.host,self.port),'pwd':pwd,'home':home}
            return media
        elif ret=='lista':
            return [ media[f]['path'] for f in media]

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
    def getFile(self,name,full=1,code='',modo='rb',join=None,sep=':',prefijo='',buscar=[]):
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
            for k in ret:
                clave=k.split(sep)[0]
                if buscar:
                    if clave in buscar:join[prefijo+clave]=k[len(clave)+1:]
                else:
                    join[prefijo+clave]=k[len(clave)+1:]
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
            