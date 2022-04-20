#!/usr/bin/env python
# -*- coding: utf-8 -*-
# archivo generado por Diseño Libre para microservicio

#Modulos importados
import threading

info={
    'autor':'Lucas Mathias Villalba Diaz',
    'name':'microservicio',
    'text':'Servidor HTTP Python',
    'descripcionBreve':'servidor http para  hacer correr como una API rest Full en red, para nuestros proyectos Mbarete',
    'descripcionLarga':'Servidor HTTP montado con Socket y threading , falta la integracion para que funcione de forma automatica dentro de nuestros proyectos mbarete, cargar logica del proyecto en el servidor y luego generar los response desde la clase mbarete del modulo mbarete',
    'img':'logo.png',
    'enlace':'mathiaslucasvidipy@gmail.com',
    'etiquetas':['default', 'inicio', 'servidor', 'http', 'socket', 'APIrest Full', 'html', 'css', 'javascript', 'typescript', 'BBDD']
}
widgets={
    'microservicioPanel':{
        'inputType':'panel',#OBLIGATORIO
        'etiquetas':['id','Inicio','default','panel','microservicio'],
        'name':'microservicio',#OBLIGATORIO
        'text':'Inicio Servidor HTTP Python',#OBLIGATORIO
        'anchor':'e',
        'inputs':{
            'inicio':{
                'inputType':'Button',
                'command':'manager',
                'text':'Administrador'
            }
        }
    },
    'microservicioFrame':{
        'inputType':'Frame',#OBLIGATORIO
        'etiquetas':['id','Inicio','Frame','microservicio'],
        'name':'microservicioFrame',#OBLIGATORIO
        'text':'Frame Servidor HTTP Python',#OBLIGATORIO
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
