
"""
Nota
Por razones de eficiencia, cada módulo es importado solo una vez 
por sesión del intérprete. Por lo tanto, si cambias tus módulos, 
debes reiniciar el interprete – ó, si es un solo módulo que quieres 
probar de forma interactiva, usa importlib.reload(), 
por ejemplo: 
	import importlib
	importlib.reload(modulename). 
"""



"""
Archivos «compilados» de Python
Para acelerar la carga de módulos, Python cachea las versiones 
compiladas de cada módulo en el directorio __pycache__ bajo el 
nombre module.version.pyc, dónde la versión codifica el formato 
del archivo compilado; generalmente contiene el número de versión 
de Python. Por ejemplo, en CPython release 3.3 la versión compilada 
de spam.py sería cacheada como __pycache__/spam.cpython-33.pyc. 
Este convención de nombre permite compilar módulos desde diferentes 
releases y versiones de Python para coexistir.
Python chequea la fecha de modificación de la fuente contra la 
versión compilada para ver si esta es obsoleta y necesita ser 
recompilada. Esto es un proceso completamente automático. También, 
los módulos compilados son independientes de la plataforma, así 
que la misma biblioteca puede ser compartida a través de sistemas 
con diferentes arquitecturas.
Python no chequea el caché en dos circunstancias. Primero, siempre 
recompila y no graba el resultado del módulo que es cargado 
directamente desde la línea de comando. Segundo, no chequea el caché 
si no hay módulo fuente. Para soportar una distribución sin fuente 
(solo compilada), el módulo compilado debe estar en el directorio 
origen, y no debe haber un módulo fuente.
Algunos consejos para expertos:
    Puedes usar los modificadores -O o -OO en el comando de Python para reducir el tamaño del módulo compilado. El modificador -O remueve las declaraciones assert, el modificador -OO remueve declaraciones assert y cadenas __doc__. Dado que algunos programas pueden confiar en tenerlos disponibles, solo deberías usar esta opción si conoces lo que estás haciendo. Los módulos «optimizados» tienen una etiqueta opt- y generalmente son mas pequeños. Releases futuras pueden cambiar los efectos de la optimización.
    Un programa no se ejecuta mas rápido cuando es leído de un archivo .pyc que cuando es leído de un archivo .py; la única cosa que es mas rápida en los archivos .pyc es la velocidad con la cual son cargados.
    El módulo compileall puede crear archivos .pyc para todos los módulos en un directorio.
    Hay mas detalle de este proceso, incluyendo un diagrama de flujo de decisiones, en PEP 3147.
"""




""" Módulos estándar
Python viene con una biblioteca de módulos estándar, descrita en un 
documento separado, la Referencia de la Biblioteca de Python 
(de aquí en más, «Referencia de la Biblioteca»). 
Algunos módulos se integran en el intérprete; estos proveen acceso a 
operaciones que no son parte del núcleo del lenguaje pero que sin 
embargo están integrados, tanto por eficiencia como para proveer 
acceso a primitivas del sistema operativo, como llamadas al sistema. 

Un módulo en particular merece algo de atención: sys, el que está integrado en todos los intérpretes de Python.

La variable sys.path es una lista de cadenas que determinan el 
camino de búsqueda del intérprete para los módulos. Se inicializa 
por omisión a un camino tomado de la variable de entorno PYTHONPATH, 
o a un valor predefinido en el intérprete si PYTHONPATH no está 
configurada. Lo puedes modificar usando las operaciones estándar de listas:

>>> import sys
>>> sys.path.append('/ufs/guido/lib/python')

"""



"""La función dir()
La función integrada dir() se usa para encontrar qué nombres define un módulo. Retorna una lista ordenada de cadenas:
Sin argumentos, dir() lista los nombres que tienes actualmente definidos:
Note que lista todos los tipos de nombres: variables, módulos, funciones, etc.

dir() no lista los nombres de las funciones y variables integradas. 
Si quieres una lista de esos, están definidos en el módulo estándar builtins:
>>> import builtins
>>> dir(builtins)  

"""

"""
Paquetes

Los Paquetes son una forma de estructurar el espacio de nombres de módulos de 
Python usando «nombres de módulo con puntos». Por ejemplo, el nombre del 
módulo A.B designa un submódulo B en un paquete llamado A. Así como el uso de 
módulos salva a los autores de diferentes módulos de tener que preocuparse por 
los nombres de las variables globales de cada uno, el uso de nombres de módulo 
con puntos salva a los autores de paquetes con múltiples módulos, como NumPy o 
Pillow de preocupaciones por los nombres de los módulos de cada uno.

Supongamos que quieres designar una colección de módulos (un «paquete») para 
el manejo uniforme de archivos y datos de sonidos. Hay diferentes formatos 
de archivos de sonido (normalmente reconocidos por su extensión, por ejemplo: 
.wav, .aiff, .au), por lo que tienes que crear y mantener una colección siempre 
creciente de módulos para la conversión entre los distintos formatos de archivos. 
Hay muchas operaciones diferentes que quizás quieras ejecutar en los datos de 
sonido (como mezclarlos, añadir eco, aplicar una función ecualizadora, crear 
un efecto estéreo artificial), por lo que además estarás escribiendo una lista 
sin fin de módulos para realizar estas operaciones. Aquí hay una posible estructura 
para tu paquete (expresados en términos de un sistema jerárquico de archivos):

sound/                          Top-level package
      __init__.py               Initialize the sound package
      formats/                  Subpackage for file format conversions
              __init__.py
              wavread.py
              wavwrite.py
              aiffread.py
              aiffwrite.py
              auread.py
              auwrite.py
              ...
      effects/                  Subpackage for sound effects
              __init__.py
              echo.py
              surround.py
              reverse.py
              ...
      filters/                  Subpackage for filters
              __init__.py
              equalizer.py
              vocoder.py
              karaoke.py
              ...


"""









"""
Ejecutando módulos como scripts
Cuando ejecutes un módulo de Python con
>>> python fibo.py <arguments>

el código en el módulo será ejecutado, tal como si lo hubieses importado, 
pero con __name__ con el valor de "__main__". 
Eso significa que agregando este código al final de tu módulo:
if __name__ == "__main__":
    import sys
    print(sys.argv[1])

Puedes hacer que el archivo sea utilizable tanto como script, 
como módulo importable, porque el código que analiza la línea 
de órdenes sólo se ejecuta si el módulo es ejecutado como archivo principal

"""
if __name__ == "__main__":
    from ..setup import main_funcion
    fib(int(sys.argv[1]))
    main_funcion()
