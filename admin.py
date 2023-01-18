from mbarete.mbarete import mbarete,calculadora,geometria,GUI
import os
#obtenemos los sub-programas de la carpeta principal
admin=mbarete(
    pwd='',
    baseName='diseñoLibre',
    nombre='Diseño Libre',
    cargarScript='mbarete.py',
    ficheroCRUD='',
    archivosInternos=['__pycache__','__init__.py','media','bibliografia','preload.py','mbarete','manager'],
    formato=[''],
    fullDir=1,
    renombrarArchivos=1,
    ignorar=[],
    reset=1,
    campoAutoincrement='id',
    gitBranch='master',
    gitignore=['bibliografia','__pycache__']
    )
admin.preload()
from diseñoLibre.preload import proyectos,command
from diseñoLibre.manager import mbarete as manager
admin.manager = manager.info['name']

# declaramos 'G' de la clase GUI que se encargara 
# de gran parte de la grafica del programa
G=GUI(
    titulo=admin.nombre,reset=admin.reset,
    dirCRUD=admin.dirCRUD,pwd=admin.ubi.pwd
    )
admin.defaultCommand=G.defaultCommand
# A partir de los sub-proyectos generamos la  
# informacion necesaria para administrar 
# todos los Sub-Proyectos como uno solo
widgets={}
for proyecto in proyectos:
    widgets[proyecto]=admin.getWidget(
        proyecto, proyectos[proyecto].widgets, 
        proyectos[proyecto].info
        )
widget_manager=manager.widgets
widget_manager['subProyectos']['inputs']=admin.getInicio()
widgets[admin.manager]=admin.getWidget(
    admin.manager, widget_manager, manager.info
    )
# buscar=admin.info['inicio']['command']['buscar']
# G.command[buscar]=lambda : print(G.widgets['menu']['value'])
# Comandos Generales Para 'G'
command(admin,G,admin.manager)
manager.command(
    admin, G, admin.info[admin.manager], 
    calculadora, geometria
    )
mostrarInfo=False
if mostrarInfo:
    print('Mostrar Info:')
    for subProyecto in proyectos:
        print(subProyecto,admin.info[subProyecto])
    
#Le Pasamos a 'G' los comandos de los Sub-proyectos
for subProyecto in proyectos:
    proyectos[subProyecto].command( 
        admin, G, admin.info[subProyecto], 
        calculadora, geometria 
        )
for widget in widgets[admin.manager]:
    G.SetWidget( atributos=widgets[admin.manager][widget] )
#declaramos los widgets de los proyectos
for proyecto in proyectos:
    for widget in widgets[proyecto]:
        G.SetWidget( atributos=widgets[proyecto][widget] )

admin.start(G)
print(admin.nombre)
