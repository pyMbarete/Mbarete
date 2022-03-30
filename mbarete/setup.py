#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys
import csv
import time
import datetime
import math
#from mbarete.mbarete import geometria as g
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
class consola(object):
    """docstring for programador_consola"""
    def __init__(self, name='',fuente=['mbarete','consolas'],code='latin-1'):
        super(programador_consola, self).__init__()
        self.name=name
        self.fuente=fuente
        self.code=code
        self.o=self.start()
        self.s = self.o['start']

    def start(self,name='',fuente=[]):
        if not name: name=self.name
        if not fuente: fuente=self.fuente
        import os
        if 'WINDIR' in os.environ:
            o={'OS':'windows','V':os.environ['OS']}
            o['name']=name+'.auto.cmd'
            o['cross']=r'%cross% '
            o['f']=''
            for d in fuente: o['f']+=d+'\\'
            o['start']=[
                '@ECHO off',
                'setlocal',
                'set "fuente='+o['f']+'"',
                r'set "cross=call %fuente%cmd_principal.cmd command"',
                r'call %fuente%cmd_principal.cmd inicio %fuente%'
                ]
            o['end']=['endlocal']
            o['to_var']=lambda v: r'%'+v+r'%'
            o['if_eq']=lambda a,b: 'IF "%'+str(a)+'%" == "'+str(b)+'" ('
            o['fi']=')'
            o['read']=lambda a: 'SET /p '+str(a)+'=Ingrese una Opcion:'
        elif 'SHELL' in os.environ:
            if os.environ['SHELL'].strip()=='/bin/bash':
                o={'OS':'linux','V':'debian'}
                o['name']=name+'.auto.sh'
                o['cross']=r'cross '
                o['f']='./'
                for d in fuente: o['f']+=d+'/'
                o['start']=[
                    '#!/bin/bash',
                    'fuente='+o['f'],
                    'source "$fuente"bash_principal.sh'
                ]
                o['end']=['']
                o['to_var']=lambda v: r'$'+v
                o['if_eq']=lambda a,b: 'if [ "$'+str(a)+'" == "'+str(b)+'" ];then'
                o['fi']='fi'
                o['read']=lambda a: 'read -p "Ingrese una Opcion:" '+str(a)
            else:
                o={'OS':os.environ['SHELL'],'V':os.environ['SHELL']}
        elif 'ANDROID_ROOT' in os.environ:
            o={'OS':'android','V':os.environ['SHELL']}
        o['info']={v.split(':')[0]:v[len(v.split(':')[0])+1:] for v in self.getFile(o['f']+'info')}
        o['loop_num']=1
        o['for_num']=1
        o['while_num']=1
        return o

    def estructura_secuencial(self,c):
        if str == c.__class__: c=[c]
        #(script,commands,OS)
        for i in range(len(c)):
            for v in self.o['info']: c[i]=c[i].replace('$'+v[6:],self.o['to_var'](v))
            c[i]=self.o['cross']+'"'+c[i].strip().replace(';;','; ;').replace(';;','; ;').replace('"',"'")+' "'
        self.s+=c

    def estructura_loop(self,menu):
        l='loop_'+str(self.o['loop_num'])
        vl='var_'+l
        self.o['loop_num']+=1
        if self.o['OS'] == 'windows':
            self.s+=[':'+l]
        if self.o['OS'] == 'linux':
            self.s+=[l+'=true']
            self.s+=['while [ $'+l+' == true ] ;do']

        if 'inicio' in menu: self.set(menu['inicio'])
        self.s+=['echo '+menu['cabezera']]
        for op in range(1,1+len(menu['lista'])): self.s+=['echo '+str(op)+'.'+menu['lista'][op-1]['opcion']]
        self.s+=['echo "  <<< ENTER PARA SALIR >>>"']
        self.s+=[self.o['read'](vl)]
        if self.o['OS'] == 'windows': self.s+=['if "%'+vl+'%"=="" (goto :eof)']
        if self.o['OS'] == 'linux': self.s+=['if [ -z $'+vl+' ];then '+l+'=false ;fi']
        for op in range(1,1+len(menu['lista'])):
            self.s+=[self.o['if_eq'](vl,op)]
            self.set(menu['lista'][op-1]['commands'])
            self.s+=[self.o['fi']]
        if self.o['OS'] == 'windows': self.s+=['goto :'+l]
        if self.o['OS'] == 'linux': self.s+=['done']
        

    def getFile(name,full=1,code=''):
        if not code: code=self.code
        file=open(name,'rb')
        ret=[]
        for line in file:
            line=line.decode(code).strip()
            if line!='':
                ret += [line if full else line.strip()]
        file.close()
        return ret if len(ret)>1 else ret[0]
    def setFile(self,name,valor=[],echo=1,code=''):
        if not code: code=self.code
        if echo:
            print('Archivo:',name)
        file=open(name,"wb")
        if list == valor.__class__:
            for line in valor:
                if echo: print(line.encode(code))
                file.write(line.encode(code)+b'\n')    
        else:
            file.write(valor+b'\n')
        file.close()
    def set(self,c):
        if dict == c.__class__:
            if ('inicio' in c) and ('cabezera' in c) and ('lista' in c):
                self.estructura_loop(c)
        else:
            self.estructura_secuencial(c)
    def save(self):
        self.setFile(self.o['name'],self.s+self.o['end'],echo=0)

def crearInfo(search=[]):
    import os,sys,platform
    #
    dir(os)
    variables_de_entorno={env:os.environ[env] for env in os.environ}
    print("Search:",True if search else False)
    for variable in variables_de_entorno:
        if search:
            v=next((variable for s in search if s.lower() in variable.lower()),None)
            if v:
                print("%s: %s" % (v, variables_de_entorno[v]))
        else:
            print("%s: %s" % (variable, variables_de_entorno[variable]))
    o={}
    print('os.name:', os.name )
    if os.name == 'nt':
        o['sysname'] ,o['nodename'] ,o['release'] ,o['version'] ,o['machine'] ,o['processor'] = platform.uname()
        
    if os.name == 'posix':
        o['sysname'] ,o['nodename'] ,o['release'] ,o['version'] ,o['machine'] = os.uname()
        o['info'] = {v.split('=')[0]:v[len(v.split('=')[0])+1:] for v in consola.getFile('/etc/os-release',code='utf-8')}
    print(o)
    print('sys.prefix:',sys.prefix)
    print('sys.platform:',sys.platform)
    print('sys.version_info:',sys.version_info)
    print('sys.version:',sys.version)
    print('sys.:',sys)
def programador():
    #"comando principla;confirmarComando;banderas;archivoDeSalida;observacion"
    auto=programador_consola(name='subir_push',fuente=['mbarete','consolas'])
    print(auto.o['info'])
    commands=[
        'git status;false;;',
        'git add -A;;;',
        'git commit;;m="commit automatico desde LinuxLite bash";output',
        "git push origin $branch;true;;",
        "git status;false;;"
    ]
    auto.set(commands)
    auto.save()
def programador2():
    auto=programador_consola(name='bajar_pull',fuente=['mbarete','consolas'])
    #print(auto.o)
    auto.set("git pull; ; ; ;trae datos del repositorio remoto y luego mezcla los cambios con el repositorio local")
    menu={
        'inicio':'git status;false;;;',
        'cabezera':'Si obtuvo algun error, por favor ingrese un numero de las siguientes opciones',
        'lista':[{
            'opcion':'No importan los cambios locales y desea sobrescribirlos',
            'commands':[
                "git fetch;false;;;solo traerá datos del repositorio remoto del 'branch' actual",
                "git reset --hard HEAD;false;;;restablecerá el branch a su último estado committed",
                r"git merge '@{u}';false;;;para mezclar los cambios con el repositorio local"
                ]
            },{
            'opcion':'Te importan los cambios y te gustaría mantenerlos después de traer los cambios remotos',
            'commands':[
                "git fetch;false;;;solo traerá datos del repositorio remoto del 'branch' actual",
                "git stash;false;;;significa guardar los cambios 'uncommitted' por un momento para traerlos nuevamente más tarde",
                r"git merge '@{u}'; ;;;para mezclar los cambios con el repositorio local",
                "git stash pop;false;;;para recuperar los cambios guardados en el último stash, este comando también elimina el 'stash commit' hecho con 'git stash'"
                ]
            },{
            'opcion':'Deseas descargar los cambios remotos pero aún no aplicarlos',
            'commands':[
                "git fetch --all;false;;;para obtener los cambios de todos los branches.",
                "git fetch --prune;true;;;limpiar algunas de las ramas que ya no existen en el repositorio remoto."
                ]
            }
        ]
    }
    auto.set(menu)
    auto.save()

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


from practicas.pruebas import main_pruebas

if 'main' in __name__:
    pruebas={
        1:{'titulo':"Lista o buscar informacion del sistema",'f':lambda: crearInfo(search=[])},
        2:{'titulo':"programando en shell secuencial",'f':programador},
        3:{'titulo':"programando en shell loop",'f':programador2},
        4:{'titulo':"mostrar valores de start('nombre_de_archivo'):",'f':lambda: print(start('nombre_de_archivo'))},
        5:{'titulo':"buscar",'f':buscador}
        }
    main_pruebas(pruebas,sys.argv)