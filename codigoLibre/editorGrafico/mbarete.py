#!/usr/bin/env python
# -*- coding: latin-1 -*-
# archivo generado por Diseño Libre para DiseñadorDeEtiquetas

#Modulos importados
import os, math, sqlite3
from PIL import Image, ImageTk

info={
    'autor':'Lucas Mathias Villalba Diaz',
    'name':'DiseñadorGrafico',
    'text':'Diseñador de Imagenes y Etiquetas',
    'descripcionBreve':'Diseñador de IMAGENES',
    'descripcionLarga':'Diseñador graficos para imagenes y etiquetas, generados a partir de un archivo externo CSV',
    'img':'logo.png',
    'enlace':'mathiaslucasvidipy@gmail.com',
    'etiquetas':['default', 'inicio', 'graficos', 'PNG', 'GENERADOR', 'IMAGENES']
}
widgets={
    'DiseñadorDeEtiquetasPanel':{
        'inputType':'panel',#OBLIGATORIO
        'etiquetas':['id','Inicio','default','panel','DiseñadorDeEtiquetas'],
        'name':'DiseñadorGrafico',#OBLIGATORIO
        'text':'Inicio Diseñador Grafico',#OBLIGATORIO
        'anchor':'o',
        'inputs':{
            'inicio':{
                'inputType':'Button',
                'command':'manager',
                'text':'Administrador'
            }
        }
    },
    'DiseñadorDeEtiquetasFrame':{
        'inputType':'Frame',#OBLIGATORIO
        'etiquetas':['id','Inicio','Frame','DiseñadorDeEtiquetas'],
        'name':'DiseñadorDeEtiquetasFrame',#OBLIGATORIO
        'text':'Frame Diseñador de Etiquetas',#OBLIGATORIO
        'inputs':{
            'inicio':{
                'inputType':'Button',
                'command':'manager',
                'text':'Administrador'
            }
        }
    }
}

def command(admin,G,info,ec,geo):
    print(info['subProyecto'])
    print('Info:',info['info'])
    print('Widgest:',info['widget'])
    print('Comandos',info['command']) 
    G.command[info['command']['manager']]=lambda : admin.transicion(G,admin.manager)
