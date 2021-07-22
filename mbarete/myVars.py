# -*- coding=UTF-8 -*-
#BGD 764
"""
	CONJUNTO DE VARIABLES PARA EL PROYECTO MBARETE
	EN ESTE SCRIPT SOLO HAY DECLARACIONES DE VARIABLES
	PARA LUEGO SER IMPORTADOS Y USADOS EN EL SRCIPT 'mbarete.py' 
"""
lenguaje={
    'es':{
        'Aceptar':'Aceptar',
        'Borrar':'Borrar',
        'Guardar':'Guardar',
        'Cancelar':'Cancelar',
        'Ignorar':'Ignorar',
        'Exportar':'Exportar',
        'Inicio':'Inicio',
        'Anterior':'Anterior',
        'Siguiente':'Siguiente',
        'Buscar':'Buscar',
        'Cerrar':'Cerrar',
        'Actualizar':'Actualizar',
        'Saltar':'Saltar'
    }
}
atributos={
    'user':'Hall 9000',
    'titulo':'Mbarete',
    'bbdd':'Mbarete.sql',
    'modoDesarrollador':1,
    'ancho':1000,
    'alto':600,
    'Xexterior':10,
    'Yexterior':10,
    'fontSizeToAlto':{
        'Arial':[0, 4, 7, 9, 11, 12, 18, 21, 25, 26, 28, 30, 32, 33, 39, 40, 42, 46, 47, 49, 56, 56, 58, 61, 63, 67, 70, 72, 74, 77, 79, 82, 86, 88],
        'Comic Sans MS':[0, 5, 7, 9, 12, 18, 18, 23, 26, 30, 32, 35, 40, 42, 46, 49, 51, 54, 58, 60, 67, 68, 70, 77, 79, 81, 86, 89, 91, 95, 98, 100, 105, 107]
        },
    'fontSizeToCorrectorAncho':{
        'Comic Sans MS':[1,1,1,0,0,0,0,0,0,-1,-1,-1,-1,-2,-2,-2,-2,-2,-2,-3,-3,-3,-3,-3,-3,-4,-4,-4,-5,-4,-5,-5,-5,-5,-5,-5],
        'Arial':[1,1,1,0,0,0,0,0,-1,-1,-1,-1,-2,-3,-2,-3,-3,-3,-3,-3,-3,-4,-4,-4,-4,-5,-5,-5,-5,-5,-6,-6,-6,-6,-6,-6]
        },
    'colorFondo':"#e0e0ff",
    'fondo':"#f0f0ff",
    'colorSeleccion_a':"#893301",
    'colorTitulo':"#000f00",
    'foco':"Raiz",
    'scrollVerticalAncho':16,
    'scrollHorizontalAlto':16,
    'espacioHorizontalEntreWidgets':20,
    'espacioVerticalEntreWidgets':5,
    'transicion':'manager',
    'subtransicion':'Inicio',
    'frameActivo':'',
    'campoAutoincrement':'id integer primary key autoincrement'
    }

atributos['botonAncho']=atributos['ancho']
atributos['botonAlto']=atributos['alto']
atributos['menuAlto']=atributos['alto']
atributos['menuAncho']=atributos['ancho']
font={
    'comic':{
        'name':'Comic Sans MS',
        'size':{10:20,11:24,12:27,14:30},
        },
    'arial':{
        'name':'Arial',
        'size':{10:20,11:24,12:27,14:30},
        }
    }
input_type={
	"panel":{
        'botones':{
            "Button1":{
                'text':'botonio',
                'img':'filedir.jpg'
                }
            },
        'tabla':{
            'Clientes':["RUC TEXT","RazonSocial TEXT","NombresApellidos TEXT","Direccion TEXT","Telefono TEXT","saldo TEXT"],
            }
        },
    "formIn":{
        'botones':["Aceptar","Aplicar","Modificar","Guardar","Siguiente","Anterior","Ignorar","Cancelar","Salir"],
        'tabla':"nombreDeLaTabla",
        'campos':["nombreDeLaTabla",'id integer autoincrement','COD text','nombre text','precio integer'],
        'camposHabilitados':['COD text','nombre text','precio integer']
        },
    "formOut":{
        'botones':["Aceptar","Aplicar","Modificar","Guardar","Siguiente","Anterior","Ignorar","Cancelar","Salir"],
        'tabla':"nombreDeLaTabla",
        'campos':["nombreDeLaTabla",'id integer autoincrement','COD text','nombre text','precio integer'],
        'camposHabilitados':['COD text','nombre text','precio integer']
        },
    'Label':{
        "descripcion":'descripcion kaigue XD',#OBLIGATORIO
        "etiquetas":['Label','tk'],#AUTOMATICO/OBLIGATORIO
        "text":"Label Tk",#OBLIGATORIO
        'padre':"Widget Principal"
        },#falta definir como asignar
    'Entry':{
        'padre':"Widget Principal",
        'validacion':{
            'None':'no validara el dato',
            'date':'str',
            'dateAndTime':'str',
            'password':'str',
            'email':'str',
            'telefono':'str',
            'direccion':'str',
            'personalizado':'str'},
        "descripcion":"",
        "etiquetas":["",""],
        "typeSalida":"['str','int','float','bool','date','bytes']",
        "name":"",#OBLIGATORIO
        "text":"",#OBLIGATORIO
        "value":'',
        "max":'',
        "min":'',
        "step":'',
        },#falta definir como asignar
    'Button':{
        'padre':"Widget Principal",
        'text':"botonio",
        'comando':'command1'
        },#falta definir como asignar
    'Toplevel':{'padre':"Widget Principal"},#falta definir como asignar
	'Canvas':{'padre':"Widget Principal"},#falta definir como asignar
	'Frame':{'padre':"Widget Principal"},#falta definir como asignar
	'Menu':{'padre':"Widget Principal"},#falta definir como asignar
	'OptionMenu':{'padre':"Widget Principal"},#falta definir como asignar
	'Scale':{'padre':"Widget Principal"},#falta definir como asignar
	'Text':{'padre':"Widget Principal"},#falta definir como asignar
	'CheckButton':{'padre':"Widget Principal"},#falta definir como asignar
	'LabelFrame':{'padre':"Widget Principal"},#falta definir como asignar
	'Menubutton':{'padre':"Widget Principal"},#falta definir como asignar
	'PanedWindow':{'padre':"Widget Principal"},#falta definir como asignar
	'Scrollbar':{'padre':"Widget Principal"},#falta definir como asignar
	'BitmapClass':{'padre':"Widget Principal"},#falta definir como asignar
	'Listbox':{'padre':"Widget Principal"},#falta definir como asignar
	'Message':{'padre':"Widget Principal"},#falta definir como asignar
	'Radiobutton':{'padre':"Widget Principal"},#falta definir como asignar
	'Spinbox':{'padre':"Widget Principal"},#falta definir como asignar
	'ImageClass':{'padre':"Widget Principal"},#falta definir como asignar
	'colorChoser':{'padre':"Widget Principal"},#falta definir como asignar
	'comboBox':{'padre':"Widget Principal"},#falta definir como asignar
	"panel":"input para menu general del programa",
    "botontk":"boton creado con tkinter",
    "botoncanvas":"boton creado con canvas",
    "boolean":"boton tipo on/off",
    "date":"input, para validar y seleccionar fechas",
    "textbox":"caja de texto para escribir varias lineas de texto",
    "scrolledtext":"textarea, caja de texto con barra de scroll, para texto muy largo",
    "sound":"input para recibir y validar archivos de audio",
    "slidebar":"input, barra para seleccionar nivel de volumen",
    "filedialog":"input, ventana para buscar, seleccionar un archivo del sistema",
    "fontchoser":"input selectlist, seleccionar un estilos de texto",
    "photoimage":"input, buscador, seleccionador, editor, diseñador de imagenes",
    "selectlist":"lista desplegable para selecionar una cosa a la ves"
}
inputsDefault={
    "help":{
    	'inputType':"help",
        "id":"NUMERO GENERADO AUTOMATICAMENTE PARA EL INPUT",#AUTOMATICO
        "descripcion":"breve descripcion del input, podra mostrarse en pantalla si es necesario",#OBLIGATORIO
        "etiquetas":"conjuntos de etiquetas vinculadas al input",#AUTOMATICO/OBLIGATORIO
        "typeSalida":"formato del dato de salida del input algunos input tienen su salida por defecto ['str'/'int'/'float'/'bool'/'date'/'bytes']",#OPCIONAL
        "name":"dentro del diccionario que retornara el form, este parametro del input es el 'nombre_clave' que estara asignado al dato de salida del input, tambien es el nombre que usaremos para vincular la salida de este input con el campo de la tabla correspondiente al form",#OBLIGATORIO
        "text":"nombre del input que sera mostrado en pantalla, para el usuario final",#OBLIGATORIO
        "value":"valor por defecto que se le asignara al input al iniciar el form",#OPCIONAL
        "max":"segun el tipo de input podemos asignar un maximo, para que no valide el form si el parametro supera el maximo asignado, este parametro estara mejor explicado en la funcion de validacion del form",#OPCIONAL
        "min":"lo mismo que 'max' pero desde abajo, los parametros max y min siempre estan incluidos dentro de los limites respectivos [MIN:MAX]",#OPCIONAL
        "step":"como seran tomados los datos cada n dias, numeros, letras. este parametro solo alpica a algunos input",#OPCIONAL
        "ancho":"el ancho en pixeles que ocupa el input en el eje x, en pantalla",#OPCIONAL
        "alto":"el alto en pixeles que ocupa el input en el eje y, en pantalla",#OPCIONAL
        "width":13,#OPCIONAL
        "xPlace":"la posicion en x, en pixeles de la ezquina superio izquierda del input, dentro del form",#AUTOMATICO
        "yPlace":"la posicion en y, en pixeles de la ezquina superio izquierda del input, dentro del form",#AUTOMATICO
        "visible":"si el input esta habilitado para ser editado",#OPCIONAL
        "editable":"si el input esta habilitado para ser editado",#OPCIONAL
        "degradado":0,#OPCIONAL
        "bgColor":"el color del fondo del input en hexagesimal, ejem: '#00417f'",#OPCIONAL
        "bgRelleno":"en caso de tener habilitado 'photoImage' para poder ponerle al input una imagen de fondo",#OPCIONAL
        "bordeColor":"color de la linea que bordea el input en hexagesimal ejem: '#00417f'",#OPCIONAL
        "bordeSize":"grosor de la linea que bordea el input en pixeles",#OPCIONAL
        "bordeRadio":"radio interno de las curvas en pixeles, en todas las ezquina del input",#OPCIONAL
        "fontType":"el estilo de letras en el input, ejemplo: Comic Sans Ms ",#OPCIONAL
        "fontSize":"tamaño de las letras en el input",#OPCIONAL
        "fontColor":"color del texto en el input",#OPCIONAL
        "fontMostrar":"si es legible, que el texto sea visible y legible, sino seran remplazados todos los caracters del texto por '*'",#AUTOMATICO/OPCIONAL
        "padre":"la name del input que controla a este, generalmente los input hijos son creados automaticamente y deben ser identificados por el name padre",#AUTOMATICO/OPCIONAL
        "hijo":"la name del unico hijo al cual debe llamar, el input hijo de este puede ser el input padre de otros input",#AUTOMATICO/OPCIONAL
        "stileId":"en caso de usar estilos de css en algun momento, para asignar un atributo al input",#OPCIONAL
        "stileClass":"en caso de usar estilos de css en algun momento, para asignar una clase al input",#OPCIONAL
        "urlDir":"direccion url vinculada al input, ejemplo:'https://www.facebook.com/profile/32154613'",#OPCIONAL
        "fileDir":"archivo vinculado al input",#OPCIONAL
        "fileType":"formato del archivo vinculado al input",#OPCIONAL
        "fileName":"nombre del archivo vinculado al input",#AUTOMATICO
        "tipoDeVista":"como se podra mostrar el conjuntos de elemento o inputs hijos que pertenescan a este input, ejemplo:listaSimple/listaDetallada/segunEspacioEnX/segunEspacioEnY/matrizFija/ ",#AUTOMATICO
        'relief':"tipo de borde [sunken/]",
        'borde':"grosor del borde",
        'cursor':"cambiar el cursor [heart/]",
        'fill':"el widget ocupara todo el espacio disponible en 'X' o 'Y', o ambos con 'both',  ['X'/'Y'/'both'/'none']",
        'expand':"el widget si puede cambiar de tamaño una vez iniciado el programa [0/1/'True'/'False']",
        'side':"para asignar la posicon del widget ['left'/'right'/'top'/'bottom']",
        'widget':"El objeto TKINTER",
        'justify':"left",
        'anchor':'E',
        'command':'nombre asignado al comando que eventualmente debe ejecutar el widget',
        'img':"imagen asignada al widget" },
    "Frame":{
        'inputType':"Frame",
        "id":None,#AUTOMATICO
        "descripcion":"Es el Frame principal, este widget puede ser manipulado como un Frame Normal.",#OBLIGATORIO
        "etiquetas":['id','','name','Frame','menu'],#AUTOMATICO/OBLIGATORIO
        "typeSalida":"command",#OPCIONAL
        "name":'Menu',#OBLIGATORIO
        "text":'Menu',#OBLIGATORIO
        "value":'',#OPCIONAL
        "max":None,#OPCIONAL
        "min":None,#OPCIONAL
        "step":None,#OPCIONAL
        "crearTabla":0,#OPCIONAL
        "gitAdd":0,#OPCIONAL
        "subProyecto":0,#OPCIONAL
        "ancho":500,#OPCIONAL
        "alto":500,#OPCIONAL
        "width":13,#OPCIONAL
        "xPlace":0,#AUTOMATICO
        "yPlace":0,#AUTOMATICO
        "visible":1,#OPCIONAL
        "editable":1,#OPCIONAL
        "degradado":0,#OPCIONAL
        "bgColor":'#00417f',#OPCIONAL
        "fgColor":'#040407',#OPCIONAL
        "bgRelleno":None,#OPCIONAL
        "bordeColor":'#19211f',#OPCIONAL
        "bordeSize":2,#OPCIONAL
        "bordeRadio":10,#OPCIONAL
        "fontType":'Comic Sans MS',#OPCIONAL
        "fontSize":14,#OPCIONAL
        "fontColor":'#ffa000',#OPCIONAL
        "fontMostrar":True,#AUTOMATICO/OPCIONAL
        "padre":None,#AUTOMATICO/OPCIONAL
        "hijo":None,#AUTOMATICO/OPCIONAL
        "stileId":'',#OPCIONAL
        "stileClass":'',#OPCIONAL
        "urlDir":None,#OPCIONAL
        "fileDir":None,#OPCIONAL
        "fileType":None,#OPCIONAL
        "fileName":None,#AUTOMATICO
        "tipoDeVista":None,#AUTOMATICO
        'relief':None,
        'borde':None,
        'cursor':None,
        'fill':'none',
        'expand':1,
        'side':None,
        'widget':None,
        'justify':None,
        'anchor':None,
        'img':""
        },
    "panel":{
        'inputType':"panel",
        "id":None,#AUTOMATICO
        "descripcion":"Input Para ejecutar funciones solo botones y entrys",#OBLIGATORIO
        "etiquetas":['id','','panel','typeSalida','panel'],#AUTOMATICO/OBLIGATORIO
        "typeSalida":"command",#OPCIONAL
        "name":'panel',#OBLIGATORIO
        "text":'Panel',#OBLIGATORIO
        "value":'',#OPCIONAL
        "max":None,#OPCIONAL
        "min":None,#OPCIONAL
        "step":None,#OPCIONAL
        "ancho":500,#OPCIONAL
        "alto":500,#OPCIONAL
        "width":13,#OPCIONAL
        "xPlace":0,#AUTOMATICO
        "yPlace":0,#AUTOMATICO
        "visible":1,#OPCIONAL
        "editable":1,#OPCIONAL
        "degradado":0,#OPCIONAL
        "bgColor":'#00417f',#OPCIONAL
        "fgColor":'#040407',#OPCIONAL
        "bgRelleno":None,#OPCIONAL
        "bordeColor":'#19211f',#OPCIONAL
        "bordeSize":2,#OPCIONAL
        "bordeRadio":10,#OPCIONAL
        "fontType":'Comic Sans MS',#OPCIONAL
        "fontSize":14,#OPCIONAL
        "fontColor":'#ffa000',#OPCIONAL
        "fontMostrar":True,#AUTOMATICO/OPCIONAL
        "padre":None,#AUTOMATICO/OPCIONAL
        "hijo":None,#AUTOMATICO/OPCIONAL
        "stileId":'',#OPCIONAL
        "stileClass":'',#OPCIONAL
        "urlDir":None,#OPCIONAL
        "fileDir":None,#OPCIONAL
        "fileType":None,#OPCIONAL
        "fileName":None,#AUTOMATICO
        "tipoDeVista":None,#AUTOMATICO
        'relief':None,
        'borde':None,
        'cursor':None,
        'fill':'none',
        'expand':1,
        'side':None,
        'widget':None,
        'justify':None,
        'anchor':None ,
        'img':""
        },
    "formIn":{
        'inputType':"formIn",
        "id":None,#AUTOMATICO
        "descripcion":"Input para Diseño de Formulario",#OBLIGATORIO
        "etiquetas":['id','','name','typeSalida','text'],#AUTOMATICO/OBLIGATORIO
        "typeSalida":"TYPESALIDA",#OPCIONAL
        "name":'NAME',#OBLIGATORIO
        "text":'TEXT',#OBLIGATORIO
        "value":'',#OPCIONAL
        "max":None,#OPCIONAL
        "min":None,#OPCIONAL
        "step":None,#OPCIONAL
        "ancho":500,#OPCIONAL
        "alto":700,#OPCIONAL
        "width":13,#OPCIONAL
        "xPlace":0,#AUTOMATICO
        "yPlace":0,#AUTOMATICO
        "visible":1,#OPCIONAL
        "editable":1,#OPCIONAL
        "degradado":0,#OPCIONAL
        "bgColor":'#00417f',#OPCIONAL
        "fgColor":'#040407',#OPCIONAL
        "bgRelleno":None,#OPCIONAL
        "bordeColor":'#19211f',#OPCIONAL
        "bordeSize":2,#OPCIONAL
        "bordeRadio":10,#OPCIONAL
        "fontType":'Comic Sans MS',#OPCIONAL
        "fontSize":14,#OPCIONAL
        "fontColor":'#ffa000',#OPCIONAL
        "fontMostrar":True,#AUTOMATICO/OPCIONAL
        "padre":None,#AUTOMATICO/OPCIONAL
        "hijo":None,#AUTOMATICO/OPCIONAL
        "stileId":'',#OPCIONAL
        "stileClass":'',#OPCIONAL
        "urlDir":None,#OPCIONAL
        "fileDir":None,#OPCIONAL
        "fileType":None,#OPCIONAL
        "fileName":None,#AUTOMATICO
        "tipoDeVista":'SegunEspacioEnX ',#AUTOMATICO
        'relief':None,
        'borde':None,
        'cursor':None,
        'fill':None,
        'expand':1,
        'side':None,
        'widget':None,
        'justify':None,
        'anchor':None,
        'img':""},
    "formOut":{
        'inputType':"formOut",
        "id":None,#AUTOMATICO
        "descripcion":"Input para Informes y Graficos",#OBLIGATORIO
        "etiquetas":['id','','name','Graficos','Informes'],#AUTOMATICO/OBLIGATORIO
        "typeSalida":"TYPESALIDA",#OPCIONAL
        "name":'NAME',#OBLIGATORIO
        "text":'TEXT',#OBLIGATORIO
        "value":'',#OPCIONAL
        "max":None,#OPCIONAL
        "min":None,#OPCIONAL
        "step":None,#OPCIONAL
        "ancho":500,#OPCIONAL
        "alto":700,#OPCIONAL
        "width":13,#OPCIONAL
        "xPlace":0,#AUTOMATICO
        "yPlace":0,#AUTOMATICO
        "visible":1,#OPCIONAL
        "editable":1,#OPCIONAL
        "degradado":0,#OPCIONAL
        "bgColor":'#00417f',#OPCIONAL
        "fgColor":'#040407',#OPCIONAL
        "bgRelleno":None,#OPCIONAL
        "bordeColor":'#19211f',#OPCIONAL
        "bordeSize":2,#OPCIONAL
        "bordeRadio":10,#OPCIONAL
        "fontType":'Comic Sans MS',#OPCIONAL
        "fontSize":14,#OPCIONAL
        "fontColor":'#ffa000',#OPCIONAL
        "fontMostrar":True,#AUTOMATICO/OPCIONAL
        "padre":None,#AUTOMATICO/OPCIONAL
        "hijo":None,#AUTOMATICO/OPCIONAL
        "stileId":'',#OPCIONAL
        "stileClass":'',#OPCIONAL
        "urlDir":None,#OPCIONAL
        "fileDir":None,#OPCIONAL
        "fileType":None,#OPCIONAL
        "fileName":None,#AUTOMATICO
        "tipoDeVista":'SegunEspacioEnX ',#AUTOMATICO
        'relief':None,
        'borde':None,
        'cursor':None,
        'fill':None,
        'expand':1,
        'side':None,
        'widget':None,
        'justify':None,
        'anchor':None ,
        'img':""},
    "Button":{
    	'inputType':"Button",
        "id":None,#AUTOMATICO
        "descripcion":"objeto de la clase tkinter.Button(), es un objeto Button de Tkinter, posee todos los metodos y atributos de un Button()",#OBLIGATORIO
        "etiquetas":['id','botontk','name','typeSalida','text'],#AUTOMATICO/OBLIGATORIO
        "typeSalida":"command",#OPCIONAL
        "name":'Botonio',#OBLIGATORIO
        "text":'Boton Tkinter',#OBLIGATORIO
        "value":'',#OPCIONAL
        "max":None,#OPCIONAL
        "min":None,#OPCIONAL
        "step":None,#OPCIONAL
        "ancho":150,#OPCIONAL
        "alto":20,#OPCIONAL
        "width":13,#OPCIONAL
        "xPlace":0,#AUTOMATICO
        "yPlace":0,#AUTOMATICO
        "visible":1,#OPCIONAL
        "editable":1,#OPCIONAL
        "degradado":0,#OPCIONAL
        "bgColor":'#00417f',#OPCIONAL
        "fgColor":'#040407',#OPCIONAL
        "bgRelleno":None,#OPCIONAL
        "bordeColor":'#19211f',#OPCIONAL
        "bordeSize":2,#OPCIONAL
        "bordeRadio":10,#OPCIONAL
        "fontType":'Comic Sans MS',#OPCIONAL
        "fontSize":14,#OPCIONAL
        "fontColor":'#ffa000',#OPCIONAL
        "fontMostrar":True,#AUTOMATICO/OPCIONAL
        "padre":None,#AUTOMATICO/OPCIONAL
        "hijo":None,#AUTOMATICO/OPCIONAL
        "stileId":'botontk',#OPCIONAL
        "stileClass":'botontk',#OPCIONAL
        "urlDir":None,#OPCIONAL
        "fileDir":None,#OPCIONAL
        "fileType":None,#OPCIONAL
        "fileName":None,#AUTOMATICO
        "tipoDeVista":'SegunEspacioEnX ',#AUTOMATICO
        'relief':None,
        'borde':None,
        'cursor':None,
        'fill':None,
        'expand':1,
        'side':None,
        'widget':None,
        'justify':None,
        'anchor':None ,
        'img':""},
    "ButtonMbarete":{
    	'inputType':"ButtonMbarete",
        "id":None,#AUTOMATICO
        "descripcion":"Es un dibujo en el lienzo canvas, asignara el area que ocupa el dibujo a un comando. Este lienzo detectara los click del raton y si el click esta dentro del area que fue asignada al comando este comando sera ejecutado.",#OBLIGATORIO
        "etiquetas":['id','botoncanvas','botonMbarete','typeSalida','text'],#AUTOMATICO/OBLIGATORIO
        "typeSalida":"command",#OPCIONAL
        "name":'Botonio',#OBLIGATORIO
        "text":'Boton Canvas',#OBLIGATORIO
        "value":'',#OPCIONAL
        "max":None,#OPCIONAL
        "min":None,#OPCIONAL
        "step":None,#OPCIONAL
        "ancho":150,#OPCIONAL
        "alto":20,#OPCIONAL
        "width":13,#OPCIONAL
        "xPlace":0,#AUTOMATICO
        "yPlace":0,#AUTOMATICO
        "visible":1,#OPCIONAL
        "editable":1,#OPCIONAL
        "degradado":0,#OPCIONAL
        "bgColor":'#00417f',#OPCIONAL
        "fgColor":'#040407',#OPCIONAL
        "bgRelleno":None,#OPCIONAL
        "bordeColor":'#19211f',#OPCIONAL
        "bordeSize":2,#OPCIONAL
        "bordeRadio":10,#OPCIONAL
        "fontType":'Comic Sans MS',#OPCIONAL
        "fontSize":14,#OPCIONAL
        "fontColor":'#ffa000',#OPCIONAL
        "fontMostrar":True,#AUTOMATICO/OPCIONAL
        "padre":None,#AUTOMATICO/OPCIONAL
        "hijo":None,#AUTOMATICO/OPCIONAL
        "stileId":'botoncanvas',#OPCIONAL
        "stileClass":'botoncanvas',#OPCIONAL
        "urlDir":None,#OPCIONAL
        "fileDir":None,#OPCIONAL
        "fileType":None,#OPCIONAL
        "fileName":None,#AUTOMATICO
        "tipoDeVista":'SegunEspacioEnX ',#AUTOMATICO
        'relief':None,
        'borde':None,
        'cursor':None,
        'fill':None,
        'expand':1,
        'side':None,
        'widget':None,
        'justify':None,
        'anchor':None ,
        'img':""},
    "Label":{
    	'inputType':"Label",
        "id":None,#AUTOMATICO
        "descripcion":"",#OBLIGATORIO
        "etiquetas":['id','labelTk','name','typeSalida','text'],#AUTOMATICO/OBLIGATORIO
        "typeSalida":None,#OPCIONAL
        "name":'Label',#OBLIGATORIO
        "text":'Label Tkinter',#OBLIGATORIO
        "value":'',#OPCIONAL
        "max":None,#OPCIONAL
        "min":None,#OPCIONAL
        "step":None,#OPCIONAL
        "ancho":150,#OPCIONAL
        "alto":20,#OPCIONAL
        "width":13,#OPCIONAL
        "xPlace":0,#AUTOMATICO
        "yPlace":0,#AUTOMATICO
        "visible":1,#OPCIONAL
        "editable":0,#OPCIONAL
        "degradado":0,#OPCIONAL
        "bgColor":'#00417f',#OPCIONAL
        "fgColor":'#040407',#OPCIONAL
        "bgRelleno":None,#OPCIONAL
        "bordeColor":'#19211f',#OPCIONAL
        "bordeSize":2,#OPCIONAL
        "bordeRadio":10,#OPCIONAL
        "fontType":'Comic Sans MS',#OPCIONAL
        "fontSize":14,#OPCIONAL
        "fontColor":'#ffa000',#OPCIONAL
        "fontMostrar":True,#AUTOMATICO/OPCIONAL
        "padre":None,#AUTOMATICO/OPCIONAL
        "hijo":None,#AUTOMATICO/OPCIONAL
        "stileId":'botoncanvas',#OPCIONAL
        "stileClass":'botoncanvas',#OPCIONAL
        "urlDir":None,#OPCIONAL
        "fileDir":None,#OPCIONAL
        "fileType":None,#OPCIONAL
        "fileName":None,#AUTOMATICO
        "tipoDeVista":'SegunEspacioEnX ',#AUTOMATICO
        'relief':None,
        'borde':None,
        'cursor':None,
        'fill':None,
        'expand':1,
        'side':None,
        'widget':None,
        'justify':None,
        'anchor':None ,
        'img':""},
    "LabelCanvas":{
    	'inputType':"LabelCanvas",
        "id":None,#AUTOMATICO
        "descripcion":"",#OBLIGATORIO
        "etiquetas":['id','labelCanvas','name','typeSalida','text'],#AUTOMATICO/OBLIGATORIO
        "typeSalida":None,#OPCIONAL
        "name":'LabelCanvas',#OBLIGATORIO
        "text":'Label Canvas',#OBLIGATORIO
        "value":'',#OPCIONAL
        "max":None,#OPCIONAL
        "min":None,#OPCIONAL
        "step":None,#OPCIONAL
        "ancho":150,#OPCIONAL
        "alto":20,#OPCIONAL
        "width":13,#OPCIONAL
        "xPlace":0,#AUTOMATICO
        "yPlace":0,#AUTOMATICO
        "visible":1,#OPCIONAL
        "editable":0,#OPCIONAL
        "degradado":0,#OPCIONAL
        "bgColor":'#00417f',#OPCIONAL
        "fgColor":'#040407',#OPCIONAL
        "bgRelleno":None,#OPCIONAL
        "bordeColor":'#19211f',#OPCIONAL
        "bordeSize":2,#OPCIONAL
        "bordeRadio":10,#OPCIONAL
        "fontType":'Comic Sans MS',#OPCIONAL
        "fontSize":14,#OPCIONAL
        "fontColor":'#ffa000',#OPCIONAL
        "fontMostrar":True,#AUTOMATICO/OPCIONAL
        "padre":None,#AUTOMATICO/OPCIONAL
        "hijo":None,#AUTOMATICO/OPCIONAL
        "stileId":'labelCanvas',#OPCIONAL
        "stileClass":'labelCanvas',#OPCIONAL
        "urlDir":None,#OPCIONAL
        "fileDir":None,#OPCIONAL
        "fileType":None,#OPCIONAL
        "fileName":None,#AUTOMATICO
        "tipoDeVista":'SegunEspacioEnX ',#AUTOMATICO
        'relief':None,
        'borde':None,
        'cursor':None,
        'fill':None,
        'expand':1,
        'side':None,
        'widget':None,
        'justify':None,
        'anchor':None ,
        'img':""},
    "Entry":{
        'inputType':"Entry",
        "id":None,#AUTOMATICO
        "descripcion":"Entry sin validacion, para uso general",#OBLIGATORIO
        "etiquetas":['id','','name','typeSalida','text'],#AUTOMATICO/OBLIGATORIO
        "typeSalida":"TYPESALIDA",#OPCIONAL
        "name":'NAME',#OBLIGATORIO
        "text":'TEXT',#OBLIGATORIO
        "value":'',#OPCIONAL
        "max":None,#OPCIONAL
        "min":None,#OPCIONAL
        "step":None,#OPCIONAL
        "ancho":150,#OPCIONAL
        "alto":20,#OPCIONAL
        "width":13,#OPCIONAL
        "xPlace":0,#AUTOMATICO
        "yPlace":0,#AUTOMATICO
        "visible":1,#OPCIONAL
        "editable":1,#OPCIONAL
        "degradado":0,#OPCIONAL
        "bgColor":'#00417f',#OPCIONAL
        "fgColor":'#040407',#OPCIONAL
        "bgRelleno":None,#OPCIONAL
        "bordeColor":'#19211f',#OPCIONAL
        "bordeSize":2,#OPCIONAL
        "bordeRadio":10,#OPCIONAL
        "fontType":'Comic Sans MS',#OPCIONAL
        "fontSize":14,#OPCIONAL
        "fontColor":'#ffa000',#OPCIONAL
        "fontMostrar":True,#AUTOMATICO/OPCIONAL
        "padre":None,#AUTOMATICO/OPCIONAL
        "hijo":None,#AUTOMATICO/OPCIONAL
        "stileId":'',#OPCIONAL
        "stileClass":'',#OPCIONAL
        "urlDir":None,#OPCIONAL
        "fileDir":None,#OPCIONAL
        "fileType":None,#OPCIONAL
        "fileName":None,#AUTOMATICO
        "tipoDeVista":'SegunEspacioEnX ',#AUTOMATICO
        'relief':None,
        'borde':None,
        'cursor':None,
        'fill':None,
        'expand':1,
        'side':None,
        'widget':None,
        'justify':None,
        'anchor':None,
        'img':""},
    "Radiobutton":{
        'inputType':"Radiobutton",
        "id":None,#AUTOMATICO
        "descripcion":"Radiobutton para seleccionar solo un elemento de la Lista",#OBLIGATORIO
        "etiquetas":['id','','name','typeSalida','text'],#AUTOMATICO/OBLIGATORIO
        "typeSalida":"TYPESALIDA",#OPCIONAL
        "name":'NAME',#OBLIGATORIO
        "text":'TEXT',#OBLIGATORIO
        "value":0,#OPCIONAL
        "max":None,#OPCIONAL
        "min":None,#OPCIONAL
        "step":None,#OPCIONAL
        "ancho":150,#OPCIONAL
        "alto":30,#OPCIONAL
        "width":13,#OPCIONAL
        "xPlace":0,#AUTOMATICO
        "yPlace":0,#AUTOMATICO
        "visible":1,#OPCIONAL
        "editable":1,#OPCIONAL
        "degradado":0,#OPCIONAL
        "bgColor":'#00417f',#OPCIONAL
        "fgColor":'#040407',#OPCIONAL
        "bgRelleno":None,#OPCIONAL
        "bordeColor":'#19211f',#OPCIONAL
        "bordeSize":2,#OPCIONAL
        "bordeRadio":10,#OPCIONAL
        "fontType":'Comic Sans MS',#OPCIONAL
        "fontSize":14,#OPCIONAL
        "fontColor":'#ffa000',#OPCIONAL
        "fontMostrar":True,#AUTOMATICO/OPCIONAL
        "padre":None,#AUTOMATICO/OPCIONAL
        "hijo":None,#AUTOMATICO/OPCIONAL
        "stileId":'',#OPCIONAL
        "stileClass":'',#OPCIONAL
        "urlDir":None,#OPCIONAL
        "fileDir":None,#OPCIONAL
        "fileType":None,#OPCIONAL
        "fileName":None,#AUTOMATICO
        "tipoDeVista":'SegunEspacioEnX ',#AUTOMATICO
        'relief':None,
        'borde':None,
        'cursor':None,
        'fill':None,
        'expand':1,
        'side':None,
        'widget':None,
        'justify':None,
        'anchor':None,
        'img':""},
    "Checkbutton":{
        'inputType':"Checkbutton",
        "id":None,#AUTOMATICO
        "descripcion":"Checkbutton sin validacion, para uso general",#OBLIGATORIO
        "etiquetas":['id','','name','typeSalida','text'],#AUTOMATICO/OBLIGATORIO
        "typeSalida":"TYPESALIDA",#OPCIONAL
        "name":'NAME',#OBLIGATORIO
        "text":'TEXT',#OBLIGATORIO
        "value":0,#OPCIONAL
        "max":None,#OPCIONAL
        "min":None,#OPCIONAL
        "step":None,#OPCIONAL
        "ancho":150,#OPCIONAL
        "alto":30,#OPCIONAL
        "width":13,#OPCIONAL
        "xPlace":0,#AUTOMATICO
        "yPlace":0,#AUTOMATICO
        "visible":1,#OPCIONAL
        "editable":1,#OPCIONAL
        "bgColor":'#00417f',#OPCIONAL
        "bgRelleno":None,#OPCIONAL
        "bordeColor":'#19211f',#OPCIONAL
        "bordeSize":2,#OPCIONAL
        "bordeRadio":10,#OPCIONAL
        "fontType":'Comic Sans MS',#OPCIONAL
        "fontSize":14,#OPCIONAL
        "fontColor":'#ffa000',#OPCIONAL
        "fontMostrar":True,#AUTOMATICO/OPCIONAL
        "padre":None,#AUTOMATICO/OPCIONAL
        "hijo":None,#AUTOMATICO/OPCIONAL
        "stileId":'',#OPCIONAL
        "stileClass":'',#OPCIONAL
        "urlDir":None,#OPCIONAL
        "fileDir":None,#OPCIONAL
        "fileType":None,#OPCIONAL
        "fileName":None,#AUTOMATICO
        "tipoDeVista":'SegunEspacioEnX ',#AUTOMATICO
        'relief':None,
        'borde':None,
        'cursor':None,
        'fill':None,
        'expand':1,
        'side':None,
        'widget':None,
        'justify':None,
        'anchor':None,
        'img':""},
    "boolean":None,
    "date":None,
    "textbox":None,
    "scrolledtext":None,
    "password":None,
    "email":None,
    "sound":None,
    "direccion":None,
    "telefono":None,
    "slidebar":None,
    "filedialog":None,
    "fontchoser":None,
    "colorchoser":None,
    "photoimage":None,
    "selectlist":None,
    "menu":None }
