#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys

"""
    Ver versión de Linux con /etc/os-release
    El archivo /etc/os-release contiene datos de identificación del sistema operativo activo. 
    El formato de este archivo básico os-release es una lista separada por líneas nuevas de 
    asignaciones de variables compatibles a un entorno y alli podemos obtener la configuración 
    de los scripts de Shell. 
    El archivo os-release contiene datos definidos por el proveedor del sistema operativo y 
    como tal no deben ser modificados por el administrador ya que pueden afectar otros 
    servicios adicionales de la propia distribución.

"""

def buscador():
    import os,shutil
    #for root, dirs, files in os.walk('../'): print(root,dirs,files)
    muestra=['123.jpg','132_456.jpg','4566_444_.jpg','1_1235_.jpg','123456_456123_465.jpg','789789_789789_789789.jpg']
    search=['132.jpg','465.jpg','456.jpg','789.jpg']
    #find for root, dirs, files in os.walk('../'):
    for f in muestra:
        i=f.replace(".jpg","").split("_")
        i=next((f for e in search if e.replace(".jpg","") in i),None)
        print(i)


if 'main' in __name__:
    from modulos.pruebas import main_pruebas,consola
    pruebas=[
        {'titulo':"Lista Variable de entorno del sistema",'f':buscarVariableDeEntorno},
        {'titulo':"programando en shell secuencial para GIT_PUSH",'f':git_push},
        {'titulo':"programando en shell un bucle loop para GIT_PULL",'f':git_pull},
        {'titulo':"mostrar valores de start('nombre_de_archivo'):",'f':lambda: print(consola.start(name='nombre_de_archivo'))},
        {'titulo':"buscar",'f':buscador},
        {'titulo':"git_crear_branch de este repo",'f':git_crear_branch}
        ]
    main_pruebas(pruebas,sys.argv)