#!/usr/bin/env python
# -*- coding: latin-1 -*-
__all__=["main_pruebas","deco"]
import os,sys
""" 
Barrio San Miguel San Lorenzo .Giuzzio
7 Aplicaciones que debes construir | desafío de código
https://www.youtube.com/watch?v=psSO3T7gslU
App 1 : Chat Bot Conocidos
App 2 : Bus Bot Recorridos
App 3 : Web Scrapper
App 4 : Eventos Grupales
App 5 : Tracker CriptoMoneda
App 6 : Tendencia Inversiones
App 7 : Juego de Rol
"""
def powerPath(pwd=os.getcwd()):
    """Datos de rutas y carpetas y archivos:"""
    import os,sys
    """
        True si se pueden utilizar cadenas Unicode 
        arbitrarias como nombres de archivo 
        (dentro de las limitaciones impuestas 
        por el sistema de archivos).
    """
    print(os.path.supports_unicode_filenames )
    """
        ruta path de mi ubicacion actual donde 
        se esta ejecutando este Script
    """
    pwdA=pwd 
    os.chdir(pwdA)
    os.chdir('..')
    """
        path de la carpeta superior a la carpeta 
        actual donde esta este Script
    """
    pwdB=os.getcwd() 
    os.chdir(pwdA)
    """
        lista de archivos en pwd y agregamos 
        la ruta completa a cada archivo
    """
    fullPathA=[pwdA+'\\'+d for d in os.listdir(pwdA)] 
    fullPathB=[pwdB+'\\'+d for d in os.listdir(pwdB)]
    """
        Retorna la sub-ruta común más larga de cada 
        nombre de ruta en la secuencia paths.
    """
    print(
        'os.path.commonpath(fullPathA+fullPathB)',
        os.path.commonpath(fullPathA+fullPathB)
        ) 
    """
        Retorna el prefijo de ruta más largo (tomado carácter por 
        carácter) que es un prefijo de todas las rutas en list. 
    """
    print(
        'os.path.commonprefix(fullPathA+fullPathB)',
        os.path.commonprefix(fullPathA+fullPathB)
        ) 
    pathB=''
    power={}
    #recorremos todos los archivos para obtener los datos de cada archivo
    for path in fullPathA:   
        if not pathB: pathB=path
        #Retorna un nombre base de nombre de ruta path.
        power['basename'] = os.path.basename(path)   
        #Retorna una versión normalizada y absoluta del nombre de ruta path.
        power['abspath']= os.path.abspath(path)  
        #Retorna el nombre del directorio de la ruta path.
        power['dirname']= os.path.dirname(path)  
        """
            Retorna True si path se refiere a una ruta existente o 
            un descriptor de archivo abierto. Retorna False para 
            enlaces simbólicos rotos. En algunas plataformas, esta 
            función puede retornar False si no se concede permiso 
            para ejecutar os.stat() en el archivo solicitado, 
            incluso la ruta path existe físicamente.
        """
        power['exists'] = os.path.exists(path)   
        """
            Retorna True si path se refiere a un camino existente. 
            Retorna True para los enlaces simbólicos rotos
        """
        power['lexists'] = os.path.lexists(path) 
        """
            En Unix y Windows, retorna el argumento con un 
            componente inicial de ~ o ~user reemplazado por 
            el directorio home de user
        """
        power['expanduser'] = os.path.expanduser(path) 
        """
            Retorna el argumento con variables de entorno expandidas.
        """
        power['expandvars']=os.path.expandvars(path)
        """
            Retorna la hora del ultimo acceso de path. 
            El valor de retorno es un numero de punto flotante 
            que da el numero de segundos desde la epoca 
        """
        power['ultimoAcceso'] = os.path.getatime(path)
        """
            Retorna el tiempo de la ultima modificación de path.
            El valor de retorno es un numero de punto flotante 
            que da el numero de segundos desde la epoca
        """
        power['ultimaModificacion'] = os.path.getmtime(path)
        """
            Retorna el ctime del sistema que, en algunos sistemas (como 
            Unix) es la hora del ultimo cambio de metadatos y, en otros 
            (como Windows), es el tiempo de creacion de path. 
            El valor retornado es un numero que da el 
            numero de segundos desde la epoca
        """
        power['creacionOModificacion']=os.path.getctime(path)
        """
            Retorna el tamaño en bytes de path, Lanza una excepcion 
            OSError si el archivo no existe o es inaccesible
        """
        power['getsize'] =os.path.getsize(path)

        """
            Retorna True si path es un nombre de ruta de acceso absoluto. 
            En Unix, eso significa que comienza con una barra diagonal, 
            en Windows que comienza con una barra diagonal (invertida) 
            despues de cortar una letra de unidad potencial.
        """
        power['isabs'] = os.path.isabs(path) 
        """
            Retorna True si path es un archivo existing. Esto sigue los 
            enlaces simbólicos, por lo que tanto islink() como isfile() 
            pueden ser verdaderos para la misma ruta.
        """
        power['isfile'] =os.path.isfile(path)
        """
            Retorna True si path es un directorio existing. 
            Esto sigue los enlaces simbólicos, por lo que tanto islink() 
            como isdir() pueden ser verdaderos para la misma ruta.
        """
        power['isdir'] = os.path.isdir(path)
        """
            Retorna True si path hace referencia a una entrada de 
            directorio existing que es un enlace simbólico. 
            Siempre False si el entorno de ejecución de Python no 
            admite vínculos simbólicos.
        """
        power['islink'] =os.path.islink(path)
        """
            Retorna True si el nombre de ruta path es un 
            mount point: un punto en un sistema de archivos donde 
            se ha montado un sistema de archivos diferente. 
            En POSIX, la función comprueba si el elemento 
            primario de path, path/.., se encuentra en un dispositivo 
            diferente de path, o si path/.. y path apuntan al mismo 
            i-node en el mismo dispositivo — esto debería detectar 
            puntos de montaje para todas las variantes Unix y POSIX. 
            No es capaz de detectar de forma fiable los montajes de 
            enlace en el mismo sistema de archivos. En Windows, una 
            raíz de letra de unidad y un recurso compartido UNC 
            siempre son puntos de montaje, y para cualquier otra 
            ruta de acceso GetVolumePathName se llama para ver si 
            es diferente de la ruta de acceso de entrada.
        """
        power['ismount']=os.path.ismount(path)
        """
            Unir uno o más componentes de ruta de acceso de forma 
            inteligente. El valor retornado es la concatenación de 
            path y cualquier miembro de *paths con exactamente un 
            separador de directorios (os.sep) después de cada parte 
            no vacía, excepto la última, lo que significa que el 
            resultado solo terminará en un separador si la última 
            parte está vacía. Si un componente es una ruta absoluta, 
            todos los componentes anteriores se desechan y la unión 
            continúa desde el componente de ruta absoluta.
            En Windows, la letra de la unidad no se restablece 
            cuando se encuentra un componente de ruta absoluta 
            (por ejemplo, r'\foo'). 
            Si un componente contiene una letra de unidad, todos 
            los componentes anteriores se desechan y la letra de 
            unidad se restablece. 
            Ten en cuenta que, dado que hay un directorio actual 
            para cada unidad, `` os.path.join («c:», «foo») `` 
            representa una ruta relativa al directorio actual 
            en la unidad C: (c:foo),, no c:\foo.
        """
        power['join']=os.path.join(path, sys.argv[0])
        """
            Normaliza las mayúsculas y minúsculas de un nombre de ruta. 
            En Windows convierte todos los caracteres en el nombre de 
            ruta a minúsculas y también convierte las barras inclinadas 
            hacia atrás en barras inclinadas hacia atrás. 
            En otros sistemas operativos, retorna la ruta sin cambios.
        """
        power['normcase']=os.path.normcase(path)
        """
            Normaliza un nombre de ruta colapsando separadores 
            redundantes y referencias de nivel superior para que 
            A//B, A/B/, A/./B y A/foo/../B se transformen en``A/B``. 
            Esta modificación de cadena puede que modifique el 
            significado de la ruta que contenga enlaces simbólicos. 
            En Windows, convierte las barras inclinadas hacia 
            adelante en barras hacia atrás. Para normalizar 
            mayúsculas y minúsculas, utiliza normcase().
        """
        power['normpath']=os.path.normpath(path)
        """
            Retorna la ruta canónica del nombre de archivo 
            especificado, eliminando cualquier enlace simbólico 
            encontrado en la ruta (si es que tienen soporte 
            por el sistema operativo).
        """
        power['realpath']=os.path.realpath(path)
        """
            Retorna un nombre de ruta relativo a path desde el 
            directorio actual o de un directorio start opcional. 
            Este es un cálculo de ruta: No se accede al sistema 
            de archivos para confirmar la existencia o la 
            naturaleza de path o start.
            start toma de forma predeterminada el valor de os.curdir.
        """
        power['relpath']=os.path.relpath(path, start=os.curdir)
        """
            Retorna True si ambos argumentos de nombre de ruta 
            refieren al mismo archivo o directorio. Esto se 
            determina por el número de dispositivo y el número 
            de i-node y lanza una excepción si una llamada de 
            os.stat() en alguno de los nombres de ruta falla.
        """
        power['samefile']=os.path.samefile(pathB, path)
        """
            Retorna True si los descriptores de archivo fp1 y fp2 
            se refieren al mismo archivo.
        """
        sameOpenFile=os.path.sameopenfile(os.stat(pathB), os.stat(path))
        """
            Retorna True si las tuplas de stat (stat1 y stat2) 
            refieren al mismo archivo. Estas estructuras pueden haber 
            sido retornadas por os.fstat(), os.lstat(), o os.stat().
            Esta función implementa la comparación subyacente 
            utilizada por: samefile() y sameopenfile().
        """
        power['samestat']=os.path.samestat(os.stat(pathB), os.stat(path))
        """
            Divide el nombre de la ruta path * en un par, (head, tail) 
            donde *tail es el último componente del nombre de la ruta 
            y head es todo lo que conduce a eso. 
            La parte head nunca contendrá una barra; si head 
            termina en una barra, tail estará vacía. Si no hay 
            barra inclinada en path, head estará vacío. 
            Si path está vacía, tanto head como tail estarán vacíos. 
            Las barras diagonales finales se eliminan de head a 
            menos que sea la raíz (solo una o más barras). 
            En todos los casos, join(head, tail) retorna una ruta a la 
            misma ubicación que path (pero las cadenas pueden diferir). 
        """
        power['split']=os.path.split(path)
        """
            Divide el nombre de ruta path en un par (drive, tail) donde 
            drive es un punto de montaje o una cadena vacía. 
            En sistemas que no utilizan especificaciones de unidad, 
            drive siempre será una cadena vacía. 
            En todos los casos, drive + tail será lo mismo que path.
            En Windows, divide un nombre de ruta en unidad / punto 
            compartido UNC y ruta relativa.
            Si la ruta contiene una letra de unidad, la unidad 
            contendrá todo hasta los dos puntos inclusive. 
            p.ej. splitdrive("c:/dir") retorna ("c:", "/dir")
            Si la ruta contiene una ruta UNC, drive contendrá 
            el nombre de host y el recurso compartido, hasta 
            el cuarto separador, pero sin incluirlo. 
            p.ej. splitdrive("//host/computer/dir") 
            retorna ("//host/computer", "/dir")
        """
        power['splitdrive']=os.path.splitdrive(path)
        """
            Divide el nombre de ruta path en un par (root, ext) de tal 
            forma que root + ext == path, y ext queda vacío o inicia 
            con un punto y contiene a lo mucho un punto. 
            Se ignoran los puntos iniciales del nombre base;
            splitext('.cshrc') retorna ('.cshrc', '').
        """
        power['splitext']=os.path.splitext(path)
        print('\n')
        for atributo in power:
            print(f'.{atributo}: {power[atributo]}')
def pasarEnterosaBytes(desde=0,hasta=100,paso=1,numeroDeBytes=1):
    """Prueba para calcular espacios en bits de numeros enteros y flotantes"""
    import sys
    for x in range(desde,hasta,paso):
        orden=sys.byteorder #Para indicar que queremos usar el ordenamiento propio de la plataforma
        orden='big'         #el byte mas significativo ocupa la primera posición en el vector
        orden='little'      #el byte mas significativo estará en la última posición
        bi=(x).to_bytes(numeroDeBytes, byteorder=orden) #convertimos el entero a tipo byte
        entero=int.from_bytes(bi, byteorder=orden) #convertimos el byte a entero 
        print(x,bin(x),x.bit_length(),bi,entero)
def os_walk_size():
    """Buscar archivos pesados"""
    obj=object_mbarete()
    buscando=1
    pwd = '/'
    Lista=['#!/bin/bash','ls / > info_size.txt']
    cmd='du -sh '
    ignorarCarpeta=['media','home','dev','mnt','usr','proc']
    escala={'0':1.0,'K':1.0,'M':1024.0,'G':1024.0*1024.0}
    for carpeta in os.listdir(pwd):
        if not carpeta in ignorarCarpeta:
            Lista+=['echo '+cmd+pwd+carpeta+' >> info_size.txt']
            Lista+=[cmd+pwd+carpeta+' >> info_size.txt']
    obj.setFile('Listar_size.sh',valor=Lista)
    pwd = '//'
    Lista=[]
    while buscando:
        buscando=input('Buscar en la siguiente direccion %s:'%(pwd))
        if buscando not in ['no','N','n','NO']:
            buscando=0
        else:
            buscando=1
        for carpeta in os.listdir(pwd):
            if not carpeta in ignorarCarpeta:
                prom=cmd+pwd+carpeta
                print('$',prom)
                #estado = os.stat(pwd+carpeta)
                #size = estado.st_size
                Lista += obj.return_system(prom,join=[],sep=' ')
                #Lista += [[carpeta,size]]
                #os.system(prom)
        
        for x in range(len(Lista)):
            size=Lista[x].split('/')[0].strip()
            ruta=Lista[x][len(size):].strip()
            size=[size,escala[size[-1]]]
            size[0]=obj.if_exist_split(['K','M','G'],size[0],sino=[size[0]])
            size=float(size[0][0].replace(',','.'))*size[1]
            Lista[x]=[ruta,size]
        Lista.sort(reverse=True, key=lambda x: x[1])
        for x in range(len(Lista)):print(Lista[x])
        pwd+=input('ingrese la carpeta a escanear')+os.sep     
def playlist(pwd='.'):
    '''crea un fichero "000_playList.m3u" de archivos que puede reproducir VLC'''
    tiempo=45
    ignorarArchivo=['config.py','0000_archivos.txt']
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
    """recorrer directorio con os_walk"""
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
def VariablesDeEntorno():
    """Lista de las variables del sistema"""
    import os
    for k in os.environ:  print("%s: %s" % (k, os.environ[k]))
def timeConOsPath():
    """time ,pruebas con la libreria time"""
    import os, sys,time,datetime
    print('time.gmtime(0):',time.gmtime(0)) #
    print('time.ctime(0):',time.ctime(0))
    print('sys.argv[0]:',sys.argv[0])
    print('os.path.getatime(sys.argv[0]):',os.path.getatime(sys.argv[0]))
    print('Tiempo de la ultima modificación de path')
    print('time.ctime(os.path.getmtime(sys.argv[0])):',time.ctime(os.path.getmtime(sys.argv[0])))
    print('En algunos sistemas (como Unix) es la hora del ultimo cambio de metadatos y, en otros (como Windows), es el tiempo de creacion de path')
    print('time.ctime(os.path.getctime(sys.argv[0])):',time.ctime(os.path.getctime(sys.argv[0])))
    print('Hora del ultimo acceso de path')
    print('time.ctime(os.path.getatime(sys.argv[0])):',time.ctime(os.path.getatime(sys.argv[0])),'Hora del ultimo acceso de path')

    print(r'strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime(os.path.getatime(sys.argv[0]))):')
    print(time.strftime("%a, %d %b %Y %H:%M:%S +0000", time.gmtime(os.path.getatime(sys.argv[0]))))
    fecha=['Año','Mes','Dia del Mes']
    #fecha=[int(input('Ingrese %s:'%(i))) for i in fecha]
    fecha=[1995,5,21]
    print(datetime(*fecha)<datetime.now())
    fechas=[fecha,[1998,7,3],[1958,8,21],[2005,1,4],[1975,1,4]]
    print(fechas)
    fechas.sort(key=lambda e:  datetime.now()-datetime(*e))
    print(fechas)
def arboldearchivos(pwd=''):
    ret=[]
    if not pwd:
        pwd = os.getcwd()
    for check in os.listdir(pwd):
        if os.path.isfile(pwd+os.sep+check):
            ret += [pwd+os.sep+check]
        else:
            ret += arboldearchivos(pwd+os.path.sep+check)
    return ret
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
        elif decorator_self.flag=='tiempo':
            import time
            def wrappee(*args, **kwargs):
                T0=time.time()
                f_return= original_func(*args,**kwargs)
                print(decorator_self.msj,time.time()-T0)
                return f_return
            return wrappee            
        elif decorator_self.flag=='async_loop':
            import asyncio
            def partial(original_func, /, *args, **keywords):
                def newfunc(*fargs, **fkeywords):
                    newkeywords = {**keywords, **fkeywords}
                    return original_func(*args, *fargs, **newkeywords)
                newfunc.original_func = original_func
                newfunc.args = args
                newfunc.keywords = keywords
                return newfunc
            blocking_io = partial(original_func, *args,**kwargs)

            async def wrappee(*args,**kwargs):
                loop = asyncio.get_running_loop()

                # 1. Run in the default loop's executor:
                result = await loop.run_in_executor(
                    None, 
                    blocking_io
                    )
                #ret=funcion(*args,**kwargs)
                #print('default thread pool', result)
                return result
        else:
            print('#'*30+'\n'+'#'*30)
            print('En decorador:', decorator_self.flag)
            print("Funcion Ignorada:",original_func.__name__)
            print('#'*30+'\n'+'#'*30)
            return args,kwargs
        return wrappee
def multitarea_asyncio():
    """codigo async/await con ASYNCIO:"""
    import asyncio
    print('Tiempo real: async def funcname()')
    async def io_operation(ident,t):
        print(f'La operación {ident} ha comenzado')
        # Solo para emular una operación I/O bloqueante
        await asyncio.sleep(t) 
        print(f'La operación {ident} ha terminado')
    async def main():
        await asyncio.gather(
            io_operation('A',2),
            io_operation('B',1),
            )
    if __name__ == '__main__':
        loop = asyncio.get_event_loop() # Ciclo de eventos
        loop.run_until_complete( main() )

    print('Tiempo real: async with expr as var')
    class Foo:
        async def __aenter__(self):
            print("Entrando en el contexto")
            await asyncio.sleep(1)
        async def __aexit__(self, exc_type, exc, tb):
            print("Saliendo del contexto")
            await asyncio.sleep(1)
    async def main():
        async with Foo() as foo:  # <<<<<<<<<<<<<<<<<<<<<<<<<
            print("Algo ocurre en medio...") 
    if __name__ == '__main__':
        loop = asyncio.get_event_loop() # Ciclo de eventos
        loop.run_until_complete( main() )

    print('Tiempo real: async for target in iter')
    class IterableAsincrono:
        def __init__(self, n):
            self._n = n

        def __aiter__(self):
            return self

        async def __anext__(self):
            item = await self.get_next()
            if item:
                return item
            else:
                raise StopAsyncIteration

        async def get_next(self):
            if self._n > 0:
                await asyncio.sleep(1)
                self._n -= 1
                return self._n

    async def main():
        async for item in IterableAsincrono(5):  # <<<<<<<<<<<<<<<<
            print(item) 

    if __name__ == '__main__':
        loop = asyncio.get_event_loop() # Ciclo de eventos
        loop.run_until_complete(main())
def multitarea_multiprocess():
    import asyncio
    print('Tiempo real: async def funcname()')
    async def io_operation(ident,t):
        print(f'La operación {ident} ha comenzado')
        # Solo para emular una operación I/O bloqueante
        await asyncio.sleep(t) 
        print(f'La operación {ident} ha terminado')
    async def main():
        await asyncio.gather(
            io_operation('A',2),
            io_operation('B',1),
            )
    if __name__ == '__main__':
        loop = asyncio.get_event_loop() # Ciclo de eventos
        loop.run_until_complete( main() )

    print('Tiempo real: async with expr as var')
    class Foo:
        async def __aenter__(self):
            print("Entrando en el contexto")
            await asyncio.sleep(1)
        async def __aexit__(self, exc_type, exc, tb):
            print("Saliendo del contexto")
            await asyncio.sleep(1)
    async def main():
        async with Foo() as foo:  # <<<<<<<<<<<<<<<<<<<<<<<<<
            print("Algo ocurre en medio...") 
    if __name__ == '__main__':
        loop = asyncio.get_event_loop() # Ciclo de eventos
        loop.run_until_complete( main() )

    print('Tiempo real: async for target in iter')
    class IterableAsincrono:
        def __init__(self, n):
            self._n = n

        def __aiter__(self):
            return self

        async def __anext__(self):
            item = await self.get_next()
            if item:
                return item
            else:
                raise StopAsyncIteration

        async def get_next(self):
            if self._n > 0:
                await asyncio.sleep(1)
                self._n -= 1
                return self._n

    async def main():
        async for item in IterableAsincrono(5):  # <<<<<<<<<<<<<<<<
            print(item) 

    if __name__ == '__main__':
        loop = asyncio.get_event_loop() # Ciclo de eventos
        loop.run_until_complete(main())
def decoranding():
    """Ejercico con DECORADORES:"""
    print("falta agregar codigo para decorar")
def ahorcado():
    obj=object_mbarete(
        pwd='media',
        carpetas={'dir_media':'/mbarete/media'}
        )
    import random
    vidas='******'
    letrasCantadas=''
    secretos=obj.getFile("palabras.txt")
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


def main_pruebas(pruebas,i=' '):
    '''CLI para Probar las funciones'''
    import datetime
    print( __name__,datetime.datetime.now() )
    if len(sys.argv)>1:
        pruebas[int(sys.argv[1])-1]()
        exit()
    while i != '':
        print('#'*70)
        for p in range(len(pruebas)):
            #print([])
            print(f'{p+1}.{pruebas[p].__doc__}: >>> {pruebas[p].__name__}()')
        i=input('Ingrese el numero de la siguiente prueba: ').strip()
        if i=='' : break
        else: i = int(float(i))-1
        print(f'PRUEBA: {pruebas[i].__doc__} Iniciada...')
        #llamamos a la funcion Decorada y esperamos que termine
        pruebas[i]()
        #Aviso de que la funcion termino.
        print(f'PRUEBA: {pruebas[i].__doc__} Terminada...')
        print('#'*70+'\n')
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
def crud_sqLite3():
    """CRUD sqlite3"""
    from bbdd import CRUD, query_sqLite3
    import sqlite3
    tablas={
        'alumnos':["id","name TEXT","address TEXT","edad integer"]
    }
    crud=CRUD(
        sqlite3,
        tablas,
        query=query_sqLite3,
        dbname='sql/pruebas.bd',
        reset=0
    )
    print(crud.campoID)
    print(crud.tablas['alumnos'])
    crud.Cargar('alumnos',tablas['alumnos'],['mathias','San Lorenzo',27])
    crud.Cargar('alumnos',tablas['alumnos'],['Avi','Luque',24])
    crud.Cargar('alumnos',tablas['alumnos'],['Robert','Lambare',25])
    print(crud.SelectAll('alumnos'))
    from extras import tabla_automatica
    x=tabla_automatica[0]
    for k in x:
        print(crud.query['getCampo'](k,x[k]))
    crud.infoSQL()
def crud_postgres():
    """CRUD PostgreSQL"""
    from bbdd import CRUD, query_postgres
    import psycopg2

    tablas={
        'alumnos':["id","name TEXT","address TEXT","edad int"]
    }
    crud=CRUD(
        psycopg2,
        tablas,
        query=query_postgres,
        reset=1
    )
    print(crud.campoID)
    crud.Cargar('alumnos',tablas['alumnos'],['mathias','San Lorenzo',27])
    crud.Cargar('alumnos',tablas['alumnos'],['Avi','Luque',24])
    crud.Cargar('alumnos',tablas['alumnos'],['Robert','Lambare',25])
    print(crud.SelectAll('alumnos'))
    from extras import tabla_automatica
    x=tabla_automatica[0]
    for k in x:
        print(crud.query['getCampo'](k,x[k]))
def Gestor_flatpak():
    """Obtener informacion de flatpak"""
    from extras import object_mbarete
    obj=object_mbarete()
    listar='flatpak list'
    campos_list=['Nombre','AppID','Version','Branch','Installation']
    escala={'0':1.0,'kB':1.0,'MB':1024.0,'GB':1024.0*1024.0}
    size_list=0
    ret=obj.ret_system(
        'flatpak list',
        join=[],
        campos_list=campos_list,
        sep='\t'
        )
    for x in range(len(ret)):
        App=ret[x]
        ret[x]=obj.ret_system(
            'flatpak info '+App['AppID']+'//'+App['Branch'],
            join=App,
            sep=':'
        )
        ret[x]['autoremove']=1
    #calculamos el peso Total de Flatpak
    for x in range(len(ret)):
        s=ret[x]['Installed'].split('\xa0')
        s[0]=float(s[0].replace(',','.'))
        ret[x]['Installed']=round(s[0]*escala[s[-1].strip()]/1024.0)
        size_list+=ret[x]['Installed']

    #ordenamos del mas pesado al menos pesado
    ret.sort(reverse=1,key=lambda x: x['Installed'])

    obj.p(int(size_list),'MB')

    #Verificamos dependencias
    runtime=[]
    platform=[e['Referencia'][8:] for e in ret if '.Platform/' in e['Referencia']]
    for e in ret:
        if 'app/' == e['Referencia'][:4]:
            obj.p(e['Nombre'],e['Runtime'])        
            runtime+=[e['Runtime']]
            if e['Runtime'] in platform:
                platform.pop(platform.index(e['Runtime']))
    obj.p('Runtimes Necesarios:')
    obj.p(runtime,listar=1)
    obj.p('\n')
    obj.p('Runtimes que NO son Necesarios:')
    obj.p(platform,listar=1)
    #mostranddo las Apps que ya no son necesarias
    for app in platform: print('flatpak uninstall '+app)
    obj.p('flatpak_status=',ret)
    #obj.setFile('flatpak_status',[for r in ret])
def generador_imagen_to_unicode():
    """Imagen_to_unicode"""
    obj=object_mbarete(
        pwd='media',
        carpetas={'dir_media':'mbarete/media/'}
        )
    valores=[]
    n=1
    ok=1
    while ok:
        try:
            valores+=['']
            for x in range(100):
                valores[-1]+=str(n+x)+':'+chr(n+x)+','
            print(valores[-1].encode(obj.code))
            n+=100
        except:
            ok=0
    obj.setFile(obj.pwd+'caracteres_unicode.txt', valores,echo=0)
def conector_FireBase():
    """Prueba de acceso a base de datos de www.FireBase.com"""
    from firebase import Firebase
    config = {
        "apiKey": "apiKey",
        "authDomain": "projectId.firebaseapp.com",
        "databaseURL": "https://databaseName.firebaseio.com",
        "storageBucket": "projectId.appspot.com"
        }
    firebase = Firebase(config)
if 'main' in __name__:
    #from pruebas import main_pruebas
    main_pruebas([
        decoranding,multitarea_asyncio,crud_sqLite3,
        crud_postgres,Gestor_flatpak,
        generador_imagen_to_unicode,
        ])
            