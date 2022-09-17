from tkinter import *
from tkinter import font
from reportlab import *
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib.colors import tan, black, green
from reportlab.lib.units import inch,mm
import tkinter.colorchooser as colorchooser
import math
import time
import threading
import os

from extras import saveVar,saveColeccionVar
from matematica import geometria,varianza,promedio,multiplicarMatriz
from mbarete import calculadora
from GUI import FrameScroll,widgetUtils

def crono(mini=0,maxi=5,step=1,ti='seg'):
    tiempo={'seg':1,'miliseg':0.001}
    t=tiempo[ti]
    for x in range(mini+1,maxi+1,step): 
        labelcrono.config(text=str(x))
        raiz.update()
        time.sleep(t)
def circulin(radio=10,Cx=10,Cy=10,grado0=0,gradoF=360):
    r=float(radio)
    centroX=float(Cx)
    centroY=float(Cy)
    g0=grado0
    gf=gradoF
    if math.fabs(grado0-gradoF)>=360:
        circulo=(centroX+math.cos(math.radians(float(g0)))*r,centroY+math.sin(math.radians(float(g0)))*r)
    else:
        circulo=(centroX,centroY)
        circulo+=(centroX+math.cos(math.radians(float(g0)))*r,centroY+math.sin(math.radians(float(g0)))*r)
    for g in range(g0,gf,1):
        rad=math.radians(float(g))
        circulo+=(centroX+math.cos(rad)*r,centroY-math.sin(rad)*r)
    #cu.create_polygon(circulo,fill=fondot,outline=fondo)
def polig(xplace,yplace,ancho,alto,radio=10,text="",fontSize=11,fontType='Arial',fill='#ff0000',outline='#ff00f0',fontColor='#ffffff',alcance=100):
    def get_puntos(p=(1.0,1.0),r=1.0,desde=0,hasta=90,pasos=1):
        pasos=int(abs(pasos) if desde<hasta else -1*abs(pasos))
        #calculamos los puntos de la curva de la ezquinas
        if r>0:
            Cx=p[0]-r*( math.cos(math.radians(float(desde)))+math.cos(math.radians(float(hasta))) )
            Cy=p[1]+r*( math.sin(math.radians(float(desde)))+math.sin(math.radians(float(hasta))) )
            p=(Cx+math.cos(math.radians(float(desde)))*r,Cy-math.sin(math.radians(float(desde)))*r)
            for g in range(desde,hasta,pasos):
                rad=math.radians(float(g))
                p+=(Cx+math.cos(rad)*r,Cy-math.sin(rad)*r)
            p+=(Cx+math.cos(math.radians(float(hasta)))*r,Cy-math.sin(math.radians(float(hasta)))*r)
        return p
    
    r=float( radio if ( (radio*2<=alto) and (radio*2<=ancho) ) else (alto//2 if alto<ancho else ancho//2) ) 

    #superior  izquierdo
    puntos=get_puntos(p=(xplace,yplace),desde=180,hasta=90,r=r)
    #superior derecho
    puntos+=get_puntos(p=(xplace+ancho,yplace),desde=90,hasta=0,r=r)
    #inferior derecho
    puntos+=get_puntos(p=(xplace+ancho,yplace+alto),desde=0,hasta=-90,r=r)
    #inferior izquierdo
    puntos+=get_puntos(p=(xplace,yplace+alto),desde=-90,hasta=-180,r=r)

    cu.create_polygon(puntos,fill=fill,outline=outline)
    if text and (len(text)*7):
        cu.create_text(xplace+int(ancho/2), yplace+int(alto/2),fill=fontColor,font=(fontType,fontSize), text=str(text))
def aspas(x=10,y=10,dividir=120,baseRadio=100.0,altura=100.0,revolucion=360,rotorRadio=5.0,fondo=60):
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
    yOut=[geo.dis([xR[0],yR[0],zR[0]],[xA[0],yA[0],zA[0]])]
    xIn =[0]
    yIn =[0]
    for n in range(1,fin+1,1):
        A=[xA[n-1],yA[n-1],zA[n-1]] #punto que ya esta en el plano
        B=[xR[n-1],yR[n-1],zR[n-1]] #punto origen que ya esta en plano
        C=[xA[n],yA[n],zA[n]]       #punto que se agregara al plano
        xO=geo.dis(geo.alt(C,A,B),C)
        yO=geo.dis(geo.alt(C,A,B),B)
        #print(math.degrees(angRad([0,1,0],resta([xIn[-1],yIn[-1],0],[xOut[-1],yOut[-1],0]))))
        rot= -1*math.fabs(geo.angRad([0,1,0],geo.resta([xIn[-1],yIn[-1],0],[xOut[-1],yOut[-1],0])))
        xRot, yRot=geo.rotar(rot,[xO,yO,0])
        xTras, yTras=geo.trasladar([xIn[-1],yIn[-1],0],[xRot,yRot,0])
        yOut.append(yTras)
        xOut.append(xTras)
        A=[xA[n],yA[n],zA[n]]
        B=[xR[n-1],yR[n-1],zR[n-1]]
        C=[xR[n],yR[n],zR[n]]
        xO= geo.dis(geo.alt(C,A,B),C)
        yO= geo.dis(geo.alt(C,A,B),B) if geo.dis(geo.alt(C,A,B),A)<geo.dis(A,B) else geo.dis(geo.alt(C,A,B),B)*(-1)
        rot= -1*math.fabs(geo.angRad([0,1,0],geo.resta([xIn[-1],yIn[-1],0],[xOut[-1],yOut[-1],0])))
        xRot, yRot=geo.rotar(rot,[xO,yO,0])
        xTras, yTras=geo.trasladar([xIn[-1],yIn[-1],0],[xRot,yRot,0])
        yIn.append(yTras)
        xIn.append(xTras)
    angulo = [(n, xOut[n]+(x), yOut[n]+(y), xIn[n]+(x), yIn[n]+(y), zR[n]+fondo) for n in range(0,len(xOut),dividir)]+[(fin, xOut[fin]+(x), yOut[fin]+(y), xIn[fin]+(x), yIn[fin]+(y), zR[fin]+fondo)]
    poligono = [(xOut[n]+(x),yOut[n]+(y)) for n in range(0,len(xOut),1)]+[(xIn[n]+(x),yIn[n]+(y)) for n in range(len(xIn)-1,-1,-1)]+[(xOut[0]+x,yOut[0]+y)]
    return poligono, angulo, fin
def penciltip(debug=1):
    from reportlab.lib.colors import tan, black, green
    from reportlab.lib.units import mm
    from reportlab.pdfgen import canvas
    canvas = canvas.Canvas("plano.pdf", pagesize=letter)
    canvas.setLineWidth(.3)
    canvas.setFont('Helvetica', 8)
    baseRadio=100.0
    profundidad=60.0
    angulos=120
    altura=100.0
    revolucion=360
    rotorRadio=5.0
    puntos,angulo,fin = aspas(x=10,y=int((780-(geometria().hypotenusa(baseRadio,profundidad)*mm))/mm),dividir=angulos,baseRadio=baseRadio,altura=altura,revolucion=revolucion,rotorRadio=rotorRadio,fondo=profundidad)
    #canvas.line(480,747,580,747)
    canvas.drawString(10,70,'Plano: ')
    canvas.drawString(10,60,'Giro real: '+str(fin)+" grados")
    canvas.drawString(10,50,'Radio Base: '+str(baseRadio)+" mm")
    canvas.drawString(10,40,'Radio Rotor: '+str(rotorRadio)+" mm")
    canvas.drawString(10,30,'Fondo: '+str(profundidad)+" mm")
    canvas.drawString(10,20,'Altura: '+str(altura)+" mm")
    canvas.drawString(10,10,'Giro Especulado: '+str(revolucion)+" grados")
    canvas.setLineWidth(3)
    canvas.drawString(10.0*mm,780,'100mm')
    canvas.line(10.0*mm, 780, 110.0*mm, 780)
    canvas.line(5.0*mm, 250*mm, 5.0*mm, 150*mm)
    canvas.setLineWidth(.3)
    for g in range(0,len(puntos)-1,1):
        canvas.line(puntos[g][0]*mm, puntos[g][1]*mm, puntos[g+1][0]*mm, puntos[g+1][1]*mm)
    canvas.setLineWidth(3)
    for g in range(0,len(angulo),1):
        canvas.line(angulo[g][1]*mm, angulo[g][2]*mm, angulo[g][3]*mm, angulo[g][4]*mm)
        canvas.drawString(angulo[g][1]*mm+((angulo[g][1]*mm-angulo[g][3]*mm)/100), angulo[g][2]*mm+((angulo[g][2]*mm-angulo[g][4]*mm)/100),'_'+str(angulo[g][0])+'grados, altura: '+str( str(angulo[g][5]) if (6 > len(str(angulo[g][5]))) else str(angulo[g][5])[:5] )+'mm')
    #canvas.drawString(puntos[int((len(puntos)-2)/2)][0]*mm, puntos[int((len(puntos)-2)/2)][1]*mm,'_'+str(int((len(puntos)-1)/2))+'grados')
    canvas.save()
    print("Ok")
def totalScroll_treview():
    from myVars import inputsDefault
    from tkinter import ttk
    root=Tk()
    #root.wm_attributes('-alpha',0.5)
    # with Windows OS
    root.bind("<MouseWheel>",lambda event: canvas.yview_scroll(int(-1*(event.delta/120)), "units"))
    root.bind("<Destroy>",lambda event: print('<Destroy>') )
    #root.bind("<Leave>",lambda event: print('<Leave>') )
    root.bind("<Map>",lambda event: print(event) )
    root.bind("<Expose>",lambda event: print(event) )
    #root.bind("<13>",lambda event: print('<GraphicsExpose>',event) )
    #root.bind("<NoExpose>",lambda event: print('<NoExpose>') )
    root.bind("<Visibility>",lambda event: print(event) )
    #root.bind("<UnMap>",lambda event: print('<UnMap>') )
    root.bind("<MapRequest>",lambda event: print('<MapRequest>') )
    root.bind("<Reparent>",lambda event: print('<Reparent>') )
    #root.bind("<Selection>",lambda event: print('<Selection>') )
    #root.bind("<Mapping>",lambda event: print('<Mapping>') )
    root.bind("<Activate>",lambda event: print('<Activate>') )
    root.bind("<Deactivate>",lambda event: print('<Deactivate>') )
    #root.bind("<SelectionClear>",lambda event: print('<SelectionClear>') )
    root.bind("<FocusIn>",lambda event: print(event) )
    root.bind("<FocusOut>",lambda event: print('<FocusOut>') )
    root.bind("<Gravity>",lambda event: print('<Gravity>') )
    #root.bind("<Keymap>",lambda event: print('<Keymap>') )
    root.bind("<Create>",lambda event: print('<Create>') )
    root.bind("<Circulate>",lambda event: print('<Circulate>') )
    #root.bind("<>",lambda event: print('<>') )
    root.bind("<Property>",lambda event: print('<Property>') )
    root.bind("<Configure>",lambda event: print(event) )
    # with Linux OS
    #root.bind("<Button-4>",MouseWheelHandler)
    #root.bind("<Button-5>",MouseWheelHandler)
    frame=FrameScroll(root,geometry=(100,100,10,10))
    for x in range(10):
        Label(frame, text='Prueba Label '+str('@'*(x+1)),bg='#f0f0f0').pack()   

    tree = ttk.Treeview(frame,columns=tuple('#'+str(c+1) for c in range(len(inputsDefault['help']))))
    tree.pack()
    tree.heading("#0", text="ID")
    num=['#'+str(c+1) for c in range(len(inputsDefault['help']))]
    count=0
    for c in inputsDefault['help']:
        print(str(c))
        tree.heading(str(num[count]), text=c,width=50)
        count += 1
    #
    count=0
    for c in inputsDefault:
        #inputsDefault[c]['id']=count
        if inputsDefault[c]:
            tree.insert("", END, text=count,
                values=tuple(inputsDefault[c][h] for h in inputsDefault[c]))
        count += 1
 
    root.update()
    root.mainloop()
def hexagesimal_to_int(*color):
    escala={
        '0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,
        'a':10,'b':11,'c':12,'d':13,'e':14,'f':15
        }
    rgb=[]
    for c in [*color]:
        rgb+=[[]]
        for h in range(1,len(c),2):
            rgb[-1]+=[float((escala[c[h]]*16)+(escala[c[h-len(c)+1]]))]
    return tuple(rgb)
def int_to_hexagesimal(*arg):
    r=''
    for h in [*arg]:
        r += ("" if h>15 else "0")+str(hex(h))[2:]
    if len(r)==6: r='#'+r
    return r
def Gradient(color1,color2,h=500,w=500,ang=0.0,x=0.0,y=0.0):
    geo=geometria()
    [r1,g1,b1],[r2,g2,b2]=hexagesimal_to_int(color1,color2)
    
    lines=[]
    
    if ang!=0.0:
        ang=math.radians(ang)
        p=[
            [x-w/2.0,y-h/2.0],[x+w/2.0,y-h/2.0],
            [x-w/2.0,y+h/2.0],[x+w/2.0,y+h/2.0]
            ]
        p= [ geo.rotar(ang,v,O=[x,y]) for v in p ]
        p.sort(reverse=False,key=lambda x: x[0])
        A,C=p[0],p[3]
        B,D=p[1],p[2] if  p[1]>p[2] else p[2],p[1]
        ACx=int(A[0]-C[0])
        r=(r2-r1)/(ACx)
        g=(g2-g1)/(ACx)
        b=(b2-b1)/(ACx)
        print(p)
        for i in range(int(A[0]),int(C[0])):
            RR=int(r1+(r*(i-int(A[0]))))
            GG=int(g1+(g*(i-int(A[0]))))
            BB=int(b1+(b*(i-int(A[0]))))
            if A[0]<=i<=B[0]:
                j0=(((A[0]-B[0])*(A[0]-i))/(A[0]+B[0]))+B[1]
            elif B[0]<=i<=C[0]:
                j0=(((B[0]-C[0])*(B[0]-i))/(B[0]+C[0]))+C[1]
            if A[0]<=i<=D[0]:
                j1=(((A[0]-D[0])*(A[0]-i))/(A[0]+D[0]))+D[1]
            elif D[0]<=i<=C[0]:
                j1=(((D[0]-C[0])*(D[0]-i))/(D[0]+C[0]))+C[1]
            color=[int_to_hexagesimal(RR,GG,BB)]
            lines +=[geo.rotar(-ang,[i,j0],O=[x,y])+geo.rotar(-ang,[i,j1],O=[x,y])+color]

    else:
        for i in range(w):
            RR=int(r1+(r*i))
            GG=int(g1+(g*i))
            BB=int(b1+(b*i))
            color=int_to_hexagesimal(RR,GG,BB)
            lines +=[[i,0,i,h,color]]
            #,tags=("gradient",)
    return lines
def pruebaTreeview():
    from myVars import inputsDefault
    from tkinter import ttk

    window = Tk()
    treeview = ttk.Treeview(window)
    treeview.pack()
    treeview.insert("", END, text="Elemento 1")
    item = treeview.insert("", END, text="Elemento 2")
    treeview.insert(item, END, text="Subelemento 2")
    # Imprime los elementos del árbol.
    print(treeview.get_children())
    # Imprime los elementos dentro del Elemento 1.
    print(treeview.get_children(item))
    item1 = treeview.insert("", END, text="Elemento 1")
    item2 = treeview.insert("", END, text="Elemento 2")
    #Podemos mover el Elemento 1 dentro del Elemento 2 vía:
    treeview.move(item1, item2, END)
    # Elimina el elemento 2.
    item1 = treeview.insert("", END, text="Elemento 1")
    item2 = treeview.insert("", END, text="Elemento 2")
    treeview.delete(item2)
    # Desvincula el elemento 1.
    treeview.detach(item1)            

    print(treeview.exists(item2))  # False.
    print(treeview.exists(item1))  # True.
    treeview.focus(item)  # Pone el foco en item.
    print(treeview.focus())  # Retorna el ID de item.
    item1 = treeview.insert("", END, text="Elemento 1")
    item2 = treeview.insert("", END, text="Elemento 2")
    print(treeview.index(item1))  # 0
    print(treeview.index(item2))  # 1
    print(inputsDefault['help'])
    print(tuple(c for c in inputsDefault['help'] if c!='id'))

    tree = ttk.Treeview(window,columns=tuple('#'+str(c+1) for c in range(len(inputsDefault['help']))))
    tree.pack()
    tree.heading("#0", text="ID")
    num=['#'+str(c+1) for c in range(len(inputsDefault['help']))]
    count=0
    for c in inputsDefault['help']:
        print(str(c))
        tree.heading(str(num[count]), text=c)
        count += 1
    #
    count=0
    for c in inputsDefault:
        #inputsDefault[c]['id']=count
        if inputsDefault[c]:
            tree.insert("", END, text=count,
                values=tuple(inputsDefault[c][h] for h in inputsDefault[c]))
        count += 1
            #tree.insert(inputsDefault[c]['id'],inputsDefault[c]['id'], inputsDefault[c]['id'])
    #tree.insert("", END, text="README.txt",values=("850 bytes", "18:30"))
    # Imprime {'lastmod': '18:30', 'size': '850 bytes'}.
    print(tree.set(item))

    window.mainloop()
class longuitud_de_Fonts(widgetUtils,FrameScroll):
    """docstring for longuitud_de_Fonts"""
    def __init__(self, *arg,**kwargs):
        widgetUtils.__init__(self)
        self.c_width = {}
        self.label={}
        self.c_width={'key':[],'mono':[]}
        FrameScroll.__init__(
            self,
            Tk(),
            titulo="Medidas de los caracteres en pixeles ",
            icon='',
            geometry=(650,400,700,50)
            )
        self.font_family=list(font.families())
        print(len(self.font_family))
        self.font_family.sort()
        #['\t','\r','\n']+
        x,y=self.setVar(
            [
                ('widget',list(self.class_tk)[0],list(self.class_tk)),
                ('fontSize',list(self.Sizes)[3],list(self.Sizes)),
                ('fontType',self.font_family[0],self.font_family),
                ('letra',' ',[str(chr(x)) for x in range(32,127)]),
                ('repeticiones',40,range(10,50,5)),
                ('ancho',0,range(0,500,10))
                ],
            widget=self.crearEntry,
            x=10,y=10,limites=(self.ancho,self.alto),inputVar=1
            )
        #Separator(self.raiz, orient=HORIZONTAL)
        self.setVar(
            [   
                ('dibujar_todos','Todos',self.muestreo),
                ('dibujar_este','Este',self.dibujar),
                ('mostar_Fonts','Fonts',self.dibujar_todos),
                ('mostar_btn','Widget',self.getWidgetWidth),
                ('mostar_btn','Guardar',self.guardarVariables)
                ],
            widget=self.crearButton,
            x=x,y=y,limites=(self.ancho,self.alto)
            )
        #self.showVars()
        self.updateScroll()
        self.loop()
    def guardarVariables(self):
        from widgetSizebtn import widgetSizebtn
        from widgetSizeentry import widgetSizeentry
        from fontSize import fontSizes
        saveColeccionVar(
            [
                ['font',fontSizes],
                ['btn',widgetSizebtn],
                ['entry',widgetSizeentry]
                ],
            file='Sizes.py',m='a'
            )
        
    def setDiv(self,name,text,command,place,**kwarg):
        self.widgets[name]=Button(
            self,
            text=text,
            command=command,
            **kw
            )
        self.widgets[name].place(x=place[0],y=place[1])    
    def dibujar_todos(self):
        
        ancho=self.v['ancho'].get()
        self.v['ancho'].set(0)
        for x in self.font_family:
            self.v['fontType'].set(x)
            self.dibujar()
        self.v['ancho'].set(ancho)
        saveVar(
            'fontSize.py',
            {'Sizes':self.Sizes,**self.c_width},
            name='fontSizes'
            )
        
    def guardar_letra(self,var,file,**kw):
        #guardara la variable 'var' con las indentaciones para leer facil
        saveVar(file,var,**kw)
        print('guardado: %s'%(file))        
    def crearEntry(self,e,x,y,limites=(),w=160, h=75,x0=0,y0=0,**kw):
        #self.setWidget(w_tk,name,text='',width=None,place=(),**kwarg)
        mas_x,mas_y=[0],[0]
        if x+w>=limites[0]:
            mas_x+=[x0-x]
            mas_y+=[h]
            x,y=x0,y+h
        sizelb=self.setWidget('lb',e[0],text=e[0],place=(x,y),**kw)
        mas_x+=[sizelb['text'][0]]
        size_y=sizelb['text'][1]
        if e[2]:
            size=self.setWidget(
                'btn',
                'bajar_'+e[0],
                text='Bajar',
                command=lambda :self.cambiar(e[0],-1),
                place=(x,y+sizelb['text'][1]),
                **kw
                )
            mas_x+=[size['widget'][0]]
            size_y+=size['widget'][1]
            size=self.setWidget(
                'btn',
                'subir_'+e[0],
                text='Subir',
                command=lambda :self.cambiar(e[0],+1),
                place=(x+mas_x[-1],y+sizelb['text'][1]),
                **kw
                )
            mas_x[-1]+=size['widget'][0]
            #size['widget']=(sizelb['widget'][0]+size['widget'][0],sizelb['widget'][1]+size['widget'][1])
        self.widgets['btn']['bajar_'+e[0]].update()
        self.widgets['btn']['subir_'+e[0]].update()
        h=self.widgets['btn']['subir_'+e[0]].winfo_height()
        w=self.widgets['btn']['subir_'+e[0]].winfo_width()
        size=self.setWidget(
            'entry',
            e[0],
            place=(x, y+size_y),
            textvariable=self.v[e[0]],
            **kw
            )
        mas_x+=[size['widget'][0]]
        return max(mas_x)+min(mas_x),sum(mas_y)
    def crearButton(self,e,x,y,w=160, h=75,x0=0,y0=0,limites=(),**kw):
        #self.setWidget(w_tk,name,text='',width=None,place=(),**kwarg)
        sizelb=self.setWidget('btn',e[0],text=e[1],command=e[2],place=(x,y),**kw)
        return sizelb['widget'][0],0
    def dibujar(self):
        self.liberarCanvas()
        ySuma=200
        abc=self.valores['letra']
        ancho=self.v['ancho'].get()
        alto_letras={}
        x_alto=abc.index(' ')
        #self.polig(0,0,self.ancho,(len(abc)*len(self.Sizes)*20)+ySuma,radio=5,fill=self.color['bg'],outline='#ff00f0')
        self.c_width[self.v['fontType'].get()] = {}
        new_dict={ k:{} for k in self.keySizes }
        for x in range(len(abc)):
            c=abc[x]*self.v['repeticiones'].get()
            #polig(50,ySuma,int(strPixel("abc defg_hijklmnñopqrstuvwxyz....."[0:x])),20,radio=5,text=str("abc defg_hijklmnñopqrstuvwxyz.....")[0:x])
            for k in self.keySizes:
                self.v['fontSize'].set( self.keySizes[k] )
                #self.Sizes[self.v['fontSize'].get()]
                size = self.polig(
                    50,
                    ySuma,
                    ancho,
                    20,
                    radio=5,
                    text=c,
                    size=1
                    )
                if (x==3) and (not k in alto_letras):
                    alto_letras[k]=size[1]
                promedio=round(float(size[0])/float(self.v['repeticiones'].get()),4)
                #alto=size[1]
                self.polig(
                    int(self.ancho*0.5)+120, 
                    ySuma,
                    0,
                    20,
                    text='%s,%s'%(promedio,size[1])
                    )
                ySuma += 20
                new_dict[k][ord(abc[x])]=promedio
        for k in new_dict:
            if new_dict[k] in self.c_width['key']:
                ID=self.c_width['key'].index(new_dict[k])
            else:
                ID=len( self.c_width['key'] )
                self.c_width['key'] += [new_dict[k]]
            new_dict[k]=ID
        self.c_width[self.v['fontType'].get()]['width']=new_dict
        self.c_width[self.v['fontType'].get()]['height']=alto_letras
        self.updateScroll( h=ySuma )
        print(self.v['fontType'].get(),alto_letras)
    
    def writeString(self,t,x,y,font,size,**kw):
        w=self.textWidth(t,font,self.Sizes[size])
        h=self.fontSize[font]['height'][size]
        self.polig(x,y,w,h, radio=5, text=t,**kw)
        return w,h
    def muestreo(self):
        self.liberarCanvas()
        text=['Vote for difficulty. Current difficulty : [Basic]']
        ySuma=200
        xMax=0
        k=self.v['fontSize'].get()
        for ft in self.fontSize:
            for t in text:
                print(ft,k)
                if 'Sizes' == ft: continue
                xSuma=50
                self.v['fontType'].set(ft)
                w,h=self.writeString(ft,xSuma,ySuma,ft,k)
                xSuma+=w
                #alto=size[1]
                w,h=self.writeString(t,xSuma,ySuma,ft,k)
                xSuma+=w
                if (xSuma > xMax): xMax=xSuma
                ySuma += h
            self.updateScroll( h=ySuma ,w=xMax)
        print(self.v['fontType'].get(),text)
    def getWidgetWidth(self):
        self.liberarCanvas()
        self.widthHeight={'key':[]}
        ID=0
        widget=self.v['widget'].get()
        for ft in self.font_family:
            if 'Sizes' == ft: continue
            self.v['fontType'].set(ft)
            ySuma=200
            xMax=0
            self.widthHeight[ft]={'width':{},'height':{}}
            for i in self.keySizes:
                new_list=[0]
                h=0
                for s in range(1,35):
                    size=self.setWidget(
                        widget,
                        'width_%s'%(s),
                        text='width_%s'%(s),
                        width=s,
                        font=(ft,i),
                        place=(10,ySuma)
                        )
                    self.widgets[widget]['width_%s'%(s)].update()
                    h=self.widgets[widget]['width_%s'%(s)].winfo_height()
                    w=self.widgets[widget]['width_%s'%(s)].winfo_width()
                    new_list+=[w]
                    ySuma+=h
                    if w>xMax:xMax=w
                    self.updateScroll( h=ySuma ,w=xMax)
                for s in range(1,35):
                    self.widgets[widget]['width_%s'%(s)].destroy()
                    del self.widgets[widget]['width_%s'%(s)]
                if new_list in self.widthHeight['key']:
                    ID=self.widthHeight['key'].index(new_list)
                else:
                    ID=len(self.widthHeight['key'])
                    self.widthHeight['key']+=[new_list]
                self.widthHeight[ft]['width'][i]=ID
                self.widthHeight[ft]['height'][i]=h
            print(int((self.font_family.index(ft)/len(self.font_family))*100))
        saveVar(
            'widgetSize'+widget+'.py',
            self.widthHeight,
            name='widgetSize'+widget
            )
        
    def gradient(self,color1,color2,text="",h=500,w=500,ang=0.0,x=0.0,y=0.0,size=0):
        geo=geometria()
        [r1,g1,b1],[r2,g2,b2]=hexagesimal_to_int(color1,color2)
        lines=[]
        ang=math.radians(ang)
        if g!=0.0:
            p=[[x-w/2.0,y-h/2.0],[x+w/2.0,y-h/2.0],[x-w/2.0,y+h/2.0],[x+w/2.0,y+h/2.0]]
            p= [geo.rotar(ang,v,O=[x,y]) for v in p]
            p.sort(reverse=False,key=lambda x: x[0])
            A,C=p[0],p[3]
            B,D=p[1],p[2] if  p[1]>p[2] else p[2],p[1]
            ACx=int(A[0]-C[0])
            r=(r2-r1)/(ACx)
            g=(g2-g1)/(ACx)
            b=(b2-b1)/(ACx)
            print(p)
            for i in range(int(A[0]),int(C[0])):
                RR=int(r1+(r*(i-int(A[0]))))
                GG=int(g1+(g*(i-int(A[0]))))
                BB=int(b1+(b*(i-int(A[0]))))
                if A[0]<=i<=B[0]:
                    j0=(((A[0]-B[0])*(A[0]-i))/(A[0]+B[0]))+B[1]
                elif B[0]<=i<=C[0]:
                    j0=(((B[0]-C[0])*(B[0]-i))/(B[0]+C[0]))+C[1]
                if A[0]<=i<=D[0]:
                    j1=(((A[0]-D[0])*(A[0]-i))/(A[0]+D[0]))+D[1]
                elif D[0]<=i<=C[0]:
                    j1=(((D[0]-C[0])*(D[0]-i))/(D[0]+C[0]))+C[1]
                color=int_to_hexagesimal(RR,GG,BB)
                p=[geo.rotar(-ang,[i,j0],O=[x,y])+geo.rotar(-ang,[i,j1],O=[x,y])]
                self.canvas.create_line(*p,fill=color)
                lines +=[p+[color]]
        else:
            for i in range(w):
                RR=int(r1+(r*i))
                GG=int(g1+(g*i))
                BB=int(b1+(b*i))
                color=int_to_hexagesimal(RR,GG,BB)
                lines +=[[i,0,i,h,color]]
                #,tags=("gradient",)
        if text:
            if size:
                size=self.canvas.bbox(self.canvas.create_text(x+int(w/2), y+int(h/2),fill=self.color_fg,font=(self.v['fontType'].get(),self.Sizes[self.v['fontSize'].get()]), text=str(text)))
                return ( size[2] - size[0], size[3] - size[1] )
            else:
                self.canvas.create_text(xplace+int(w/2), y+int(h/2),fill=self.color_fg,font=(self.v['fontType'].get(),self.Sizes[self.v['fontSize'].get()]), text=str(text))
        return lines
    def polig(self,xplace,yplace,ancho,alto,radio=10,text="",fontSize=11,fontType='Arial',fill='#ff0f0f',outline='#0101f0',fontColor='#ffffff',alcance=100,size=0):
        def get_puntos(p=(1.0,1.0),r=1.0,desde=0,hasta=90,pasos=1):
            pasos=int(abs(pasos) if desde<hasta else -1*abs(pasos))
            #calculamos los puntos de la curva de la ezquinas
            if r>0:
                Cx=p[0]-r*( math.cos(math.radians(float(desde)))+math.cos(math.radians(float(hasta))) )
                Cy=p[1]+r*( math.sin(math.radians(float(desde)))+math.sin(math.radians(float(hasta))) )
                p=(Cx+math.cos(math.radians(float(desde)))*r,Cy-math.sin(math.radians(float(desde)))*r)
                for g in range(desde,hasta,pasos):
                    rad=math.radians(float(g))
                    p+=(Cx+math.cos(rad)*r,Cy-math.sin(rad)*r)
                p+=(Cx+math.cos(math.radians(float(hasta)))*r,Cy-math.sin(math.radians(float(hasta)))*r)
            return p
            
        if ancho and alto:
            r=float( radio if ( (radio*2<=alto) and (radio*2<=ancho) ) else (alto//2 if alto<ancho else ancho//2) ) 
            #superior  izquierdo
            puntos=get_puntos(p=(xplace,yplace),desde=180,hasta=90,r=r)
            #superior derecho
            puntos+=get_puntos(p=(xplace+ancho,yplace),desde=90,hasta=0,r=r)
            #inferior derecho
            puntos+=get_puntos(p=(xplace+ancho,yplace+alto),desde=0,hasta=-90,r=r)
            #inferior izquierdo
            puntos+=get_puntos(p=(xplace,yplace+alto),desde=-90,hasta=-180,r=r)
            self.canvas.create_polygon(puntos,fill=fill,outline=outline)
        if text and (len(text)*7):
            if size:
                size=self.canvas.bbox(self.canvas.create_text(
                    xplace+int(ancho/2), 
                    yplace+int(alto/2),
                    fill=self.color['frame']['fg'],
                    font=(
                        self.v['fontType'].get(),
                        self.Sizes[self.v['fontSize'].get()]
                        ), 
                    text=str(text)
                    ))
                return ( size[2] - size[0], size[3] - size[1] )
            else:
                self.canvas.create_text(
                    xplace+int(ancho/2), 
                    yplace+int(alto/2),
                    fill=self.color['frame']['fg'],
                    font=(
                        self.v['fontType'].get(),
                        self.Sizes[self.v['fontSize'].get()]
                        ), 
                    text=str(text)
                    )

def setter_loop(var,value,keys=[]):
    if keys:
        if not len(keys):print(keys)
        var[keys[0]]=setter_loop(var[keys[0]],value,keys=keys[1:])
    else:
        var=value
    return var
def compresion(l,unicos,_get=None,keys=None):
    if l.__class__ in [list,dict]:
        if l.__class__ == list:iterar=range(len(l))
        if l.__class__ == dict:iterar=l
        for e in iterar:
            u=_get(l[e]) if _get else l[e]
            if u in unicos: i=unicos.index(u)
            else:
                i=len(unicos)
                unicos+=[u]
            if keys: l[e]=setter_loop(l[e],i,keys=keys)
            else: l[e]= i
    return l,unicos

def analizarVariables():
    
    from Sizes import font as f
    from Sizes import btn,entry
    print(len(f['key']))
    #[str(chr(x)) for x in range(32,127)]
    for x in list(range(32,127))+[10]: print(',',x,':',str(chr(x)),end='')
    ignorar_key=['Sizes','meta','mono','key']
    f['meta']={}
    key_ord=[]
    key=[[]]
    mono={}
    v=[]
    new_index={}
    new_Font={}
    width = []
    height = []
    for c in f['key'][0]: 
        key_ord+=[c]
        key[0]+=[f['key'][0][c]]
    v+=[round(varianza(key[-1]),4)]
    for x in range(1,len(f['key'])):
        comp=[f['key'][x][i] for i in f['key'][x]]
        v+=[round(varianza(comp),4)]
        if v[-1] == 0.0:
            mono[x]=round(promedio(comp),4)
        else:
            new_index[x]=len(key)
            key+=[comp]
    f['meta']['Sizes']=f['Sizes']
    f['meta']['new_index']=new_index
    f['meta']['mono']=mono
    f['meta']['key_varianza']=v
    f['meta']['key_ord']=key_ord
    f['meta']['key']=key
    del f['Sizes']
    del f['mono']
    l=[[k for k in e if not k in ignorar_key] for e in [f,entry,btn] ]
    if l[0]==l[1]==l[2]:
        l=[f,entry,btn]
        print('font, btn y entry iguales')
        ft=[k for k in f if not k in ignorar_key]
        for v in range(len(l)):
            l[v]={k:l[v][k] for k in ft} 
            l[v],width=compresion(
                l[v],
                width,
                _get=lambda d : d['width'],
                keys=['width']
                )
            l[v],height=compresion(
                l[v],
                height,
                _get=lambda d : d['height'],
                keys=['height']
                )
        ft={ft[k]:k for k in range(len(ft))}
        for v in range(len(l)):
            l[v]=[(l[v][e]['width'],l[v][e]['height']) for e in ft]
        for s in range(len(width)):
            width[s]=[width[s][i] for i in width[s]]
        for s in range(len(height)):
            height[s]=[height[s][i] for i in height[s]]

        
    else:
        print(" las variables no son iguales ")
    
    del f['key']
    #print(l[1])
        
    saveColeccionVar([
        ['widget',{'font':l[0],'entry':l[1],'btn':l[2]}],
        ['meta',
            {
                'width':width,'height':height,
                'Sizes':f['meta']['Sizes'],'new_index':new_index,
                'mono':mono,'fontType':ft,'key_ord':key_ord
                }
            ],
        ['key',key]
        ],
        file='fontWidthHeightSizes.py',m='a',deep=2
        )
    os.system('ls -hs fontWidthHeight*')
    print('2146.54'.isdigit(),'4.5'.isnumeric())
def longitud_de_caracteres():
    #print(hexagesimal_to_int('#408080'))
    App=longuitud_de_Fonts()
    #lines=Gradient('#408080','#040808',h=App.height,w=500,ang=20.0,x=0.0,y=0.0)

#clase principal
class function:
    def __init__(self, x,name):
        self.x = np.array(x)
        self.name = name
    def __str__(self):
        info = 'Function ' + self.name
        return info
    def plot3D(self):
        a = np.linspace(-1, 1, 10) # Search Space
        x1, x2 = np.meshgrid(a, a)
        X = np.column_stack((np.ravel(x1), np.ravel(x2)))
        Z = np.apply_along_axis(self.value, 1, X) #aqui self.value
        Z = Z.reshape(x1.shape)
        fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
        surf = ax.plot_surface(
            x1, x2, Z, 
            cmap = cm.coolwarm, 
            linewidth=0, 
            antialiased=False
            )
        plt.tight_layout()
        plt.show()
#subclase
class Sphere(function):
    def __init__(self, x,name = 'Sphere'):
        super(Sphere,self).__init__(x,name)
        #ya heredaste la clase principal 'function' 
        #ahora la 'function' puede usar 'value' con self.value
    def value(self,*arg):
        print([*arg],end='')
        return np.sum(self.x**2)
def pruebas_herencias():
    import numpy as np
    from matplotlib import cm
    import matplotlib.pyplot as plt
    x = [1,1,1,1,1]
    f1 = Sphere(x)
    print(f1)
    #print("f(x) = ",f1.value())
    f1.plot3D()
def veces_seccion(s,m):
    memo=[]
    l=len(s)
    for j0 in range(l,len(m)):
        if s == m[j0-l:j0]:
            if not memo:
                memo+=[[j0-l,j0]]
            if [ j0 for p in memo if not (p[0]<=j0<=(p[1]+l)) ]:
                memo+=[[j0-l,j0]]
    return memo
            
def list_test():
    key=[
        [1.05, 1.05, 2.05, 3.05, 3.05, 4.05, 3.05, 1.05, 2.05, 2.05, 3.05, 3.05, 1.05, 2.05, 1.05, 3.05, 3.05, 1.05, 3.05, 3.05, 3.05, 3.05, 3.05, 2.05, 3.05, 3.05, 1.05, 1.05, 2.05, 3.05, 2.05, 3.05, 4.05, 3.05, 3.05, 3.05, 3.05, 2.05, 2.05, 3.05, 3.05, 1.05, 3.05, 3.05, 2.05, 3.05, 3.05, 3.05, 3.05, 3.05, 3.05, 3.05, 2.05, 3.05, 3.05, 4.05, 3.05, 3.05, 2.05, 2.05, 3.05, 2.05, 3.05, 2.05, 3.05, 3.05, 3.05, 2.05, 3.05, 2.05, 2.05, 3.05, 3.05, 1.05, 1.05, 2.05, 1.05, 4.05, 3.05, 3.05, 3.05, 3.05, 2.05, 2.05, 2.05, 3.05, 2.05, 3.05, 2.05, 2.05, 2.05, 2.05, 1.05, 2.05, 3.05],
        [2.05, 2.05, 3.05, 5.05, 4.05, 6.05, 4.05, 1.05, 2.05, 2.05, 4.05, 4.05, 1.05, 3.05, 1.05, 4.05, 4.05, 2.05, 3.05, 4.05, 3.05, 4.05, 4.05, 3.05, 4.05, 4.05, 1.05, 1.05, 3.05, 4.05, 3.05, 3.05, 5.05, 4.05, 4.05, 4.05, 4.05, 3.05, 3.05, 4.05, 4.05, 2.05, 3.05, 3.05, 3.05, 4.05, 4.05, 4.05, 4.05, 4.05, 4.05, 4.05, 3.05, 4.05, 3.05, 5.05, 3.05, 3.05, 3.05, 3.05, 4.05, 3.05, 4.05, 3.05, 4.05, 3.05, 3.05, 3.05, 3.05, 3.05, 2.05, 3.05, 3.05, 2.05, 2.05, 3.05, 2.05, 5.05, 3.05, 3.05, 3.05, 3.05, 3.05, 3.05, 2.05, 3.05, 3.05, 4.05, 3.05, 3.05, 3.05, 3.05, 2.05, 3.05, 4.05],
        [2.05, 2.05, 4.05, 6.05, 5.05, 8.05, 5.05, 2.05, 3.05, 3.05, 5.05, 5.05, 2.05, 4.05, 2.05, 5.05, 5.05, 2.05, 5.05, 5.05, 5.05, 5.05, 5.05, 4.05, 5.05, 5.05, 2.05, 2.05, 4.05, 5.05, 4.05, 5.05, 7.05, 5.05, 5.05, 5.05, 5.05, 4.05, 4.05, 5.05, 5.05, 2.05, 5.05, 5.05, 4.05, 6.05, 5.05, 5.05, 5.05, 6.05, 5.05, 5.05, 4.05, 5.05, 5.05, 7.05, 5.05, 5.05, 4.05, 4.05, 5.05, 4.05, 5.05, 4.05, 5.05, 5.05, 5.05, 5.05, 5.05, 5.05, 3.05, 5.05, 5.05, 2.05, 2.05, 4.05, 2.05, 7.05, 5.05, 5.05, 5.05, 5.05, 4.05, 4.05, 3.05, 5.05, 4.05, 6.05, 4.05, 4.05, 4.05, 4.05, 3.05, 4.05, 6.05],
        [3.05, 4.05, 5.05, 9.05, 7.05, 12.05, 8.05, 3.05, 5.05, 5.05, 7.05, 7.05, 3.05, 5.05, 3.05, 8.05, 8.05, 4.05, 7.05, 8.05, 7.05, 7.05, 8.05, 6.05, 8.05, 8.05, 3.05, 3.05, 6.05, 8.05, 6.05, 7.05, 10.05, 7.05, 8.05, 8.05, 8.05, 6.05, 6.05, 8.05, 8.05, 4.05, 7.05, 7.05, 6.05, 9.05, 8.05, 8.05, 7.05, 8.05, 8.05, 7.05, 6.05, 8.05, 7.05, 10.05, 7.05, 7.05, 6.05, 5.05, 8.05, 5.05, 7.05, 6.05, 7.05, 7.05, 7.05, 7.05, 7.05, 7.05, 4.05, 7.05, 7.05, 3.05, 3.05, 6.05, 3.05, 10.05, 7.05, 7.05, 7.05, 7.05, 6.05, 6.05, 5.05, 7.05, 6.05, 9.05, 6.05, 6.05, 6.05, 6.05, 4.05, 6.05, 9.05],
        [5.05, 5.05, 8.05, 14.05, 11.05, 18.05, 12.05, 4.05, 7.05, 7.05, 11.05, 11.05, 4.05, 8.05, 4.05, 12.05, 12.05, 5.05, 10.05, 11.05, 10.05, 11.05, 11.05, 10.05, 12.05, 11.05, 4.05, 4.05, 9.05, 12.05, 9.05, 10.05, 15.05, 11.05, 11.05, 11.05, 12.05, 10.05, 9.05, 11.05, 12.05, 5.05, 10.05, 10.05, 9.05, 13.05, 12.05, 12.05, 11.05, 12.05, 11.05, 11.05, 9.05, 12.05, 10.05, 15.05, 10.05, 10.05, 9.05, 8.05, 12.05, 8.05, 11.05, 10.05, 11.05, 10.05, 10.05, 10.05, 10.05, 10.05, 6.05, 10.05, 10.05, 5.05, 5.05, 9.05, 5.05, 16.05, 10.05, 10.05, 10.05, 10.05, 9.05, 10.05, 7.05, 10.05, 9.05, 13.05, 9.05, 9.05, 9.05, 9.05, 5.05, 9.05, 13.05],
        [2.05, 2.05, 4.05, 4.05, 4.05, 6.05, 6.05, 2.05, 3.05, 3.05, 4.05, 6.05, 2.05, 2.05, 2.05, 3.05, 4.05, 4.05, 4.05, 4.05, 4.05, 4.05, 4.05, 4.05, 4.05, 4.05, 2.05, 2.05, 7.05, 6.05, 7.05, 3.05, 6.05, 5.05, 4.05, 5.05, 5.05, 4.05, 4.05, 5.05, 5.05, 2.05, 3.05, 5.05, 4.05, 6.05, 5.05, 6.05, 4.05, 6.05, 4.05, 3.05, 4.05, 5.05, 5.05, 6.05, 5.05, 4.05, 4.05, 3.05, 3.05, 3.05, 3.05, 3.05, 4.05, 3.05, 4.05, 3.05, 4.05, 3.05, 2.05, 3.05, 4.05, 2.05, 2.05, 3.05, 2.05, 6.05, 4.05, 4.05, 4.05, 4.05, 3.05, 2.05, 2.05, 4.05, 3.05, 5.05, 4.05, 3.05, 3.05, 3.05, 3.05, 3.05, 7.05],
        [3.05, 3.05, 5.05, 6.05, 6.05, 9.05, 8.05, 3.05, 4.05, 4.05, 6.05, 9.05, 3.05, 3.05, 3.05, 4.05, 6.05, 6.05, 6.05, 6.05, 6.05, 6.05, 6.05, 6.05, 6.05, 6.05, 3.05, 3.05, 9.05, 9.05, 9.05, 5.05, 9.05, 7.05, 6.05, 6.05, 7.05, 5.05, 5.05, 7.05, 7.05, 3.05, 4.05, 6.05, 5.05, 8.05, 7.05, 8.05, 5.05, 8.05, 6.05, 5.05, 5.05, 7.05, 6.05, 8.05, 6.05, 6.05, 6.05, 4.05, 4.05, 4.05, 4.05, 4.05, 6.05, 4.05, 5.05, 4.05, 5.05, 4.05, 3.05, 5.05, 5.05, 2.05, 2.05, 5.05, 2.05, 7.05, 5.05, 5.05, 5.05, 5.05, 3.05, 3.05, 3.05, 5.05, 4.05, 7.05, 5.05, 5.05, 4.05, 4.05, 4.05, 4.05, 9.05],
        [4.05, 4.05, 7.05, 8.05, 8.05, 12.05, 11.05, 4.05, 5.05, 5.05, 8.05, 12.05, 4.05, 4.05, 4.05, 6.05, 8.05, 8.05, 8.05, 8.05, 8.05, 8.05, 8.05, 8.05, 8.05, 8.05, 4.05, 4.05, 12.05, 12.05, 12.05, 6.05, 12.05, 9.05, 8.05, 9.05, 9.05, 7.05, 7.05, 9.05, 9.05, 4.05, 5.05, 9.05, 7.05, 11.05, 10.05, 11.05, 7.05, 11.05, 8.05, 6.05, 7.05, 9.05, 9.05, 11.05, 9.05, 8.05, 8.05, 6.05, 6.05, 6.05, 6.05, 6.05, 8.05, 6.05, 7.05, 6.05, 7.05, 6.05, 5.05, 6.05, 7.05, 3.05, 3.05, 6.05, 3.05, 10.05, 7.05, 7.05, 7.05, 7.05, 5.05, 5.05, 5.05, 7.05, 6.05, 9.05, 7.05, 6.05, 5.05, 6.05, 6.05, 6.05, 12.05],
        [6.05, 6.05, 10.05, 11.05, 11.05, 17.05, 16.05, 6.05, 8.05, 8.05, 11.05, 17.05, 6.05, 6.05, 6.05, 8.05, 11.05, 11.05, 11.05, 11.05, 11.05, 11.05, 11.05, 11.05, 11.05, 11.05, 6.05, 6.05, 18.05, 17.05, 18.05, 9.05, 17.05, 13.05, 12.05, 13.05, 13.05, 10.05, 10.05, 13.05, 14.05, 6.05, 8.05, 12.05, 10.05, 17.05, 14.05, 16.05, 10.05, 16.05, 12.05, 9.05, 11.05, 14.05, 13.05, 17.05, 12.05, 11.05, 11.05, 8.05, 8.05, 8.05, 9.05, 9.05, 11.05, 8.05, 10.05, 8.05, 10.05, 9.05, 7.05, 9.05, 10.05, 5.05, 5.05, 9.05, 5.05, 15.05, 10.05, 10.05, 10.05, 10.05, 7.05, 7.05, 7.05, 10.05, 9.05, 13.05, 10.05, 9.05, 8.05, 9.05, 9.05, 9.05, 18.05],
        [9.05, 9.05, 15.05, 17.05, 17.05, 26.05, 24.05, 9.05, 12.05, 12.05, 17.05, 26.05, 9.05, 9.05, 9.05, 12.05, 17.05, 17.05, 17.05, 17.05, 17.05, 17.05, 17.05, 17.05, 17.05, 17.05, 9.05, 9.05, 27.05, 26.05, 27.05, 14.05, 26.05, 20.05, 18.05, 19.05, 20.05, 15.05, 15.05, 20.05, 21.05, 9.05, 11.05, 19.05, 15.05, 25.05, 22.05, 24.05, 16.05, 24.05, 18.05, 14.05, 16.05, 21.05, 19.05, 25.05, 19.05, 17.05, 17.05, 12.05, 12.05, 12.05, 13.05, 13.05, 17.05, 12.05, 15.05, 12.05, 15.05, 13.05, 10.05, 14.05, 15.05, 7.05, 7.05, 14.05, 7.05, 22.05, 15.05, 15.05, 15.05, 15.05, 10.05, 10.05, 10.05, 15.05, 13.05, 20.05, 14.05, 14.05, 11.05, 13.05, 13.05, 13.05, 27.05],
        [2.05, 2.05, 4.05, 4.05, 4.05, 7.05, 6.05, 2.05, 3.05, 3.05, 4.05, 7.05, 2.05, 2.05, 2.05, 3.05, 4.05, 4.05, 4.05, 4.05, 4.05, 4.05, 4.05, 4.05, 4.05, 4.05, 2.05, 2.05, 7.05, 7.05, 7.05, 3.05, 7.05, 5.05, 5.05, 5.05, 5.05, 4.05, 4.05, 5.05, 5.05, 3.05, 3.05, 5.05, 4.05, 7.05, 6.05, 6.05, 4.05, 6.05, 5.05, 4.05, 4.05, 5.05, 5.05, 7.05, 5.05, 4.05, 4.05, 3.05, 3.05, 3.05, 3.05, 3.05, 4.05, 3.05, 4.05, 3.05, 4.05, 3.05, 2.05, 4.05, 4.05, 2.05, 2.05, 4.05, 2.05, 6.05, 4.05, 4.05, 4.05, 4.05, 3.05, 3.05, 3.05, 4.05, 4.05, 5.05, 4.05, 4.05, 3.05, 3.05, 3.05, 3.05, 7.05]
    ]
    contador={}
    new_key=[]
    l=6
    for i in range(len(key)):
        for i0 in range(l,len(key[i])):
            s=key[i][i0-l:i0]
            for j in range(len(key)):
                memo=veces_seccion(s,key[j])
                if ([i0-l,i0] in memo) and j==i:
                    memo.pop(memo.index([i0-l,i0]))
                if memo:
                    if (not (s in new_key)):
                        contador[len(new_key)]=1
                        new_key+=[s]
                        print('New Seccion TRUE')
                    else:
                        contador[new_key.index(s)]+=1
    repe=[contador[c]*l for c in contador]
    print(len(new_key),len(contador))
    print(repe)
    print(len(key)*len(key[0]),sum(repe),len(new_key)*l)


if 'main' in __name__:
    from pruebas import main_pruebas
    pruebas=[
        {'titulo':"Nombre del script:",'f':lambda: print(__name__)},
        {'titulo':"hallar longuitud de caracteres:",'f':longitud_de_caracteres},
        {'titulo':"Analizar variables grandes:",'f':analizarVariables},
        {'titulo':"Herencias:",'f':pruebas_herencias},
        {'titulo':"Listas Pruebas:",'f':list_test}
        ]
    main_pruebas(pruebas,sys.argv)