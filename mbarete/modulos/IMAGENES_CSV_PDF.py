#!/usr/bin/env python
# -*- coding: latin-1 -*-
import os
import sys
import csv
import time
import datetime
import math
from reportlab.lib.units import mm, inch
from reportlab.pdfgen import canvas as pdf
from extras import V
#from mbarete.mbarete import geometria
global d,canvas_width,canvas_height
d={
    'img':os.getcwd()+os.path.sep+"media"+os.path.sep,
    'audio':os.getcwd()+os.path.sep+"media"+os.path.sep
    }
canvas_width = 1100
canvas_height =1000
print(datetime.datetime.now())

def powerPDF():
    import os,datetime
    from reportlab.lib.units import mm, inch
    from reportlab.pdfgen import canvas as pdf
    from reportlab.lib.pagesizes import A4 as size
    #/src/reportlab/lib/pagesizes.py
    txt=[
        'nombreCompleto','direccion','numeroDeTelefono',
        'fechaDeNacimiento','tipoDeSangre',
        ]
    txt=[ V.toText(t) for t in txt ]
    value = [ input(f'Ingrese su, {t}:') for t in txt]
    Lsize=700
    print("Los valores ingresados son",size)
    for key,val in zip(txt,value):
        print(key,':',val)
    
    canvas = pdf.Canvas(value[0]+".pdf", pagesize = size)
    canvas.setLineWidth(.3)
    canvas.setFont('Helvetica', 12)
    canvas.drawString(30,750,'CARTA DE PRUEBA')
    canvas.drawString(500,750,str(datetime.date.today()))
    canvas.drawString(30,735,"setFont('Helvetica', 12)")
    canvas.line(480,747,580,747)
    canvas.drawString(275,725,'ESTIMADO:')
    canvas.drawString(500-(len(value[0])*3),725,value[0])
    canvas.line(378,723,580,723)
    for x in range(0,len(txt),1):
        y=size[1]-((x+1)*15)
        canvas.drawString(30,y,txt[x]+':')
        canvas.line(120,y,size[0]-30,y)
        canvas.drawString( 120,y,value[x] )
    canvas.save()
    if os.path.isfile(value[0]+".pdf"):
        print(f'Abriendo el archivo "{value[0]}.pdf"')
        os.system(f'xdg-open "{value[0]}.pdf"')
def showAlbum(alto=200,ancho=200):
    from tkinter import Tk,Scrollbar,Canvas,Frame,Label,Button,RIGHT,PhotoImage,Y
    #from tkinter import Tk,Scrollbar,Canvas,Frame,Label
    #from PIL import Image, ImageTk
    from PIL import Image,ImageTk

    import os
    global d,canvas_width,canvas_height
    obj=object_mbarete(
        pwd='repo_path',
        flags=['error','init','acceso_directo'],
        carpetas={
            'dir_media':'mbarete/media/',
            'web_servidor':'mbarete/servidor/',
        }
    )
    pwd=obj.carpetas['media']
    obj.p('Ubicacion:',pwd)
    #inicia codigo de la prueba
    lista=is_extend(os.listdir(pwd),["jpg","png","jpg","jpeg"])
    obj.p("archivos encontrados:",lista)
    miniatura={}
    contador=0
    obj.p('columnas:',int(canvas_width//ancho))
    obj.p('filas:',int(canvas_width//alto))
    my_canvas_height=int(int(len(lista)//int(canvas_width//ancho))*alto+alto)
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
    
    for y in range(10,my_canvas_height,alto):
        for x in range(0,canvas_width-ancho,ancho):
            if contador==len(lista):
                break
            #cargamos la imagen Original        
            img=Image.open(pwd+str(lista[contador]))
            #calculamos las nuevas medidas para la Imagen que Mostraremos Por pantalla
            if img.size[0]>img.size[1]:
                redimencionar= (int(img.size[0]*(ancho/img.size[0])),int(img.size[1]*(ancho/img.size[0]))) 
            else: 
                redimencionar= (int(img.size[0]*(alto/img.size[1])),int(img.size[1]*(alto/img.size[1])))
            
            #Convertimos a PNG si esta en otro formato
            if lista[contador][-1] in ['jpg','jpeg','bmp']:
                img.save(pwd+str(lista[contador]).replace('.'+lista[contador][-1],'.png'),'png')
                os.remove(pwd+str(lista[contador]))
            img.close()
            miniatura.setdefault(contador,{'Image':Image.open(pwd+str(lista[contador]).replace('.jpg','.png')).resize(redimencionar)})
            miniatura[contador]['PhotoImage']=ImageTk.PhotoImage(image=miniatura[contador]['Image'])
            canvas.create_image(x+int((ancho-redimencionar[0])/2),y+int((alto-redimencionar[1])/2),image=miniatura[contador]['PhotoImage'],anchor='nw')
            print(redimencionar,str(lista[contador]))
            contador=contador+1
    raiz.update()
    c.config(scrollregion=c.bbox("all"))
    raiz.geometry(str(canvas_width)+"x"+str(canvas_height)+"+10+10")
    raiz.mainloop()    
def editImagen():
    from PIL import Image
    import os
    global d
    pwd=d['img']
    file=[str(img) for img in os.listdir(d['img']) if (('.png' in img[-4:]) or ('.jpg' in img[-4:]))][0]
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
def ButtonConImagen():
    from tkinter import Tk,PhotoImage,Button
    from PIL import Image
    import os
    global canvas_width,canvas_height,d
    pwd=d['img']
    file=[str(img) for img in os.listdir(d['img']) if (('.png' in img[-4:]) or ('.jpg' in img[-4:]))][0]
    raiz = Tk() 
    raiz.geometry(str(canvas_width)+"x"+str(canvas_height))
    try:
        #guardo la imagen con formato PNG, usando el modulo Image, de esta forma tkinter siempre podra cargar la nueva imagen correctamente
        #la nueva imagen generada con Image.save("nuevoArchivoMiFoto.PNG") normalmente carga con exito en Tkinter
        Image.open(pwd+file).save(pwd+file.replace('.jpg','.png'))

    except IOError:
        print("No se puede convertir la imagen")
    #el archivo de origen puede ser JPG o PNG, lo importante es guardas la imagen en PNG
    #redimensionamos la imagen con Image.resize((200,200)), los parametros alto y ancho en una tupla ejem:(alto,ancho), alto y ancho en pixeles
    #luego, al cargar la imagen y mostrala en pantalla con Tkinter ocupara las dimensiones que le dimos con 'Image.resize'. GUardo la IMagen en un
    #archivo nuevo en formato PNG generado con Image.save("myNuevaImagen.png","png")
    imgOriginal = Image.open(pwd+file.replace('.jpg','.png')).resize((200,200)).save(pwd+'myNuevaImagen.png','png')
    #cargamos el nuevo archivo "myNuevaImagen.png" creado en la linea anterior
    imgNueva =  PhotoImage(file=pwd+"myNuevaImagen.png")
    #creamos un widget Button y le pasamos la variable que contiene la nueva imagen con image=imgNueva 
    #el parametro text="Botonio", quedara debajo de la imagen y alineada con la imagen, el boton ocupara el lugar de la imagen mas el Texto
    #si no le damos texto ,ejemplo: Button(raiz, image=imgNueva, bd=0, etc etc ...) el boton tomara las medidas de la imagen
    boton = Button(raiz, image=imgNueva,text=pwd+"myNuevaImagen.png", bd=0, compound="top",command=lambda:print("Click XD"))
    boton.place(x=0, y=50)
    raiz.mainloop()

def aspas(x=10,y=10,escalar=1.0,dividir=120,baseRadio=375.0,altura=375.0,revolucion=360,rotorRadio=12.0,fondo=200.0):
    baseRadio=375.0*escalar
    altura=375.0*escalar
    rotorRadio=12.0*escalar
    fondo=200.0*escalar
    # retorna un poligono de una helise de unas aspas de un aero generador de viento 
    print('escalar:',escalar,'x:',x,'y:',y,'dividir:',dividir,'baseRadio:', baseRadio,'altura:', altura,'revolucion:', revolucion,'rotorRadio:', rotorRadio,'fondo:', fondo)
    datos={'x':x,'y':y,'dividir':dividir,'baseRadio':baseRadio,'altura': altura,'revolucion': revolucion,'rotorRadio': rotorRadio,'fondo': fondo}
    geo=geometria()
    xR=[0.0]
    yR=[rotorRadio]
    zR=[-1*(fondo/baseRadio)*(baseRadio-rotorRadio)]
    xA=[0.0]
    yA=[baseRadio]
    zA=[0.0]
    tanA=baseRadio/altura
    for ang in range(1,revolucion,1):
        if (((altura-((altura/float(revolucion))*float(ang)))*tanA) >= rotorRadio):
            rad=math.radians(float(ang))
            zA.append((altura/float(revolucion))*float(ang))
            p=((altura-zA[-1])*tanA)
            yA.append(p*math.cos(rad))
            xA.append(p*math.sin(rad))
            zR.append((-1*(((fondo+zA[-1])/p)*(p-rotorRadio))+zA[-1]))
            yR.append((rotorRadio)*math.cos(rad))
            xR.append((rotorRadio)*math.sin(rad))
            fin=ang
    xOut=[0]
    yOut=[geo.dist([xR[0],yR[0],zR[0]],[xA[0],yA[0],zA[0]])]
    xIn =[0]
    yIn =[0]
    for n in range(1,fin+1,1):
        A=[xA[n-1],yA[n-1],zA[n-1]] #punto que ya esta en el plano
        B=[xR[n-1],yR[n-1],zR[n-1]] #punto origen que ya esta en plano
        C=[xA[n],yA[n],zA[n]]       #punto que se agregara al plano
        xO=geo.dist(geo.alt(C,A,B),C)
        yO=geo.dist(geo.alt(C,A,B),B)
        #print(math.degrees(angRad([0,1,0],resta([xIn[-1],yIn[-1],0],[xOut[-1],yOut[-1],0]))))
        rot= -1*math.fabs(geo.angRad([0,1,0],geo.resta([xIn[-1],yIn[-1],0],[xOut[-1],yOut[-1],0])))
        xRot, yRot=geo.rotar(rot,[xO,yO,0])
        xTras, yTras=geo.trasladar([xIn[-1],yIn[-1],0],[xRot,yRot,0])
        yOut.append(yTras)
        xOut.append(xTras)
        A=[xA[n],yA[n],zA[n]]
        B=[xR[n-1],yR[n-1],zR[n-1]]
        C=[xR[n],yR[n],zR[n]]
        xO= geo.dist(geo.alt(C,A,B),C)
        yO= geo.dist(geo.alt(C,A,B),B) if geo.dist(geo.alt(C,A,B),A)<geo.dist(A,B) else geo.dis(geo.alt(C,A,B),B)*(-1)
        rot= -1*math.fabs(geo.angRad([0,1,0],geo.resta([xIn[-1],yIn[-1],0],[xOut[-1],yOut[-1],0])))
        xRot, yRot=geo.rotar(rot,[xO,yO,0])
        xTras, yTras=geo.trasladar([xIn[-1],yIn[-1],0],[xRot,yRot,0])
        yIn.append(yTras)
        xIn.append(xTras)
    for n in range(0,len(xOut),dividir):
        datos[str(n)+'grados']=str(int(n))+' grados, alturaRelativa= '+str(int(fondo+zR[n]))+'mm, largo= '+str(geo.dist([xIn[n],yIn[n],0],[xOut[n],yOut[n],0]))+', angulo= '+str(math.degrees(geo.angRad([0,0,1],geo.resta([xR[n],yR[n],zR[n]],[xA[n],yA[n],zA[n]]))))
    datos[str(fin)+'grados']=str(int(fin))+' grados, alturaRelativa= '+str(int(fondo+zR[fin]))+'mm, largo= '+str(geo.dist([xIn[fin],yIn[fin],0],[xOut[fin],yOut[fin],0]))+', angulo= '+str(math.degrees(geo.angRad([0,0,1],geo.resta([xR[fin],yR[fin],zR[fin]],[xA[fin],yA[fin],zA[fin]]))))
    textos = [[xIn[n]+x, yIn[n]+y,geo.ang(geo.resta([xIn[n]+(x), yIn[n]+(y),0],[xOut[n]+x, yOut[n]+y,0]),[-1,0,0])-180,'__'+str(n)+' grados'] for n in range(0,len(xOut),dividir)]+[geo.medio([xOut[fin]+x, yOut[fin]+y,0], [xIn[fin]+(x), yIn[fin]+(y),0])[0:2]+[geo.ang(geo.resta([xIn[fin]+(x), yIn[fin]+(y),0],[xOut[fin]+x, yOut[fin]+y,0]),[-1,0,0])-180,'__'+str(fin)+' grados']]
    lineas = [[xOut[n]+(x), yOut[n]+(y), xIn[n]+(x), yIn[n]+(y)] for n in range(0,len(xOut),dividir)]+[[xOut[fin]+(x), yOut[fin]+(y), xIn[fin]+(x), yIn[fin]+(y)]]
    poligono = [[xOut[n]+(x),yOut[n]+(y)] for n in range(0,len(xOut),1)]+[[xIn[n]+(x),yIn[n]+(y)] for n in range(len(xIn)-1,0,-1)]+[[xIn[0]+(x),yIn[0]+(y)]]+[[xOut[0]+x,yOut[0]+y]]
    datos['giroReal'] = fin
    return poligono, lineas, datos,textos
def poligonoToPDF(debug=1,calibrar=1,miniatura=1,margenes=[],REALmm=[200.0,200.0],datos={},printTEXT=[[100,100,0,"hola"],[100,100,90,"hola"],[100,100,180,"hola"],[100,100,270,"hola"]],REALsize=[0.0,0.0],escalar=1.0,cuadricular=1,imprimirHojasEnblanco=0, poligonos=[[(10,10),(15,15),(15,20),(20,20),(10,20),(10,10)]], lineas=[(10,10,0,0),(15,15,0,0),(15,20,0,0),(20,20,0,0),(10,20,0,0),(10,10,0,0)], fin = 6):
    from reportlab.lib.colors import tan, black, green
    from reportlab.lib.units import mm
    from reportlab.pdfgen import canvas
    fontSize=10
    hoja={
        'A0':(841*mm,1189*mm),
        'A1':(594*mm,841*mm),
        'A2':(420*mm,594*mm),
        'A3':(297*mm,420*mm),
        'A4':(210*mm,297*mm),
        'A5':(148*mm,210*mm),
        'A6':(105*mm,148*mm),
        'A7':(74*mm,105*mm),
        'A8':(52*mm,74*mm),
        'A9':(37*mm,52*mm),
        'A10':(26*mm,37*mm),
        'B0':(1000*mm,1414*mm),
        'B1':(707*mm,1000*mm),
        'B2':(500*mm,707*mm),
        'B3':(353*mm,500*mm),
        'B4':(250*mm,353*mm),
        'B5':(176*mm,250*mm),
        'B6':(125*mm,176*mm),
        'B7':(88*mm,125*mm),
        'B8':(62*mm,88*mm),
        'B9':(44*mm,62*mm),
        'B10':(31*mm,44*mm),
        'C0':(917*mm,1297*mm),
        'C1':(648*mm,917*mm),
        'C2':(458*mm,648*mm),
        'C3':(324*mm,458*mm),
        'C4':(229*mm,324*mm),
        'C5':(162*mm,229*mm),
        'C6':(114*mm,162*mm),
        'C7':(81*mm,114*mm),
        'C8':(57*mm,81*mm),
        'C9':(40*mm,57*mm),
        'C10':(28*mm,40*mm),
        'oficio':(216*mm,330*mm)
    }
    Xmm=200.0/REALmm[0]
    Ymm=200.0/REALmm[1]
    page=hoja['A4']
    escala=escalar
    escalaX,escalaY=(REALsize[0]/(page[0]/mm)) if REALsize[0]>0.0 else 1.0,(REALsize[1]/(page[1]/mm)) if REALsize[1]>0.0 else 1.0
    menorX,menorY,mayorX,mayorY=0,0,0,0
    poligono=poligonos
    lines=lineas
    textos=printTEXT

    for polig in range(0,len(poligono),1): 
        for p in range(0,len(poligono[polig]),1):
            poligono[polig][p]=[poligono[polig][p][0]*mm*Xmm , poligono[polig][p][1]*mm*Ymm]
        for p in poligono[polig]:
            if p[0]<menorX:
                menorX=p[0]
            if p[0]>mayorX:
                mayorX=p[0]
            if p[1]<menorY:
                menorY=p[1]
            if p[1]>mayorY:
                mayorY=p[1]    
    for l in range(0,len(lines),1): 
        lines[l] = [lines[l][0]*mm*Xmm,lines[l][1]*mm*Ymm,lines[l][2]*mm*Xmm,lines[l][3]*mm*Ymm]
        menorX=lines[l][0] if lines[l][0]<menorX else menorX
        mayorX=lines[l][0] if lines[l][0]>mayorX else mayorX
        menorX=lines[l][2] if lines[l][2]<menorX else menorX
        mayorX=lines[l][2] if lines[l][2]>mayorX else mayorX
        menorY=lines[l][1] if lines[l][1]<menorY else menorY
        mayorY=lines[l][1] if lines[l][1]>mayorY else mayorY
        menorY=lines[l][3] if lines[l][3]<menorY else menorY
        mayorY=lines[l][3] if lines[l][3]>mayorY else mayorY
        #print(lines[l])
    mayorX=mayorX-menorX
    mayorY=mayorY-menorY
    divisionX=1
    divisionY=1
    if (page[0]*escalaX) < mayorX:
        divisionX=int(mayorX/(page[0]*escalaX))+1
        
    if (page[1]*escalaY) < mayorY:
        divisionY=int(mayorY/(page[1]*escalaY))+1
    geo=geometria()
    planos=[]
    #trasladamos todos los puntos de todos los poligonos al primer Cuadrante
    for t in range(0,len(textos),1):
        print(textos[t])
        textos[t][0]=textos[t][0]*mm*Xmm-(menorX)
        textos[t][1]=textos[t][1]*mm*Ymm-(menorY)
    for polig in range(0,len(poligono),1): 
        for p in range(0,len(poligono[polig]),1):
            poligono[polig][p]=(poligono[polig][p][0]-(menorX),poligono[polig][p][1]-(menorY))
    for l in range(0,len(lines),1): 
        lines[l] = [lines[l][0]-menorX,lines[l][1]-menorY,lines[l][2]-menorX,lines[l][3]-menorY]
    #pasamos las lineas a poligonos
    divX=[x*page[0]*escalaX for x in range(0,divisionX,1)]+[mayorX]
    divY=[y*page[1]*escalaY for y in range(0,divisionY,1)]+[mayorY]
    print("cortando")
    for l in range(0,len(lines),1): 
        v=[lines[l][2]-lines[l][0],lines[l][3]-lines[l][1],0]
        oX = lines[l][0] if v[0]==0.0 else -1.0
        oY = lines[l][1] if v[1]==0.0 else -1.0
        Yf=lines[l][1] if lines[l][1]>lines[l][3] else lines[l][3]
        Yi=lines[l][1] if lines[l][1]<lines[l][3] else lines[l][3]
        Xf=lines[l][0] if lines[l][0]>lines[l][2] else lines[l][2]
        Xi=lines[l][0] if lines[l][0]<lines[l][2] else lines[l][2]
        # dividimos en Y
        div=[divY[d] for d in range(0,len(divY)-1,1) if ((divY[d]<=Yi) and (divY[d+1]>=Yi))]
        div = div[0] if div else 0.0
        puntos = [[(((float(y)/10.0)-lines[l][1])/(v[1]/v[0])+lines[l][0]) if v[0]!=0.0 else lines[l][0],(float(y)/10.0)] for y in range(int(div*10),int(Yf*10),int(page[1]*escalaY*10))[1:]]
        # dividimos en X
        div=[divX[d] for d in range(0,len(divX)-1,1) if ((divX[d]<=Xi) and (divX[d+1]>=Xi))]
        div = div[0] if div else 0.0
        puntos += [[float(x)/10.0,(((float(x)/10.0)-lines[l][0])*(v[1]/v[0])+lines[l][1]) if v[1]!=0.0 else lines[l][1]] for x in range(int(div*10),int(Xf*10),int(page[0]*escalaX*10))[1:]]
        polig=[lines[l][0:2]]
        distancias=[[geo.dist(lines[l][0:2]+[0],p+[0]),p[0],p[1]] for p in puntos]
        for p in range(0,len(puntos),1):
            menor=geo.dist(lines[l][0:2]+[0],lines[l][2:]+[0])
            pos=0
            for x in range(0,len(distancias),1):
                if distancias[x][0]<menor:
                    menor=distancias[x][0]
                    pos=x
            polig += [[(((distancias[pos][2]-1.0)-lines[l][1])/(v[1]/v[0])+lines[l][0]) if v[0]!=0.0 else lines[l][0],distancias[pos][2]-1.0]]
            polig += [[(((distancias[pos][2]+1.0)-lines[l][1])/(v[1]/v[0])+lines[l][0]) if v[0]!=0.0 else lines[l][0],distancias[pos][2]+1.0]]
            distancias.pop(pos)
        polig += [lines[l][2:]]
        poligono += [polig]
    margen=margenes if margenes else [((page[0]*(1.0-escalaX))/2),((page[1]*(1.0-escalaY))/2)]
    txt=[]
    for x in range(0,divisionX,1):
        for y in range(0,divisionY,1):
            txt= [[]]+txt
            for t in textos:
                if (((page[0]*escalaX)>=(t[0]-(x*page[0]*escalaX))) and ((t[0]-(x*page[0]*escalaX))>=0.0) ) and (((page[1]*escalaY) >= (t[1]-(y*page[1]*escalaY)))  and ((t[1]-(y*page[1]*escalaY))>=0.0)) :
                    txt[0] += [[ t[0]-(x*page[0]*escalaX)+margen[0],t[1]-(y*page[1]*escalaY)+margen[1],t[2],t[3] ]]
    for polig in range(0,len(poligono),1): 
        plano=[]
        matriz=[]
        for x in range(0,divisionX,1):
            for y in range(0,divisionY,1):
                plano = [[]] + plano
                matriz += [[divisionX-x-1,divisionY-y-1]]
                for p in poligono[polig]:
                    if (((page[0]*escalaX)>=(p[0]-(x*page[0]*escalaX))) and ((p[0]-(x*page[0]*escalaX))>=0.0) ) and (((page[1]*escalaY) >= (p[1]-(y*page[1]*escalaY)))  and ((p[1]-(y*page[1]*escalaY))>=0.0)) :
                        plano[0] += [ [(p[0]-(x*page[0]*escalaX))+margen[0] , (p[1]-(y*page[1]*escalaY))+margen[1]]]
                        
        planos += [plano]
    global canvas
    canvas = canvas.Canvas(datos['archivo'], pagesize=page)
    def texto(x,y,ang,txt):
        print(x,y,ang,txt)
        canvas.saveState()
        rad=-1*math.radians(float(ang))
        i, j=geo.rotar(rad,[x,y,0])
        canvas.rotate(ang)
        canvas.drawString(i,j,str(txt))
        canvas.restoreState()

    def cuadriculando(cuadricular):
        if cuadricular:
            canvas.saveState()
            canvas.setDash(1,10)
            canvas.setLineWidth(0.1)
            #linea Vartical
            canvas.line((page[0]/2), page[1]-margen[1], (page[0]/2), margen[1])
            #linea Horizontal
            canvas.line(margen[0],(page[1]/2),page[0]-margen[0],(page[1]/2))
            #linea Diagonal de Superior Izquierdo a inferior derecho
            canvas.line(margen[0], page[1]-margen[1], page[0]-margen[0],margen[1])
            #linea Diagonal de inferior Izquierdo a Superior Derecho
            canvas.line(margen[0],margen[1],page[0]-margen[0],page[1]-margen[1])
            #limites
            canvas.setDash(5,5)
            canvas.setLineWidth(0.3)
            #limite horizontal superior
            canvas.line((page[0]/2)-50, page[1]-margen[1],(page[0]/2)+50, page[1]-margen[1])
            #limite horizontal inferior
            canvas.line((page[0]/2)-50, margen[1],(page[0]/2)+50, margen[1])
            #limite Vertical Derecho
            canvas.line((page[0]-margen[0]), (page[1]/2)-50,(page[0]-margen[0]), (page[1]/2)+50)
            #limite Vertical Izquierdo
            canvas.line((margen[0]), (page[1]/2)-50,(margen[0]), (page[1]/2)+50)
            canvas.restoreState()
            
    if not calibrar:
        hojaConDibujo=[0]*(divisionY*divisionX)
        print(hojaConDibujo)
        canvas.setLineWidth(3)
        for x in range(0,(divisionY*divisionX),1):
            dibujado=0
            if txt[x]:
                for t in txt[x]:
                    texto(*t)
            for p in range(0,len(planos),1):
                if len(planos[p][x])>1:
                    hojaConDibujo[x] = 1        
                if len(planos[p][x])>1 or imprimirHojasEnblanco:
                    cuadriculando(cuadricular)
                    dibujado=1
                    for g in range(0,len(planos[p][x])-1,1):
                        canvas.line(planos[p][x][g][0], planos[p][x][g][1], planos[p][x][g+1][0], planos[p][x][g+1][1])
            if dibujado:
                canvas.drawString(10.0*mm,800,str(matriz[x]))
                canvas.drawString(page[0]-20.0*mm,(15*mm),str(x+1))
                canvas.showPage()
                canvas.setLineWidth(3)
        print(hojaConDibujo)
        datos['cantidadTotalDeHojas']=divisionX*divisionY
        datos['HojasEnBlanco']=str([x+1 for x in range(0,len(hojaConDibujo),1) if hojaConDibujo[x]==0 ])
        datos['HojasConDibujo']=str([x+1 for x in range(0,len(hojaConDibujo),1) if hojaConDibujo[x]>0 ])
    canvas.setLineWidth(0.3)
    canvas.setFont('Helvetica', fontSize)
    contador=1
    datos['miniatura']=str(bool(miniatura))
    datos['tipoDeHoja']='A4'
    datos['medidasDeLaHoja']=[page[0]/mm,page[1]/mm]
    datos['ALTOdelDibujo']=mayorY/mm
    datos['ANCHOdelDibujo']=mayorX/mm
    datos['imprimirHojasEnblanco']=str(bool(imprimirHojasEnblanco))
    canvas.setLineCap(1) #extremo de la linea redondeada
    cuadriculando(cuadricular)
    canvas.setDash(6,3)# sucesion de 6 puntos trazados y 3 no trazados
    for x in datos:
        if (page[1]-(contador*fontSize*mm))<(fontSize*mm):
            canvas.showPage()
            canvas.setLineCap(1)
            contador=1
            cuadriculando(cuadricular)
            canvas.setDash(6,3)# sucesion de 6 puntos trazados y 3 no trazados
        canvas.drawString(30+margen[0],page[1]-(contador*fontSize*2.0)-margen[1],str(x)+':')
        #((0,len(str(datos[x])),40))
        canvas.line(100+((len(x)-10)*5 if len(x)>10 else 0)+margen[0],page[1]-(contador*fontSize*2.0)-2-margen[1],580-margen[0],page[1]-(contador*fontSize*2.0)-2-margen[1])
        canvas.drawString(100+((len(x)-10)*5 if len(x)>10 else 0)+margen[0],page[1]-(contador*fontSize*2.0)-margen[1],str(datos[x]))
        contador += 1
    canvas.setLineWidth(1)
    canvas.setDash(1,0) #dibuja 1 puntos y ignora 0 puntos
    canvas.setLineCap(2) #extremo de la linea cuadrada
    #linea que agarra toda la hoja de izquierda a derecha, osea horizontal
    canvas.drawString((page[0]/2),page[1]-(contador*fontSize*2.0)+5,str(page[0]/mm)+'mm. RealANCHO')
    canvas.line(0, page[1]-(contador*fontSize*2.0), page[0], page[1]-(contador*fontSize*2.0))
    contador+=1
    #100mm horizontales
    canvas.drawString((page[0]/2),page[1]-(contador*fontSize*2.0)+5,str(100)+'mm. REALmmX')
    canvas.line((page[0]/2)-50.0*mm, page[1]-(contador*fontSize*2.0), (page[0]/2)+50.0*mm, page[1]-(contador*fontSize*2.0))

    texto(page[0]-10.0*mm-margen[0],(page[1]/2),90.0,str(page[1]/mm)+'mm. RealALTO')
    texto(page[0]-20.0*mm-margen[0],(page[1]/2),90.0,str(100)+'mm. REALmmY')
    #100mm verticales
    canvas.line(page[0]-10.0*mm-margen[0], page[1], page[0]-10.0*mm-margen[0], 0.0)
    #linea que agarra toda la hoja de arriba a abajo, osea vertical
    canvas.line(page[0]-20.0*mm-margen[0], (page[1]/2)+50.0*mm, page[0]-20.0*mm-margen[0], (page[1]/2)-50.0*mm)    
    canvas.save()
    print("Ok")
def planos():
    escala=1.0
    puntos,lineas,datos,textos = aspas(escalar=escala)
    datos['plano']="Hoja de una turbina de viento"
    datos['archivo']="plano_escala_1.0_Turbina_eolica.pdf"
    datos['UnidadDeMedida']="milimetros"
    datos['escala']=str(escala)
    poligonoToPDF(calibrar=0,miniatura=1,poligonos=[puntos],lineas=lineas,datos=datos, printTEXT=textos)
    if input("Ya imprimio y saco las medidas de la hoja de prueba? S/N:").lower()=="s":
        RealANCHO=float(input("RealANCHO: "))
        RealALTO=float(input("RealALTO: "))
        REALmmX=float(input("REALmmX: "))
        REALmmY=float(input("REALmmY: "))
        margenX=float(input("margen superior: "))
        margenY=float(input("margen Izquierdo: "))
        miniatura=int(input("ImprmirMiniatura 1/0 : "))
        #=float(input(": "))
        poligonoToPDF(calibrar=0,miniatura=miniatura,REALsize=[RealANCHO,RealANCHO],margenes=[margenX,margenY],REALmm=[REALmmX,REALmmY],poligonos=[puntos],lineas=lineas,datos=datos)

if 'main' in __name__:
    from pruebas import main_pruebas
    pruebas=[powerPDF]
    main_pruebas(pruebas,sys.argv)
            