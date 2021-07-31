from tkinter import *
from reportlab import *
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib.colors import tan, black, green
from reportlab.lib.units import inch
from reportlab.lib.units import mm
import tkinter.colorchooser as colorchooser
import math
import time
import threading
import os
os.chdir('..')
from mbarete import geometria,calculadora
global raiz,cu, largo,fondo,fondor,fondot,valor,labelcrono,textos,alto,ancho
global baseRadio,altura,revolucion,rotorRadio,fondo,angulos

class btnCanvas(object):
    """botones creados en el lienzo de canvas"""
    def __init__(self, arg):
        super(btnCanvas, self).__init__()
        self.arg = arg
        """
        Button(
            self.widgets[myWidget['padre']]['widget'], 
            text=myWidget['text'], 
            width=myWidget['width'] if myWidget['width'] else None, 
            bg=myWidget['bgColor'],
            fg=myWidget['fontColor'],
            font=(myWidget['fontType'],myWidget['fontSize']),
            command=lambda:threading.Thread(target=self.command[mywidget['name']][0],args=self.command[mywidget['name']][1]).start()
            )
        """        

largo=800
alto=largo
ancho=650
fondor= '#00001a'
fondot='#408080'
fondo='#f3a80c'
valor='texto de ejemplo'
def strToUnicode(strng):
    unicod=""
    for x in str(strng):
        unicod += r" "+str(ord(x))
    return unicod.strip()
def unicodeToStr(unicod):
    strng=""
    if unicod.strip()=="":
        return unicod
    else:
        for x in unicod.split(" "):
            strng += str(chr(int(x)))
        return strng.strip()
escala11={
    'Arial':{
        ' ':6.0,
        '_':8.0,
        '.':3.75,
        'a':7.833,
        'b':7.833,
        'c':7.833,
        'd':7.833,
        'e':7.833,
        'f':3.954,
        'g':7.833,
        'h':7.833,
        'i':2.809,
        'j':3.5,
        'k':7.0,
        'l':2.809,
        'm':13.0,
        'n':7.833,
        'ñ':7.833,
        'o':7.833,
        'p':7.833,
        'q':7.833,
        'r':6.0,
        's':7.769,
        't':3.954,
        'u':7.833,
        'v':6.5,
        'w':11.0,
        'x':6.7,
        'y':6.7,
        'z':7.6
    }
}
listaunicode={}
for letra in escala11['Arial']:
    listaunicode.setdefault(strToUnicode(letra),escala11['Arial'][letra])
def strPixel(string,fontType='Arial',fontSize=11):
    escala={'Arial':{'32': 6.0, '95': 8.0, '46': 3.75, '97': 7.833, '98': 7.833, '99': 7.833, '100': 7.833, '101': 7.833, '102': 3.954, '103': 7.833, '104': 7.833, '105': 2.809, '106': 3.5, '107': 7.0, '108': 2.809, '109': 13.0, '110': 7.833, '241': 7.833, '111': 7.833, '112': 7.833, '113': 7.833, '114': 6.0, '115': 7.769, '116': 3.954, '117': 7.833, '118': 6.5, '119': 11.0, '120': 6.7, '121': 6.7, '122': 7.6}}
    longitud=0
    for letra in string:
        longitud+=escala[fontType][strToUnicode(letra)]    
    return longitud+1
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
    cu.create_polygon(circulo,fill=fondot,outline=fondo)
def polig(xplace,yplace,ancho,alto,radio=10,text="",fontSize=11,fontType='Arial',fill='#ff0000',outline='#ff00f0',fontColor='#ffffff',alcance=100):
    if (radio*2<=alto) and (radio*2<=ancho):
        r=float(radio)
    else:
        r=float(int(alto/2)) if alto<ancho else float(int(ancho/2))  
    if r>0:    
        punto1=(xplace,yplace+r)
        centroX=xplace+r
        centroY=yplace+r
        for g in range(180,90,-1):
            rad=math.radians(float(g))
            punto1+=(centroX+math.cos(rad)*r,centroY-math.sin(rad)*r)
        punto1+=(xplace+r,yplace)
    else:
        punto1=(xplace,yplace)
    if r>0:
        punto2=(xplace+ancho-r,yplace)
        centroX=xplace+ancho-r
        centroY=yplace+r
        for g in range(90,0,-1):
            rad=math.radians(float(g))
            punto2+=(centroX+math.cos(rad)*r,centroY-math.sin(rad)*r)
        punto2+=(xplace+ancho,yplace+r)
    else:
        punto2=(xplace+ancho,yplace)
    if r>0:
        punto3=(xplace+ancho,yplace+alto-r)
        centroX=xplace+ancho-r
        centroY=yplace+alto-r
        for g in range(0,-90,-1):
            rad=math.radians(float(g))
            punto3+=(centroX+math.cos(rad)*r,centroY-math.sin(rad)*r)
        punto3+=(xplace+ancho-r,yplace+alto)
    else:
        punto3=(xplace+ancho,yplace+alto)
    if r>0:
        punto4=(xplace+r,yplace+alto)
        centroX=xplace+r
        centroY=yplace+alto-r
        for g in range(-90,-180,-1):
            rad=math.radians(float(g))
            punto4+=(centroX+math.cos(rad)*r,centroY-math.sin(rad)*r)
        punto4+=(xplace,yplace+alto-r)
    else:
        punto4=(xplace,yplace+alto)
    puntos=punto1+punto2+punto3+punto4
    cu.create_polygon(puntos,fill=fill,outline=outline)
    if text and (len(text)*7):
        cu.create_text(xplace+int(ancho/2), yplace+int(alto/2),fill=fontColor,font=(fontType,fontSize), text=str(text))
        cu.create_text(alcance+10, yplace+int(alto/2),fill=fontColor,font=(fontType,fontSize), text=str(len(text))+' , '+str(ancho)+' , '+str(float(ancho)/float(len(text)))[0:5])
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
#penciltip()
def escalarHex(h="#ffffff",factor=1.0):
    escala={'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'a':10,'b':11,'c':12,'d':13,'e':14,'f':15}
    RR=int(float((escala[h[1:3][0]])*16+(escala[h[1:3][1]]))*factor)
    GG=int(float((escala[h[3:5][0]])*16+(escala[h[3:5][1]]))*factor)
    BB=int(float((escala[h[5:][0]])*16+(escala[h[5:][1]]))*factor)
    #print(str(hex(RR)),str(hex(GG)),str(hex(BB)))
    ret='#'+("" if RR>15 else "0")+str(hex(RR))[2:]+("" if GG>15 else "0")+str(hex(GG))[2:]+("" if BB>15 else "0")+str(hex(BB))[2:]
    #print(RR,GG,BB,ret[0:7])
    return ret[0:7]
import builtins
global correo,cu,labelcrono,raiz,textos,correoVar,ciVar,totalVar,timbreVar,v
def caja():
    #print(dir(memoryview.tobytes))
    #print(dir(globals))
    #print(dir(builtins))
    def len_string(string,fontType='Arial',fontSize=11):
        longitud={
            'Arial':{
                'A':9.0,'a':8.0,'b':8.0,'c':8.0,'d':8.0,'e':8.0,'f':4.0,
                'g':8.0,'h':8.0,'i':3.0,'j':3.0,'k':7.0,'l':3.0,'m':13.0,
                'n':8.0,'ñ':8.0,'o':8.0,'p':8.0,'q':8.0,'r':5.0,'s':8.0,
                't':4.0,'u':8.0,'v':7.0,'w':11.0,'x':7.0,'y':7.0,'z':8.0,
                '.':4.0,'B':10.0,'C':11.0,'D':11.0,'E':10.0,'F':9.0,'G':11.0,
                'H':10.0,'I':3.0,'J':7.0,'K':10.0,'L':8.0,'M':11.0,'N':10.0,
                'Ñ':10.0,'O':12.0,'P':10.0,'Q':12.0,'R':11.0,'S':10.0,'T':9.0,
                'U':10.0,'V':9.0,'W':15,'X':9.0,'Y':9.0,'Z':8.0,'0':8.0,
                '1':8.0,'2':8.0,'3':8.0,'4':8.0,'5':8.0,'6':8.0,'7':8.0,'8':8.0,'9':8.0
                }
            }
        l=0.0
        for c in string:
            if c in longitud[fontType]:
                l+=longitud[fontType][c]
            else:
                l += 8.0
        return l

    global correo,cu,labelcrono,raiz,textos,correoVar,ciVar,totalVar,timbreVar,widgets,v
    def validar(name,valido,*arg):
        #print(*arg)
        # 'highlightbackground' parametro para el color del borde cuando no esta enfocado
        # 'highlightcolor' color del entry couando esta enfocado
        # 'highlightthickness' grosol del borde
        if name in v:
            ret=v[name].get()
            #print(ret)
        if valido=="correo" and ret:
            if "@" in ret and (ret.split('@')[-1] in ['gmail.com','es','edu']):
                widgets[name].config(highlightbackground='green', highlightcolor= "green",highlightthickness=2)
            else:
                widgets[name].config(highlightbackground='red', highlightcolor= "red",highlightthickness=5)
    def dibujar(v,alto=800,ancho=650):
        polig(0,0,ancho,alto,radio=5,fill='#ff0000',outline='#ff00f0')
        fontType=v['fontType'].get()
        fontSize=v['fontSize'].get()
        repeticiones=v['repeticiones'].get()
        letra=v['letra'].get()
        desde=v['desde'].get()
        hasta=v['hasta'].get()
        pasos=v['pasos'].get()
        ySuma=200
        for x in range(desde,hasta,pasos):
            #polig(50,ySuma,int(strPixel("abc defg_hijklmnñopqrstuvwxyz....."[0:x])),20,radio=5,text=str("abc defg_hijklmnñopqrstuvwxyz.....")[0:x])

            polig(50,ySuma,x,20,radio=5,text=letra*repeticiones,fontSize=fontSize,fontType=fontType,fill='#0f0f0f',outline='#010101',alcance=int(ancho*0.8))

            #circulin(radio=10,Cx=25,Cy=ySuma,grado0=0,gradoF=int(360/(34-x)))
            ySuma += 30
        miFrameinicio.configure(width = ancho, height=ySuma+100)
        cu.configure(width = ancho, height=ySuma+100)
        raiz.update()
    def dibujarExacta(v,alto=800,ancho=650):
        polig(0,0,ancho,alto,radio=5,fill='#ff0000',outline='#ff00f0')
        fontType=v['fontType'].get()
        fontSize=v['fontSize'].get()
        repeticiones=v['repeticiones'].get()
        letra=v['letra'].get()
        desde=v['desde'].get()
        hasta=v['hasta'].get()
        pasos=v['pasos'].get()
        ySuma=200
        for x in range(desde,hasta,pasos):
            #polig(50,ySuma,int(strPixel("abc defg_hijklmnñopqrstuvwxyz....."[0:x])),20,radio=5,text=str("abc defg_hijklmnñopqrstuvwxyz.....")[0:x])

            polig(50,ySuma,x,20,radio=5,text=letra*repeticiones,fontSize=fontSize,fontType=fontType,fill='#0f0f0f',outline='#010101',alcance=int(ancho*0.8))

            #circulin(radio=10,Cx=25,Cy=ySuma,grado0=0,gradoF=int(360/(34-x)))
            ySuma += 30
        miFrameinicio.configure(width = ancho, height=ySuma+100)
        cu.configure(width = ancho, height=ySuma+100)
        raiz.update()
    widgets={}
    v={}
    label={}
    raiz=Tk()
    raiz.title("El Mejor Cajero del Mundo")
    scrollbar=Scrollbar(raiz)
    c = Canvas(raiz, yscrollcommand=scrollbar.set)
    scrollbar.config(command=c.yview)
    scrollbar.pack(side=RIGHT, fill=Y)
    miFrameinicio=Frame(c)
    miFrameinicio.configure(width = ancho, height=largo)
    cu=Canvas(miFrameinicio, width=ancho, height=largo, background=fondor)
    cu.place(x=-1, y=-1)
    c.pack(side="left" , fill="both", expand=True)
    c.create_window(0,0,window=miFrameinicio, anchor='nw')
    c.config(scrollregion=c.bbox("all"))
    v['fontType']=StringVar(value=str('Arial'))
    v['letra']=StringVar(value=str('a'))
    v['fontSize']=IntVar(value=11)
    v['desde']=IntVar(value=50)
    v['hasta']=IntVar(value=100)
    v['pasos']=IntVar(value=5)
    v['repeticiones']=IntVar(value=20)
    #Separator(self.raiz, orient=HORIZONTAL)

    label['fontSize']=Label(miFrameinicio, text='fontSize',fg=fondor,bg=fondo,font=("Arial",10),bd=0,justify="left",anchor=E)
    label['fontSize'].place(x=10, y=10)
    widgets['fontSize']=Entry(miFrameinicio,textvariable=v['fontSize'])
    widgets['fontSize'].place(x=10, y=45)

    label['fontType']=Label(miFrameinicio, text='fontType',fg=fondor,bg=fondo,font=("Arial",10),bd=0,justify="left",anchor=E)
    label['fontType'].place(x=150, y=10)
    widgets['fontType']=Entry(miFrameinicio,textvariable=v['fontType'])
    widgets['fontType'].place(x=150, y=45)
    
    label['letra']=Label(miFrameinicio, text='letra',fg=fondor,bg=fondo,font=("Arial",10),bd=0,justify="left",anchor=E)
    label['letra'].place(x=290, y=10)
    widgets['letra']=Entry(miFrameinicio,textvariable=v['letra'])
    widgets['letra'].place(x=290, y=45)
    
    label['desde']=Label(miFrameinicio, text='desde',fg=fondor,bg=fondo,font=("Arial",10),bd=0,justify="left",anchor=E)
    label['desde'].place(x=10, y=65)
    widgets['desde']=Entry(miFrameinicio,textvariable=v['desde']).place(x=10, y=100)

    label['hasta']=Label(miFrameinicio, text='hasta',fg=fondor,bg=fondo,font=("Arial",10),bd=0,justify="left",anchor=E)
    label['hasta'].place(x=150, y=65)
    widgets['hasta']=Entry(miFrameinicio,textvariable=v['hasta'])
    widgets['hasta'].place(x=150, y=100)

    label['pasos']=Label(miFrameinicio, text='pasos',fg=fondor,bg=fondo,font=("Arial",10),bd=0,justify="left",anchor=E)
    label['pasos'].place(x=290, y=65)
    widgets['pasos']=Entry(miFrameinicio,textvariable=v['pasos'])
    widgets['pasos'].place(x=290, y=100)
    
    label['repeticiones']=Label(miFrameinicio, text='repeticiones',fg=fondor,bg=fondo,font=("Arial",10),bd=0,justify="left",anchor=E)
    label['repeticiones'].place(x=10, y=120)
    widgets['repeticiones']=Entry(miFrameinicio,textvariable=v['repeticiones'])
    widgets['repeticiones'].place(x=10, y=155)

    widgets['boton']=Button(miFrameinicio,text='Dibujar',command=lambda: dibujar(v),width=5,bg='#2e2e2e').place(x=150,y=155)
    
    raiz.geometry(str(ancho)+"x"+str(alto)+"+10+10")
    raiz.update()
    c.config(scrollregion=c.bbox("all"))
    #print(foco)
    #threading.Thread(target=crono).start()
    raiz.mainloop()
def totalScroll():
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
    f = Frame(root)
    width = height = 100
    canvas=Canvas(f)
    yscrollbar = Scrollbar(f, orient='vertical',command=canvas.yview)
    xscrollbar = Scrollbar(f, orient='horizontal',command=canvas.xview)
    frame=Frame(canvas)
    print(canvas.bbox("all"))
    frame.bind("<Configure>",lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
    canvas.create_window((0, 0), window=frame, anchor="nw")#esta linea equivale a: frame.pack(in_=canvas,anchor="nw")
    canvas.configure(xscrollcommand=xscrollbar.set,yscrollcommand=yscrollbar.set)
    yscrollbar.pack(side='right', fill='y')
    xscrollbar.pack(side='bottom', fill='x')
    f.pack(expand=1, fill='both')
    canvas.pack(side='left', fill='both', expand=1)
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
def canvasGradient(padre,color1,color2):
    escala={'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'a':10,'b':11,'c':12,'d':13,'e':14,'f':15}
    r1=float((escala[color1[1:3][0]])*16+(escala[color1[1:3][1]]))
    g1=float((escala[color1[3:5][0]])*16+(escala[color1[3:5][1]]))
    b1=float((escala[color1[5:][0]])*16+(escala[color1[5:][1]]))
    r2=float((escala[color2[1:3][0]])*16+(escala[color2[1:3][1]]))
    g2=float((escala[color2[3:5][0]])*16+(escala[color2[3:5][1]]))
    b2=float((escala[color2[5:][0]])*16+(escala[color2[5:][1]]))
    height=padre.winfo_height()
    width=padre.winfo_width()
    c=Canvas(padre,height=padre.winfo_height(),width=padre.winfo_width())
    print((c,height,width,color1,color2))
    r=(r2-r1)/width
    g=(g2-g1)/width
    b=(b2-b1)/width
    for i in range(width):
        RR=int(r1+(r*i))
        GG=int(g1+(g*i))
        BB=int(b1+(b*i))
        color='#'+("" if RR>15 else "0")+str(hex(RR))[2:]+("" if GG>15 else "0")+str(hex(GG))[2:]+("" if BB>15 else "0")+str(hex(BB))[2:]
        c.create_line(i,0,i,width,fill=color)
        #,tags=("gradient",)
        
    return c
def Gradient(padre,color1,color2):
    escala={'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'a':10,'b':11,'c':12,'d':13,'e':14,'f':15}
    r1=float((escala[color1[1:3][0]])*16+(escala[color1[1:3][1]]))
    g1=float((escala[color1[3:5][0]])*16+(escala[color1[3:5][1]]))
    b1=float((escala[color1[5:][0]])*16+(escala[color1[5:][1]]))
    r2=float((escala[color2[1:3][0]])*16+(escala[color2[1:3][1]]))
    g2=float((escala[color2[3:5][0]])*16+(escala[color2[3:5][1]]))
    b2=float((escala[color2[5:][0]])*16+(escala[color2[5:][1]]))
    height=padre.winfo_height()
    width=padre.winfo_width()
    r=(r2-r1)/width
    g=(g2-g1)/width
    b=(b2-b1)/width
    lines=[]
    for i in range(width):
        RR=int(r1+(r*i))
        GG=int(g1+(g*i))
        BB=int(b1+(b*i))
        color='#'+("" if RR>15 else "0")+str(hex(RR))[2:]+("" if GG>15 else "0")+str(hex(GG))[2:]+("" if BB>15 else "0")+str(hex(BB))[2:]
        lines +=[[i,0,i,height,color]]
        #,tags=("gradient",)
    return lines
def ventanaPersonalizada():
    global myX, myY,rootX,rootY,myFoco,fullalto,fullancho,ancho,alto
    myX=10
    myY=10
    rootX=10
    rootY=10
    ancho=500
    alto=300
    global lapsoRoot,lapsoOculto
    lapsoRoot=time.time()     
    lapsoOculto=time.time()     
    def expandir(v):
        global fullalto,fullancho,ancho,alto
        if v:
            btnMax.config(command=lambda:expandir(0))
            oculto.geometry('{0}x{1}+0+0'.format(10,10))
            root.geometry('{0}x{1}+0+0'.format(fullancho,fullalto-50))
            root.update()
        else:
            btnMax.config(command=lambda:expandir(1))
            oculto.geometry('{0}x{1}+0+0'.format(10,10))
            root.geometry('{0}x{1}+0+0'.format(ancho,alto))
            root.update()
    def select(w='force',event=''):
        global myFoco,lapsoRoot
        if event=='':
            return 'Null'
        elif event=='FocusIn' and w=='oculto':
            myFoco.set('otro')
            lapsoRoot=time.time()+0.01
            t='FocusIn'
        else:
            t=str(event.type)
        if w=='root' and "FocusIn" in t :
            myFoco.set('root')
        if w=='root' and "FocusOut" in t :
            myFoco.set('otro')
            lapsoRoot=time.time()
        if w=='oculto' and "FocusIn" in t:
            root.focus_force()
            myFoco.set('oculto')
            lapsoOculto=time.time()
        if w=='oculto' and "FocusOut" in t:
            myFoco.set('otro')
        if (time.time()-lapsoRoot)<0.50 and myFoco.get()=='oculto':
            root.withdraw()
            oculto.iconify()
            print('Min')
        elif (time.time()-lapsoRoot)>0.50 and myFoco.get()=='otro':
            root.deiconify()
            oculto.geometry('+{0}+{1}'.format(root.geometry().split('+')[1],root.geometry().split('+')[2]))
            root.focus_force()

            print('Max')
        print(myFoco.get()) 
    def radar(event):
        #print(str(event.state))
        if '8' in str(event.state):
            x=event.x_root-int(root.geometry().split('+')[1])
            y=event.y_root-int(root.geometry().split('+')[2])
            n=s=e=o=0
            if (root.winfo_height()-y)<10:
                s=1
            if (root.winfo_width()-x)<10:
                e=1
            if (y)<10:
                n=1
            if (x)<10:
                o=1
            #print(x,y,n,s,e,o)
    def move_window(event):
        global myX, myY,rootX,rootY
        if event.widget==tituloCanvas and "ButtonPress" in str(event.type) :
                myX=event.x_root
                myY=event.y_root  
        if event.widget==tituloCanvas and "Motion" in str(event.type) :
            #print(event)
            x=event.x_root-int(root.geometry().split('+')[1])
            y=event.y_root-int(root.geometry().split('+')[2])
            if ((y-myY)!=0 or (x-myX)!=0):
                #root.geometry('+{0}+{1}'.format(int(event.x_root-x),int(event.y_root-y)))
                oculto.geometry('+{0}+{1}'.format(int(event.x_root-x)+int(event.x_root-myX)+10,int(event.y_root-y)+int(event.y_root-myY)+10))
                root.geometry('+{0}+{1}'.format(int(event.x_root-x)+int(event.x_root-myX),int(event.y_root-y)+int(event.y_root-myY)))
                myX=event.x_root
                myY=event.y_root
        #root.focus()            
    oculto=Tk()
    oculto.iconify()
    myFoco=StringVar(value=str('root'))
    #myFoco.trace('w',lambda name,arg,mod :print(myFoco.get()))
    oculto.bind("<Destroy>",lambda event :root.destroy())
    oculto.bind("<FocusOut>",lambda e :select('oculto',event=e) )
    oculto.bind("<FocusIn>",lambda e :select('oculto',event=e) )
    #oculto.bind("<FocusOut>",lambda event :print("FocusOut Oculto") )
    #oculto.bind("<Configure>",lambda event :print("Configure Oculto") )
    oculto.geometry(str(10)+"x"+str(10)+"+10+10")
    root=Tk()
    root.bind("<Destroy>",lambda e :oculto.destroy() if oculto else print('Listo') )
    root.bind("<FocusOut>",lambda e :select('root',event=e) )
    root.bind("<FocusIn>",lambda e :select('root',event=e) )
    root.overrideredirect(True)
    root.geometry(str(ancho)+"x"+str(alto)+"+10+10")
    titulo=Frame(root,relief='flat',bd=0)
    titulo.pack(expand=1,side='top', fill='x')
    btnSalir=Button(titulo,text='X',command=lambda:root.destroy(),width=5,bg='#2e2e2e',padx=2,pady=2,activebackground='red',bd=0,font='bold',fg='#ffffff',highlightthickness=0)
    btnMax=Button(titulo,text='+',command=lambda:expandir(1),width=5,bg='#2e2e2e',padx=2,pady=2,activebackground='blue',bd=0,font='bold',fg='#ffffff',highlightthickness=0)
    btnMin=Button(titulo,text='-',command=lambda:select('oculto',event='FocusIn'),width=5,bg='#2e2e2e',padx=2,pady=2,activebackground='white',bd=0,font='bold',fg='#ffffff',highlightthickness=0)
    btnSalir.pack(side='right')
    btnMax.pack(side='right')
    btnMin.pack(side='right')
    btnSalir.bind("<Leave>",lambda event :event.widget.config(bg='#2e2e2e'))#color cuando el mouse no esta por ensima de este Widget 
    btnSalir.bind("<Enter>",lambda event :event.widget.config(bg='#891010'))#color cuando el mouse Si esta por ensima de este Widget
    btnMax.bind("<Leave>",lambda event :event.widget.config(bg='#2e2e2e'))#color cuando el mouse no esta por ensima de este Widget 
    btnMax.bind("<Enter>",lambda event :event.widget.config(bg='#891010'))#color cuando el mouse Si esta por ensima de este Widget
    btnMin.bind("<Leave>",lambda event :event.widget.config(bg='#2e2e2e'))#color cuando el mouse no esta por ensima de este Widget 
    btnMin.bind("<Enter>",lambda event :event.widget.config(bg='#891010'))#color cuando el mouse Si esta por ensima de este Widget
    root.bind("<B1-Motion>",move_window)#move_window(even)
    root.bind("<Motion>",radar)
    root.bind("<MouseWheel>",lambda event: canvas.yview_scroll(int(-1*(event.delta/120)), "units"))
    # with Linux OS
    #root.bind("<Button-4>",MouseWheelHandler)
    #root.bind("<Button-5>",MouseWheelHandler)
    f = Frame(root,relief='flat',bd=0,highlightthickness=0)
    canvas=Canvas(f,bd=0,highlightthickness=0)
    yscrollbar = Scrollbar(f, orient='vertical',command=canvas.yview,bd=0,highlightthickness=0)
    xscrollbar = Scrollbar(f, orient='horizontal',command=canvas.xview,bd=0,highlightthickness=0)
    frame=Frame(canvas,bd=0,highlightthickness=0)
    frame.bind("<Configure>",lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
    canvas.create_window((0, 0), window=frame, anchor="nw")#esta linea equivale a: frame.pack(in_=canvas,anchor="nw")
    canvas.configure(xscrollcommand=xscrollbar.set,yscrollcommand=yscrollbar.set)
    yscrollbar.pack(side='right', fill='y')
    xscrollbar.pack(side='bottom', fill='x')
    f.pack(side='bottom', fill='x', expand=1)
    canvas.pack(side='left', fill='both', expand=1)
    raiz=Canvas(frame,bd=0,highlightthickness=0)
    raiz.pack(in_=frame,fill='both',expand=1)
    for x in range(100):
        Label(raiz, text='Prueba Label '+str('@'*(x+1)),bg='#f0f0f0').pack()    
    root.update()
    print(frame.winfo_width())
    for line in Gradient(raiz,'#0f0000','#ff0f0f'):
        print(line)
        raiz.create_line(line[0],line[1],line[2],line[3],fill=line[4])
    #tituloCanvas=Canvas(titulo,height=titulo.winfo_height(),width=titulo.winfo_width(),bg='#ff0000')
    tituloCanvas=canvasGradient(titulo,'#ff0f0f','#0f0000')
    tituloCanvas.config(bd=0,highlightthickness=0)
    tituloCanvas.pack(in_=titulo)
    tituloCanvas.bind("<Button>",move_window)
    
    fullancho=root.winfo_screenwidth()
    fullalto=root.winfo_screenheight()
    root.focus_force()
    #root.()
    print('root.winfo_visual()',root.winfo_visual())
    print('root.state()',root.state())
    print('root.iconwindow()',root.iconwindow())
    print('root.winfo_visual()',root.winfo_visual())
    print('root.state()',root.state())
    print('root.frame()',root.frame())
    print('root.focusmodel()',root.focusmodel())
    print('root.attributes()',root.attributes())
    print('root.aspect()',root.aspect())
    print('root.client()',root.client())
    print('root.winfo_manager()',root.winfo_manager())
    root.mainloop()
    oculto.mainloop()
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
def unicodeP(string='',variable='',desde=0,hasta=125):
    listaunicode={}
    mayuscula=[]
    minuscula=[]
    string=string.strip()
    if ('(' in string[0]) and (')' in string[-1]):
        string=string[1:-1]
    string=string.strip()
    for l in string:
        if (97<=ord(l) and ord(l)<=122):
            if not l in minuscula:
                minuscula += [l]
        if (65<=ord(l) and ord(l)<=90):
            if not l in mayuscula:
                mayuscula += [l]
    p=[]
    for x in range(desde,hasta,1):
        p+=[[x,str(chr(int(x)))]]
        print(p[-1])
    print(p)
def strToMath(string='',variable='x',dy=0,p=0,c=None,decimales=4,signo=None,v=0,composicion=0):
    if not v:
        print('validando',string,composicion)
        v=1
    composicion += 1
    nivel=0
    esSuma=0
    signoSuma=[0]
    esProducto=0
    signoProducto=[0]
    esDivision=0
    signoDivision=[0]
    esExponente=0
    signoExponente=[0]
    esResto=0
    signoResto=[0]
    constantes={'e':math.e,'pi':3.1416,'g':9.8182}
    operador=1
    operadores=['w','sen','cos','tg','log','ln','lambert','dy','sec','cosec','cotag','arcsen','arccos','arctg','round','floor','ceil','signo','abs']
    simbolos=['*','(',')','/','+','-','.','%']
    monomio=1
    parentesis=1
    string=string.strip()
    for x in range(0,len(string),1):
        if string[x]=='(':
            nivel += 1
        if string[x]==')':
            nivel -= 1
        if string[x] in '-+' and nivel==0:
            if x>0:
                monomio=0
        if string[x] in '-+*/%' and nivel==0:
            if x>0:
                parentesis=0
    if monomio:
        if string[0] in '+' and nivel==0:
            sig= 1.0
            string=string[1:]
        elif string[0] in '-' and nivel==0:
            sig=-1.0
            string=string[1:]
        else:
            sig= 1.0
        string=string.strip()
    else:
        sig=1.0

    if parentesis:        
        if ('(' in string[0]) and (')' in string[-1]):
            string=string[1:-1]
        string=string.strip()
            
    monomio=1
    parentesis=1
    string=string.strip()
    for x in range(0,len(string),1):
        if string[x]=='(':
            nivel += 1
        if string[x]==')':
            nivel -= 1
        if string[x] in '-+' and nivel==0:
            if x>0:
                monomio=0
        if string[x] in '-+*/%' and nivel==0:
            if x>0:
                parentesis=0
    if monomio:
        if string[0] in '+' and nivel==0:
            sig= 1.0*sig
            string=string[1:]
        elif string[0] in '-' and nivel==0:
            sig=-1.0*sig
            string=string[1:]
        string=string.strip()

    if parentesis:        
        if ('(' in string[0]) and (')' in string[-1]):
            string=string[1:-1]
        string=string.strip()
    for x in range(0,len(string),1):
        if string[x]=='(':
            nivel += 1
        if string[x]==')':
            nivel -= 1
        if string[x] in '-+' and nivel==0:
            if x>0:
                esSuma=1
                signoSuma += [x]
            if not monomio:
                operador=0
        if (string[x] == '*') and ( '*' != string[x+1]) and ( '*' != string[x-1]) and nivel==0:
            esProducto=1
            signoProducto += [x]
            operador=0
        if string[x] in '/' and nivel==0:
            esDivision=1
            signoDivision += [x]
            operador=0
        if (string[x] == '*') and ( '*' == string[x+1]) and nivel==0:
            esExponente=1
            signoExponente += [x]
            operador=0
        if (string[x] == '%') and nivel==0:
            esResto=1
            signoResto += [x]
            operador=0

    if operador:
        x=0
        coincide=[op for op in operadores if op in (string if len(op)<len(string) else '')]
        if coincide:
            print(coincide)
            comas=[0]
            for x in range(0,len(string),1):
                if string[x]=='(':
                    nivel += 1
                if string[x]==')':
                    nivel -= 1
                if string[x] in ',' and nivel==0:
                    comas += [x]
            if string[:len('w')] in 'w' and nivel==0:
                pass
            if string[:len('dy')] in 'dy' and nivel==0:
                pass
            if string[:len('log')] in 'log' and nivel==0:
                #math.log(x,base)
                print('log',string)
                parteReal=strToMath(string=string[len('log'):comas[1]],dy=dy,p=p,decimales=decimales,v=v,composicion=composicion)
                if len(comas)==1:
                    base=strToMath(string='10.0',dy=dy,p=p,decimales=decimales,v=v,composicion=composicion)
                else:
                    base=strToMath(string=string[comas[1]+1:-1],dy=dy,p=p,decimales=decimales,v=v,composicion=composicion)
                def logaritmoNatural(x,dy=dy,p=p,decimales=decimales,signo=sig,mostrarSigno=0,parteReal=parteReal,base=base):
                    if mostrarSigno:
                        s='+' if signo>0.0 else '-'
                    else:
                        s=''
                    if dy:
                        if p:
                            numerador='(('+parteReal(x,p=p,dy=1,decimales=decimales,mostrarSigno=1)+'/'+parteReal(x,p=p,dy=0,decimales=decimales,mostrarSigno=1)+')-('+parteReal(x,p=p,dy=1,decimales=decimales,mostrarSigno=1)+'/'+parteReal(x,p=p,dy=0,decimales=decimales,mostrarSigno=1)+'))'
                            return s+'('+numerador+'/'+parteReal(x,p=p,dy=0,decimales=decimales,mostrarSigno=1)+')'
                        else:
                            numerador=signo*((parteReal(x,p=p,dy=1,decimales=decimales,mostrarSigno=1)/parteReal(x,p=p,dy=0,decimales=decimales,mostrarSigno=1))-(base(x,p=p,dy=1,decimales=decimales,mostrarSigno=1)/base(x,p=p,dy=0,decimales=decimales,mostrarSigno=1)))
                            return numerador/((math.log(base(x,p=p,dy=1,decimales=decimales,mostrarSigno=1)))**2)
                    else:
                        if p:
                            return s+'ln('+parteReal(x,p=p,decimales=decimales,mostrarSigno=1)+','+base(x,p=p,decimales=decimales,mostrarSigno=1)+')'
                        else:
                            return signo*math.log(parteReal(x),base(x))
                return logaritmoNatural
            if string[:len('ln')] in 'ln' and nivel==0:
                #math.log(x,base)
                print('ln',string)
                parteReal=strToMath(string=string[len('ln'):],dy=dy,p=p,decimales=decimales,v=v,composicion=composicion)
                def logaritmoNatural(x,dy=dy,p=p,decimales=decimales,signo=sig,mostrarSigno=0,parteReal=parteReal):
                    if mostrarSigno:
                        s='+' if signo>0.0 else '-'
                    else:
                        s=''
                    if dy:
                        if p:
                            return s+'('+parteReal(x,p=p,dy=1,decimales=decimales,mostrarSigno=1)+'/'+parteReal(x,p=p,dy=0,decimales=decimales,mostrarSigno=1)+')'
                        else:
                            return signo*(parteReal(x,p=p,dy=1,decimales=decimales,mostrarSigno=1)/parteReal(x,p=p,dy=0,decimales=decimales,mostrarSigno=1))
                    else:
                        if p:
                            return s+'ln('+parteReal(x,p=p,decimales=decimales,mostrarSigno=1)+')'
                        else:
                            return signo*math.log(parteReal(x))
                return logaritmoNatural
            if string[:len('abs')] in 'abs' and nivel==0:
                #math.fabs(-66.43)
                print('abs',string)
                valor=strToMath(string=string[len(''):],dy=dy,p=p,decimales=decimales,v=v,composicion=composicion)
                def valorAbsoluto(x,dy=dy,p=p,decimales=decimales,signo=sig,mostrarSigno=0,u=valor):
                    if mostrarSigno:
                        s='+' if signo>0.0 else '-'
                    else:
                        s=''
                    if dy:
                        if p:
                            return s+'(('+valor(x,p=p,dy=0,decimales=decimales,mostrarSigno=1)+'/abs('+valor(x,p=p,dy=0,decimales=decimales,mostrarSigno=1)+'))*('+valor(x,p=p,dy=1,decimales=decimales,mostrarSigno=1)+'))'
                        else:
                            return signo*((valor(x,p=p,dy=0,decimales=decimales)/math.fabs(valor(x,p=p,dy=0,decimales=decimales)))*valor(x,p=p,dy=1,decimales=decimales)) 
                    else:
                        if p:
                            return s+'abs('+valor(x,p=p,decimales=decimales,mostrarSigno=1)+')'
                        else:
                            return signo*math.fabs(valor(x))
                return valorAbsoluto
            if string[:len('tg')] in 'tg' and nivel==0:
                #math.tan()
                print('tg',string)
                radian=strToMath(string=string[len('tg'):],dy=dy,p=p,decimales=decimales,v=v,composicion=composicion)
                def tangente(x,dy=dy,p=p,decimales=decimales,signo=sig,mostrarSigno=0,radian=radian):
                    if mostrarSigno:
                        s='+' if signo>0.0 else '-'
                    else:
                        s=''
                    if dy:
                        if p:
                            return s+'((1+tg('+radian(x,dy=0,p=p,decimales=decimales,mostrarSigno=1)+')**2)*('+radian(x,dy=dy,p=p,decimales=decimales,mostrarSigno=1)+'))'
                        else:
                            return signo*(1+math.tan(radian(x))**2)*radian(x,dy=dy)
                    else:
                        if p:
                            return s+'tg('+radian(x,dy=dy,p=p,decimales=decimales,mostrarSigno=1)+')'
                        else:
                            return signo*math.tan(radian(x))
                return tangente
            if string[:len('sen')] in 'sen' and nivel==0:
                #math.sin()
                print('sen',string)
                radian=strToMath(string=string[len('sen'):],dy=dy,p=p,decimales=decimales,v=v,composicion=composicion)
                def seno(x,dy=dy,p=p,decimales=decimales,signo=sig,mostrarSigno=0,radian=radian):
                    if mostrarSigno:
                        s='+' if signo>0.0 else '-'
                    else:
                        s=''
                    if dy:
                        if p:
                            return s+'(cos('+radian(x,dy=0,p=p,decimales=decimales,mostrarSigno=1)+')*('+radian(x,dy=dy,p=p,decimales=decimales,mostrarSigno=1)+'))'
                        else:
                            return signo*math.cos(radian(x))*radian(x,dy=dy)
                    else:
                        if p:
                            return s+'sen('+radian(x,dy=dy,p=p,decimales=decimales,mostrarSigno=1)+')'
                        else:
                            return signo*math.sin(radian(x))
                return seno
            if string[:len('cos')] in 'cos' and nivel==0:
                #math.cos()
                print('cos',string)
                radian=strToMath(string=string[len('cos'):],dy=dy,p=p,decimales=decimales,v=v,composicion=composicion)
                def coseno(x,dy=dy,p=p,decimales=decimales,signo=sig,mostrarSigno=0,radian=radian):
                    if mostrarSigno:
                        s='+' if signo>0.0 else '-'
                    else:
                        s=''
                    if dy:
                        if p:
                            s=('-' if signo>0.0 else '+') if mostrarSigno else ''
                            return +s+'(sen('+radian(x,dy=0,p=p,decimales=decimales,mostrarSigno=1)+')*('+radian(x,dy=dy,p=p,decimales=decimales,mostrarSigno=1)+'))'
                        else:
                            return -1*signo*math.sin(radian(x))*radian(x,dy=dy,p=p,decimales=decimales,mostrarSigno=1)
                    else:
                        if p:
                            return s+'cos('+radian(x,dy=dy,p=p,decimales=decimales,mostrarSigno=1)+')'
                        else:
                            return signo*math.cos(radian(x))
                return coseno
            if string[:len('arcsen')] in 'arcsen' and nivel==0:
                #math.asin()
                pass
            if string[:len('arccos')] in 'arccos' and nivel==0:
                #math.acos()
                pass
            if string[:len('arctg')] in 'arctg' and nivel==0:
                #math.atan()
                pass
            if string[:len('signo')] in 'signo' and nivel==0:
                pass
            if string[:len('entero')] in 'entero' and nivel==0:
                pass
            if string[:len('decimal')] in 'decimal' and nivel==0:
                pass
            if string[:len('round')] in 'round' and nivel==0:
                print('round',string)
                redondeo=strToMath(string=string[len('round'):],dy=dy,p=p,decimales=decimales,v=v,composicion=composicion)
                def redondear(x,dy=dy,p=p,decimales=decimales,signo=sig,mostrarSigno=0,redondeo=redondeo):
                    if mostrarSigno:
                        s='+' if signo>=0.0 else '-'
                    else:
                        s=''
                    if dy:
                        if p:
                            return '0.0'
                        else:
                            return 0.0
                    else:
                        if p:
                            return s+'round('+defecto(x,p=p,decimales=decimales,mostrarSigno=1)+')'
                        else:
                            return signo*math.round(defecto(x))
                return redondear
            if string[:len('floor')] in 'floor' and nivel==0:
                print('floor',string)
                defecto=strToMath(string=string[len('floor'):],dy=dy,p=p,decimales=decimales,v=v,composicion=composicion)
                def redondearHaciaAbajo(x,dy=dy,p=p,decimales=decimales,signo=sig,mostrarSigno=0,defecto=defecto):
                    if mostrarSigno:
                        s='+' if signo>0.0 else '-'
                    else:
                        s=''
                    if dy:
                        if p:
                            return '0.0'
                        else:
                            return 0.0
                    else:
                        if p:
                            return s+'floor('+defecto(x,p=p,decimales=decimales,mostrarSigno=1)+')'
                        else:
                            return signo*math.floor(defecto(x))
                return redondearHaciaAbajo
            if string[:len('ceil')] in 'ceil' and nivel==0:
                print('ceil',string)
                exceso=strToMath(string=string[len('ceil'):],dy=dy,p=p,decimales=decimales,v=v,composicion=composicion)
                def redondearHaciaArriba(x,dy=dy,p=p,decimales=decimales,signo=sig,mostrarSigno=0,exceso=exceso):
                    if mostrarSigno:
                        s='+' if signo>0.0 else '-'
                    else:
                        s=''
                    if dy:
                        if p:
                            return '0.0'
                        else:
                            return 0.0
                    else:
                        if p:
                            return s+'ceil('+exceso(x,p=p,decimales=decimales,mostrarSigno=1)+')'
                        else:
                            return signo*math.ceil(exceso(x))
                return redondearHaciaArriba
            else:
                esConstante=1
            """
            if string[:len('')] in '' and nivel==0:
                print('',string)
                =strToMath(string=string[len(''):],dy=dy,p=p,decimales=decimales,v=v)
                def op(x,dy=dy,p=p,decimales=decimales,signo=sig,mostrarSigno=0):
                    #f(x,dy=dy,p=p,decimales=decimales,mostrarSigno=0)
                    if mostrarSigno:
                        s='+' if signo>0.0 else '-'
                    else:
                        s=''
                    if dy:
                        if p:
                            return s
                        else:
                            ret = 
                            return signo*ret
                    else:
                        if p:
                            return s
                        else:
                            return signo*
                return op
            """
        else:
            c=None
            if string in constantes:
                c=constantes[string]
            elif sum([1 for l in string if ((48<=ord(l) and ord(l)<=57) or (ord(l)==46))])==len(string):
                c=float(string)
            if c:
                print('constante',c)
                def constante(x,dy=dy,p=p,c=c,decimales=decimales,signo=sig,mostrarSigno=0):
                    if mostrarSigno:
                        s='+' if signo>0.0 else '-'
                    else:
                        s=''
                    if dy:
                        if p:
                            return '0.'+'0'*decimales
                        else:
                            return 0
                    else:
                        if p:
                            return s+str(c)[:decimales]
                        else:
                            return c*signo
                return constante
            if string==variable:
                print('variable',string,sig)
                def variable(x,dy=dy,p=p,decimales=decimales,signo=sig,mostrarSigno=0):
                    if mostrarSigno:
                        s='+' if signo>=0.0 else '-'
                    else:
                        s=''
                    if dy:
                        if p:
                            return '1.0'
                        else:
                            return 1.0
                    else:
                        if p:
                            return s+str(x)[:decimales]
                        else:
                            return x*signo
                return variable
        
    else:
        #parentecis,exponente/radicales,multiplicacion/division,suma/resta
        if esSuma:
            print('suma',string,signoSuma)
            if len(signoSuma)==1:
                sumandos=[strToMath(string=string[1:],dy=dy,p=p,decimales=decimales,v=v,composicion=composicion)]
            else:
                sumandos=[]
                for sumando in range(0,len(signoSuma)-1,1):
                    sumandos+=[strToMath(string=string[signoSuma[sumando]:signoSuma[sumando+1]],dy=dy,p=p,decimales=decimales,v=v,composicion=composicion)]
                sumandos+=[strToMath(string=string[signoSuma[-1]:],dy=dy,p=p,decimales=decimales,v=v,composicion=composicion)]
            def suma(x,dy=dy,p=p,decimales=decimales,sumandos=sumandos,signo=sig,mostrarSigno=0):
                if mostrarSigno:
                    s='+' if signo>0.0 else '-'
                else:
                    s=''
                if dy:
                    if p:
                        ret = s+'('
                        for sumando in sumandos:
                            ret += ' '+sumando(x,p=p,dy=dy,decimales=decimales,mostrarSigno=1)
                        return ret+')'
                    else:
                        return signo*sum([sumando(x,dy=dy) for sumando in sumandos])
                else:
                    if p:
                        ret = s+'('
                        for sumando in sumandos:
                            ret += ' '+sumando(x,p=p,decimales=decimales,mostrarSigno=1)
                        return ret+')'
                    else:
                        ret = 0.0
                        for sumando in sumandos:
                            ret += sumando(x)
                        return signo*ret
            return suma
        elif esDivision:
            print('division',string,signoDivision)
            signoDivision+=[]
            numerador=strToMath(string=string[0:signoDivision[1]],dy=dy,p=p,decimales=decimales,v=v,composicion=composicion)
            denominador=strToMath(string=string[signoDivision[1]+1:],dy=dy,p=p,decimales=decimales,v=v,composicion=composicion)
            def division(x,dy=dy,p=p,decimales=decimales,numerador=numerador,denominador=denominador,signo=sig,mostrarSigno=0):
                if mostrarSigno:
                    s='+' if signo>0.0 else '-'
                else:
                    s=''
                if dy:
                    if p:
                        return s+'(('+numerador(x,p=p,dy=1,decimales=decimales)+')*('+denominador(x,p=p,dy=0,decimales=decimales)+')-('+numerador(x,p=p,dy=0,decimales=decimales)+')*('+denominador(x,p=p,dy=1,decimales=decimales)+'))/(('+denominador(x,p=p,dy=0,decimales=decimales)+')**2)'
                    else:
                        return signo*((numerador(x,p=p,dy=1,decimales=decimales)*denominador(x,p=p,dy=0,decimales=decimales))-(numerador(x,p=p,dy=0,decimales=decimales)*denominador(x,p=p,dy=1,decimales=decimales)))/(denominador(x,p=p,dy=0,decimales=decimales)**2)
                else:
                    if p:
                        return s+'('+numerador(x,p=p,dy=0,decimales=decimales)+'/'+denominador(x,p=p,dy=0,decimales=decimales)+')'
                    else:
                        return signo*numerador(x,dy=0,decimales=decimales)/denominador(x,dy=0,decimales=decimales)
            return division
        elif esResto:
            print('resto',string,signoResto)
            signoResto+=[]
            numerador=strToMath(string=string[0:signoResto[1]],dy=dy,p=p,decimales=decimales,v=v,composicion=composicion)
            denominador=strToMath(string=string[signoResto[1]+1:],dy=dy,p=p,decimales=decimales,v=v,composicion=composicion)
            def restoPorDefecto(x,dy=dy,p=p,decimales=decimales,numerador=numerador,denominador=denominador,signo=sig,mostrarSigno=0):
                if mostrarSigno:
                    s='+' if signo>0.0 else '-'
                else:
                    s=''
                if dy:
                    if p:
                        return ''
                    else:
                        return None
                else:
                    if p:
                        return s+'('+numerador(x,p=p,dy=0,decimales=decimales)+'%'+denominador(x,p=p,dy=0,decimales=decimales)+')'
                    else:
                        return signo*numerador(x,dy=0,decimales=decimales)%denominador(x,dy=0,decimales=decimales)
            return restoPorDefecto
        elif esProducto:
            print('producto',string,signoProducto)
            factores=[]
            for factor in range(0,len(signoProducto)-1,1):
                factores+=[strToMath(string=string[signoProducto[factor]+(1 if 0<factor else 0 ):signoProducto[factor+1]],dy=dy,p=p,decimales=decimales,v=v,composicion=composicion)]
            factores+=[strToMath(string=string[signoProducto[-1]+1:],dy=dy,p=p,decimales=decimales,v=v,composicion=composicion)]
            def producto(x,dy=dy,p=p,decimales=decimales,signo=sig,factores=factores,mostrarSigno=0):
                if mostrarSigno:
                    s='+' if signo>0.0 else '-'
                else:
                    s=''
                if dy:
                    if p:
                        ret=s+'('
                        factor='('
                        for derivar in range(0,len(factores),1):
                            factor=factores[derivar](x,dy=1,p=p,decimales=decimales)
                            for escalar in range(0,len(factores),1):
                                if not (derivar == escalar):
                                    factor += '*'+factores[escalar](x,dy=0,p=p,decimales=decimales)
                            ret += factor+')+'
                        return ret[:-1]+')'
                    else:
                        ret=0.0
                        factor=1.0
                        for derivar in range(0,len(factores),1):
                            factor=factores[derivar](x,dy=1,p=p,decimales=decimales)
                            for escalar in range(0,len(factores),1):
                                if not (derivar == escalar):
                                    factor*=factores[escalar](x,dy=0,p=p,decimales=decimales)
                            ret += factor
                        return signo*ret
                else:
                    if p:
                        ret = s+'('+factores[0](x,dy=0,p=p,decimales=decimales)
                        for factor in factores[1:]:
                            ret += '*'+factor(x,dy=0,p=p,decimales=decimales)
                        return ret+')'
                    else:
                        ret = 1.0
                        for factor in factores:
                            ret *= factor(x,dy=0,p=0)
                        return signo*ret
            return producto
        elif esExponente:
            print('exponente',string,signoExponente)
            signoExponente+=[]
            base=strToMath(string=string[0:signoExponente[1]],dy=dy,p=p,decimales=decimales,v=v,composicion=composicion)
            exponente=strToMath(string=string[signoExponente[1]+2:],dy=dy,p=p,decimales=decimales,v=v,composicion=composicion)
            def potencia(x,dy=dy,p=p,decimales=decimales,signo=sig,base=base,exponente=exponente,mostrarSigno=0):
                if mostrarSigno:
                    s='+' if signo>0.0 else '-'
                else:
                    s=''
                if dy:
                    if p:
                        return s+'((('+exponente(x,dy=0,p=p,decimales=decimales)+'*('+base(x,dy=0,p=p,decimales=decimales)+'**('+exponente(x,dy=0,p=p,decimales=decimales)+'-1))*'+base(x,dy=1,p=p,decimales=decimales)+') + ('+exponente(x,dy=1,p=p,decimales=decimales)+'*('+base(x,dy=0,p=p,decimales=decimales)+'**'+exponente(x,dy=0,p=p,decimales=decimales)+')*ln('+base(x,dy=0,p=p,decimales=decimales)+'))))'
                    else:
                        ret = exponente(x,dy=0,p=p,decimales=decimales)*(base(x,dy=0,p=p,decimales=decimales)**(exponente(x,dy=0,p=p,decimales=decimales)-1))*base(x,dy=1,p=p,decimales=decimales) + exponente(x,dy=1,p=p,decimales=decimales)*(base(x,dy=0,p=p,decimales=decimales)**exponente(x,dy=0,p=p,decimales=decimales))*math.log(base(x,dy=0,p=p,decimales=decimales))
                        return signo*ret
                else:
                    if p:
                        return s+base(x,p=p,decimales=decimales)+'**('+exponente(x,p=p,decimales=decimales,mostrarSigno=1)+')'
                    else:
                        return signo*base(x)**exponente(x)
            return potencia
          
#pruebaTreeview()
#ventanaPersonalizada()
#caja()
def g(x):
    return (x*math.e**x)/(math.e**x+math.e**(-x))

f=calculadora()
f.setEcuacion('senhP',string='sen(360/x)+x',variable='x',constantes={'alto':80.0})
f.setEcuacion('coshP',string='senhP(x+bajo)/cos(x)',variable='x',constantes={'bajo':10.0})

print(f.ec['senhP'](3,p=1,dy=1),'=',f.ec['senhP'](3,p=0,dy=1))
print(f.ec['coshP'](3,p=1,dy=1),'=',f.ec['coshP'](3,p=0,dy=1))
#print('(x*e**x)/(e**x+e**(-x))','=',g(3))
