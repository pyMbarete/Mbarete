#!/usr/bin/env python
# -*- coding: utf-8 -*-
# archivo generado por Diseño Libre para practicaImagenes
#Modulos importados
import os, sys, math
from tkinter import Label
from PIL import Image, ImageTk
info={
    'autor':'Lucas Mathias Villalba Diaz',
    'name':'practicaImagenes',
    'text':'Imagenes',
    'descripcionBreve':'PIL,ImageTK,Image',
    'descripcionLarga':'Pruebas con IMAGENES de los widgets de tkinter en la clase GUI del modulo Mbarete, editar, administrar, etc etc.',
    'img':'\\media\\img\\logo.png',
    'enlace':'mathiaslucasvidipy@gmail.com',
    'etiquetas':['default', 'Imagenes', 'PIL', 'Image', 'ImageTK', 'manipular Imagenes']
}
widgets={
    'practicaImagenesPanel':{
        'inputType':'panel',#OBLIGATORIO
        'etiquetas':['id','default','panel','practicaImagenes'],
        'name':'practicaImagenes',#OBLIGATORIO
        'text':'Inicio Imagenes',#OBLIGATORIO
        'anchor':'o',
        'inputs':{
            'inicio':{
                'inputType':'Button',
                'command':'manager',
                'text':'Administrador'
            },
            'showAlbum':{
                'inputType':'Button',
                'command':'showAlbum',
                'text':'Show Album'
            }
        }
    },
    'practicaImagenesFrame':{
        'inputType':'Frame',#OBLIGATORIO
        'etiquetas':['id','Inicio','Frame','practicaImagenes'],
        'name':'practicaImagenesFrame',#OBLIGATORIO
        'text':'Frame Imagenes',#OBLIGATORIO
        'inputs':{
            'inicio':{
                'inputType':'Button',
                'command':'manager',
                'text':'Administrador'
            }
        }
    }
}

canvas_width = 1100
canvas_height =1000
def showAlbum(admin,G,info,canvas_height=1000,canvas_width=1100,alto=200,ancho=500):
    pwd=info['info']['pwd']+'\\'+"media"+'\\'+"img"
    canvas_height=G.widgets[info['widget']['practicaImagenesFrame']]['alto']
    canvas_width=G.widgets[info['widget']['practicaImagenesFrame']]['ancho']
    alto=200
    ancho=500
    galeria=admin.ubi.directorio['SubCarpetas'][info['subProyecto']]['SubCarpetas']['media']['SubCarpetas']['img']['ficheros']
    lista=[galeria[i]['pwd'] for i in galeria if ('.png' in galeria[i]['tags'])]
    print("Archivos encontrados:",lista)
    miniatura={}
    contador=0
    #calculamos el alto en pixele que ocupara las imagenes en pantalla
    my_canvas_height=int(int(len(lista)/int(int(canvas_width/ancho)*ancho))*alto+alto)
    
    #raiz=Tk()
    #scrollbar=Scrollbar(raiz)
    #c = Canvas(raiz, yscrollcommand=scrollbar.set)
    #scrollbar.config(command=c.yview)
    #scrollbar.pack(side=RIGHT, fill=Y)
    #miFrameinicio=Frame(c)
    #miFrameinicio.configure(width = canvas_width, height=my_canvas_height)
    #canvas = Canvas(miFrameinicio, width=canvas_width, height=my_canvas_height)
    #canvas.place(x=0, y=0)
    #c.pack(side="left" , fill="both", expand=True)
    #c.create_window(0,0,window=miFrameinicio, anchor='nw')
    #c.config(scrollregion=c.bbox("all"))
    for y in range(0,my_canvas_height,int(alto)):
        for x in range(0,int(canvas_width-ancho),int(ancho)):
            if contador==len(lista):
                break
            img=Image.open(lista[contador])
            redimencionar=( ancho, int(img.size[1]*(ancho/img.size[0])) ) if img.size[0]>img.size[1] else ( int(img.size[0]*(alto/img.size[1])), alto )
            print(redimencionar,str(lista[contador]))
            if '.jpg' in str(lista[contador])[-5:]:
                img.save(lista[contador].replace('.jpg','.png'),'png')
                img=Image.open(lista[contador].replace('.jpg','.png'))
            miniatura[contador]={'img':img.resize(redimencionar)}
            miniatura[contador]['PhotoImage']=ImageTk.PhotoImage(miniatura[contador]['img'])
            #miniatura[contador]['widget']=Label(G.widgets[info['widget']['practicaImagenesFrame']]['widget'],image=miniatura[contador]['PhotoImage'])
            #miniatura[contador]['widget'].image=miniatura[contador]['PhotoImage']
            #miniatura[contador]['widget'].place(x=x,y=y)
            G.widgets[info['widget']['practicaImagenesFrame']]['canvas'].create_image(x+int((ancho-redimencionar[0])/2),y+int((alto-redimencionar[1])/2),image=miniatura[contador]['PhotoImage'],anchor='nw')
            if ".jpg" in str(lista[contador])[-5:]:
                os.remove(pwd+str(lista[contador]))
            contador=contador+1
    G.widgets[info['widget']['practicaImagenesFrame']]['canvas'].update()
    """
    c.config(scrollregion=c.bbox("all"))
    raiz.geometry(str(canvas_width)+"x"+str(canvas_height)+"+10+10")
    raiz.mainloop() 
    """
    
def editImagen(admin,G,info):
    pwd=info['info']['pwd']+'\\'+"media"+'\\'+"img"
    file=[str(img) for img in os.listdir(pwd) if (('.png' in img[-4:]) or ('.jpg' in img[-4:]))][0]
    print('Ubicacion:',pwd) #la direccion dela carpeta de donde sacara la imagen
    print('Imagen: ',file) #la primera imagen que se encuentre en la ubicacion de pwd
    #inicia codigo de la prueba
    im = Image.open(pwd+file)
    im.rotate(45) #no siempre funciona, rota la imagen en sentido orario en grados Sexagecimales
    im.show() #abrimos la imagen con el programa predeterminado del sistema operativo, ejemplo: "Visor de Imagenes" 
    # por alguna razon el archivo deja de ser accecible para nuestra programa
    # o sea que despues de im.show() el programa sigue con la siguente linea del codigo
    im.close()
    time.sleep(10)#esperamos 10 segundos
def ButtonConImagen(admin,G,info):
    pwd=info['info']['pwd']+'\\'+"media"+'\\'+"img"
    file=[str(img) for img in os.listdir(pwd) if (('.png' in img[-4:]) or ('.jpg' in img[-4:]))][0]
    canvas_height=G.widgets[info['widget']['pruebasConImagenes']]['alto']
    canvas_width=G.widgets[info['widget']['pruebasConImagenes']]['ancho']
    #inicia codigo de la prueba
    raiz = Tk() 
    raiz.geometry(str(canvas_width)+"x"+str(canvas_height))
    try:
        #guardo la imagen con formato PNG, usando el modulo Image, de esta forma tkinter siempre podra cargar la nueva imagen correctamente
        #la nueva imagen generada con Image.save("nuevoArchivoMiFoto.PNG") normalmente siempre se carga bien los programas con Tkinter
        Image.open(pwd+file).save(pwd+file.replace('.jpg','.png'))

    except IOError:
        print("No se puede convertir la imagen")
    #el archivo de origen puede ser JPG o PNG, lo importante es guardas la imagen en PNG
    #redimensionamos la imagen con Image.resize((200,200)), los parametros son en pixeles
    #luego al cargar la imagen y mostrala en pantalla con Tkinter ocupara las demenciones que le allamos dado
    #archivo nuevo en formato PNG generado con Image.save("myNuevaImagen.png","png")
    imgOriginal = Image.open(pwd+file.replace('.jpg','.png')).resize((200,200)).save(pwd+'myNuevaImagen.png','png')
    #cargamos el nuevo archivo "myNuevaImagen.png" creado en la linea anterior en una nuava variable
    imgNueva =  PhotoImage(file=pwd+"myNuevaImagen.png")
    #creamos un widget Button y le pasamos la variable que contiene la nueva imagen con image=imgNueva 
    #el parametro text="Botonio", quedara debajo de la imagen y alineada con la imagen, el boton ocupara el lugar de la imagen y tambien del Texto
    #si no le damos texto ,ejemplo: Button(raiz, image=imgNueva, bd=0, etc etc ...) el boton tomara las medidas de la imagen
    boton = Button(raiz, image=imgNueva,text=pwd+"myNuevaImagen.png", bd=0, compound="top",command=lambda:print("Click XD"))
    boton.place(x=0, y=50)
    raiz.mainloop()

def command(admin,G,info,ec,geo):
    print(info['subProyecto'])
    print('Info:',info['info'])
    print('Widgest:',info['widget'])
    print('Comandos',info['command']) 
    G.command[info['command']['manager']]=lambda : admin.transicion(G,admin.manager)
    G.command[info['command']['showAlbum']]=lambda : showAlbum(admin,G,info,alto=200,ancho=500)