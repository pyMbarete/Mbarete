import os
import math
global d,canvas_width,canvas_height
d={
    'img':os.getcwd()+'\\'+'media'+'\\'+"img_recursos"+'\\',
    'i':os.getcwd()+'\\'+'media'+'\\'+"img_trabajo"+'\\',
    'audio':os.getcwd()+'\\'+"audio"+'\\'
    }
canvas_width = 1100
canvas_height =int((canvas_width/5)*3)
def aclarado_inteligente(pwd_img='media\\img_trabajo\\aclar1.jpg',muestreo=0):
    if muestreo:
        global muestra
        muestra={x:0 for x in range(256)}
    from PIL import Image
    import matplotlib
    import matplotlib.pyplot as plt
    import numpy as np
    import time
    inicio_t=time.time()
    n=1
    factor_de_aclaracion=1.0
    i = 1
    j = 1
    valor_permitido=90
    im = Image.open(pwd_img)#Lea las fotos internas del sistema
    print (im.size)# Tamaño de imagen impresa
    img = im.convert ("L")
    width = img.size[0]#Longitud
    height = img.size[1]# Ancho
    total=width*height
    #aclarado = img.point(lambda x: pixel(x)*factor_de_aclaracion)  #'aclarado' contiene la imagen aligerada
    #print(muestra)
    linea_0=[img.getpixel((0,j))for j in range(0,height)]
    linea_1=[img.getpixel((1,j))for j in range(0,height)]
    linea_2=[img.getpixel((2,j))for j in range(0,height)]
    linea_3=[img.getpixel((3,j))for j in range(0,height)]
    linea_4=[img.getpixel((4,j))for j in range(0,height)]
    for i in range(2,width-2):# Iterar a través de puntos de todas las longitudes
        for j in range(2,height-2):# Iterar a través de puntos de todos los anchos
            #p=img.getpixel((i,j))
            #print(((i*width)+j)/total)
            #data = (img.getpixel((i,j)))# Imprima todos los puntos de la imagen
            #print (data)# Imprima el valor del color RGBA de cada píxel (r, g, b, alfa)
            #print (data[0])# Imprimir valor de RGBA
            #matriz
            m=[
                [linea_0[j-1],linea_0[j],linea_0[j+1]],
                [linea_1[j-2],linea_1[j-1],linea_1[j],linea_1[j+1],linea_1[j+2]],
                [linea_2[j-2],linea_2[j-1],linea_2[j],linea_2[j+1],linea_2[j+2]],
                [linea_3[j-2],linea_3[j-1],linea_3[j],linea_3[j+1],linea_3[j+2]],
                [linea_4[j-1],linea_4[j],linea_4[j+1]]
            ]
            #promedio
            p=sum([sum(l) for l in m])/21.0
            #varianza
            v=sum([sum([abs(abs(x)-p) for x in l]) for l in m])/21.0
            #Color mas CLARO
            #mayor=max([max(l) for l in m])
            #Color mas OSCURO
            menor=min([min(l) for l in m])
            #valorIdeal
            Ideal=p-v*2
            if (menor<=valor_permitido):
                if muestreo:
                    muestra[j]+=1
            elif valor_permitido>=Ideal:
                #print(Ideal)
                if muestreo:
                    muestra[j]+=1
            else:
                im.putpixel((i,j),(255,255,255,255))# El color de estos píxeles se cambia a blanco
        print(i/width)
        if i<height:
            linea_0=linea_1
            linea_1=linea_2
            linea_2=linea_3
            linea_3=linea_4
            linea_4=[img.getpixel((i+2,j)) for j in range(0,height)]

    # img = img.convert("RGB")# Forzar la imagen a RGB
    archivo_salida=pwd_img.split('\\')[-1].replace(".jpg",'').replace(".png",'')+'_aclarado_avanzado_'+str(valor_permitido)+'_.png'
    print("Guardando:",archivo_salida)
    im.save(archivo_salida,'png')#Guarde la imagen después de modificar los píxeles

    print(time.time()-inicio_t)
    if muestreo:
        print(muestra)
        #Definimos una lista con paises como string
        color = [k for k in muestra]
        #Definimos una lista con ventas como entero
        porciento = [(muestra[k]/total)*100.0 for k in muestra]
        fig, ax = plt.subplots()
        #Colocamos una etiqueta en el eje Y
        ax.set_ylabel('Porciento')
        #Colocamos una etiqueta en el eje X
        ax.set_xlabel('Porcentaje de Pexiles por cada Color')
        ax.set_title(pwd_img)
        #Creamos la grafica de barras utilizando 'paises' como eje X y 'ventas' como eje y.
        plt.bar(color, porciento)
        plt.savefig(pwd_img.split('\\')[-1].replace(".jpg",'').replace(".png",'')+'muestreo_barras_simple.png')
        #Finalmente mostramos la grafica con el metodo show()
        plt.show()
aclarado_inteligente()
def actualizarCodigo(pwd,file):
    import os
    ignorar=['temporal.png','fondo.png']
    temp='temporal.png'
    codigo_nuevo='convertRGBA_'
    codigo='convertRGBA_FULL_'
    if (codigo==file[:len(codigo_nuevo)]) and (file[-4:]=='.png') and (not file in ignorar):
        os.rename(pwd+file,pwd+codigo_nuevo+file[len(codigo):])
    else:
        print('ya esta,',file)
def prepararPNG(pwd,file):
    from PIL import Image
    import os
    ignorar=['temporal.png','fondo.png']
    temp='temporal.png'
    codigo='convertRGBA_'
    codigo_nuevo='convertRGBA_FULL_'
    if (codigo!=file[:len(codigo)]) and (codigo_nuevo!=file[:len(codigo_nuevo)]) and (file[-4:]=='.png') and (not file in ignorar):
        background = Image.open(pwd+"fondo.png")
        foreground = Image.open(pwd+file)
        h=foreground.size[1]
        w=foreground.size[0]
        lado=int(((h**2)+(w**2))**(1/2))
        grado=str(math.asin(h/lado)*(180.0/math.pi))
        grado_decimales=str(int(int(grado.split('.')[1][:4])/100))
        grado=grado.split('.')[0]+'.'+grado_decimales+'_'
        #print(h,w,lado,grado)
        x=int((lado-w)/2)
        y=int((lado-h)/2)
        background=background.resize((lado,lado))
        background.save(pwd+'temporal.png','png')
        background = Image.open(pwd+"temporal.png")
        background.paste(foreground, (x, y),foreground.convert('RGBA'))
        background.save(pwd+codigo_nuevo+grado+lado+'_'+file,'png')
        os.remove(pwd+file)
    elif (codigo==file[:len(codigo)]) and (codigo_nuevo!=file[:len(codigo_nuevo)]) and (not file in ignorar):
        foreground = Image.open(pwd+file,'r')
        lado=foreground.size[1]
        #foreground.save(pwd+file)
        foreground.close()
        os.rename(pwd+file,pwd+codigo_nuevo+file[len(codigo):len(codigo)+6]+str(lado)+'_'+file[len(codigo)+6:])
    else:
        print('ya esta,',file)
def showAlbum():
    from tkinter import Tk, Scrollbar,Canvas,Frame,IntVar,Entry,Button,RIGHT,Y,Label
    from PIL import Image, ImageTk
    global d,canvas_width,canvas_height
    def dibujar(alto,ancho,rotar):
        my_canvas_height=int(int(len(lista)/int(range(0,canvas_width,ancho)[-1]/ancho))*alto+alto)
        miFrameinicio.configure(bg='#090929',width = canvas_width, height=my_canvas_height)
        canvas.configure(bg='#090929',width = canvas_width, height=my_canvas_height)
        canvas.create_polygon((0,0,canvas_width,0,canvas_width,my_canvas_height,0,my_canvas_height),fill='#090929')
        #miniatura={}
        contador=0
        for y in range(30,my_canvas_height,alto):
            for x in range(0,canvas_width-ancho,ancho):
                if contador==len(lista):
                    break
                img=Image.open(pwd+str(lista[contador])).rotate(rotar)
                h0=img.size[1]#alto inicial
                w0=img.size[0]#ancho inicial
                redimencionar=(w0*(ancho/w0),h0*(ancho/w0)) if w0>h0 else (w0*(alto/h0),h0*(alto/h0))
                w0,h0 = redimencionar[0],redimencionar[1]
                h=h0*math.cos(math.radians(rotar))+w0*math.sin(math.radians(rotar)) #alto
                w=h0*math.sin(math.radians(rotar))+w0*math.cos(math.radians(rotar)) #ancho
                redimencionar=(w0*(ancho/w0),h0*(ancho/w0)) if w0>h0 else (w0*(alto/h0),h0*(alto/h0))
                redimencionar=(int(w0),int(h0))
                print(redimencionar,str(lista[contador]))
                if '.jpg' in str(lista[contador])[-5:]:
                    img.save(pwd+str(lista[contador]).replace('.jpg','.png'),'png')
                    img=Image.open(pwd+str(lista[contador]).replace('.jpg','.png'))
                miniatura[contador]={'img':img.resize(redimencionar)}
                miniatura[contador]['PhotoImage']=ImageTk.PhotoImage(miniatura[contador]['img'])
                miniatura[contador]['widget']=Label(miFrameinicio,image=miniatura[contador]['PhotoImage'])
                canvas.create_image(x+int((ancho-redimencionar[0])/2),y+int((alto-redimencionar[1])/2),image=miniatura[contador]['PhotoImage'],anchor='nw')
                if ".jpg" in str(lista[contador])[-5:]:
                    os.remove(pwd+str(lista[contador]))
                contador=contador+1
        raiz.update()
        c.config(scrollregion=c.bbox("all"))
        raiz.geometry(str(canvas_width)+"x"+str(canvas_height)+"+10+10")
    pwd=d['img_recursos']
    alto=200
    ancho=200
    rotar=10
    paginado=15
    print('Ubicacion:',pwd)
    #inicia codigo de la prueba
    lista=[img for img in os.listdir(pwd) if (((".jpg" in img[-5:]) and (not ".png" in img)) or ((".png" in img[-5:]) and (not ".jpg" in img)) or ((".jpeg" in img[-5:]) and (not ".png" in img)) )]
    miniatura={}
    contador=0
    print(canvas_width//ancho)
    for f in lista:
        actualizarCodigo(pwd,f)
    lista=[img for img in os.listdir(pwd) if (((".jpg" in img[-5:]) and (not ".png" in img)) or ((".png" in img[-5:]) and (not ".jpg" in img)) or ((".jpeg" in img[-5:]) and (not ".png" in img)) )]
    my_canvas_height=int(int(len(lista)/int(range(0,canvas_width,ancho)[-1]/ancho))*alto+alto)
    raiz=Tk()
    scrollbar=Scrollbar(raiz)
    c = Canvas(raiz, yscrollcommand=scrollbar.set)
    scrollbar.config(command=c.yview)
    scrollbar.pack(side=RIGHT, fill=Y)
    miFrameinicio=Frame(c)
    miFrameinicio.configure(width = canvas_width, height=my_canvas_height)
    canvas = Canvas(miFrameinicio, width=canvas_width, height=my_canvas_height)
    canvas.place(x=0, y=0)
    c.pack(side="left" , fill="both", expand=True)
    c.create_window(0,0,window=miFrameinicio, anchor='nw')
    c.config(scrollregion=c.bbox("all"))
    img_ancho=IntVar(value=ancho)
    img_alto=IntVar(value=alto)
    img_rota=IntVar(value=rotar)
    entry_ancho=Entry(miFrameinicio,textvariable=img_ancho,width=10)
    entry_ancho.place(x=10, y=10)
    entry_alto=Entry(miFrameinicio,textvariable=img_alto,width=10)
    entry_alto.place(x=76, y=10)
    entry_rota=Entry(miFrameinicio,textvariable=img_rota,width=10)
    entry_rota.place(x=142, y=10)
    btn_aplicar=Button(miFrameinicio,text='Aplicar',command=lambda: dibujar(img_alto.get(),img_ancho.get(),img_rota.get()),width=10)
    btn_aplicar.place(x=208, y=10)
    dibujar(img_alto.get(),img_ancho.get(),img_rota.get())
    #raiz.update()
    #c.config(scrollregion=c.bbox("all"))
    #raiz.geometry(str(canvas_width)+"x"+str(canvas_height)+"+10+10")
    print("Mostrando las imagenes con tkinter y PIL...")
    raiz.focus_force()
    raiz.mainloop()    
#showAlbum()
#100-240 1.4a, 50-60hz
#19.5 2.31 45w
#prepararPNG(d['img'],"convertRGBA_FULL_53.53_sexy.png")
def aclarar():
    """ Como aclarar una imagen en Python
        #https://www.ubiquitour.com/5ZdEnDbW/
    
        October 27, 2020

        El lenguaje de programación Python puede manipular una gran variedad de tipos de datos, incluyendo texto e imágenes. 
        La biblioteca de imágenes de Python, o PIL, contiene una serie de métodos para la apertura y realizar operaciones en archivos de imagen. 
        Con el PIL y sus métodos de apoyo, particularmente el método de "punto", puede aclarar u oscurecer imágenes y así aclarar o desvanecer colores de cualquier imagen.

        Instrucciones
        1 Descargar e instalar la última versión de biblioteca de imágenes de Python (PIL) de la página web Pythonware.com.
        2 Abrir un archivo de imagen y guardar en un objeto de imagen mediante código como el siguiente:
            #Reemplazar "/ home/pic.jpg" con la ruta y el nombre de la imagen que desea aclarar.
            form PIL import Image
            im = Image.open('/home/pic.jpg')

        3 Aclarar la imagen llamando al metodo del "point", que se pueden realizar una operacion sobre todos los pixeles de la imagen. 
            El metodo de "point" toma una funcion como argumento, en que este ejemplo, usaras una funcion lambda que cada valor de pixel se multiplica por 1.9. 
            Multiplicar el pixel por un numero mayor que 1 para aumentar la intensidad o menos de 1 para oscurecerlo:
                cambiado = im.point (lambda x: x * 1.9) / / 'cambiado' contiene la imagen aligerada
    """
    def pixel(x,factor_de_aclaracion):
        print(x)
        return x * factor_de_aclaracion
    from PIL import Image, ImageTk
    pwd=d['i']
    factor_de_aclaracion=1.5
    lista=[img for img in os.listdir(pwd) if (((".jpg" in img[-5:]) and (not ".png" in img)) or ((".png" in img[-5:]) and (not ".jpg" in img)) or ((".jpeg" in img[-5:]) and (not ".png" in img)) )]    
    for i in lista:
        im = Image.open(pwd+i)
        ByN = im.convert ("L")
        aclarado = ByN.point(lambda x: pixel(x,factor_de_aclaracion))  #'aclarado' contiene la imagen aligerada
        aclarado.save(pwd+'aclarado_'+str(factor_de_aclaracion)+'_'+i.replace('.jpg','.png').replace('.jpeg','.png'),'png')
        #pasando tla imagen a blanco y negro
        #ByN = im.convert ("L")
        #ByN.save(pwd+'ByN_'+i.replace('.jpg','.png').replace('.jpeg','.png'),'png')
    print("Aclaracion Finalizada")
#aclarar()