#
import math
baseRadio=75.0
altura=75.0
revolucion=360
rotorRadio=1.0
profundidad=60.0
info={
    'autor':'Lucas Mathias Villalba Diaz',
    'name':'arquimedes',
    'text':'Aspas de Viento de Arquimedes',
    'descripcionBreve':'Sub-Proyecto Aero generador Arquimedes',
    'descripcionLarga':'Sub-proyecto arquimedes, diseños de aspas para aerogeneradores caseros',
    'img':'projecto.jpg',
    'enlace':'mathiaslucasvidipy@gmail.com',
    'etiquetas':['energia eolica','aspas de viento','arquimedes','aerogenerador']
}
widgets={
    'aspas':{
        'inputType':"panel",
        "etiquetas":['id','default','Frame'],#AUTOMATICO/OBLIGATORIO
        "typeSalida":"command",#OPCIONAL
        "name":'aspas',#OBLIGATORIO
        "text":'Aspas Euclides',#OBLIGATORIO
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
                'text':'Radio de Base:',
                'value':375.0,
                'typeSalida':'float'
            },
            'Fondo':{
                'inputType':'Entry',
                'text':'Fondo:',
                'value':200.0,
                'typeSalida':'float'
            },
            'giroReal':{
                'inputType':'Entry',
                'text':'Giro Ideal:',
                'value':360,
                'typeSalida':'int'
            },
            'rotorRadio':{
                'inputType':'Entry',
                'text':'Radio del Rotor:',
                'value':12.0,
                'typeSalida':'float'
            },
            'alto':{
                'inputType':'Entry',
                'text':'Alto de Ataque:',
                'value':375.0,
                'typeSalida':'float'
            },
            'escala':{
                'inputType':'Entry',
                'text':'Escalar:',
                'value':1.0,
                'typeSalida':'float'
            },
            'mostrar':{
                'inputType':'Button',
                'command':'mostrar',
                'text':'mostrar'
                },
            'desmarcar':{
                'inputType':'Button',
                'command':'desmarcar',
                'text':'(C)alcular'
                },
            'calcular':{
                'inputType':'Button',
                'command':'aspas',
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
"""
command={
    'mostrar':lambda : print('mostrar arquimedes'),
    'desmarcar':lambda : print('desmarcar arquimedes') ,
    'borrar':lambda : print('borrar arquimedes'),
    'aspas':lambda : print('aspas arquimedes')
    }
"""
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

def command(admin,G,info,ec,geo):
    print(info['subProyecto'])
    print('Info:',info['info'])
    print('Widgest:',info['widget'])
    print('Comandos',info['command']) 
    G.command[info['command']['manager']]=lambda : admin.transicion(G,admin.manager)
    G.command[info['command']['mostrar']]=lambda : print('mostrar arquimedes')
    G.command[info['command']['desmarcar']]=lambda : print('desmarcar arquimedes') 
    G.command[info['command']['borrar']]=lambda : print('borrar arquimedes')
    G.command[info['command']['aspas']]=lambda : print('aspas arquimedes')
def ejecutar(admin,G,info,ec,geo):
    print(variables)
    lambert=ecuacion(ec,extras={'name':'lambert','dominio':[-1/math.e,'inf'],'string':'(x*(e**x)'})
    print(lambert.extras['string'])
    for x in range(variables['inicio'],variables['final'],variables['pasos']):
        print(x,lambert.f(x))