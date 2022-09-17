from tkinter import Tk,Label,font
import math,os
from extras import *
from pruebas import *
from matematica import calc
from GUI import FrameScroll

class puntos(object):
    """docstring for curvas"""
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
    def getArco(p=(1.0,1.0),r=1.0,desde=0,hasta=90,pasos=1):
        if r>0:
            pasos=int( abs(pasos) if desde<hasta else -1*abs(pasos) )
            #calculamos los puntos de la curva
            grados=range(desde,hasta,pasos)
            desde=math.radians(float(desde))
            hasta=math.radians(float(hasta))
            #calculamos el centro de la curva
            Cx=p[0]-r*( math.cos(desde)+math.cos(hasta) )
            # el sentido del ejeY es inverso al del eje cartesiano
            Cy=p[1]+r*( math.sin(desde)+math.sin(hasta) )
            #primer punto
            p =( Cx+math.cos(desde)*r, Cy-math.sin(desde)*r )
            for g in grados:
                rad=math.radians(float(g))
                p+=( Cx+math.cos(rad)*r, Cy-math.sin(rad)*r )
            p+=( Cx+math.cos(hasta)*r, Cy-math.sin(hasta)*r )
        return p
    def getCuadro(x,y,ancho,alto,radio=10):
        if ( (radio*2<=alto) and (radio*2<=ancho) ):
            r=float(radio)
        else:
            if alto<ancho : r=float(alto//2)
            else: r=float(ancho//2)
        if r.__class__==list:
            r1,r2,r3,r4=r[0],r[1],r[2],r[3]
        else:
            r1=r2=r3=r4=r
        #superior  izquierdo
        p= puntos.getArco(p=(x,y),desde=180,hasta=90,r=r1)
        #superior derecho
        p+=puntos.getArco(p=(x+ancho,y),desde=90,hasta=0,r=r2)
        #inferior derecho
        p+=puntos.getArco(p=(x+ancho,y+alto),desde=0,hasta=-90,r=r3)
        #inferior izquierdo
        p+=puntos.getArco(p=(x, y+alto),desde=-90,hasta=-180,r=r4)
        return p
            
def aspas(x=10,y=10,dividir=120,baseRadio=100.0,altura=100.0,revolucion=360,rotorRadio=5.0,fondo=60):
    '''calculamos los puntos en un plano de una aspa de arquimedes'''
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
    yOut=[calc.dist([xR[0],yR[0],zR[0]],[xA[0],yA[0],zA[0]])]
    xIn =[0]
    yIn =[0]
    for n in range(1,fin+1,1):
        A=[xA[n-1],yA[n-1],zA[n-1]] #punto que ya esta en el plano
        B=[xR[n-1],yR[n-1],zR[n-1]] #punto origen que ya esta en plano
        C=[xA[n],yA[n],zA[n]]       #punto que se agregara al plano
        xO=calc.dist(calc.alt(C,A,B),C)
        yO=calc.dist(calc.alt(C,A,B),B)
        #print(math.degrees(angRad([0,1,0],resta([xIn[-1],yIn[-1],0],[xOut[-1],yOut[-1],0]))))
        rot= -1*math.fabs(calc.angRad([0,1,0],calc.resta([xIn[-1],yIn[-1],0],[xOut[-1],yOut[-1],0])))
        [xRot, yRot]=calc.rotar(rot,[xO,yO,0])
        [xTras, yTras,_]=calc.trasladar([xIn[-1],yIn[-1],0],[xRot,yRot,0])
        yOut.append(yTras)
        xOut.append(xTras)
        A=[xA[n],yA[n],zA[n]]
        B=[xR[n-1],yR[n-1],zR[n-1]]
        C=[xR[n],yR[n],zR[n]]
        xO= calc.dist(calc.alt(C,A,B),C)
        yO= calc.dist(calc.alt(C,A,B),B) if calc.dist(calc.alt(C,A,B),A)<calc.dist(A,B) else calc.dist(calc.alt(C,A,B),B)*(-1)
        rot= -1*math.fabs(calc.angRad([0,1,0],calc.resta([xIn[-1],yIn[-1],0],[xOut[-1],yOut[-1],0])))
        [xRot, yRot]=calc.rotar(rot,[xO,yO,0])
        [xTras, yTras,_]=calc.trasladar([xIn[-1],yIn[-1],0],[xRot,yRot,0])
        yIn.append(yTras)
        xIn.append(xTras)
    angulo = [(n, xOut[n]+(x), yOut[n]+(y), xIn[n]+(x), yIn[n]+(y), zR[n]+fondo) for n in range(0,len(xOut),dividir)]+[(fin, xOut[fin]+(x), yOut[fin]+(y), xIn[fin]+(x), yIn[fin]+(y), zR[fin]+fondo)]
    poligono = [(xOut[n]+(x),yOut[n]+(y)) for n in range(0,len(xOut),1)]+[(xIn[n]+(x),yIn[n]+(y)) for n in range(len(xIn)-1,-1,-1)]+[(xOut[0]+x,yOut[0]+y)]
    return poligono, angulo, fin
def aspaConica(debug=1):
    '''Crear plano de una figura Tridimencional'''
    from reportlab.lib.colors import tan, black, green
    from reportlab.lib.units import mm
    from reportlab.pdfgen import canvas
    from reportlab.lib.pagesizes import letter
    c = canvas.Canvas("plano.pdf", pagesize=letter)
    c.setLineWidth(.3)
    c.setFont('Helvetica', 8)
    kw={
        'baseRadio':100.0,
        'fondo':60.0,
        'dividir':120,
        'altura':100.0,
        'revolucion':360,
        'rotorRadio':5.0,
        }
    puntos,angulo,kw['giroReal'] = aspas(
        x=10,
        y=int((780-(calc.hypotenusa(kw['baseRadio'],kw['fondo'])*mm))/mm),
        **kw
        )
    #canvas.line(480,747,580,747)

    c.drawString(10,70,'Plano: ')
    c.drawString(10,60,f"Giro Real: { kw['giroReal'] } grados")
    c.drawString(10,50,f"Radio Base: {kw['baseRadio']}mm")
    c.drawString(10,40,f"Radio Rotor: {kw['rotorRadio']}mm")
    c.drawString(10,30,f"Fondo: {kw['fondo']}mm")
    c.drawString(10,20,f"Altura: {kw['altura']}mm")
    c.drawString(10,10,f"Giro Especulado: {kw['revolucion']}mm")
    c.setLineWidth(3)
    c.drawString(10.0*mm,780,'100mm')
    c.line(10.0*mm, 780, 110.0*mm, 780)
    c.line(5.0*mm, 250*mm, 5.0*mm, 150*mm)
    c.setLineWidth(.3)
    for g in range(0,len(puntos)-1,1):
        c.line(puntos[g][0]*mm, puntos[g][1]*mm, puntos[g+1][0]*mm, puntos[g+1][1]*mm)
    c.setLineWidth(3)
    for g in range(0,len(angulo),1):
        c.line(angulo[g][1]*mm, angulo[g][2]*mm, angulo[g][3]*mm, angulo[g][4]*mm)
        c.drawString(angulo[g][1]*mm+((angulo[g][1]*mm-angulo[g][3]*mm)/100), angulo[g][2]*mm+((angulo[g][2]*mm-angulo[g][4]*mm)/100),'_'+str(angulo[g][0])+'grados, altura: '+str( str(angulo[g][5]) if (6 > len(str(angulo[g][5]))) else str(angulo[g][5])[:5] )+'mm')
    #canvas.drawString(puntos[int((len(puntos)-2)/2)][0]*mm, puntos[int((len(puntos)-2)/2)][1]*mm,'_'+str(int((len(puntos)-1)/2))+'grados')
    c.save()
    print("Ok")
def totalScroll_treview():
    """practica de widget ttk.Treeview()"""
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
    es,inter=comprimir.esIguales(None,inputsDefault,normal=True)
    print(es,inter)
    frame=FrameScroll(root,geometry=(1500,800,10,10))
    tree = ttk.Treeview(
        frame,columns=tuple(f'#{c+1}' for c in inter)
        )
    tree.pack()
    tree.heading("#0", text="ID")
    count=0
    for c in inter:
        print(c,inter[c],end=';')
        tree.heading(f'#{c+1}', text=inter[c])
        count += 1
    count=0
    for c in inputsDefault:
        #inputsDefault[c]['id']=count
        if inputsDefault[c]:
            tree.insert(
                "", END, text=count,
                values=tuple(inputsDefault[c][inter[h]] for h in inter)
                )
        count += 1
    root.update()
    root.mainloop()
def mouseScroll():
    '''Hcaer scroll con el mouse desde cualquier parte de la ventana'''
    
    # explore the mouse wheel with the Tkinter GUI toolkit
    # Windows and Linux generate different events
    # tested with Python25

    #from tkinter import *
    global count
    def mouse_wheel(event):
        global count
        # respond to Linux or Windows wheel event
        if event.num == 5 or event.delta == -120:
            count -= 1
        if event.num == 4 or event.delta == 120:
            count += 1
        print(event.num,event.delta)
        label['text'] = count


    count = 0
    root = Tk()
    root.title('turn mouse wheel')
    root['bg'] = 'darkgreen'
    # with Windows OS
    root.bind("<MouseWheel>", mouse_wheel)
    # with Linux OS
    root.bind("<Button-4>", mouse_wheel)
    root.bind("<Button-5>", mouse_wheel)
    label = Label(root, font=('courier', 18, 'bold'), width=10)
    label.pack(padx=40, pady=40)
    '''
    #frame=Scrollbarframe(root,500,500,0,0)
    '''
    root.mainloop()
class RGB:
    """docstring for colorUtils"""
    escala={
        '0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,
        'a':10,'b':11,'c':12,'d':13,'e':14,'f':15
        }
    verReturn=False
    def hex_int(*color):
        rgb=[]
        for c in [*color]:
            rgb+=[[]]
            for h in range(1,len(c),2):
                rgb[-1]+=[float((RGB.escala[c[h]]*16)+(RGB.escala[c[h-len(c)+1]]))]
        if RGB.verReturn:print(rgb)
        return tuple(rgb)
    def int_hex(*arg):
        
        r=''
        for h in [*arg]:
            r += ("" if h>15 else "0")+str(hex(h))[2:]
        if len(r)==6: r='#'+r
        if RGB.verReturn:print([*arg],'->',r)
        return r
def Gradient(color1,color2,h=500,w=500,ang=0.0,x=0.0,y=0.0):
    [r1,g1,b1],[r2,g2,b2]=RGB.hex_int(color1,color2)
    lines=[]
    if ang!=0.0:
        ang=math.radians(ang)
        p = [
            [x-w/2.0,y-h/2.0],[x+w/2.0,y-h/2.0],
            [x-w/2.0,y+h/2.0],[x+w/2.0,y+h/2.0]
            ]
        p = [ calc.rotar(ang,v,O=[x,y]) for v in p ]
        p.sort(reverse=False,key=lambda x: x[0])
        A,C=p[0],p[3]
        B,D=p[1],p[2] if  p[1]>p[2] else p[2],p[1]
        ACx=int(A[0]-C[0])
        r=(r2-r1)/(ACx)
        g=(g2-g1)/(ACx)
        b=(b2-b1)/(ACx)
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
            color=[RGB.int_hex(RR,GG,BB)]
            lines +=[calc.rotar(-ang,[i,j0],O=[x,y])+calc.rotar(-ang,[i,j1],O=[x,y])+color]

    else:
        for i in range(w):
            RR=int(r1+(r*i))
            GG=int(g1+(g*i))
            BB=int(b1+(b*i))
            color=RGB.int_hex(RR,GG,BB)
            lines +=[[i,0,i,h,color]]
            #,tags=("gradient",)
    return lines
class widgetSizeCache(FrameScroll):
    """
    Interfas grafica para hacer un cache de las medidas width y height de widgets,
    crea un script Sizes.py con las medidas en pixeles.

        Obtener las futuras medidas en pixeles del widget:
            cache[claseWidget][fontFamily][size][fontSize][widthWidget] -> int

        Crear o instanciar el widget con los atributos:
            instansiaWidget=claseWidget(
                padrewidget,
                font=(fontFamily,fontSize),
                width=widthWidget
                )
        Para usar la variable con los datos:
            claseWidget: ['radiobtn'/'checkbtn'/'btn'/'lb'/'entry']
                'radiobtn':Radiobutton,
                'checkbtn':Checkbutton,
                'btn':Button,
                'lb':Label,
                'entry':Entry
            fontFamily: ['Agency FB'/'Albertus'/.../'Verdana'/'Webdings'/'Z003']
                Para ver la lista completa:
                    from tkinter import font
                    print(list(font.families()))
            size: ['width'/'height']
                el lado que desea obtener
            fontSize:  list(range(4,54,2))+[7/9/11/13/15/17]
                medida del font, debe pertenecer a la lista resultante de arriba
                Para ver la lista resultante:
                    listaResultante=[ list(range(4,54,2))+[7,9,11,13,15,17] ]
                    print(listaResultante)
            widthWidget: [ 1/2/3/.../33/34 ]
                esta opcion sera definida por la clase widgetUtils o por el usuario
                este atributo se pasa al widget al momento de ser instansiado
                
    """
    def __init__(self, *arg,**kwargs):
        self.cache = {}
        self.idConf={}
        self.valores = {}
        FrameScroll.__init__(
            self,Tk(),
            titulo="Cache de Medidas de los Widget en pixeles ",
            icon='',geometry=(400,500,100,10)
            )
        self.font_family = list(font.families())
        self.font_family.sort()
        self.font_sizes = list(range(4,54,2))+[7,9,11,13,15,17]
        self.font_sizes.sort()
        y=10
        #['\t','\r','\n']+
        [x,y]=self.setContenedor(
            'conf',
            [
                ('widget',list(self.class_tk)[0],list(self.class_tk)),
                ('fontSize',10,self.font_sizes),
                ('fontType',self.font_family[0],self.font_family),
                ('repeticiones',40,range(10,50,5)),
                ('ancho',0,range(0,500,10))
                ],
            setElemento=self.crearEntry, style='bobEsponja',side="right" ,
            x=10, y=y
            )
        #Separator(self.raiz, orient=HORIZONTAL)
        [x,y]=self.setContenedor(
            'botones',
            [   
                ('textoDePrueba',self.textoDePrueba),
                ('mostrarFonts',self.tkinterFontFont),
                ('generarCache',self.generarCache),
                ('guardarCache',self.guardarCache),
                ('comprimirCache',self.comprimir_dimensiones )
                ],
            setElemento=self.crearButton, style='bobEsponjaGrande',
            x=10, y=y,display='inline'
            )
        #self.showVars()
        self.updateScroll( h=y )
        self.loop()
    def idValue(self,n):
        #retorna el valor del widget
        return self.tkValue[ self.idConf[n] ]
    def guardarCache(self):
        tiempos.setTotal(2)
        print(tiempos.medirTiempo())
        V.saveVars(
            [[ 'cache',self.cache ]],
            file='Sizes.py',m='a'
            )
        print(tiempos.medirTiempo())
    def cambiar(self,name,n):
        if self.tkValue[name] in self.valores[name]:
            i=self.valores[name].index(self.tkValue[name])
        else:
            i=self.valores[name][0]
        if len(self.valores[name]) > (i+n) >= 0: 
            self.setVarID(name,self.valores[name][i+n])
        elif len(self.valores[name]) == (i+n): 
            self.setVarID(name,self.valores[name][0])
        elif (i+n) < 0: 
            self.setVarID(name,self.valores[name][-1])
        
    def crearEntry(self,e,**kw):
        #self.setWidget(w_tk,name,text='',width=None,place=(),**kwarg)
        self.valores[self.nextIdVar]=list(e[2])
        self.setWidget( 'lb',e[0],text=V.toText(e[0],'camel'),**kw )
        if e[2]:
            self.setWidget(
                'btn','bajar_'+e[0],text='Bajar',display='inline',
                command=lambda :self.cambiar(self.nextIdVar,-1),**kw
                )
            self.setWidget(
                'btn','subir_'+e[0],text='Subir',display='inline',
                command=lambda :self.cambiar(self.nextIdVar,+1),**kw
                )
        self.idConf[e[0]]=self.setWidget('entry',e[0],typeVar=e[1],**kw )
    def crearButton(self,e,**kw):
        #self.setWidget(w_tk,name,text='',width=None,place=(),**kwarg)
        self.setWidget('btn',e[0],text=V.toText(e[0],'camel'),command=e[1],**kw)
    def tkinterFontFont(self):
        tiempos.setTotal(2)
        print(tiempos.medirTiempo())
        text = ['Vote for difficulty. Current difficulty : [ Basic ]']
        #for f in font.families(): print( f,end=',' )
        self.liberarCanvas()
        ySuma = 200
        xMax = 0
        for name in font.families():
            ft=name
            name=font.Font(family=name,size=self.idValue('fontSize'))
            name.actual()
            for t in text:
                #print(t,ft,k)
                xSuma=50
                self.setVarID( self.idConf['fontType'], ft )
                w=name.measure(ft)
                h=name.metrics('ascent')+name.metrics('descent')
                self.polig( xSuma,ySuma,w,h, radio=5, text=ft )
                xSuma+=w
                w=name.measure( t )
                self.polig( xSuma,ySuma,w,h, radio=5, text=t )
                xSuma+=w
                ySuma+=h
                if (xSuma > xMax): xMax=xSuma
            self.updateScroll( h=ySuma ,w=xMax)
        print(tiempos.medirTiempo())
    def textoDePrueba(self,**kw):
        self.liberarCanvas()
        text = ['Vote for difficulty. Current difficulty : [ Basic ]']
        name=font.Font(
            family=self.idValue('fontType'),
            size=self.idValue('fontSize')
            )
        print(name.actual())
        print(name.metrics())
        ySuma = 200
        xMax = 0
        for t in text:
            w = name.measure(t)
            h = name.metrics('ascent')+name.metrics('descent')
            self.polig(10,ySuma,w,h, text=t,gradiente=True,**kw)
            ySuma+=h
            if (w > xMax): xMax=w
    def generarCache(self):
        b='default'
        self.liberarCanvas()
        l = len(self.font_family)
        for widget in self.class_tk:
            if widget in ['lb']:continue
            self.setVarID( self.idConf['widget'], widget )
            self.cache[widget]={}
            ySuma=200
            xMax=0
                
            size=self.setWidget(
                widget,'getWidgetWidth',text='getWidgetWidth',
                width=1,place=(10,ySuma),size=False
                )
                
            for ft in range(l):
                if 'Sizes' == ft: continue
                self.widgets['conf']['widget']['lb']['widget'].config(
                    text=f'Widget: {widget}, {round((ft/l)*100.0,2)}%'
                    )
                self.widgets['conf']['widget']['lb']['widget'].update()
                ft=self.font_family[ft]
                self.setVarID( self.idConf['fontType'], ft )
                self.cache[widget][ft]={'width':{},'height':{}}
                for i in self.font_sizes:
                    new_list=[0]
                    h=0
                    for width in range(1,35):
                        self.widgets[b][b][widget]['getWidgetWidth'].config(
                            width=width ,font=(ft,i)
                            )
                        self.widgets[b][b][widget]['getWidgetWidth'].update()
                        if h==0:
                            h=self.widgets[b][b][widget]['getWidgetWidth'].winfo_height()
                        w=self.widgets[b][b][widget]['getWidgetWidth'].winfo_width()
                        new_list+=[w]
                        if w>xMax: xMax=w
                    self.cache[widget][ft]['width'][i]=new_list
                    self.cache[widget][ft]['height'][i]=h
            self.widgets[b][b][widget]['getWidgetWidth'].destroy()
            del self.widgets[b][b][widget]['getWidgetWidth']
    def gradient(self,x,y,w,h,ang,lineFill,color1='#0f0f0f',color2='#f0f0f0'):
        [r1,g1,b1],[r2,g2,b2]=RGB.hex_int(color1,color2)
        lines=[]
        ang=math.radians(ang)
        if ang!=0.0:
            h=h/2.0
            w=w/2.0
            p = [[x-w,y-h], [x+w,y-h], [x-w,y+h], [x+w,y+h]]
            p = [ calc.rotar(ang,v,O=[x,y]) for v in p ]
            p.sort(key=lambda x: x[0])
            A,C = p[0],p[3]
            if  p[1][1]>p[2][1]: B,D = p[1],p[2]
            else: B,D = p[2],p[1]
            print(A,B,D,C)
            ACx=int(C[0]-A[0])
            r=(r2-r1)/(ACx)
            g=(g2-g1)/(ACx)
            b=(b2-b1)/(ACx)
            print(ACx,[r,g,b])
            for i in range(int(A[0])+1,int(C[0])):
                #lados superiores del cuadro
                if A[0]<=i<=B[0]:
                    j0=calc.rectaAB(A,B,x=i)
                elif B[0]<=i<=C[0]:
                    j0=calc.rectaAB(B,C,x=i)
                #lados inferiores del cuadro
                if A[0]<=i<=D[0]:
                    j1=calc.rectaAB(A,D,x=i)
                elif D[0]<=i<=C[0]:
                    j1=calc.rectaAB(D,C,x=i)
                #aplicando los valores calculados
                print(i,j0,j1)
                color=RGB.int_hex(
                    int(r1+(r*(i-A[0]))),
                    int(g1+(g*(i-A[0]))),
                    int(b1+(b*(i-A[0])))
                    )
                lineFill(
                    calc.rotar(-ang,[i,j0],O=[x,y])+calc.rotar(-ang,[i,j1],O=[x,y]),
                    fill=color
                    )
        else:
            for i in range(w):
                lineFill(
                    [i,0,i,h],
                    fill=RGB.int_hex(
                        int(r1+(r*i)),
                        int(g1+(g*i)),
                        int(b1+(b*i))
                        )
                    )
    def polig(self,x,y,ancho,alto,radio=10,text="",gradiente=False,**kw):
        """Dibuja en el lienzo, un cuadrado y un texto"""
        if 0<=alto and 0<=ancho and gradiente==False:
            self.canvas.create_polygon(
                puntos.getCuadro(x,y,ancho,alto,radio=radio),
                fill='#ff0f0f',outline='#0101f0',**kw
                )
        elif gradiente:
            self.gradient(
                x+(ancho/2),y+(alto/2),ancho,alto,5,
                self.canvas.create_line,**kw
                )
        if text :
            self.canvas.create_text(
                x+int(ancho/2),y+int(alto/2),text=str(text),
                fill=self.styleTk['color']['default']['default']['bg'],
                font=(self.idValue('fontType'),self.idValue('fontSize'))
                )
    def comprimir_dimensiones(self):
        """comprimir_dimensiones"""
        """
            valores Iniciales:
            tamaño de los archivos
            3,2M Sizes.py
            Peso de la variable en memoria: 7496.806640625KB
            
            aplicando metodos de compresion, en listas y diccionarios
            
            valores Finales:
            tamaño de los archivos
            Guardado:sizes en "sizes.py"
            356K sizes.py
            Peso de la variable en memoria: 967.619140625KB
        """
        #from Sizes import cache
        info=comprimir(
            'sizes',self.cache,
            ignore = [ 'Sizes','meta','mono','key' ]
            )
        print('Peso de la variable en memoria:', info.getSize() )
        print('APLICANDO METODOS DE COMPRESION, EN LISTAS Y DICCIONARIOS\n',info.D)

        info.indexar_dimension(
            'widgetWidth',[[],[],['width'],[]],
            )
        info.indexar_dimension(
            'sizes',[[],[],[]],
            def_get=lambda d: list(d.values())
            )
        info.unificar(3)
        print('Peso de la variable en memoria:',info.getSize())
        info.guardar()
        os.system('ls -hs *izes.py')
def longitud_de_caracteres():
    """hallar longuitud de caracteres"""
    #print(widgetSizeCache.__doc__)
    App=widgetSizeCache()
    
if 'main' in __name__:
    main_pruebas([
        longitud_de_caracteres,aspaConica,totalScroll_treview,
        widgetSizeCache.comprimir_dimensiones,mouseScroll
        ])