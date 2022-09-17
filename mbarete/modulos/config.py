#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os,sys
from pruebas import *
from extras import V
from extras import p
"""
    También podes importar modulos individuales si deseas manipular 
    una ruta que siempre está en uno de los diferentes formatos. 
    Todos tienen la misma interfaz:
        posixpath para rutas con estilo UNIX
        ntpath para rutas Windows
"""
#p=printer()
class cmd:
    """
        generar scrpit 
        'batch' para windows, 'bash' para linux 
        segun en el que se este ejecutando
    """
    ignorar='.auto.'
    name=''
    code='latin-1'
    #cmd.info_system({'pwd_consola':'mbarete/consolas'})
    #cmd.crearInfo(info=cmd.info,force=0)
    def new(*arg,pwd=None,**kw):
        
        
        cmd.start(**kw)
        print(cmd.o['info'])
        cmd.s = cmd.o['start']
        print(cmd.o['info'])
        cmd.crearInfo(info=cmd.info,**kw)
        print(cmd.o['info'])
    def paths_directos():

        cmd.carpetas={}
        prefijos={'dir_':4,'web_':4,'pwd_':4,'git_repo_path':4}
        if 'git_repo_path' in cmd.info :
            cmd.repo_path=cmd.info['git_repo_path'] 
        #else:repo_path=cmd.info['dir_repo_path']
        for k in cmd.info:
            if k[:4] in ['dir_','web_','pwd_']: 
                cmd.info[k] = cmd.repo_path+cmd.info[k]

        for k in cmd.info:
            pre=next( ( p for p in prefijos if p==k[:len(p)] ), None )
            if pre in prefijos: 
                cmd.carpetas[k[prefijos[pre]:]]=cmd.info[k]
        p(cmd.carpetas,flag='paths_directos',listar=1)
    def ret_system(command,**kw):
        os.system(command+" > "+cmd.info['home']+'mbarete_tmp')
        ret = p.getFile(
            cmd.info['home']+'mbarete_tmp',
            **kw
            )
        os.remove(cmd.info['home']+'mbarete_tmp')
        return ret
    def info_system(directorios):
        info={
            'file':'info'+cmd.ignorar,
            'prefijo':'cross_',
            'file_tmp':'temp_mbarete.',
            'ignorar':cmd.ignorar,
            **directorios
            }
        if os.name == 'nt':
            import platform
            info={
                **info,
                'OS':'windows',
                'V':os.environ['OS'],
                'tmp':os.environ['TEMP']+os.sep,
                'home':os.environ['USERPROFILE']+os.sep
                }
            info['uname_sysname'] ,info['uname_nodename'] ,info['uname_release'] ,info['uname_version'] ,info['uname_machine'] ,info['uname_processor'] = platform.uname()
            info['uname_version']='"'+info['uname_version']+'"'
        elif 'ANDROID_ROOT' in os.environ:
            info={
                **info,
                'OS':'android',
                'V':os.environ['SHELL'],
                'tmp':'/tmp/',
                'home':os.environ['HOME']+os.sep
                }
        elif os.name == 'posix':
            info=p.getFile(
                '/etc/os-release',
                join={
                    **info,
                    'OS':'linux',
                    'tmp':'/tmp/',
                    'home':os.environ['HOME']+os.sep
                    },
                sep='=',
                prefijo='OS_',
                buscar=['VERSION','ID','ID_LIKE','PRETTY_NAME']
            )
            info['uname_sysname'] ,info['uname_nodename'] ,info['uname_release'] ,info['uname_version'] ,info['uname_machine'] = os.uname()
            info['V']='"'+info['OS_ID']+', '+info['OS_PRETTY_NAME'][1:-1]+'"'
            info['uname_version']='"'+info['uname_version']+'"'
        info['sys_prefix']='"'+sys.prefix+'"'
        info['sys_platform']=sys.platform
        info['sys_version']='"'+sys.version.replace('\n',' ')+'"'
        cmd.info = info
        cmd.info_git()
        cmd.paths_directos()
        print(cmd.info)
    def info_git():
        buscar=['git_repo_path','git_repo_name','git_branch','pwd_consola','pwd_modulos','pwd_servidor']
        buscar=[ cmd.info['prefijo']+b for b in buscar ]
        cmd.info['git_branch']=next(
            (e[2:] for e in cmd.ret_system("git branch") if '*' in e[0]),
            None
            )
        tmp_git=cmd.info['file_tmp']+cmd.info['file']
        myTMP=[]
        for file in os.listdir(cmd.info['home']): 
            if tmp_git in file[:len(tmp_git)]:
                myTMP+=[file]
        cmd.mis_repos = {}
        for repo in myTMP:
            cmd.mis_repos[repo[len(tmp_git):]]=p.getFile(
                cmd.info['home']+repo ,
                join={},buscar=buscar,sep=':'
            )
        p(cmd.mis_repos,flag='info_git',listar=1)
        if cmd.info['git_branch']:
            #Hallamos la direccion raiz de este 'repositorio'
            h=[os.getcwd()]
            while not '.git' in os.listdir():
                os.chdir('..')
                h+=[os.getcwd()]
            cmd.info['git_repo_path']=h[-1]+os.sep
            os.chdir(h[0])
            # obtenemos la lista de configuracion de git global y local
            git=cmd.ret_system("git config --list",join={},sep='=')
            p(git,flag='info_git',listar=1)
            config={
                'email':'user.email',
                'username':'user.name'
            }
            for g in config:
                if config[g] in git:
                    cmd.info['git_'+g]= git[config[g]] 
                else:
                    cmd.info['git_'+g]=input(f'Ingrese su {g} de github:')
            if 'remote.origin.url' in git:
                (cmd.info['git_repo_username'],cmd.info['git_repo_name'])=git['remote.origin.url'].split('/')[-2:]
        else:
            pass
            """
            codigo para:
            *instalar git
            *activar git en este proyecto, 'git init'
            *crear cuenta en github
            *metodos de autenticacion del usuario
            *conectar este repositorio con Github
            """
        if not 'git_repo_path' in cmd.info :
            #esta sera la ruta 'repo_path' de self.carpetas
            cmd.info['dir_repo_path']=os.getcwd()+os.sep
        
    def start(name=''):
        if not name: name=cmd.name
        cmd.o={
            'OS':cmd.info['OS'],
            'V':cmd.info['V'],
            'f':cmd.info['pwd_consola'].replace('/',os.sep)
        }
        if 'windows' in cmd.info['OS']:
            cmd.o['name']=name+cmd.info['ignorar']+'cmd'
            cmd.o['cross']=r'%cross% '
            cmd.o['start']=[
                '@ECHO off',
                'setlocal',
                'set "fuente='+cmd.o['f']+'"',
                'set "fuenteinfo='+cmd.o['f']+cmd.info['file']+'"',
                r'set "cross=call %fuente%cmd_principal.cmd command"',
                r'call %fuente%cmd_principal.cmd inicio %fuente%'
                ]
            cmd.o['end']=['endlocal']
            cmd.o['to_var']=lambda v: r'%'+v+r'%'
            cmd.o['if_eq']=lambda a,b: 'IF "%'+str(a)+'%" == "'+str(b)+'" ('
            cmd.o['fi']=')'
            cmd.o['read']=lambda a: 'SET /p '+str(a)+'=Ingrese una Opcion:'
        elif 'linux' in cmd.info['OS']:
            cmd.o['name']=name+cmd.info['ignorar']+'sh'
            cmd.o['cross']=r'cross '
            cmd.o['start']=[
                '#!/bin/bash',
                'fuente='+cmd.o['f'],
                'fuenteinfo='+cmd.o['f']+cmd.info['file'],
                'source "$fuente"bash_principal.sh'
            ]
            cmd.o['end']=['']
            cmd.o['to_var']=lambda v: r'$'+v
            cmd.o['if_eq']=lambda a,b: 'if [ "$'+str(a)+'" == "'+str(b)+'" ];then'
            cmd.o['fi']='fi'
            cmd.o['read']=lambda a: 'read -p "Ingrese una Opcion:" '+str(a)
            cmd.o['abrir']=lambda f: 'xdg-open %s'%(f)
        
        elif 'android' in cmd.info['OS']:
            pass
        cmd.o['info']=p.getFile(
            cmd.info['pwd_consola']+cmd.info['file'],
            join={},sep=':'
            )
        cmd.o['info']['prefijo']=p.getFile(
            cmd.info['pwd_consola']+cmd.info['file'],
            buscar=['prefijo'],sep=':',join={}
            )['prefijo']
        
        
        cmd.o['loop_num']=1
        cmd.o['for_num']=1
        cmd.o['while_num']=1
    def estructura_secuencial(c):
        if str == c.__class__: c=[c]
        #(script,commands,OS)

        for i in range(len(c)):
            for v in cmd.o['info']: 
                #print(v,v[len(cmd.o['info']['prefijo']):])
                c[i]=c[i].replace(
                    '$'+v[len(cmd.o['info']['prefijo']):],
                    cmd.o['to_var'](v)
                    )
            c[i]=cmd.o['cross']+'"'+c[i].strip().replace(';;','; ;').replace(';;','; ;').replace('"',"'")+' "'
        cmd.s+=c
    def estructura_loop(menu):
        l='loop_'+str(cmd.o['loop_num'])
        vl='var_'+l
        cmd.o['loop_num']+=1
        if cmd.o['OS'] == 'windows':
            cmd.s+=[':'+l]
        if cmd.o['OS'] == 'linux':
            cmd.s+=[l+'=true']
            cmd.s+=['while [ $'+l+' == true ] ;do']

        if 'inicio' in menu: cmd.set(menu['inicio'])
        cmd.s+=['echo '+menu['cabezera']]
        for op in range(1,1+len(menu['lista'])): 
            cmd.s+=['echo '+str(op)+'.'+menu['lista'][op-1]['opcion']]
        cmd.s+=['echo "  <<< ENTER PARA SALIR >>>"']
        cmd.s+=[cmd.o['read'](vl)]
        if cmd.o['OS'] == 'windows': cmd.s+=['if "%'+vl+'%"=="" (goto :eof)']
        if cmd.o['OS'] == 'linux': cmd.s+=['if [ -z $'+vl+' ];then '+l+'=false ;fi']
        for op in range(1,1+len(menu['lista'])):
            cmd.s+=[cmd.o['if_eq'](vl,op)]
            cmd.set(menu['lista'][op-1]['commands'])
            cmd.s+=[cmd.o['fi']]
        if cmd.o['OS'] == 'windows': cmd.s+=['goto :'+l]
        if cmd.o['OS'] == 'linux': cmd.s+=['done']
    def set(c):
        if dict == c.__class__:
            if ('inicio' in c) and ('cabezera' in c) and ('lista' in c):
                cmd.estructura_loop(c)
        else:
            cmd.estructura_secuencial(c)
    def save():
        #crea y guarda el script, esto sobreescribe el archivo si es que ya existe
        p.setFile(cmd.repo_path+cmd.o['name'],cmd.s+cmd.o['end'],echo=0)
    def crearInfo(*arg,info={},force=0,**kw):
        if 'git_branch' in cmd.info:
            # codigo para crear el archivo info, en caso de ser necesario
            # codigos para un proyecto con git activado
            # codigos para proyecto sin git activado, y si 
            pass  
        info_default={
            'git_repo_branch':'master',
            'git_repo_email':'mathiaslucasvidipy@gmail.com',
            'sub_proyectos':'codigoLibre',
            'version':1.0,
            'modo_seguro':'false'
        }
        info={**info_default,**cmd.info,**info}
        print(info['pwd_consola']+'info.'+info['OS'])
        info=p.getFile(info['pwd_consola']+'info.'+info['OS'],join=info)

        prefijo=lambda k :info['prefijo'] if k!='prefijo' else ''

        pwd=[info[k]+info['file'] for k in info if 'pwd_' in k[:4]]

        tmp=info['home']+info['file_tmp']+info['file']+info['git_repo_name']

        p(tmp,info['OS']+'.'+info['V'])

        info={k:(f'"{info[k]}"') if 'comand_' in k[:7] else info[k] for k in info }

        info=[ prefijo(k)+f'{k}:{info[k]}' for k in info ]

        p.setFile(tmp,valor=info,echo=0)
        for file in pwd: 
            if (not os.path.exists(file)) or force:
                p.setFile(file,valor=info,echo=0)
        for e in info:p(e,flag='info')

def git_admin():

    """
    //Segmento de windows CMD
    SET /p sigue=Hacer "git add -A" s/n?:
    if "%sigue%"=="n" (goto :fin)
    if "%sigue%"=="N" (goto :fin)
    echo Ejecutando: git add -A
    git add -A

    #segmento de Linux Bash
    """
def git_crear_branch():
    '''Crear una rama dentro del repositorio'''
    #"comando principla;confirmarComando;banderas;archivoDeSalida;observacion"
    
    cmd(
        name='checkout_pull',
        fuente=['mbarete','consolas']
        )
    commands=[
        'git checkout $git_repo_branch;false;;',
        "git pull origin $git_repo_branch;false; ; ;trae datos del repositorio remoto y luego mezcla los cambios con el repositorio local",
        "git checkout $git_branch;false;;"
        ]
    cmd.set(commands)
    cmd.save()
    V.p(cmd.info,cmd.mis_repos,listar=1,flag='crear_branch')
    V.p(cmd.pwd,flag='crear_branch')
def git_push():
    '''generar script para subir los cambios a Github'''
    #"comando principla;confirmarComando;banderas;archivoDeSalida;observacion"
    
    cmd.new(name='subir_push')
    p( cmd.carpetas )
    commands=[
        'git checkout $git_branch;false;;',
        'git add -A;;;',
        'git commit;;m="automatico desde $V";output',
        "git push origin $git_branch;true;;",
        'git checkout $git_branch;false;;',
        "git status;false;;"
    ]
    cmd.set(commands)
    cmd.save()
def git_pull():
    '''generar script para bajar los cambios desde Github'''
    cmd.new(name='bajar_pull')
    #print(auto.o)
    commands=[
        'git checkout $git_repo_branch;false;;;pasamas a la branch "$git_repo_branch"',
        "git pull origin $git_repo_branch;false; ; ;trae datos de la branch $git_repo_branch del repositorio remoto y luego mezcla los cambios con la branch $git_repo_branch del repositorio local",
        'git checkout $git_branch;false; ; ;pasamas a la branch "$git_branch"',
        "git pull origin $git_branch;false; ; ;trae datos del repositorio remoto de la branch '$git_branch' y luego mezcla los cambios con la branch '$git_branch' del repositorio local",
    ]
    cmd.set(commands)
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
    cmd.set(menu)
    cmd.save()
def git_branch():
    # funcion activar git 
    # manejar los archivos 'ejecutables' de git
    pass
def requeriments():
    #requeriments system
    #virtualenv
    #requeriments PIP-WHEEL
    #requeriments system
    #config system
    pass
   

class install(object):
    """configuraciones para un instalador"""
    lanzador={
        'Version':'1.0',
        'Type':'Application',
        'Name':'Sublime Text',
        'GenericName':'Text Editor',
        'Comment':'Sophisticated text editor for code, markup and prose',
        'Exec':'/opt/sublime_text/sublime_text %F',
        'Terminal':'false',
        'MimeType':'text/plain;',
        'Icon':'sublime-text',
        'Categories':'TextEditor;Development;',
        'StartupNotify':'true',
        }
    def accesoDirecto(osKey,**kw):
        if osKey=='posixDesktop':
            linkScript=["[Desktop Entry]"]
            for k in kw:
                linkScript.append(f'{k}={kw[k]}')
            
        elif osKey=='posixMovil':
            linkScript=f"""
                [Desktop Entry]
                Version=1.0
                Type=Application
                Name=Sublime Text
                GenericName=Text Editor
                Comment=Sophisticated text editor for code, markup and prose
                Exec=/opt/sublime_text/sublime_text %F
                Terminal=false
                MimeType=text/plain;
                Icon=sublime-text
                Categories=TextEditor;Development;
                StartupNotify=true
                Actions=new-window;new-file;

                [Desktop Action new-window]
                Name=New Window
                Exec=/opt/sublime_text/sublime_text --launch-or-new-window
                OnlyShowIn=Unity;

                [Desktop Action new-file]
                Name=New File
                Exec=/opt/sublime_text/sublime_text --command new_file
                OnlyShowIn=Unity;
            """
        

if 'main' in __name__:
    p.config(flags=['init','error','info_git','init_consola'])
    carpetas_test={
        'pwd_consola':'mbarete/consolas/',
        'pwd_modulos':'mbarete/modulos/',
        'web_media':'mbarete/media/',
        'dir_servidor':'mbarete/servidor/'
        }
    cmd.info_system(carpetas_test)
    main_pruebas([git_crear_branch,git_push,git_pull])