#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys
import csv
import time
import datetime
import math

#from mbarete.mbarete import geometria
global d,canvas_width,canvas_height
d={
    'img':os.getcwd()+os.path.sep+"media"+os.path.sep,
    'audio':os.getcwd()+os.path.sep+"media"+os.path.sep
    }
canvas_width = 1100
canvas_height =1000
print(datetime.datetime.now())
print(d)
def timeConOsPath():
    import os, sys,time
    #time ,pruebas con la libreria time:
    print('time.gmtime(0):',time.gmtime(0)) #
    print('time.ctime(0):',time.ctime(0))
    print('sys.argv[0]:',sys.argv[0])
    print('os.path.getatime(sys.argv[0]):',os.path.getatime(sys.argv[0]))
    print('time.ctime(os.path.getmtime(sys.argv[0])):',time.ctime(os.path.getmtime(sys.argv[0])),'Tiempo de la ultima modificación de path')
    print('time.ctime(os.path.getctime(sys.argv[0])):',time.ctime(os.path.getctime(sys.argv[0])),'En algunos sistemas (como Unix) es la hora del ultimo cambio de metadatos y, en otros (como Windows), es el tiempo de creacion de path')
    print('time.ctime(os.path.getatime(sys.argv[0])):',time.ctime(os.path.getatime(sys.argv[0])),'Hora del ultimo acceso de path')
    print(r'strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime(os.path.getatime(sys.argv[0]))):',time.strftime("%a, %d %b %Y %H:%M:%S +0000", time.gmtime(os.path.getatime(sys.argv[0]))))
def VariablesDeEntorno():
    import os
    for k in os.environ:  print("%s: %s" % (k, os.environ[k]))
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
def pasarEnterosaBytes(desde=0,hasta=100,paso=1,numeroDeBytes=1):
    import sys
    for x in range(desde,hasta,paso):
        orden=sys.byteorder #Para indicar que queremos usar el ordenamiento propio de la plataforma
        orden='big'         #el byte mas significativo ocupa la primera posición en el vector
        orden='little'      #el byte mas significativo estará en la última posición
        bi=(x).to_bytes(numeroDeBytes, byteorder=orden) #convertimos el entero a tipo byte
        entero=int.from_bytes(bi, byteorder=orden) #convertimos el byte a entero 
        print(x,bin(x),x.bit_length(),bi,entero)
def playlist(pwd='.'):
    #inicia codigo de la prueba
    tiempo=45
    ignorarArchivo=['Crear Lista.py','0000_archivos.txt']
    formatos=['.mp3','.mp4','.wav','.avi','.webm','.ogg','.m4a','.mkv','.rmvb','.vob','.wmv']
    playListFile=pwd+'\\'+"000_playList.m3u"
    if playListFile in os.listdir(pwd):
        os.remove(playListFile)
    palabra=input("ingrese una palabra para filtrar los archivos : ")
    midir=[archivo for archivo in os.listdir(pwd) if ((archivo not in ignorarArchivo) and (os.path.isfile(pwd+'\\'+archivo)))]
    midir=[archivo for archivo in midir if [archivo for exten in formatos if (exten in archivo[-6:].lower()) ] ]
    midir=[archivo for archivo in midir if (palabra.lower() in archivo.lower())]
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
        ('  ',' ')
        ]
    for contador in range(0,len(midir),1):
            archivo=str(midir[contador]).lower()
            for change in filtro:
                archivo=archivo.replace(change[0],change[1])
            os.rename(pwd+'\\'+midir[contador], pwd+'\\'+archivo)
            midir[contador]=archivo
    playList=open(playListFile,"a")
    playList.write('#EXTM3U\n')
    for contador in range(0,len(midir),1):
        playList.write('#EXTINF:'+str(tiempo)+','+str(midir[contador])+'\n')
        playList.write(pwd+'\\'+str(midir[contador])+'\n')
    playList.close()
    if midir:
        os.system(playListFile)

def os_walk():
    import os
    from datetime import datetime
    media={}
    ruta_app = os.getcwd()
    total = 0
    num_archivos = 0
    formato = '%d-%m-%y %H:%M:%S'
    linea = '-' * 60
    user=''
    for ruta, directorios, archivos in os.walk(ruta_app, topdown=True):
        print('\nruta       :', ruta) 
        for elemento in archivos:
            num_archivos += 1
            archivo = ruta + os.sep + elemento
            estado = os.stat(archivo)
            tamanho = estado.st_size
            ult_acceso = datetime.fromtimestamp(estado.st_atime)
            modificado = datetime.fromtimestamp(estado.st_mtime)
            ult_acceso = ult_acceso.strftime(formato)
            modificado = modificado.strftime(formato)

            total += tamanho
            print(linea)
            print('archivo      :', elemento)
            print('modificado   :', modificado)        
            print('último acceso:', ult_acceso)
            print('tamaño (byte)  :', tamanho)

    print(linea)
    print('Núm. archivos:', num_archivos)
    print('Total (kb)   :', round(total/1024, 1))
from pruebas import main_pruebas
if 'main' in __name__:
    import sys
    pruebas={           
        1:{'titulo':"Lista de las variables del sistema",'f':VariablesDeEntorno},
        2:{'titulo':"os.path, Manipulaciones comunes de nombre de ruta:",'f':powerPath},
        3:{'titulo':"Prueba para calcular espacios en bits de numeros enteros y flotantes:",'f':pasarEnterosaBytes},
        4:{'titulo':"Crear un archivo PLayList para reproducir con el 'Reproductor Multimedia' del sistema operativo",'f':playlist},
        5:{'titulo':"recorrer directorio con os_walk:",'f':os_walk},
        6:{'titulo':"time ,pruebas con la libreria time:",'f':timeConOsPath},
        }

    main_pruebas(pruebas,sys.argv)