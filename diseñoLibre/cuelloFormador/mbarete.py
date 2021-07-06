import math
#generador de planos de cuello formador

info={
    'autor':'Lucas Mathias Villalba Diaz',
    'name':'cuelloFormador',
    'text':'Cuello Formador de Bolsas',
    'descripcionBreve':'Sub-Proyecto para Diseñar un cuello formador de bolsas para empaquetado automatico',
    'descripcionLarga':'Sub-proyecto para Diseñar un cuello formador de bolsas para empaquetado automatico',
    'img':'cuello.png',
    'enlace':'mathiaslucasvidipy@gmail.com',
    'etiquetas':['Former Shulder','Cuello Formador','industrial','empaquetado']
}
def ec(x,extras={}):
    return float(x)*math.exp(x)


def getInversa(error=0.00001,f=lambda abscisa : abscisa ,extras={}):
    def ret(ordenada,error=error,f=f,extras=extras):
        ordenada=float(ordenada)
        mayor=0.0
        menor=0.0
        abscisa=0.0
        while f(mayor,extras)<ordenada:
            mayor += 10.0
        while f(menor,extras)>ordenada:
            menor -= 1.0
        while ((ordenada-f(abscisa,extras))**(2))**(1/2) > error:
            if ordenada<f((mayor+menor)/2.0,extras):
                mayor=(mayor+menor)/2.0
            elif ordenada>f((mayor+menor)/2.0,extras):
                menor=(mayor+menor)/2.0
            abscisa=(mayor+menor)/2.0   
        return abscisa
    return ret

widgets={
    'principal':{
        'inputType':"Frame",
        "etiquetas":['id','Inicio','Frame','menu'],#AUTOMATICO/OBLIGATORIO
        "typeSalida":"command",#OPCIONAL
        "name":'principal',#OBLIGATORIO
        "text":'Principal',#OBLIGATORIO
        'fontSize':10,
        'bgColor':'#080904',  
        'degradado':0,  
        'inputs':{
            'prueba':{
                'inputType':'Checkbutton',
                'text':'Esta es una Prueba',
                'value':0.0,
                'command':'checkPrueba'
            },
            'HojasEnBlanco':{
                'inputType':'Checkbutton',
                'text':'Imprimir Hojas En Blanco',
                'value':0.0,
                'command':'checkHojaenBlanco'
            },
            'programador':{
                'inputType':'Checkbutton',
                'text':'Es usted programador',
                'value':0.0,
                'command':'checkProgramador'
            },
            'escala':{
                'inputType':'Entry',
                'text':'Escalar:',
                'value':1.0,
                'typeSalida':'float'
            },
            'desmarcar':{
                'inputType':'Button',
                'command':'desmarcar',
                'text':'Desmarcar'
            },
            'mostrar':{
                'inputType':'Button',
                'command':'mostrar',
                'text':'Mostrar'
            },
            'salir':{
                'inputType':'Button',
                'command':'salir',
                'text':'Destroy'
            }},
        'tabla':{'Clientes':["RUC TEXT","RazonSocial TEXT","NombresApellidos TEXT","Direccion TEXT","Telefono TEXT","saldo TEXT"]}
    },
    'cuello':{
        'inputType':"panel",
        "etiquetas":['id','default','panel'],#AUTOMATICO/OBLIGATORIO
        "typeSalida":"command",#OPCIONAL
        "name":'cuello',#OBLIGATORIO
        "text":'Cuello Formador',#OBLIGATORIO
        "value":'',#OPCIONAL  
        'anchor':'e',
        'fontType':'Arial',
        'fontSize':12,
        'degradado':1,
        'visible':0,
        'fgColor':'#0f0f0f',  
        'inputs':{
            'inicio':{
                'inputType':'Button',
                'command':'manager',
                'text':'Administrador'
            },
            'baseRadio':{
                'inputType':'Entry',
                'text':'Radio de Base en mm:',
                'value':25.0,
                'typeSalida':'float'
            },
            'alto':{
                'inputType':'Entry',
                'text':'Altura en mm:',
                'value':100.0,
                'typeSalida':'float'
            },
            'espalda':{
                'inputType':'Entry',
                'text':'Angulo de La Espalda:',
                'value':90,
                'typeSalida':'int'
            },
            'anchodelRollo':{
                'inputType':'Entry',
                'text':'Ancho del Rollo:',
                'value':12.0,
                'typeSalida':'float'
            },
            'escalar':{
                'inputType':'Entry',
                'text':'Ancho del Rollo:',
                'value':12.0,
                'typeSalida':'float'
            },
            'calcular':{
                'inputType':'Button',
                'command':'calcular',
                'text':'(C)alcular'
                },
            'borrar':{
                'inputType':'Button',
                'command':'borrar',
                'text':'Borrar todo'
                }
            },
        'tabla':{'Clientes':["RUC TEXT","RazonSocial TEXT","NombresApellidos TEXT","Direccion TEXT","Telefono TEXT","saldo TEXT"]}
    }
}
def command(admin,G,info,ec,geo):
    print(info['subProyecto'])
    print('Info:',info['info'])
    print('Widgest:',info['widget'])
    print('Comandos',info['command']) 
    G.command[info['command']['manager']]=lambda : admin.transicion(G,admin.manager)
    G.command[info['command']['borrar']]=lambda : print('command borrar cuello'),
    G.command[info['command']['calcular']]=lambda : print('command calcular  cuello')
    G.command[info['command']['desmarcar']]=lambda : G.setVar(info['widget']['nuevo'],{'autor':'','name':'','text':'','descripcionBreve':'','descripcionLarga':'','img':'','enlace':'','etiquetas':''})
    G.command[info['command']['checkPrueba']]=lambda : print('command checkPrueba  cuello')
    G.command[info['command']['checkProgramador']]=lambda : print('command checkProgramador  cuello')
    G.command[info['command']['checkHojaenBlanco']]=lambda : print('command checkHojaenBlanco  cuello')
    G.command[info['command']['mostrar']]=lambda : print('command   cuello')
    G.command[info['command']['salir']]=lambda : print('command   cuello')

def ejecutar(admin,G,info,ecuacion,geo):
    #G.command['menuAspas']=lambda : menu('aspas') 
    #G.command['principal']=lambda : menu('principal')
    print(variables)
    lambert=ecuacion(ec,extras={'name':'lambert','dominio':[-1/math.e,'inf'],'string':'(x*(e**x)'})
    print(lambert.extras['string'])
    for x in range(variables['inicio'],variables['final'],variables['pasos']):
        print(x,lambert.f(x))
    lambert.trasladar(o=[1,-1.0])
    #lambert.rotar(o=[0.0,0.0],alfa=math.radians(30))
    print(lambert.extras['string'])
    for x in range(variables['inicio'],variables['final'],variables['pasos']):
        print(x,lambert.f(x))
    w=getInversa(error=0.0000001,f=ec)
    for x in range(variables['inicio'],variables['final'],variables['pasos']):
        y=ec((x/100.0)-1/math.e,lambert.extras)
        x0=w(y)
        print(x,(x/100.0)-1/math.e,x0)

