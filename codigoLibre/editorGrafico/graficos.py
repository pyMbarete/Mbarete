import os,math,time
global d,canvas_width,canvas_height
d={
    'img':os.getcwd()+'\\'+'media'+'\\'+"img_recursos"+'\\',
    'i':os.getcwd()+'\\'+'media'+'\\'+"img_trabajo"+'\\',
    'audio':os.getcwd()+'\\'+"audio"+'\\'
    }
canvas_width = 1100
canvas_height =int((canvas_width/5)*3)

def cronometro(*total):
    if total:
        total=int(total[0])
    else:
        total=2
    t=0
    suma=0.0
    t0=time.time()
    T=t0
    while t <= total:
        T=time.time()
        suma += T-t0
        yield 'T%s:%s, suma:%s'%(t,round(T-t0,4),suma)
        t0=T
        t+=1
def agrupacion_maxima(img,zancada):
    ancho=img.size[0]
    alto=img.size[1]
    ret=img.resize((int(ancho//zancada),int(alto//zancada)))
    for x in range(1,ancho,zancada):
        for y in range(1,alto,zancada):
            maximo=max([max([img.getpixel((x+i,y+j)) for i in range(-1,2)]) for j in range(-1,2)])
            ret.putpixel((x//zancada,y//zancada),(maximo))
    return ret
def filtro(img,nucleo):
    ancho=img.size[0]
    alto=img.size[1]
    ret=img.convert ("L")
    img=ret
    for x in range(1,ancho-1):
        for y in range(1,alto-1):
            maximo=sum([sum([img.getpixel((x+i,y+j))*nucleo[i+1][j+1] for i in range(-1,2)]) for j in range(-1,2)])
            ret.putpixel((x,y),(maximo))
    return ret

def aclarado_inteligente(pwd_img='media/img_trabajo/',muestreo=0):
    from PIL import Image
    imgs=['aclar0','aclar1','aclar2','aclar3','aclar4','aclar5']
    tiempo=cronometro(len(imgs))
    print(next(tiempo))
    limiteInferior=90
    limiteSuperior=150
    seccion=[1,3,5,3,1]
    #cantidad total de puntos por seccion
    n=float(sum(seccion))
    seccion = [s//2 for s in seccion]
    cY = (len(seccion)//2)+1
    cX = seccion[cY]+1
    for d in imgs:
        im = Image.open(pwd_img+d+'.jpg')# la foto del sistema
        img = im.convert ("L")
        #'aclarado' contiene la imagen aligerada
        #aclarado = img.point(lambda x: pixel(x)*factor_de_aclaracion)
        area=[]
        for s in range(len(seccion)):
            area += [[img.getpixel((x,s))for x in range(0,img.size[0]-1)]]
        for y in range(cY,img.size[1]-cY):
            for x in range(cX,img.size[0]-cX):
                menor=255
                p=0.0
                for s in range(len(seccion)):
                    #print(area[s][x-seccion[s]:x+seccion[s]+1])
                    p += sum( area[s][x-seccion[s] : x+seccion[s]+1] )
                    minimo=min( area[s][x-seccion[s]:x+seccion[s]+1] )
                    if menor > minimo: menor=minimo
                p = p/n
                if area[cY][x]>=limiteSuperior:
                    # El color de estos píxeles se cambia a blanco
                    #im.getpixel((x,s))
                    im.putpixel( (x,y),(255,255,255,255) )
                elif area[cY][x]<limiteInferior:
                    pass
                elif area[cY][x]>limiteInferior and area[cY][x]==menor:
                    (r,g,b)=im.getpixel((x,y))
                    f=255/p
                    #f=((p+255)/(2*p))
                    (r,g,b)=(int(r*f),int(g*f),int(b*f))
                    # El color de este píxel cambia a blanco
                    im.putpixel((x,y),(r,g,b,255))
                else:
                    (r,g,b)=im.getpixel((x,y))
                    f=((p+255)/2)
                    (r,g,b)=(int(r*f),int(g*f),int(b*f))
                    # El color de este píxel cambia a blanco
                    im.putpixel((x,y),(r,g,b,255))
                    
            print(y/img.size[1],end='\r')
            if y<img.size[1]:
                area.pop(0)
                area+=[[img.getpixel((x,y+cY)) for x in range(0,img.size[0])]]
        # img = img.convert("RGB")# Forzar la imagen a RGB
        archivo_salida=(pwd_img+d)+'_'+str(limiteInferior)+'_.png'
        print("Guardando:",archivo_salida)
        #Guarda la imagen después de modificar los píxeles
        im.save(archivo_salida,'png')
        print(next(tiempo))

aclarado_inteligente()
def sin_fondo(pwd='media\\img_sin_fondos\\',file='cam.jpg',img_fondo='fondo.jpg'):
    from PIL import Image
    import time
    marco='producto\\'
    pwd_marco='media\\img_marco\\'
    factor_de_aclaracion=0.1
    f_0=1.0-factor_de_aclaracion
    f_1=1.0+factor_de_aclaracion
    img_f=Image.open(pwd+img_fondo)
    inicio_t=time.time()
    #lista= [file] if file else [img for img in os.listdir(pwd) if (img.endswith('.jpg') or img.endswith('.png') or img.endswith('.jpeg') or (img_fondo in img))]
    lista= [file] if file else [img for img in os.listdir(pwd) if (img.endswith('.png') or img.endswith('.jpg') or (img_fondo in img))]

    for file in lista:
        print("Procesando:",file)
        img_org=Image.open(pwd+file)
        img=img_org.convert('RGBA')
        width = img.size[0]#Longitud
        height = img.size[1]# Ancho
        linea_0=[img_f.getpixel((j,0))for j in range(0,width)]
        linea_1=[img_f.getpixel((j,1))for j in range(0,width)]
        linea_2=[img_f.getpixel((j,2))for j in range(0,width)]
        linea_3=[img_f.getpixel((j,3))for j in range(0,width)]
        linea_4=[img_f.getpixel((j,4))for j in range(0,width)]
        for y in range(2,height):
            j=0
            for x in range(2,width-2):
                j=x
                m=[linea_0[j-1],linea_0[j],linea_0[j+1]]+[linea_1[j-2],linea_1[j-1],linea_1[j],linea_1[j+1],linea_1[j+2]]+[linea_2[j-2],linea_2[j-1],linea_2[j],linea_2[j+1],linea_2[j+2]]+[linea_3[j-2],linea_3[j-1],linea_3[j],linea_3[j+1],linea_3[j+2]]+[linea_4[j-1],linea_4[j],linea_4[j+1]]
                
                p=img_org.getpixel((x,y))#pixel objetivo
                f=img_f.getpixel((x,y))#pixel del fondo
                
                if p==f:
                    img.putpixel((x,y),(0,0,0,0))
                elif p in m:
                    img.putpixel((x,y),(0,0,0,0))
                elif (f[0]*f_0<=p[0]<=f[0]) and (f[1]*f_0<=p[1]<=f[1]) and (f[2]*f_0<=p[2]<=f[2]):
                    img.putpixel((x,y),(p[0],p[1],p[2],0))
                elif (f[0]*f_1>=p[0]>=f[0]) and (f[1]*f_1>=p[1]>=f[1]) and (f[2]*f_1>=p[2]>=f[2]):
                    img.putpixel((x,y),(p[0],p[1],p[2],0))
                    #print(p,f)
            if y<height:
                linea_0=linea_1
                linea_1=linea_2
                linea_2=linea_3
                linea_3=linea_4
                linea_4=[img_f.getpixel((j,y+2)) for j in range(0,width)]
            print((100.0*((y+1.0)/height)),end='\r')
        archivo_salida=file.replace(".jpg",'').replace(".png",'')+'_sin_fondo_'+str(factor_de_aclaracion)+'_.png'
        print("Guardando:",archivo_salida)
        img.save(pwd+archivo_salida,'png')#Guarde la imagen después de modificar los píxeles
        img.close()#cerramos la imagen
    img_f.close()
    print(time.time()-inicio_t)
#sin_fondo()
def agregar_marco(pwd='media\\img_trabajo\\',file='aclar1.jpg',muestreo=0):
    if muestreo:
        global muestra
        muestra={x:0 for x in range(256)}
    from PIL import Image
    import time
    marco='producto\\'
    pwd_marco='media\\img_marco\\'

    inicio_t=time.time()
    lista= [file] if file else [img for img in os.listdir(pwd) if (img.endswith('.jpg') or img.endswith('.png') or img.endswith('.jpeg'))]
    for file in lista:
        im=Image.open(pwd+file)
        width = img.size[0]#Longitud
        height = img.size[1]# Ancho
        x_0=x_f=y_0=y_f=None

    print(time.time()-inicio_t)
def extraer(pwd='media\\img_trabajo\\',file='aclar1.jpg',muestreo=0):
    if muestreo:
        global muestra
        muestra={x:0 for x in range(256)}
    from PIL import Image
    import matplotlib
    import matplotlib.pyplot as plt
    import numpy as np
    import time
    inicio_t=time.time()
    n=20
    nucleo=[[-1,-1,-1],[-1,8,-1],[-1,-1,-1]]
    zancada=3
    factor_de_aclaracion=1.0
    i = 1
    j = 1
    varianza_permitida=5
    lista= [file] if file else [img for img in os.listdir(pwd) if (img.endswith('.jpg') or img.endswith('.png') or img.endswith('.jpeg'))]
    for file in lista:
        im=Image.open(pwd+file)
        img=agrupacion_maxima(filtro(im,nucleo),zancada)
        width = img.size[0]#Longitud
        height = img.size[1]# Ancho
        X=[sum([img.getpixel((i,j)) for j in range(0,height)])/height for i in range(0,width)]
        Y=[sum([img.getpixel((i,j)) for i in range(0,width)])/width for j in range(0,height)]
        x_0=x_f=y_0=y_f=None
        print(im.size)# Tamaño de imagen impresa
        for x in range(0,width-n):# Iterar a través de puntos de todas las longitudes
            if not x_0:
                m=[X[i] for i in range(x,x+n)]# Muestra de promedios
                p=sum(m)/n
                v=sum([abs(l-p) for l in m])/n
                if varianza_permitida<=v:
                    x_0=x
                    print(x_0,v,p)
                    for j in range(0,height*zancada):
                        im.putpixel((x_0*zancada,j),(0,0,0,255))
        for x in range(width-n,0,-1):# Iterar a través de puntos de todas las longitudes
            if not x_f:
                m=[X[i] for i in range(x,x+n)]# Muestra de promedios
                p=sum(m)/n
                v=sum([abs(l-p) for l in m])/n
                if varianza_permitida<=v:
                    x_f=x+n
                    print(x_0,v,p)
                    for j in range(0,height*zancada):
                        im.putpixel((x_f*zancada-1,j),(0,0,0,255))
        for y in range(0,height-n):# Iterar a través de puntos de todas las longitudes
            if not y_0:
                m=[Y[i] for i in range(y,y+n)]# Muestra de promedios
                p=sum(m)/n
                v=sum([abs(l-p) for l in m])/n
                if varianza_permitida<=v:
                    y_0=y
                    print(y_0,v,p)
                    for i in range(0,width*zancada):
                        im.putpixel((i,y_0*zancada),(0,0,0,255))
        for y in range(height-n,0,-1):# Iterar a través de puntos de todas las longitudes
            if not y_f:
                m=[Y[i] for i in range(y,y+n)]# Muestra de promedios
                p=sum(m)/n
                v=sum([abs(l-p) for l in m])/n
                if varianza_permitida<=v :
                    y_f=y+n
                    print(y_f,v,p)
                    for i in range(0,width*zancada):
                        im.putpixel((i,y_f*zancada-1),(0,0,0,255))
        # img = img.convert("RGB")# Forzar la imagen a RGB
        archivo_salida=file.replace(".jpg",'').replace(".png",'')+'_extraer_'+str(varianza_permitida)+'_.png'
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
        plt.savefig(file.replace(".jpg",'').replace(".png",'')+'_muestreo_barras_simple.png')
        #Finalmente mostramos la grafica con el metodo show()
        plt.show()
#extraer()
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
def menu_contextual(estructura):
    """
    Windows Registry Editor Version 5.00

    [HKEY_CLASSES_ROOT\Directory\Background\shell\Imagen]
    @="Imagine Aclarar"

    [HKEY_CLASSES_ROOT\Directory\Background\shell\Imagen\command]
    @="cmd.exe"

    [HKEY_CLASSES_ROOT\Directory\Background\shell\Aclarar Imagenes\command]
    @="\"C:\\Program Files (x86)\\Python37-32\\python.exe\" \"C:\\python\\graficos.py\" aclarar"
    """
    myCode=estructura['file']
    import os
    if 'window' in os.environ['OS'].lower(): 
        for k in os.environ:
            d=[pro for pro in os.environ['PATH'].split(';') if ((os.environ['LOCALAPPDATA']+r'\Programs\Python\Python' in pro) and (not 'Script' in pro))]
        d=d[0]+'\\python.exe'
    file=open("menu.reg","w")
    file.write("Windows Registry Editor Version 5.00\n\n")
    for clave in estructura['menu']:
        command=r"["+r"HKEY_CLASSES_ROOT\Directory\Background\shell\_"+estructura['menu'][clave]+r']'
        file.write(command)
        file.write('\n')
        command=r'@="'+estructura['menu'][clave]+r'"'
        file.write(command)
        file.write('\n')
        file.write('\n')
        command=r"["+r"HKEY_CLASSES_ROOT\Directory\Background\shell\_"+estructura['menu'][clave]+r"\command]"
        file.write(command)
        file.write('\n')
        command=r'@="\"'+d+r'\" \"'+myCode+r'\" '+clave+'"\n\n'
        file.write(command)
        file.write('\n')
        
    file.close()
    print(os.path)
    #for k in os.path:
    #    print(k,os.path[k])
estructura={
    'nombre':"Imagenes",
    'file':"C:\\python\\graficos.py",
    'menu':{
        'aclarar':'Aclarar',
        'sin_fondo':'Quitar Fondo'
        }
}
#menu_contextual(estructura)