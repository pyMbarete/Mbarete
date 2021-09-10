#!/usr/bin/env python
# -*- coding: utf-8 -*-
# archivo generado por Diseño Libre para Negocios

#Modulos importados
import os, math, threading

info={
    'autor':'Lucas Mathias Villalba Diaz',
    'name':'Negocios',
    'text':'Sistema inventario, stock y facturazion',
    'descripcionBreve':'Sisteam de control de intentario y stock, con facturazion',
    'descripcionLarga':'sistema paracontrol de inventario y stock con con contro de facturazion y corte d e caja',
    'img':'logo.png',
    'enlace':'mathiaslucasvidipy@gmail.com',
    'etiquetas':['default', 'inicio', 'inventario', 'sotck', 'facturazion']
}
widgets={
    'NegociosPanel':{
        'inputType':'panel',#OBLIGATORIO
        'etiquetas':['id','Inicio','default','panel','Negocios'],
        'name':'Negocios',#OBLIGATORIO
        'text':'Inicio Sistema inventario, stock y facturazion',#OBLIGATORIO
        'anchor':'o',
        'inputs':{
            'inicio':{
                'inputType':'Button',
                'command':'manager',
                'text':'Administrador'
            }
        }
    },
    'NegociosFrame':{
        'inputType':'Frame',#OBLIGATORIO
        'etiquetas':['id','Inicio','Frame','Negocios'],
        'name':'NegociosFrame',#OBLIGATORIO
        'text':'Frame Sistema inventario, stock y facturazion',#OBLIGATORIO
        'inputs':{
            'inicio':{
                'inputType':'Button',
                'command':'manager',
                'text':'Administrador'
            }
        }
    }
}
widgets={
    'nav':{
        'inputType':"panel",
        "etiquetas":['id','default','panel'],#AUTOMATICO/OBLIGATORIO
        "typeSalida":"command",#OPCIONAL
        "name":'menu',#OBLIGATORIO
        "text":'Menu',#OBLIGATORIO
        'anchor':'o', 
        'fontSize':15,
        'width':15,
        'bgColor':'#f00904',
        'degradado':0, 
        'inputs':{
            'inicio':{
                'inputType':'Button',
                'command':'inicio',
                'text':'Lista de Proyectos'
            },
            'nuevo':{
                'inputType':'Button',
                'command':'nuevo',
                'text':'Nuevo Proyecto'
            },
            'bbdd':{
                'inputType':'Button',
                'command':'bbdd',
                'text':'Base de Datos'
            },
            'formulario':{
                'inputType':'Button',
                'command':'formulario',
                'text':'Cargar Datos'
            },
            'salir':{
                'inputType':'Button',
                'command':'GUI_destroy',
                'text':'Destroy'
            },
            'buscar':{
                'inputType':'Entry',
                'text':'buscar:',
                'value':'Efectos Visuales'
            }
        }
    },
    'nuevo':{
        'inputType':"Frame",
        "etiquetas":['id','Nuevo','Frame','menu'],#AUTOMATICO/OBLIGATORIO
        "typeSalida":"command",#OPCIONAL
        "name":'nuevo',#OBLIGATORIO
        "text":'Nuevo Proyecto',#OBLIGATORIO
        'fontSize':12,
        'visible':0,
        'bgColor':'#080904',
        'degradado':0, 
        'inputs':{
            'autor':{
                'inputType':'Entry',
                'descripcion':'',
                'text':'Autor:',
                'value':'Lucas Mathias Villalba Diaz'
            },
            'name':{
                'inputType':'Entry',
                'descripcion':'',
                'text':'Nombre CamelCase:',
                'value':'BorrarAhora'
            },
            'text':{
                'inputType':'Entry',
                'descripcion':'',
                'text':'Nombre normal:',
                'value':'Borrar'
            },
            'descripcionBreve':{
                'inputType':'Entry',
                'descripcion':'',
                'text':'Descripcion breve:',
                'value':''
            },
            'descripcionLarga':{
                'inputType':'Entry',
                'descripcion':'',
                'text':'Descripcion larga:',
                'value':''
            },
            'img':{
                'inputType':'Entry',
                'descripcion':'',
                'text':'Imagen del proyecto:',
                'value':'logo.png'
            },
            'enlace':{
                'inputType':'Entry',
                'descripcion':'',
                'text':'Enlace o link para Contacto:',
                'value':'mathiaslucasvidipy@gmail.com'
            },
            'etiquetas':{
                'inputType':'Entry',
                'descripcion':'practicas Matplotlib,graficos',
                'text':'Etiquetas para este proyecto, separadas por comas (,):',
                'value':'default,inicio'
            },
            'media':{
                'inputType':'Checkbutton',
                'text':'Crear Carpeta [ media ]',
                'value':1.0
            },
            'dirmedia':{
                'inputType':'Entry',
                'descripcion':'carpeta 1,carpeeta 2, etc...',
                'text':'Nombre para las carpetas dentro de la carpeta [ media ], separadas por comas (,):',
                'value':'img,js,css,txt,audio'
            },
            'biblio':{
                'inputType':'Checkbutton',
                'text':'Crear Carpeta [ bibliografia ]',
                'value':1.0
            },
            'dirbiblio':{
                'inputType':'Entry',
                'descripcion':'carpeta 1,carpeeta 2, etc...',
                'text':'Nombre para las carpetas en la carpeta [ bibliografia ], separadas por comas (,):',
                'value':'pdf,img,audio,webSites,txt'
            },
            'backup':{
                'inputType':'Checkbutton',
                'text':'Crear Carpeta [ Copias_de_Seguridad ]',
                'value':1.0
            },
            'dirbackup':{
                'inputType':'Entry',
                'descripcion':'carpeta 1,carpeta 2, etc...',
                'text':'Nombre para las carpetas en la carpeta [ Copias_de_Seguridad ], separadas por comas (,):',
                'value':'Tablas,Sql,txt'
            },
            'panelUbicacion':{
                    'inputType':"Radiobutton",
                    "text":'Ubicacion del Panel de Inicio',#OBLIGATORIO
                    'radios':{
                        'n':{'text':'Superior'},
                        's':{'text':'Inferior'},
                        'e':{'text':'Derecha'},
                        'o':{'text':'Izquierda'}
                        }
            },
            'frame':{
                'inputType':'Checkbutton',
                'text':'Crear un widget Frame por default',
                'value':1.0
            },
            'os':{'inputType':'Checkbutton','text':'import os','value':0.0},
            'sys':{'inputType':'Checkbutton','text':'import sys','value':0.0},
            'math':{'inputType':'Checkbutton','text':'import math','value':0.0},
            'time':{'inputType':'Checkbutton','text':'import time','value':0.0},
            'datetime':{'inputType':'Checkbutton','text':'import datetime','value':0.0},
            'threading':{'inputType':'Checkbutton','text':'import threading','value':0.0},
            'sqlite':{'inputType':'Checkbutton','text':'import sqlite3','value':0.0},
            'PIL':{'inputType':'Checkbutton','text':'from PIL import Image, ImageTk','value':0.0},
            'crear':{
                'inputType':'Button',
                'command':'crear',
                'text':'Crear Proyecto'
            },
            'borrar':{
                'inputType':'Button',
                'command':'borrar',
                'text':'Borrar Todo'
            },
            'cancelar':{
                'inputType':'Button',
                'command':'cancelar',
                'text':'Cancelar'
            }
        }
    },
    'bbdd':{
        'inputType':"Frame",
        "etiquetas":['id','bbdd','Frame','menu'],#AUTOMATICO/OBLIGATORIO
        "typeSalida":"command",#OPCIONAL
        "name":'bbdd',#OBLIGATORIO
        "text":'Base de Datos',#OBLIGATORIO
        'width':25,
        'fontSize':10,
        'bgColor':'#080904', 
        'inputs':{
            'filesql':{
                'inputType':'Entry',
                'descripcion':'FICHERO.sql',
                'text':'Fichero Sqlite3:',
                'value':''
            },
            'filepy':{
                'inputType':'Entry',
                'descripcion':'FICHERO.py',
                'text':'Script Python:',
                'value':''
            },
            'filecsv':{
                'inputType':'Entry',
                'descripcion':'FICHERO.csv',
                'text':'Fichero CSV:',
                'value':''
            },
            'crearPY':{
                'inputType':'Button',
                'command':'exportarPython',
                'text':'Exportar a Script.py'
            },
            'crearCSV':{
                'inputType':'Button',
                'command':'exportarCSV',
                'text':'Exportar a CSV'
            }
        }
    },
    'formulario':{
        'inputType':"Frame",
        "etiquetas":['id','formulario','Frame','menu'],#AUTOMATICO/OBLIGATORIO
        "typeSalida":"command",#OPCIONAL
        "name":'formulario',#OBLIGATORIO
        "text":'Cargar Datos',#OBLIGATORIO
        'width':25,
        'fontSize':10,
        'crearTabla':1,
        'bgColor':'#080904',
        'degradado':0, 
        'inputs':{
            'nombres':{
                'inputType':'Entry',
                'descripcion':'Nombres',
                'text':'Nombre:',
                'value':''
            },
            'apellidos':{
                'inputType':'Entry',
                'descripcion':'Apellidos',
                'text':'Apellidos:',
                'value':''
            },
            'direccion':{
                'inputType':'Entry',
                'descripcion':'Donde vives?',
                'text':'Direccion Actual:',
                'value':''
            }
        }
    },
    'subProyectos':{
        'inputType':"Frame",
        "etiquetas":['id','Inicio','Frame'],#AUTOMATICO/OBLIGATORIO
        "typeSalida":"command",#OPCIONAL
        "name":'inicio',#OBLIGATORIO
        "text":'Lista de Los Sub Proyectos',#OBLIGATORIO
        'fontSize':15,
        'visible':0,
        'bgColor':'#f00904',
        'degradado':0, 
        'inputs':{}
    }
}
def crearSubProyecto(admin,G,info,nuevo):

def cancelar(admin,G,info):
    G.setVar(info['widget']['nuevo'])
    admin.subtransicion(G,info['subProyecto'],'inicio')
def bbdd(admin,G,info):
    G.setVar(info['widget']['bbdd'],{
        'filesql':admin.ficheroCRUD,
        'filepy':admin.ficheroCRUD[:-len(G.Sql.extencionCRUD)]+'.py',
        'filecsv':admin.ficheroCRUD[:-len(G.Sql.extencionCRUD)]+'.csv'
    })
    admin.subtransicion(G,info['subProyecto'],'bbdd')
def command(admin,G,info,ec,geo):
    print(info['subProyecto'])
    print('Info:',info['info'])
    print('Widgest:',info['widget'])
    print('Comandos',info['command']) 
    G.command['transicion_'+info['subProyecto']]=lambda : admin.transicion(G,info['subProyecto'])
    G.command[info['command']['inicio']]=lambda : admin.subtransicion(G,info['subProyecto'],'Inicio')
    G.command[info['command']['nuevo']]=lambda : admin.subtransicion(G,info['subProyecto'],'Nuevo')
    G.command[info['command']['formulario']]=lambda : admin.subtransicion(G,info['subProyecto'],'formulario')
    G.command[info['command']['bbdd']]=lambda : bbdd(admin,G,info)
    G.command[info['command']['crear']]=lambda : crearSubProyecto(admin,G,info,G.widgets[info['widget']['nuevo']]['value'])
    G.command[info['command']['borrar']]=lambda : G.setVar(info['widget']['nuevo'])
    G.command[info['command']['cancelar']]=lambda : cancelar(admin,G,info)
    G.command[info['command']['exportarPython']]=lambda : G.Sql.exportarTablas(tabla=[],formato="py",campoClave="",file="")
    G.command[info['command']['exportarCSV']]=lambda : G.Sql.exportarTablas(tabla=[],formato="csv",campoClave="",file="")
    



def ejecutar(admin,G,info,ec,geo):

    #G.command['menuAspas']=lambda : menu('aspas') 
    #G.command['principal']=lambda : menu('principal') 
    
    
    print(info)
def command(admin,G,info,ec,geo):
    print(info['subProyecto'])
    print('Info:',info['info'])
    print('Widgest:',info['widget'])
    print('Comandos',info['command']) 
    G.command[info['command']['manager']]=lambda : admin.transicion(G,admin.manager)
