#!/usr/bin/env python
# -*- coding: utf-8 -*-
# archivo generado por Diseño Libre para proyectoLinuxControlMental

#Modulos importados
import os, threading, sqlite3

info={
    'autor':'Lucas Mathias Villalba Diaz',
    'name':'proyectoLinuxControlMental',
    'text':'ControlRemoto',
    'descripcionBreve':'Manipularla Maquina desde otros dispositivos sin Programas Adicionales',
    'descripcionLarga':'servicio para manipular los perifericos de esta maquina desde otras maquinas por medio del servidor integrado',
    'img':'logo.png',
    'enlace':'mathiaslucasvidipy@gmail.com',
    'etiquetas':['default', 'inicio', 'Remoto', 'mouse', 'teclado', 'audio', 'video']
}
widgets={
    'proyectoLinuxControlMentalPanel':{
        'inputType':'panel',#OBLIGATORIO
        'etiquetas':['id','Inicio','default','panel','proyectoLinuxControlMental'],
        'name':'proyectoLinuxControlMental',#OBLIGATORIO
        'text':'Inicio ControlRemoto',#OBLIGATORIO
        'anchor':'0',
        'inputs':{
            'inicio':{
                'inputType':'Button',
                'command':'manager',
                'text':'Administrador'
            }
        }
    },
    'proyectoLinuxControlMentalFrame':{
        'inputType':'Frame',#OBLIGATORIO
        'etiquetas':['id','Inicio','Frame','proyectoLinuxControlMental'],
        'name':'proyectoLinuxControlMentalFrame',#OBLIGATORIO
        'text':'Frame ControlRemoto',#OBLIGATORIO
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
