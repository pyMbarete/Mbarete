import os
import math
global d,canvas_width,canvas_height
d={
    'img':os.getcwd()+'\\'+'media'+'\\'+"img"+'\\',
    'audio':os.getcwd()+'\\'+"audio"+'\\'
    }
canvas_width = 1100
canvas_height =int((canvas_width/5)*3)
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
    pwd=d['img']
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
showAlbum()

#prepararPNG(d['img'],"convertRGBA_FULL_53.53_sexy.png")