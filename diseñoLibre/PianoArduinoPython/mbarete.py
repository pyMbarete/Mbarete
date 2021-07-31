#!/usr/bin/env python
# -*- coding: utf-8 -*-
# archivo generado por Diseño Libre para PianoArduinoPython

#Modulos importados
import time, threading

info={
    'autor':'Lucas Mathias Villalba Diaz',
    'name':'PianoArduinoPython',
    'text':'Piano Sampler',
    'descripcionBreve':'Sampler con el hardware de un piano reciclado, la electronica esta hecvja en arduino, y la ejecucion de los sampler esta acargo de python con PyAudio y portAudio ',
    'descripcionLarga':'PyAudio requiere de portAudio y portAuido es un binario hecho en GNU, para poder instalar en windows debe ser compilado en un interprete de GNU (MinGW), luego de eso se podra instalar PyAudio en si interprete de python con pip y listo',
    'img':'logo.png',
    'enlace':'mathiaslucasvidipy@gmail.com',
    'etiquetas':['default', 'inicio', 'piano', 'arduino', 'musica', 'wav', 'audio']
}
widgets={
    'PianoArduinoPythonPanel':{
        'inputType':'panel',#OBLIGATORIO
        'etiquetas':['id','Inicio','default','panel','PianoArduinoPython'],
        'name':'PianoArduinoPython',#OBLIGATORIO
        'text':'Inicio Piano Sampler',#OBLIGATORIO
        'anchor':'o',
        'inputs':{
            'inicio':{
                'inputType':'Button',
                'command':'manager',
                'text':'Administrador'
            }
        }
    },
    'PianoArduinoPythonFrame':{
        'inputType':'Frame',#OBLIGATORIO
        'etiquetas':['id','Inicio','Frame','PianoArduinoPython'],
        'name':'PianoArduinoPythonFrame',#OBLIGATORIO
        'text':'Frame Piano Sampler',#OBLIGATORIO
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
