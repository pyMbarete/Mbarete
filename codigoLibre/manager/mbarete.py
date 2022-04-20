import math
import os
#Sub-proyecto Mbarete. Este proyecto esta para administrar los demas Sub-proyectos  
info={
    'autor':'Lucas Mathias Villalba Diaz',
    'name':'manager',
    'text':'Administrador',
    'descripcionBreve':'Sub-Proyecto para administrar el Proyecto General',
    'descripcionLarga':'Sub-proyecto por defecto del proyecto Mbarete, es como el administrador general por defecto, listo para ser usado en otros proyectos Mbarete',
    'img':'\\media\\img\\logo-Mbarete.jpg',
    'enlace':'',
    'etiquetas':['mbarete','admin','por defecto','automatico']
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
    if not nuevo['name'] in admin.ubi.directorio['SubCarpetas']:
        sep=os.path.sep
        os.mkdir(admin.ubi.pwd+sep+nuevo['name'])
        if nuevo['media']:
            os.mkdir(admin.ubi.pwd+sep+nuevo['name']+sep+'media')
            for carpeta in nuevo['dirmedia'].split(','): 
                os.mkdir(admin.ubi.pwd+sep+nuevo['name']+sep+'media'+sep+carpeta)
        if nuevo['biblio']:
            os.mkdir(admin.ubi.pwd+sep+nuevo['name']+sep+'bibliografia')
            for carpeta in nuevo['dirbiblio'].split(','): 
                os.mkdir(admin.ubi.pwd+sep+nuevo['name']+sep+'bibliografia'+sep+carpeta)
        if nuevo['backup']:
            os.mkdir(admin.ubi.pwd+sep+nuevo['name']+sep+'Copias_de_Seguridad')
            for carpeta in nuevo['dirbackup'].split(','): 
                os.mkdir(admin.ubi.pwd+sep+nuevo['name']+sep+'Copias_de_Seguridad'+sep+carpeta)
        i=open(admin.ubi.pwd+sep+nuevo['name']+sep+'__init__.py','w')
        i.write(r'# archivo generado por '+admin.nombre+'\n')
        i.close()
        myFile=open(admin.ubi.pwd+sep+nuevo['name']+sep+admin.cargarScript,'w')
        myFile.write(r'#!/usr/bin/env python'+'\n')
        myFile.write(r'# -*- coding: utf-8 -*-'+'\n')
        myFile.write(r'# archivo generado por '+admin.nombre+' para '+nuevo['name']+'\n'+'\n')
        myFile.write(r'#Modulos importados'+'\n')
        if nuevo['os'] or nuevo['sys'] or nuevo['math'] or nuevo['time'] or nuevo['datetime'] or nuevo['threading'] or nuevo['sqlite']:
            imports= "import"
            imports += " os," if nuevo['os'] else ''
            imports += " sys," if nuevo['sys'] else ''
            imports += " math," if nuevo['math'] else ''
            imports += " time," if nuevo['time'] else ''
            imports += " datetime," if nuevo['datetime'] else ''
            imports += " threading," if nuevo['threading'] else ''
            imports += " sqlite3," if nuevo['sqlite'] else ''
            imports=imports[:-1]
            myFile.write(imports+'\n')
        if nuevo['PIL']:
            myFile.write("from PIL import Image, ImageTk"+'\n')

        myFile.write('\n')
        myFile.write("info={"+'\n')
        myFile.write("    'autor':'"+nuevo['autor']+"',"+'\n')
        myFile.write("    'name':'"+nuevo['name']+"',"+'\n')
        myFile.write("    'text':'"+nuevo['text']+"',"+'\n')
        myFile.write("    'descripcionBreve':'"+nuevo['descripcionBreve']+"',"+'\n')
        myFile.write("    'descripcionLarga':'"+nuevo['descripcionLarga']+"',"+'\n')
        myFile.write("    'img':'"+nuevo['img']+"',"+'\n')
        myFile.write("    'enlace':'"+nuevo['enlace']+"',"+'\n')
        myFile.write("    'etiquetas':"+str(nuevo['etiquetas'].split(','))+'\n')
        myFile.write("}"+'\n')
        myFile.write("widgets={"+'\n')
        myFile.write("    '"+nuevo['name']+"Panel':{"+'\n')
        myFile.write("        'inputType':'panel',#OBLIGATORIO"+'\n')
        myFile.write("        'etiquetas':['id','"+admin.subtransicionInicio+"','default','panel','"+nuevo['name']+"'],"+'\n')
        myFile.write("        'name':'"+nuevo['name']+"',#OBLIGATORIO"+'\n')
        myFile.write("        'text':'Inicio "+nuevo['text']+"',#OBLIGATORIO"+'\n')
        if nuevo['panelUbicacion']:
            myFile.write("        'anchor':'"+nuevo['panelUbicacion']+"',"+'\n')
        myFile.write("        'inputs':{"+'\n')
        myFile.write("            'inicio':{"+'\n')
        myFile.write("                'inputType':'Button',"+'\n')
        myFile.write("                'command':'"+admin.manager+"',"+'\n')
        myFile.write("                'text':'"+admin.info[admin.manager]['info']['text']+"'"+'\n')
        myFile.write("            }"+'\n')
        myFile.write("        }"+'\n')
        if nuevo['frame']:
            myFile.write("    },"+'\n')
            myFile.write("    '"+nuevo['name']+"Frame':{"+'\n')
            myFile.write("        'inputType':'Frame',#OBLIGATORIO"+'\n')
            myFile.write("        'etiquetas':['id','"+admin.subtransicionInicio+"','Frame','"+nuevo['name']+"'],"+'\n')
            myFile.write("        'name':'"+nuevo['name']+"Frame',#OBLIGATORIO"+'\n')
            myFile.write("        'text':'Frame "+nuevo['text']+"',#OBLIGATORIO"+'\n')
            myFile.write("        'inputs':{"+'\n')
            myFile.write("            'inicio':{"+'\n')
            myFile.write("                'inputType':'Button',"+'\n')
            myFile.write("                'command':'"+admin.manager+"',"+'\n')
            myFile.write("                'text':'"+admin.info[admin.manager]['info']['text']+"'"+'\n')
            myFile.write("            }"+'\n')
            myFile.write("        }"+'\n')
            
        myFile.write("    }"+'\n')
        myFile.write("}"+'\n')
        myFile.write("def command(admin,G,info,ec,geo):"+'\n')
        myFile.write("    print(info['subProyecto'])"+'\n')
        myFile.write("    print('Info:',info['info'])"+'\n')
        myFile.write("    print('Widgest:',info['widget'])"+'\n')
        myFile.write("    print('Comandos',info['command']) "+'\n')
        myFile.write("    G.command[info['command']['manager']]=lambda : admin.transicion(G,admin.manager)"+'\n')
        myFile.close()
        print("Fue Creado Exitosamente el Proyecto:",nuevo['text'])
        G.setVar(info['widget']['nuevo'])
    else:
        print(nuevo['name'],' ya existe')


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
