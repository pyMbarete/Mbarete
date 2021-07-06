#!/usr/bin/env python
# -*- coding: latin-1 -*-
atributos={
    'user':{
        'clave':"user",
        'valor':Hall 9000
    },
    'titulo':{
        'clave':"titulo",
        'valor':Mbarete
    },
    'bbdd':{
        'clave':"bbdd",
        'valor':Mbarete.sql
    },
    'modoDesarrollador':{
        'clave':"modoDesarrollador",
        'valor':1
    },
    'ancho':{
        'clave':"ancho",
        'valor':1000
    },
    'alto':{
        'clave':"alto",
        'valor':600
    },
    'Xexterior':{
        'clave':"Xexterior",
        'valor':10
    },
    'Yexterior':{
        'clave':"Yexterior",
        'valor':10
    },
    'fontSizeToAlto':{
        'clave':"fontSizeToAlto",
        'valor':{'Arial': [0, 4, 7, 9, 11, 12, 18, 21, 25, 26, 28, 30, 32, 33, 39, 40, 42, 46, 47, 49, 56, 56, 58, 61, 63, 67, 70, 72, 74, 77, 79, 82, 86, 88], 'Comic Sans MS': [0, 5, 7, 9, 12, 18, 18, 23, 26, 30, 32, 35, 40, 42, 46, 49, 51, 54, 58, 60, 67, 68, 70, 77, 79, 81, 86, 89, 91, 95, 98, 100, 105, 107]}
    },
    'fontSizeToCorrectorAncho':{
        'clave':"fontSizeToCorrectorAncho",
        'valor':{'Comic Sans MS': [1, 1, 1, 0, 0, 0, 0, 0, 0, -1.0, -1.0, -1.0, -1.0, -2.0, -2.0, -2.0, -2.0, -2.0, -2.0, -3.0, -3.0, -3.0, -3.0, -3.0, -3.0, -4.0, -4.0, -4.0, -5.0, -4.0, -5.0, -5.0, -5.0, -5.0, -5.0, -5.0], 'Arial': [1, 1, 1, 0, 0, 0, 0, 0, -1.0, -1.0, -1.0, -1.0, -2.0, -3.0, -2.0, -3.0, -3.0, -3.0, -3.0, -3.0, -3.0, -4.0, -4.0, -4.0, -4.0, -5.0, -5.0, -5.0, -5.0, -5.0, -6.0, -6.0, -6.0, -6.0, -6.0, -6.0]}
    },
    'colorFondo':{
        'clave':"colorFondo",
        'valor':#e0e0ff
    },
    'fondo':{
        'clave':"fondo",
        'valor':#f0f0ff
    },
    'colorSeleccion_a':{
        'clave':"colorSeleccion_a",
        'valor':#893301
    },
    'colorTitulo':{
        'clave':"colorTitulo",
        'valor':#000f00
    },
    'foco':{
        'clave':"foco",
        'valor':Raiz
    },
    'scrollVerticalAncho':{
        'clave':"scrollVerticalAncho",
        'valor':16
    },
    'scrollHorizontalAlto':{
        'clave':"scrollHorizontalAlto",
        'valor':16
    },
    'espacioHorizontalEntreWidgets':{
        'clave':"espacioHorizontalEntreWidgets",
        'valor':20
    },
    'espacioVerticalEntreWidgets':{
        'clave':"espacioVerticalEntreWidgets",
        'valor':20
    },
    'transicion':{
        'clave':"transicion",
        'valor':manager
    },
    'subtransicion':{
        'clave':"subtransicion",
        'valor':Inicio
    },
    'frameActivo':{
        'clave':"frameActivo",
        'valor':
    },
    'botonAncho':{
        'clave':"botonAncho",
        'valor':1000
    },
    'botonAlto':{
        'clave':"botonAlto",
        'valor':600
    },
    'menuAlto':{
        'clave':"menuAlto",
        'valor':600
    },
    'menuAncho':{
        'clave':"menuAncho",
        'valor':1000
    }
}

inputType={
    'help':{
        'clave':"help",
        'valor':{'inputType': 'help', 'id': 'NUMERO GENERADO AUTOMATICAMENTE PARA EL INPUT', 'descripcion': 'breve descripcion del input, podra mostrarse en pantalla si es necesario', 'etiquetas': 'conjuntos de etiquetas vinculadas al input', 'typeSalida': "formato del dato de salida del input algunos input tienen su salida por defecto ['str'/'int'/'float'/'bool'/'date'/'bytes']", 'name': "dentro del diccionario que retornara el form, este parametro del input es el 'nombre_clave' que estara asignado al dato de salida del input, tambien es el nombre que usaremos para vincular la salida de este input con el campo de la tabla correspondiente al form", 'text': 'nombre del input que sera mostrado en pantalla, para el usuario final', 'value': 'valor por defecto que se le asignara al input al iniciar el form', 'max': 'segun el tipo de input podemos asignar un maximo, para que no valide el form si el parametro supera el maximo asignado, este parametro estara mejor explicado en la funcion de validacion del form', 'min': "lo mismo que 'max' pero desde abajo, los parametros max y min siempre estan incluidos dentro de los limites respectivos [MIN:MAX]", 'step': 'como seran tomados los datos cada n dias, numeros, letras. este parametro solo alpica a algunos input', 'ancho': 'el ancho en pixeles que ocupa el input en el eje x, en pantalla', 'alto': 'el alto en pixeles que ocupa el input en el eje y, en pantalla', 'width': 13, 'xPlace': 'la posicion en x, en pixeles de la ezquina superio izquierda del input, dentro del form', 'yPlace': 'la posicion en y, en pixeles de la ezquina superio izquierda del input, dentro del form', 'visible': 'si el input esta habilitado para ser editado', 'editable': 'si el input esta habilitado para ser editado', 'degradado': 0, 'bgColor': "el color del fondo del input en hexagesimal, ejem: '#00417f'", 'bgRelleno': "en caso de tener habilitado 'photoImage' para poder ponerle al input una imagen de fondo", 'bordeColor': "color de la linea que bordea el input en hexagesimal ejem: '#00417f'", 'bordeSize': 'grosor de la linea que bordea el input en pixeles', 'bordeRadio': 'radio interno de las curvas en pixeles, en todas las ezquina del input', 'fontType': 'el estilo de letras en el input, ejemplo: Comic Sans Ms ', 'fontSize': 'tamaño de las letras en el input', 'fontColor': 'color del texto en el input', 'fontMostrar': "si es legible, que el texto sea visible y legible, sino seran remplazados todos los caracters del texto por '*'", 'padre': 'la name del input que controla a este, generalmente los input hijos son creados automaticamente y deben ser identificados por el name padre', 'hijo': 'la name del unico hijo al cual debe llamar, el input hijo de este puede ser el input padre de otros input', 'stileId': 'en caso de usar estilos de css en algun momento, para asignar un atributo al input', 'stileClass': 'en caso de usar estilos de css en algun momento, para asignar una clase al input', 'urlDir': "direccion url vinculada al input, ejemplo:'https://www.facebook.com/profile/32154613'", 'fileDir': 'archivo vinculado al input', 'fileType': 'formato del archivo vinculado al input', 'fileName': 'nombre del archivo vinculado al input', 'tipoDeVista': 'como se podra mostrar el conjuntos de elemento o inputs hijos que pertenescan a este input, ejemplo:listaSimple/listaDetallada/segunEspacioEnX/segunEspacioEnY/matrizFija/ ', 'relief': 'tipo de borde [sunken/]', 'borde': 'grosor del borde', 'cursor': 'cambiar el cursor [heart/]', 'fill': "el widget ocupara todo el espacio disponible en 'X' o 'Y', o ambos con 'both',  ['X'/'Y'/'both'/'none']", 'expand': "el widget si puede cambiar de tamaño una vez iniciado el programa [0/1/'True'/'False']", 'side': "para asignar la posicon del widget ['left'/'right'/'top'/'bottom']", 'widget': 'El objeto TKINTER', 'justify': 'left', 'anchor': 'E', 'command': 'nombre asignado al comando que eventualmente debe ejecutar el widget', 'img': 'imagen asignada al widget'}
    },
    'Frame':{
        'clave':"Frame",
        'valor':{'inputType': 'Frame', 'id': 'None', 'descripcion': 'Es el Frame principal, este widget puede ser manipulado como un Frame Normal.', 'etiquetas': ['id', '', 'name', 'Frame', 'menu'], 'typeSalida': 'command', 'name': 'Menu', 'text': 'Menu', 'value': '', 'max': 'None', 'min': 'None', 'step': 'None', 'crearTabla': 0, 'ancho': 500, 'alto': 500, 'width': 13, 'xPlace': 0, 'yPlace': 0, 'visible': 1, 'editable': 1, 'degradado': 0, 'bgColor': '#00417f', 'fgColor': '#040407', 'bgRelleno': 'None', 'bordeColor': '#19211f', 'bordeSize': 2, 'bordeRadio': 10, 'fontType': 'Comic Sans MS', 'fontSize': 14, 'fontColor': '#ffa000', 'fontMostrar': True, 'padre': 'None', 'hijo': 'None', 'stileId': '', 'stileClass': '', 'urlDir': 'None', 'fileDir': 'None', 'fileType': 'None', 'fileName': 'None', 'tipoDeVista': 'None', 'relief': 'None', 'borde': 'None', 'cursor': 'None', 'fill': 'none', 'expand': 1, 'side': 'None', 'widget': 'None', 'justify': 'None', 'anchor': 'None', 'img': ''}
    },
    'panel':{
        'clave':"panel",
        'valor':{'inputType': 'panel', 'id': 'None', 'descripcion': 'Input Para ejecutar funciones solo botones y entrys', 'etiquetas': ['id', '', 'panel', 'typeSalida', 'panel'], 'typeSalida': 'command', 'name': 'panel', 'text': 'Panel', 'value': '', 'max': 'None', 'min': 'None', 'step': 'None', 'ancho': 500, 'alto': 500, 'width': 13, 'xPlace': 0, 'yPlace': 0, 'visible': 1, 'editable': 1, 'degradado': 0, 'bgColor': '#00417f', 'fgColor': '#040407', 'bgRelleno': 'None', 'bordeColor': '#19211f', 'bordeSize': 2, 'bordeRadio': 10, 'fontType': 'Comic Sans MS', 'fontSize': 14, 'fontColor': '#ffa000', 'fontMostrar': True, 'padre': 'None', 'hijo': 'None', 'stileId': '', 'stileClass': '', 'urlDir': 'None', 'fileDir': 'None', 'fileType': 'None', 'fileName': 'None', 'tipoDeVista': 'None', 'relief': 'None', 'borde': 'None', 'cursor': 'None', 'fill': 'none', 'expand': 1, 'side': 'None', 'widget': 'None', 'justify': 'None', 'anchor': 'None', 'img': ''}
    },
    'formIn':{
        'clave':"formIn",
        'valor':{'inputType': 'formIn', 'id': 'None', 'descripcion': 'Input para Diseño de Formulario', 'etiquetas': ['id', '', 'name', 'typeSalida', 'text'], 'typeSalida': 'TYPESALIDA', 'name': 'NAME', 'text': 'TEXT', 'value': '', 'max': 'None', 'min': 'None', 'step': 'None', 'ancho': 500, 'alto': 700, 'width': 13, 'xPlace': 0, 'yPlace': 0, 'visible': 1, 'editable': 1, 'degradado': 0, 'bgColor': '#00417f', 'fgColor': '#040407', 'bgRelleno': 'None', 'bordeColor': '#19211f', 'bordeSize': 2, 'bordeRadio': 10, 'fontType': 'Comic Sans MS', 'fontSize': 14, 'fontColor': '#ffa000', 'fontMostrar': True, 'padre': 'None', 'hijo': 'None', 'stileId': '', 'stileClass': '', 'urlDir': 'None', 'fileDir': 'None', 'fileType': 'None', 'fileName': 'None', 'tipoDeVista': 'SegunEspacioEnX ', 'relief': 'None', 'borde': 'None', 'cursor': 'None', 'fill': 'None', 'expand': 1, 'side': 'None', 'widget': 'None', 'justify': 'None', 'anchor': 'None', 'img': ''}
    },
    'formOut':{
        'clave':"formOut",
        'valor':{'inputType': 'formOut', 'id': 'None', 'descripcion': 'Input para Informes y Graficos', 'etiquetas': ['id', '', 'name', 'Graficos', 'Informes'], 'typeSalida': 'TYPESALIDA', 'name': 'NAME', 'text': 'TEXT', 'value': '', 'max': 'None', 'min': 'None', 'step': 'None', 'ancho': 500, 'alto': 700, 'width': 13, 'xPlace': 0, 'yPlace': 0, 'visible': 1, 'editable': 1, 'degradado': 0, 'bgColor': '#00417f', 'fgColor': '#040407', 'bgRelleno': 'None', 'bordeColor': '#19211f', 'bordeSize': 2, 'bordeRadio': 10, 'fontType': 'Comic Sans MS', 'fontSize': 14, 'fontColor': '#ffa000', 'fontMostrar': True, 'padre': 'None', 'hijo': 'None', 'stileId': '', 'stileClass': '', 'urlDir': 'None', 'fileDir': 'None', 'fileType': 'None', 'fileName': 'None', 'tipoDeVista': 'SegunEspacioEnX ', 'relief': 'None', 'borde': 'None', 'cursor': 'None', 'fill': 'None', 'expand': 1, 'side': 'None', 'widget': 'None', 'justify': 'None', 'anchor': 'None', 'img': ''}
    },
    'Button':{
        'clave':"Button",
        'valor':{'inputType': 'Button', 'id': 'None', 'descripcion': 'objeto de la clase tkinter.Button(), es un objeto Button de Tkinter, posee todos los metodos y atributos de un Button()', 'etiquetas': ['id', 'botontk', 'name', 'typeSalida', 'text'], 'typeSalida': 'command', 'name': 'Botonio', 'text': 'Boton Tkinter', 'value': '', 'max': 'None', 'min': 'None', 'step': 'None', 'ancho': 150, 'alto': 20, 'width': 13, 'xPlace': 0, 'yPlace': 0, 'visible': 1, 'editable': 1, 'degradado': 0, 'bgColor': '#00417f', 'fgColor': '#040407', 'bgRelleno': 'None', 'bordeColor': '#19211f', 'bordeSize': 2, 'bordeRadio': 10, 'fontType': 'Comic Sans MS', 'fontSize': 14, 'fontColor': '#ffa000', 'fontMostrar': True, 'padre': 'None', 'hijo': 'None', 'stileId': 'botontk', 'stileClass': 'botontk', 'urlDir': 'None', 'fileDir': 'None', 'fileType': 'None', 'fileName': 'None', 'tipoDeVista': 'SegunEspacioEnX ', 'relief': 'None', 'borde': 'None', 'cursor': 'None', 'fill': 'None', 'expand': 1, 'side': 'None', 'widget': 'None', 'justify': 'None', 'anchor': 'None', 'img': ''}
    },
    'ButtonMbarete':{
        'clave':"ButtonMbarete",
        'valor':{'inputType': 'ButtonMbarete', 'id': 'None', 'descripcion': 'Es un dibujo en el lienzo canvas, asignara el area que ocupa el dibujo a un comando. Este lienzo detectara los click del raton y si el click esta dentro del area que fue asignada al comando este comando sera ejecutado.', 'etiquetas': ['id', 'botoncanvas', 'botonMbarete', 'typeSalida', 'text'], 'typeSalida': 'command', 'name': 'Botonio', 'text': 'Boton Canvas', 'value': '', 'max': 'None', 'min': 'None', 'step': 'None', 'ancho': 150, 'alto': 20, 'width': 13, 'xPlace': 0, 'yPlace': 0, 'visible': 1, 'editable': 1, 'degradado': 0, 'bgColor': '#00417f', 'fgColor': '#040407', 'bgRelleno': 'None', 'bordeColor': '#19211f', 'bordeSize': 2, 'bordeRadio': 10, 'fontType': 'Comic Sans MS', 'fontSize': 14, 'fontColor': '#ffa000', 'fontMostrar': True, 'padre': 'None', 'hijo': 'None', 'stileId': 'botoncanvas', 'stileClass': 'botoncanvas', 'urlDir': 'None', 'fileDir': 'None', 'fileType': 'None', 'fileName': 'None', 'tipoDeVista': 'SegunEspacioEnX ', 'relief': 'None', 'borde': 'None', 'cursor': 'None', 'fill': 'None', 'expand': 1, 'side': 'None', 'widget': 'None', 'justify': 'None', 'anchor': 'None', 'img': ''}
    },
    'Label':{
        'clave':"Label",
        'valor':{'inputType': 'Label', 'id': 'None', 'descripcion': '', 'etiquetas': ['id', 'labelTk', 'name', 'typeSalida', 'text'], 'typeSalida': 'None', 'name': 'Label', 'text': 'Label Tkinter', 'value': '', 'max': 'None', 'min': 'None', 'step': 'None', 'ancho': 150, 'alto': 20, 'width': 13, 'xPlace': 0, 'yPlace': 0, 'visible': 1, 'editable': 0, 'degradado': 0, 'bgColor': '#00417f', 'fgColor': '#040407', 'bgRelleno': 'None', 'bordeColor': '#19211f', 'bordeSize': 2, 'bordeRadio': 10, 'fontType': 'Comic Sans MS', 'fontSize': 14, 'fontColor': '#ffa000', 'fontMostrar': True, 'padre': 'None', 'hijo': 'None', 'stileId': 'botoncanvas', 'stileClass': 'botoncanvas', 'urlDir': 'None', 'fileDir': 'None', 'fileType': 'None', 'fileName': 'None', 'tipoDeVista': 'SegunEspacioEnX ', 'relief': 'None', 'borde': 'None', 'cursor': 'None', 'fill': 'None', 'expand': 1, 'side': 'None', 'widget': 'None', 'justify': 'None', 'anchor': 'None', 'img': ''}
    },
    'LabelCanvas':{
        'clave':"LabelCanvas",
        'valor':{'inputType': 'LabelCanvas', 'id': 'None', 'descripcion': '', 'etiquetas': ['id', 'labelCanvas', 'name', 'typeSalida', 'text'], 'typeSalida': 'None', 'name': 'LabelCanvas', 'text': 'Label Canvas', 'value': '', 'max': 'None', 'min': 'None', 'step': 'None', 'ancho': 150, 'alto': 20, 'width': 13, 'xPlace': 0, 'yPlace': 0, 'visible': 1, 'editable': 0, 'degradado': 0, 'bgColor': '#00417f', 'fgColor': '#040407', 'bgRelleno': 'None', 'bordeColor': '#19211f', 'bordeSize': 2, 'bordeRadio': 10, 'fontType': 'Comic Sans MS', 'fontSize': 14, 'fontColor': '#ffa000', 'fontMostrar': True, 'padre': 'None', 'hijo': 'None', 'stileId': 'labelCanvas', 'stileClass': 'labelCanvas', 'urlDir': 'None', 'fileDir': 'None', 'fileType': 'None', 'fileName': 'None', 'tipoDeVista': 'SegunEspacioEnX ', 'relief': 'None', 'borde': 'None', 'cursor': 'None', 'fill': 'None', 'expand': 1, 'side': 'None', 'widget': 'None', 'justify': 'None', 'anchor': 'None', 'img': ''}
    },
    'Entry':{
        'clave':"Entry",
        'valor':{'inputType': 'Entry', 'id': 'None', 'descripcion': 'Entry sin validacion, para uso general', 'etiquetas': ['id', '', 'name', 'typeSalida', 'text'], 'typeSalida': 'TYPESALIDA', 'name': 'NAME', 'text': 'TEXT', 'value': '', 'max': 'None', 'min': 'None', 'step': 'None', 'ancho': 150, 'alto': 20, 'width': 13, 'xPlace': 0, 'yPlace': 0, 'visible': 1, 'editable': 1, 'degradado': 0, 'bgColor': '#00417f', 'fgColor': '#040407', 'bgRelleno': 'None', 'bordeColor': '#19211f', 'bordeSize': 2, 'bordeRadio': 10, 'fontType': 'Comic Sans MS', 'fontSize': 14, 'fontColor': '#ffa000', 'fontMostrar': True, 'padre': 'None', 'hijo': 'None', 'stileId': '', 'stileClass': '', 'urlDir': 'None', 'fileDir': 'None', 'fileType': 'None', 'fileName': 'None', 'tipoDeVista': 'SegunEspacioEnX ', 'relief': 'None', 'borde': 'None', 'cursor': 'None', 'fill': 'None', 'expand': 1, 'side': 'None', 'widget': 'None', 'justify': 'None', 'anchor': 'None', 'img': ''}
    },
    'Radiobutton':{
        'clave':"Radiobutton",
        'valor':{'inputType': 'Radiobutton', 'id': 'None', 'descripcion': 'Radiobutton para seleccionar solo un elemento de la Lista', 'etiquetas': ['id', '', 'name', 'typeSalida', 'text'], 'typeSalida': 'TYPESALIDA', 'name': 'NAME', 'text': 'TEXT', 'value': 0, 'max': 'None', 'min': 'None', 'step': 'None', 'ancho': 150, 'alto': 30, 'width': 13, 'xPlace': 0, 'yPlace': 0, 'visible': 1, 'editable': 1, 'degradado': 0, 'bgColor': '#00417f', 'fgColor': '#040407', 'bgRelleno': 'None', 'bordeColor': '#19211f', 'bordeSize': 2, 'bordeRadio': 10, 'fontType': 'Comic Sans MS', 'fontSize': 14, 'fontColor': '#ffa000', 'fontMostrar': True, 'padre': 'None', 'hijo': 'None', 'stileId': '', 'stileClass': '', 'urlDir': 'None', 'fileDir': 'None', 'fileType': 'None', 'fileName': 'None', 'tipoDeVista': 'SegunEspacioEnX ', 'relief': 'None', 'borde': 'None', 'cursor': 'None', 'fill': 'None', 'expand': 1, 'side': 'None', 'widget': 'None', 'justify': 'None', 'anchor': 'None', 'img': ''}
    },
    'Checkbutton':{
        'clave':"Checkbutton",
        'valor':{'inputType': 'Checkbutton', 'id': 'None', 'descripcion': 'Checkbutton sin validacion, para uso general', 'etiquetas': ['id', '', 'name', 'typeSalida', 'text'], 'typeSalida': 'TYPESALIDA', 'name': 'NAME', 'text': 'TEXT', 'value': 0, 'max': 'None', 'min': 'None', 'step': 'None', 'ancho': 150, 'alto': 30, 'width': 13, 'xPlace': 0, 'yPlace': 0, 'visible': 1, 'editable': 1, 'bgColor': '#00417f', 'bgRelleno': 'None', 'bordeColor': '#19211f', 'bordeSize': 2, 'bordeRadio': 10, 'fontType': 'Comic Sans MS', 'fontSize': 14, 'fontColor': '#ffa000', 'fontMostrar': True, 'padre': 'None', 'hijo': 'None', 'stileId': '', 'stileClass': '', 'urlDir': 'None', 'fileDir': 'None', 'fileType': 'None', 'fileName': 'None', 'tipoDeVista': 'SegunEspacioEnX ', 'relief': 'None', 'borde': 'None', 'cursor': 'None', 'fill': 'None', 'expand': 1, 'side': 'None', 'widget': 'None', 'justify': 'None', 'anchor': 'None', 'img': ''}
    },
    'boolean':{
        'clave':"boolean",
        'valor':None
    },
    'date':{
        'clave':"date",
        'valor':None
    },
    'textbox':{
        'clave':"textbox",
        'valor':None
    },
    'scrolledtext':{
        'clave':"scrolledtext",
        'valor':None
    },
    'password':{
        'clave':"password",
        'valor':None
    },
    'email':{
        'clave':"email",
        'valor':None
    },
    'sound':{
        'clave':"sound",
        'valor':None
    },
    'direccion':{
        'clave':"direccion",
        'valor':None
    },
    'telefono':{
        'clave':"telefono",
        'valor':None
    },
    'slidebar':{
        'clave':"slidebar",
        'valor':None
    },
    'filedialog':{
        'clave':"filedialog",
        'valor':None
    },
    'fontchoser':{
        'clave':"fontchoser",
        'valor':None
    },
    'colorchoser':{
        'clave':"colorchoser",
        'valor':None
    },
    'photoimage':{
        'clave':"photoimage",
        'valor':None
    },
    'selectlist':{
        'clave':"selectlist",
        'valor':None
    },
    'menu':{
        'clave':"menu",
        'valor':None
    }
}

manager_formulario={
    '1':{
        'id':1,
        'nombres':"Lucas Mathias",
        'apellidos':"Villalab",
        'direccion':San Dubai
    },
    '2':{
        'id':2,
        'nombres':"Mandarina Dulce",
        'apellidos':"Citrico",
        'direccion':San Pandemia
    },
    '3':{
        'id':3,
        'nombres':"Mandarina Dulce",
        'apellidos':"Citrico",
        'direccion':San Panemia
    }
}

