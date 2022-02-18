#!/usr/bin/env python
# -*- coding: latin-1 -*-
import os
import sys
#import csv
#import time
#import datetime
#import math
#from tkinter import*
#from PIL import Image, ImageTk
#from reportlab.lib.units import mm, inch
#from reportlab.pdfgen import canvas as pdf
#from mbarete.mbarete import geometria
global d,pruebas
d={
    'img':os.getcwd()+'\\'+"imagenes"+'\\',
    'audio':os.getcwd()+'\\'+"sonidos"+'\\'
    }
print(datetime.datetime.now())
def VariablesDeEntorno():
    import os
    variables_de_entorno={env:os.environ[env] for env in os.environ}
    for variable in variables_de_entorno: 
        print("%s: %s" % (variable, variables_de_entorno[variable]))
def powerPath(pwd=os.getcwd()):
    import os
    """
        El módulo   os.path   siempre es el módulo adecuado para el sistema operativo en el cual Python está operando, 
        y por lo tanto es utilizable para rutas locales. Sin embargo, también puedes importar y utilizar los módulos 
        individuales si deseas manipular una ruta que siempre está en uno de los diferentes formatos. Todos tienen la misma interfaz:
            posixpath para rutas con estilo UNIX
            ntpath para rutas Windows
    """
    supportUnicode=os.path.supports_unicode_filenames #True si se pueden utilizar cadenas Unicode arbitrarias como nombres de archivo (dentro de las limitaciones impuestas por el sistema de archivos).
    print(supportUnicode)
    pwdA=pwd #obtengo la ruta path de mi ubicacion actual donde se esta ejecutando este Script 
    os.chdir(pwdA)
    os.chdir('..')
    pwdB=os.getcwd() #obtengo la ruta path de la carpeta de nivel superior a la carpeta actual donde se esta ejecutando este Script 
    os.chdir(pwdA)
    fullPathA=[pwdA+'\\'+d for d in os.listdir(pwdA)] # obtenemos la lista de archivos en la direccion pwd y luego le agregamos la ruta completa al archivo
    fullPathB=[pwdB+'\\'+d for d in os.listdir(pwdB)] # obtenemos la lista de archivos en la direccion pwd y luego le agregamos la ruta completa al archivo
    print('os.path.commonpath(fullPathA+fullPathB)',os.path.commonpath(fullPathA+fullPathB)) #Retorna la sub-ruta común más larga de cada nombre de ruta en la secuencia paths. 
    print('os.path.commonprefix(fullPathA+fullPathB)',os.path.commonprefix(fullPathA+fullPathB)) #Retorna el prefijo de ruta más largo (tomado carácter por carácter) que es un prefijo de todas las rutas en list. 
    pathB=''
    power={}
    for path in fullPathA:   #recorremos todos los archivos para obtener los datos de cada archivo
        if not pathB:
            pathB=path
        # obtenemos metadatos y datos del path
        power['basename'] = os.path.basename(path)   #Retorna un nombre base de nombre de ruta path.
        power['abspath']= os.path.abspath(path)  #Retorna una versión normalizada y absoluta del nombre de ruta path.
        power['dirname']= os.path.dirname(path)  #Retorna el nombre del directorio de la ruta path.
        power['exists'] = os.path.exists(path)   #Retorna True si path se refiere a una ruta existente o un descriptor de archivo abierto. Retorna False para enlaces simbólicos rotos. En algunas plataformas, esta función puede retornar False si no se concede permiso para ejecutar os.stat() en el archivo solicitado, incluso la ruta path existe físicamente.
        power['lexists'] = os.path.lexists(path) #Retorna True si path se refiere a un camino existente. Retorna True para los enlaces simbólicos rotos
        power['expanduser'] = os.path.expanduser(path) #En Unix y Windows, retorna el argumento con un componente inicial de ~ o ~user reemplazado por el directorio home de user
        power['expandvars']=os.path.expandvars(path)#Retorna el argumento con variables de entorno expandidas.
        power['ultimoAcceso'] = os.path.getatime(path)#Retorna la hora del ultimo acceso de path. El valor de retorno es un numero de punto flotante que da el numero de segundos desde la epoca 
        power['ultimaModificacion'] = os.path.getmtime(path)#Retorna el tiempo de la ultima modificación de path. El valor de retorno es un numero de punto flotante que da el numero de segundos desde la epoca
        power['creacionOModificacion']=os.path.getctime(path)#Retorna el ctime del sistema que, en algunos sistemas (como Unix) es la hora del ultimo cambio de metadatos y, en otros (como Windows), es el tiempo de creacion de path. El valor retornado es un numero que da el numero de segundos desde la epoca
        power['getsize'] =os.path.getsize(path)#Retorna el tamaño en bytes de path, Lanza una excepcion OSError si el archivo no existe o es inaccesible
        power['isabs'] = os.path.isabs(path) #Retorna True si path es un nombre de ruta de acceso absoluto. En Unix, eso significa que comienza con una barra diagonal, en Windows que comienza con una barra diagonal (invertida) despues de cortar una letra de unidad potencial.
        power['isfile'] =os.path.isfile(path)#Retorna True si path es un archivo existing. Esto sigue los enlaces simbólicos, por lo que tanto islink() como isfile() pueden ser verdaderos para la misma ruta.
        power['isdir'] = os.path.isdir(path)#Retorna True si path es un directorio existing. Esto sigue los enlaces simbólicos, por lo que tanto islink() como isdir() pueden ser verdaderos para la misma ruta.
        power['islink'] =os.path.islink(path)#Retorna True si path hace referencia a una entrada de directorio existing que es un enlace simbólico. Siempre False si el entorno de ejecución de Python no admite vínculos simbólicos.
        power['ismount']=os.path.ismount(path)#Retorna True si el nombre de ruta path es un mount point: un punto en un sistema de archivos donde se ha montado un sistema de archivos diferente. En POSIX, la función comprueba si el elemento primario de path, path/.., se encuentra en un dispositivo diferente de path, o si path/.. y path apuntan al mismo i-node en el mismo dispositivo — esto debería detectar puntos de montaje para todas las variantes Unix y POSIX. No es capaz de detectar de forma fiable los montajes de enlace en el mismo sistema de archivos. En Windows, una raíz de letra de unidad y un recurso compartido UNC siempre son puntos de montaje, y para cualquier otra ruta de acceso GetVolumePathName se llama para ver si es diferente de la ruta de acceso de entrada.
        power['join']=os.path.join(path, sys.argv[0])
        #Unir uno o más componentes de ruta de acceso de forma inteligente. El valor retornado es la concatenación de path y cualquier miembro de *paths 
        #con exactamente un separador de directorios (os.sep) después de cada parte no vacía, excepto la última, lo que significa que el resultado solo 
        #terminará en un separador si la última parte está vacía. Si un componente es una ruta absoluta, todos los componentes anteriores se desechan y 
        #la unión continúa desde el componente de ruta absoluta.
        #En Windows, la letra de la unidad no se restablece cuando se encuentra un componente de ruta absoluta (por ejemplo, r'\foo'). 
        #Si un componente contiene una letra de unidad, todos los componentes anteriores se desechan y la letra de unidad se restablece. 
        #Ten en cuenta que, dado que hay un directorio actual para cada unidad, `` os.path.join («c:», «foo») `` representa una ruta 
        #relativa al directorio actual en la unidad C: (c:foo),, no c:\foo.
        power['normcase']=os.path.normcase(path)#Normaliza las mayúsculas y minúsculas de un nombre de ruta. En Windows convierte todos los caracteres en el nombre de ruta a minúsculas y también convierte las barras inclinadas hacia atrás en barras inclinadas hacia atrás. En otros sistemas operativos, retorna la ruta sin cambios.
        power['normpath']=os.path.normpath(path)#Normaliza un nombre de ruta colapsando separadores redundantes y referencias de nivel superior para que A//B, A/B/, A/./B y A/foo/../B se transformen en``A/B``. Esta modificación de cadena puede que modifique el significado de la ruta que contenga enlaces simbólicos. En Windows, convierte las barras inclinadas hacia adelante en barras hacia atrás. Para normalizar mayúsculas y minúsculas, utiliza normcase().
        power['realpath']=os.path.realpath(path)#Retorna la ruta canónica del nombre de archivo especificado, eliminando cualquier enlace simbólico encontrado en la ruta (si es que tienen soporte por el sistema operativo).
        power['relpath']=os.path.relpath(path, start=os.curdir)#Retorna un nombre de ruta relativo a path desde el directorio actual o de un directorio start opcional. Este es un cálculo de ruta: No se accede al sistema de archivos para confirmar la existencia o la naturaleza de path o start.
        #start toma de forma predeterminada el valor de os.curdir.
        power['samefile']=os.path.samefile(pathB, path)#Retorna True si ambos argumentos de nombre de ruta refieren al mismo archivo o directorio. Esto se determina por el número de dispositivo y el número de i-node y lanza una excepción si una llamada de os.stat() en alguno de los nombres de ruta falla.
        #sameOpenFile=os.path.sameopenfile(os.stat(pathB), os.stat(path))#Retorna True si los descriptores de archivo fp1 y fp2 se refieren al mismo archivo.        
        power['samestat']=os.path.samestat(os.stat(pathB), os.stat(path))#Retorna True si las tuplas de stat (stat1 y stat2) refieren al mismo archivo. Estas estructuras pueden haber sido retornadas por os.fstat(), os.lstat(), o os.stat(). Esta función implementa la comparación subyacente utilizada por: samefile() y sameopenfile().
        power['split']=os.path.split(path)#Divide el nombre de la ruta path * en un par, `` (head, tail) `` donde *tail es el último componente del nombre de la ruta y head es todo lo que conduce a eso. La parte head nunca contendrá una barra; si head termina en una barra, tail estará vacía. Si no hay barra inclinada en path, head estará vacío. Si path está vacía, tanto head como tail estarán vacíos. Las barras diagonales finales se eliminan de head a menos que sea la raíz (solo una o más barras). En todos los casos, join(head, tail) retorna una ruta a la misma ubicación que path (pero las cadenas pueden diferir). 
        power['splitdrive']=os.path.splitdrive(path)
        #Divide el nombre de ruta path en un par (drive, tail) donde drive es un punto de montaje o una cadena vacía. En sistemas que no utilizan especificaciones de unidad, drive siempre será una cadena vacía. En todos los casos, drive + tail será lo mismo que path.
        #En Windows, divide un nombre de ruta en unidad / punto compartido UNC y ruta relativa.
        #Si la ruta contiene una letra de unidad, la unidad contendrá todo hasta los dos puntos inclusive. p.ej. splitdrive("c:/dir") retorna ("c:", "/dir")
        #Si la ruta contiene una ruta UNC, drive contendrá el nombre de host y el recurso compartido, hasta el cuarto separador, pero sin incluirlo. p.ej. splitdrive("//host/computer/dir") retorna ("//host/computer", "/dir")
        power['splitext']=os.path.splitext(path)#Divide el nombre de ruta path en un par (root, ext) de tal forma que root + ext == path, y ext queda vacío o inicia con un punto y contiene a lo mucho un punto. Se ignoran los puntos iniciales del nombre base; splitext('.cshrc') retorna ('.cshrc', '').
        print('\n')
        for atributo in power:
            print('.'+atributo+': ',power[atributo])
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
    
def strToClave(nombre, All=1 ):
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
            ('¿',''),
            ('¿','')
            ]
        for change in filtro[0:6 if not All else -1 ]:
            clave=clave.replace(change[0],change[1])
        return clave

def infofirewall(pwd='',buscar="Open" if len(sys.argv)==2 else sys.argv[2]):
    import os
    pwd=os.getcwd() if pwd=='' else pwd
    print("PowerShell get-NetFirewallRule |PowerShell ? DisplayName -like '"+buscar+"*' >"+' "'+pwd+os.path.sep+'rules.txt"')
    os.system("PowerShell get-NetFirewallRule |PowerShell ? DisplayName -like '"+buscar+"*' >"+' "'+pwd+os.path.sep+'rules.txt"')
    """
    Nombre de regla:                      Google Chrome (tráfico mDNS entrante)
    ----------------------------------------------------------------------
    Habilitada:                           Sí
    Dirección:                            Dentro
    Perfiles:                             Dominio,Privada,Pública
    Agrupamiento:                         Google Chrome
    LocalIP:                              Cualquiera
    RemoteIP:                             Cualquiera
    Protocolo:                            UDP
    LocalPort:                            5353
    RemotePort:                           Cualquiera
    Cruce seguro del perímetro:          No
    Acción:                               Permitir
    """
    show={}
    pasar={}
    count=1
    txt="rules.txt"
    file=open(txt)
    for line in file:
        print(line)
        if line=='':
            show[str(count)+"_"+pasar['Nombrederegla']]=pasar
            pasar={}
            count += 1
        if ':' in line:
            pasar[strToClave(line.split(':')[0])]=strToClave(line.split(':')[0].strip(),All=0)
    file.close()
    for rule in show:
        print(rule)

def proxy():
    """
    Controla el firewall de Windows desde la linea de comandos Netsh

    #Conexiones activas
    #netstat -ao    
    #Get-WindowsOptionalFeature -Online -FeatureName Microsoft-Windows-Subsystem-Linux
    #Enable-WindowsOptionalFeature -Online -FeatureName Microsoft-Windows-Subsystem-Linux
    #Enable-WindowsOptionalFeature -Online -FeatureName VirtualMachinePlatform
    #Set-NetConnectionProfile -InterfaceAlias Wi-Fi -NetworkCategory Private
    #Install-PackageProvider -Name NuGet -Force
    #Get-WindowsCapability -Online | ? Name -like 'OpenSSH*'
    #Install-Module -Force OpenSSH.Utils
    #Get-NetIPConfiguration
    #Get-NetConnectionProfile
     reglas y para habilitar puertos 
    #netsh advfirewall firewall add rule name="Open Port 2222 for WSL2" dir=in action=allow protocol=TCP localport=2222
    #New-NetFirewallRule -DisplayName "Open 2222 port to SSH Connection to WSL2" -Direction Inbound -LocalPort 2222 -Protocol TCP

     tunelando puerto de ip publica a ip del wsl 
    #netsh interface portproxy help
    #netsh interface portproxy show all
    #netsh interface portproxy add v4tov6 listenaddress=Inbound listenport=22 connectaddress=::1 connectport=22
    #netsh interface portproxy add v4tov6 listenport=22 connectaddress=::1 connectport=22
    #netsh interface portproxy delete v4tov4 listenaddress=192.168.100.21 listenport=22
    
    Veremos una serie de opciones que podemos utilizar para configurar dentro del firewall de Windows desde Netsh.
    Por ejemplo, para simplemente encender o apagar el firewall hay que ejecutar el comando:
    netsh advfirewall set currentprofile state on

    Pongamos por ejemplo que queremos habilitar el puerto 80 del cortafuegos y 
    lo queremos hacer desde la línea de comandos. En este caso tendríamos que ejecutar:
    netsh advfirewall firewall add rule name= «Open Port 80» dir=in action=allow protocol=TCP localport=80

    Si queremos eliminar un programa o un puerto también podemos hacerlo fácilmente. 
    En este caso tendríamos que ejecutar:
    netsh advfirewall firewall delete rule name= rule name program=»C:ProgramasPrograma.exe»    #(en el caso de un programa)
    netsh advfirewall firewall delete rule name= rule name protocol=udp localport=500           #(en el caso de un puerto, el que sea)
    Si hemos realizado cambios para probar algunos parámetros y queremos 
    volver a como estaba originalmente, podemos hacerlo fácilmente. 
    Simplemente hay que restaurar los valores predeterminados, que podemos hacerlo 
    también desde la línea de comandos. En esta ocasión hay que ejecutar:
    netsh advfirewall reset
    En definitiva, como vemos podemos utilizar diferentes opciones para configurar el firewall de Windows fácilmente desde la línea de comandos. Una alternativa a utilizarlo de forma visual, con la aplicación integrada en el propio sistema operativo de Microsoft.
    """
    print("La documentacion esta en proceso...")
def sudoWin(archivo=os.getcwd()+os.path.sep+__name__):
    """ funcion para ejecutar comandos en modo administrador en Windows"""
    #Acceder a variable de entorno del systema: os.environ[nombre_de_la_variable_de_entorno]
    #LISTA DE VARIABLES IMPORTANTES DEL SISTEMA:
    #USERDOMAIN: DESKTOP-HJNC31M
    #USERNAME: Mathias
    #USERPROFILE: C:\Users\Mathias
    #PSMODULEPATH: C:\Program Files\WindowsPowerShell\Modules;C:\Windows\system32\WindowsPowerShell\v1.0\Modules
    #PATHEXT: .COM;.EXE;.BAT;.CMD;.VBS;.VBE;.JS;.JSE;.WSF;.WSH;.MSC;.PY;.PYW
    #OS: Windows_NT
    #LOGONSERVER: \\DESKTOP-HJNC31M
    #LOCALAPPDATA: C:\Users\Mathias\AppData\Local
    #HOMEDRIVE: C:
    #COMSPEC: C:\Windows\system32\cmd.exe
    #COMPUTERNAME: DESKTOP-HJNC31M
    #TEMP: C:\Users\Mathias\AppData\Local\Temp
    #
    #METODO DIRECTO:
    #os.system(F'runas /{os.environ[USERNAME]}:{os.environ[USERDOMAIN]} "D:\\0_PYTHON\\OPENSSH-server en wsl2 debian\\pruebas.py"')
    if 'accesoRoot.lnk' in os.listdir():
        print('ya existe el archivo')
def connectSSH(command='-v' if len(sys.argv)==2 else sys.argv[2],ipaddres='127.0.0.1'):
    command=command.strip()
    user='invitadoSSH'
    port='23'
    pubKey='~/.ssh/mykey_ecdsa'
    print("conectando")
    os.system(f"ssh -i {pubKey} {user}@{ipaddres} -p {port} {command}")
    print("desconectado")

def make():
    os.mkdir('C:'+'\\'+'archivo_root')
    file=open('C:'+'\\'+'archivo_root'+'\\'+'file_root.txt','wb')
    file.write(b'instruccion')
    file.close()

print(str(__name__),sys.argv)
if ('__main__' in __name__):
    print("True")
    pruebas={
        'VariablesDeEntorno':VariablesDeEntorno,
        'powerPath':powerPath,
        'connectSSH':connectSSH,
        'funciones':funciones,
        'infofirewall':infofirewall,
        'sudoWin':sudoWin,
        'make':make
    }
    print('\n'+'\n'+'\n')
    print("PRUEBA Inicianda..."+'\n')
    pruebas[sys.argv[1]]()
    #Aviso de que la funcion termino.
    print('\n'+"PRUEBA Terminada...")
    print('\n')
#