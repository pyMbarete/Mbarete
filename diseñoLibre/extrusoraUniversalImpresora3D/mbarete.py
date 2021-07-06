#!/usr/bin/env python
# -*- coding: utf-8 -*-
# archivo generado por Diseño Libre para extrusoraUniversalImpresora3D

#Modulos importados
import os, sys, math

info={
    'autor':'Lucas Mathias Villalba Diaz',
    'name':'extrusoraUniversalImpresora3D',
    'text':'Extrusora Impresion 3D',
    'descripcionBreve':'Resiclado,PET,Extrusora,Impresion 3D,reciclado de plasticos',
    'descripcionLarga':'Una extrusora universal puede usar plasticos reciclados de distintos tipos, para imprimir objetos con una impresora 3d que usaria estos plasticos como filamento',
    'img':'logo.png',
    'enlace':'mathiaslucasvidipy@gmail.com',
    'etiquetas':['default', 'inicio']
}
widgets={
    'extrusoraUniversalImpresora3DPanel':{
        'inputType':'panel',#OBLIGATORIO
        'etiquetas':['id','default','panel','extrusoraUniversalImpresora3D'],
        'name':'extrusoraUniversalImpresora3D',#OBLIGATORIO
        'text':'Inicio Extrusora Impresion 3D',#OBLIGATORIO
        'anchor':'o',
        'inputs':{
            'inicio':{
                'inputType':'Button',
                'command':'manager',
                'text':'Administrador'
            }
        }
    },
    'extrusoraUniversalImpresora3DFrame':{
        'inputType':'Frame',#OBLIGATORIO
        'etiquetas':['id','Inicio','Frame','extrusoraUniversalImpresora3D'],
        'name':'extrusoraUniversalImpresora3DFrame',#OBLIGATORIO
        'text':'Frame Extrusora Impresion 3D',#OBLIGATORIO
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
    G.command[info['command'][admin.manager]]=lambda : admin.transicion(G,admin.manager)
