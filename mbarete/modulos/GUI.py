from tkinter import *
from PIL import Image,ImageTk
import math,time,datetime
import threading

#from fontWidthHeight import fontSizes
from  pruebas import *

from extras import *
from extras import object_mbarete
from bbdd import *

from sizes import sizes
import sqlite3
query_sqLite3['encode']=1

def escalarHex(h="#ffffff",factor=1.0):
    escala={'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'a':10,'b':11,'c':12,'d':13,'e':14,'f':15}
    RR=int(float((escala[h[1:3][0]])*16+(escala[h[1:3][1]]))*factor)
    GG=int(float((escala[h[3:5][0]])*16+(escala[h[3:5][1]]))*factor)
    BB=int(float((escala[h[5:][0]])*16+(escala[h[5:][1]]))*factor)
    #print(str(hex(RR)),str(hex(GG)),str(hex(BB)))
    ret='#'+("" if RR>15 else "0")+str(hex(RR))[2:]+("" if GG>15 else "0")+str(hex(GG))[2:]+("" if BB>15 else "0")+str(hex(BB))[2:]
    #print(RR,GG,BB,ret[0:7])
    return ret[0:7]
class I_am_Tk(object_mbarete,Tk):
    """docstring for I_am_Mbarete"""
    def __init__(self, frame=0,titulo='I am ROOT',icon='',geometry=(),**kwarg):
        #self.obj_mbarete=obj_mbarete
        self.lapsoRoot=time.time()
        self.lapsoOculto=time.time()
        #aqui heredamos object_mbarete
        object_mbarete.__init__(self,**kwarg)
        #el widget oculto que se comunicara con el sistema
        self.info_events()
        self.oculto=Tk()
        if icon :
            #print(self.winfo_screenwidth())
            icon=self.pwd+icon
            self.p(icon)
            self.icon=PhotoImage(file=icon)
            self.oculto.iconphoto(False, self.icon)
        self.oculto.iconify()
        self.set_binds(self.oculto,'oculto')
        #heredamos los metodos y atributos de TK
        Tk.__init__(self) #aqui instanciamos Tk
        self.fullancho=self.winfo_screenwidth()
        self.fullalto=self.winfo_screenheight()
        if geometry:
            (self.ancho,self.alto,self.myX,self.myY)=geometry
        else:
            self.ancho=500
            self.alto=300
            self.myX=(self.fullancho-self.ancho)//2
            self.myY=(self.fullalto-self.alto)//2
        
        self.rootX=self.myX
        self.rootY=self.myY
        self.myFoco='root'
        self.btn={}
        self.set_binds(self,'root')
        self.overrideredirect(True)
        #self.geometry("%sx%s+%s+%s"%(self.ancho,self.alto,self.myX,self.myY))
        self.titulo=Frame(self,relief='flat',bd=0)
        self.titulo.pack(expand=1, side='top', fill='x')
        self.btnTitulo(
            'btnSalir',
            text='X',
            command=lambda:self.destroy(),
            activebackground='red'
            )
        self.btnTitulo(
            'btnMax',
            text='+',
            command=lambda:self.expandir(1),
            activebackground='blue'
            )
        self.btnTitulo(
            'btnMin',
            text='-',
            command=lambda:self.select('oculto',event='FocusIn'),
            activebackground='white'
            )
        self.bind("<B1-Motion>",self.move_window)#move_window(even)
        self.bind("<Motion>",self.radar)
        if frame:
            self.with_frame()
            print(self.frame.winfo_width())
        self.update()

        """
        for line in Gradient(self.raiz,'#0f0000','#ff0f0f'):
            self.raiz.create_line(line[0],line[1],line[2],line[3],fill=line[4])
        #tituloCanvas=Canvas(titulo,height=titulo.winfo_height(),width=titulo.winfo_width(),bg='#ff0000')
        """
        self.tituloCanvas=Canvas(self.titulo,height=self.titulo.winfo_height(),width=self.titulo.winfo_width())
        self.canvasGradient('#ff0f0f','#0f0000')
        self.tituloCanvas.config(bd=0,highlightthickness=0)
        self.tituloCanvas.pack(in_=self.titulo,expand=1,fill='x')
        self.tituloCanvas.bind("<Button>",self.move_window)
        self.conf(titulo=titulo, icon=icon, geometry=(self.ancho,self.alto,self.myX,self.myY))
        #root.()
    def set_binds(self,ref,foco):
        ref.bind(
            "<Destroy>",
            lambda e :self._destroy()
            )
        ref.bind(
            "<FocusOut>",
            lambda e :self.select(foco,event=e) 
            )
        ref.bind(
            "<FocusIn>",
            lambda e :self.select(foco,event=e) 
            )

    def info_events(self):
        """
            Tk Campo evento de Tkinter
            %f focus
            %h height
            %k keycode
            %s state
            %t time
            %w width
            %x x
            %y y
            %A char
            %E send_event
            %K keysym
            %N keysym_num
            %T type
            %W widget
            %X x_root
            %Y y_root
        """

        t={
            'linux':{
                'f_In':"9",
                'f_Out':"10",
                'btnPress':"4",
                'move':"6"
                },
            'windows':{
                'f_In':"FocusIn",
                'f_Out':"FocusOut",
                'btnPress':"ButtonPress",
                'move':"Motion"
                },
            }
        self.t=t[self.info['OS']]
    def _destroy(self):
         self.oculto.destroy()
         self.destroy()
         self.p('Listo')
    def conf(self, titulo='', icon='', geometry=()):
        # aplica cambios en el titulo, icono y la geometria de la ventana
        if icon :
            img=Image.open(icon)
            img.save(icon,'png')
            img.close()
            #print(icon)
            #self.PhotoImage=ImageTk.PhotoImage(image=Image.open(icon))
            self.oculto.focus_force()
            self.oculto.iconphoto(False, PhotoImage(name=icon))
            self.focus_force()
        if titulo: 
            self.oculto.title(titulo)
        self._geometry(geometry)
    def _geometry(self,geometry):
        if not geometry:
            geometry=(self.ancho,self.alto,self.myX,self.myY)
        if self.fullalto-50!=geometry[1]:self.alto=geometry[1]
        if self.fullancho!=geometry[0]:self.ancho=geometry[0]
        self.oculto.geometry("%sx%s+%s+%s"%(10,10,geometry[2]+10,geometry[3]+10))
        self.geometry("%sx%s+%s+%s"%geometry)
    def title(self,text):
        #cambia el nombre del titulo de la ventana
        self.oculto.title(text)
    def _iconphoto(self,arg,PhotoImg):
        #Usa una 'PhotoImage()' como Icono del Programa
        self.oculto.iconphoto(arg, PhotoImg)
    def with_frame(self):
        self.bind("<MouseWheel>",lambda event: self.canvas.yview_scroll(int(-1*(event.delta/120)), "units"))
        # with Linux OS
        #root.bind("<Button-4>",MouseWheelHandler)
        #root.bind("<Button-5>",MouseWheelHandler)
        self.f = Frame(self,relief='flat',bd=0,highlightthickness=0)
        self.canvas=Canvas(self.f,bd=0,highlightthickness=0)
        self.yscrollbar = Scrollbar(self.f, orient='vertical',command=self.canvas.yview,bd=0,highlightthickness=0)
        self.xscrollbar = Scrollbar(self.f, orient='horizontal',command=self.canvas.xview,bd=0,highlightthickness=0)
        self.frame=Frame(self.canvas,bd=0,highlightthickness=0)
        self.frame.bind("<Configure>",lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all")))
        self.canvas.create_window((0, 0), window=self.frame, anchor="nw")#esta linea equivale a: frame.pack(in_=canvas,anchor="nw")
        self.canvas.configure(xscrollcommand=self.xscrollbar.set,yscrollcommand=self.yscrollbar.set)
        self.yscrollbar.pack(side='right', fill='y')
        self.xscrollbar.pack(side='bottom', fill='x')
        self.f.pack(side='bottom', fill='x', expand=1)
        self.canvas.pack(side='left', fill='both', expand=1)
        self.raiz=Canvas(self.frame,bd=0,highlightthickness=0)
        self.raiz.pack(in_=self.frame,fill='both',expand=1)
    def loop(self):
        self.update()
        self.focus_force()
        self.mainloop()
        self.oculto.mainloop()
    def canvasGradient(self,color1,color2):
        escala={'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'a':10,'b':11,'c':12,'d':13,'e':14,'f':15}
        r1=float((escala[color1[1:3][0]])*16+(escala[color1[1:3][1]]))
        g1=float((escala[color1[3:5][0]])*16+(escala[color1[3:5][1]]))
        b1=float((escala[color1[5:][0]])*16+(escala[color1[5:][1]]))
        r2=float((escala[color2[1:3][0]])*16+(escala[color2[1:3][1]]))
        g2=float((escala[color2[3:5][0]])*16+(escala[color2[3:5][1]]))
        b2=float((escala[color2[5:][0]])*16+(escala[color2[5:][1]]))
        height=self.titulo.winfo_height()
        width=self.titulo.winfo_width()
        r=(r2-r1)/width
        g=(g2-g1)/width
        b=(b2-b1)/width
        for i in range(width):
            RR=int(r1+(r*i))
            GG=int(g1+(g*i))
            BB=int(b1+(b*i))
            color='#'+("" if RR>15 else "0")+str(hex(RR))[2:]+("" if GG>15 else "0")+str(hex(GG))[2:]+("" if BB>15 else "0")+str(hex(BB))[2:]
            self.tituloCanvas.create_line(i,0,i,width,fill=color)
            #,tags=("gradient",)
    def btnTitulo(self,name,text='btn',Leave_bg='#2e2e2e',Enter_bg='#891010',side='right',command=lambda:print('No hay comando'),bg='#2e2e2e',width=5,padx=2,pady=2,activebackground='red',bd=0,font='bold',fg='#ffffff',highlightthickness=0):
        self.btn[name]=Button(
            self.titulo,
            text=text,
            command=command,
            width=width,
            bg=bg,
            padx=padx,
            pady=pady,
            activebackground=activebackground,
            bd=bd,
            font=font,
            fg=fg,
            highlightthickness=highlightthickness
        )
        self.btn[name].pack(side=side)

        #color cuando el mouse NO esta por ensima de este Widget 
        self.btn[name].bind(
            "<Leave>",
            lambda event :
                event.widget.config(bg=Leave_bg)
        )
        #color cuando el mouse SI esta por ensima de este Widget 
        self.btn[name].bind(
            "<Enter>",
            lambda event :
                event.widget.config(bg=Enter_bg)
        )
    def expandir(self,v):
        if v:
            self.btn['btnMax'].config(command=lambda:self.expandir(0))
            self._geometry((self.fullancho,self.fullalto-50,0,0))
            self.update()
            self.canvasGradient('#ff0f0f','#0f0000')
        else:
            self.btn['btnMax'].config(command=lambda:self.expandir(1))
            self._geometry((self.ancho,self.alto,self.rootX,self.rootY))
            self.update()
            self.canvasGradient('#ff0f0f','#0f0000')
    def select(self,w='force',event=''):
        #f_in 9
        #f_out 10
        t=str(event.type)
        print(w,self.myFoco,event.type,event)
        if event=='':
            return 
        elif w=='oculto' and self.t['f_In'] in t and self.myFoco!='otro':
            self.myFoco='otro'
            self.lapsoRoot=time.time()+0.01
        if w=='root' and self.t['f_In'] in t :
            self.myFoco='root'
        if w=='root' and self.t['f_Out'] in t :
            self.myFoco='otro'
            self.lapsoRoot=time.time()
        if w=='oculto' and self.t['f_In'] in t and self.myFoco=='otro':
            self.focus_force()
            self.myFoco=w
            self.lapsoOculto=time.time()
        if w=='oculto' and self.t['f_Out'] in t and self.myFoco=='root':
            self.myFoco='otro'
        print(w,self.myFoco,t) 
        if (time.time()-self.lapsoRoot)<0.50 and self.myFoco=='oculto':
            print('Min')
            self.withdraw()
            self.oculto.iconify()
        elif (time.time()-self.lapsoRoot)>0.50 and self.myFoco=='otro':
            print('Max')
            self.deiconify()
            self.oculto.geometry('+%s+%s'%( self.rootX, self.rootY ))
            self.focus_force()
    def radar(self,event):
        #6 Motion event
        #print(event.type,str(event.state),event)
        if '8' in str(event.state):
            x=event.x_root-int(self.geometry().split('+')[1])
            y=event.y_root-int(self.geometry().split('+')[2])
            n=s=e=o=0
            if (self.winfo_height()-y)<10: s=1
            if (self.winfo_width()-x)<10: e=1
            if (y)<10: n=1
            if (x)<10: o=1
            print(x,y,n,s,e,o)
    def move_window(self,event):
        #print(event.type,str(event.state),event)
        if event.widget==self.tituloCanvas and self.t['btnPress'] in str(event.type) :
            self.myX=event.x_root
            self.myY=event.y_root  
        if event.widget==self.tituloCanvas and self.t['move'] in str(event.type) :
            x=event.x_root-self.rootX-self.myX
            y=event.y_root-self.rootY-self.myY
            if (y!=0 or x!=0):
                #root.geometry('+{0}+{1}'.format(int(event.x_root-x),int(event.y_root-y)))
                self.rootX=self.rootX+event.x_root-self.myX
                self.rootY=self.rootY+event.y_root-self.myY
                self._geometry((self.ancho,self.alto,self.rootX, self.rootY))
                self.myX=event.x_root
                self.myY=event.y_root
                
        #root.focus()
class tkinterCSS:
    """Gestor de estilos desde scripts CSS"""
    def __init__(self, *arg, **kw):
        #self.files=self.is_extend(os.listdir(self.pwd+'css'),extend)
        self.extend=['css']
        self._fontInstances={}
        self.styleTk={
            'color':{
                'default':{
                    'default':{'bg':'#f3a80c','fg':'#00007a'},
                    'radiobtn':{'bg':'#02020e','fg':'#fef3f0'},
                    'Chkbtn':{'bg':'#02020e','fg':'#fef3f0'},
                    'btn':{'bg':'#02020e','fg':'#fef3f0'},
                    },
                'queso':{
                    'default':{'bg':'#f3a80c','fg':'#00007a'},
                    'radiobtn':{'bg':'#02020e','fg':'#fef3f0'},
                    'Chkbtn':{'bg':'#02020e','fg':'#fef3f0'},
                    'btn':{'bg':'#02020e','fg':'#fef3f0'}
                    }
                },
            'font':{
                'default':{
                    'default':{'font':('Arial',12)},
                    'lb':{'font':('Comic Sans MS',12)}
                    },
                'bob':{
                    'default':{'font':('Franklin Gothic Book',12)},
                    },
                },
            'widget':{
                'default':{
                    'lb':{'bd':0,'justify':"left",'anchor':E},
                    'btn':{'bd':0,'width':5},
                    'default':{'bd':0,'width':13},
                    },
                'bob':{
                    'lb':{'bd':0,'justify':"center"},
                    'btn':{'bd':0,'width':5},
                    'default':{'bd':0,'width':15},
                    },
                'bobGrande':{
                    'lb':{'bd':0,'justify':"center"},
                    'btn':{'bd':0,'width':20},
                    'default':{'bd':0,'width':15},
                    }
                }
            }
        self.style={
            'default':{'color':'default','font':'default','widget':'default'},
            'bobEsponja':{'color':'queso','font':'bob','widget':'bob'},
            'bobEsponjaGrande':{'color':'queso','font':'bob','widget':'bobGrande'}
            }
        
    def setFontInstance(self,family,size):
        if not family in self._fontInstances:
            self._fontInstances[family]={size:font.Font(family=family,size=size)}
        elif not size in self._fontInstances[family]:
            self._fontInstances[family][size]=font.Font(family=family,size=size)
    def getTextSize(self,text,family,size,bd=0):
        return [
            self._fontInstances[family][size].measure(text)+(2*bd),
            self._fontInstances[family][size].metrics('linespace')+(2*bd)
            ]
    def scan_css(self,pwd):
        rule={'selector':{'property':'value'}}
        e=[]
        for f in self.files:
            file=self.getFile(pwd+'css'+os.sep+f)
            text=''
            for l in file:
                text+=l.strip()
            comentario=-1
            selector=-1
            regla=-1
            for c in range(len(text)):
                if '/*'==text[c:c+2]:
                    comentario=c
                elif '*/'==text[c:c+2] and comentario>=0:
                    text[comentario:c-1]
                    comentario=-1


            for l in file:
                l=l.strip()
                if l[-1]=='{':
                    e+=[l[:-1],{}]
                elif l!='}' and (l[:2]!='/*') and (l[-2:]!='*/'):
                    e[-1][l.split(':')[0].strip()]=l.split(':')[1].strip()[:-1]
        
        self.files=e
        #self.files
    def loadStyle(self,w_tk,style='default',**kwarg):
        kw={}
        if not style in self.style:
            style='default'
        for k in self.styleTk:
            if self.style[style][k] in self.styleTk[k]:
                if w_tk in self.styleTk[k][self.style[style][k]]:
                    kw = {**kw,**self.styleTk[k][self.style[style][k]][w_tk]}
                else:
                    kw = {**kw,**self.styleTk[k][self.style[style][k]]['default']}
            elif w_tk in self.styleTk[k]['default']:
                kw={**kw,**self.styleTk[k]['default'][w_tk]}
            else:
                kw={**kw,**self.styleTk[k]['default']['default']}
        self.setFontInstance( *kw['font'] )
        return {**kw,**kwarg}
    def keyCSS_to_keyttkStyle():
        """
        https://developer.mozilla.org/en-US/docs/Web/CSS/Pseudo-classes
        https://developer.mozilla.org/en-US/docs/Web/CSS/Pseudo-classes

        #id-name
        .class-name
        selector:pseudo-class {
            property: value;
        }
        CSS selectors
        CSS selectors define the elements to which a set of CSS rules apply.
        Note: There are no selectors or combinators to select parent items, 
        siblings of parents, or children of parent siblings.

        Basic selectors
            Universal selector
                Selects all elements. 
                Optionally, it may be restricted to a specific 
                namespace or to all namespaces. 
                Syntax: * ns|* *|* Example: * will match all 
                the elements of the document.

            Type selector
                Selects all elements that have the given node name. 
                Syntax: elementname Example: input will match 
                any <input> element.

            Class selector
                Selects all elements that have the given class attribute. 
                Syntax: .classname Example: .index will match any element 
                that has a class of "index".

            ID selector
                Selects an element based on the value of its id attribute. 
                There should be only one element with a given ID in a 
                document. Syntax: #idname Example: #toc will match the 
                element that has the ID "toc".

            Attribute selector
                Selects all elements that have the given attribute. 
                Syntax: [attr] [attr=value] [attr~=value] [attr|=value] 
                [attr^=value] [attr$=value] [attr*=value] 
                Example: [autoplay] will match all elements that have 
                the autoplay attribute set (to any value).

        Grouping selectors
            Selector list
                The , selector is a grouping method that selects all 
                the matching nodes. Syntax: A, B Example: div, span 
                will match both <span> and <div> elements.

        Combinators
            Descendant combinator
                The " " (space) combinator selects nodes that are 
                descendants of the first element. Syntax: A B 
                Example: div span will match all <span> elements 
                that are inside a <div> element.
            Child combinator
                The > combinator selects nodes that are direct children 
                of the first element. Syntax: A > B Example: ul > li 
                will match all <li> elements that are nested directly 
                inside a <ul> element.
            General sibling combinator
                The ~ combinator selects siblings. This means that the 
                second element follows the first (though not necessarily 
                immediately), and both share the same parent. 
                Syntax: A ~ B Example: p ~ span will match all <span> 
                elements that follow a <p>, immediately or not.
            Adjacent sibling combinator
                The + combinator matches the second element only if it 
                immediately follows the first element. Syntax: A + B 
                Example: h2 + p will match all <p> elements that 
                immediately follow an <h2> element.
            Column combinator Experimental
                The || combinator selects nodes which belong to a column. 
                Syntax: A || B Example: col || td will match all <td> 
                elements that belong to the scope of the <col>.

        Pseudo
            Pseudo classes
                The : pseudo allow the selection of elements based on 
                state information that is not contained in the document 
                tree. Example: a:visited will match all <a> elements 
                that have been visited by the user.
            Pseudo elements
                The :: pseudo represent entities that are not included 
                in HTML. Example: p::first-line will match the first 
                line of all <p> elements.



        CSS layout is mostly based on the box model.
        padding, the space around the content. In the example below, it is the space around the paragraph text.
        border, the solid line that is just outside the padding.
        margin, the space around the outside of the border.

        In this section we also use:
            width: (of an element).
            background-color:, the color behind an element's content and padding.
            color:, the color of an element's content (usually text).
            text-shadow: sets a drop shadow on the text inside an element.
            display: sets the display mode of an element. (keep reading to learn more)
            text-shadow: 3px 3px 1px black;


        *{
        margin:0px;
        padding:0px;
        }
        Element:
        header{
            background:red;
            height:100px;
            width:100%;
            margin:0px;
            text-align:center;
            line-height:100px;
            color:white;
            border-bottom: 3px dasher black;
        }
        nav{
            background:lightblue;
            height:50px;
            borde-bottom: 1px solid black;
        }
        nav ul li{
            float:left;
            list-style:none;
            margin:10px;     
            line-height:30px;
        }
        .clearfix{
            clear:both
        }
        #contenedor{
            float:left;    
            width:calc(80%-80px);
            background:green;
            min-height:500px;
            padding:40px;
        }

        .article{
            color:white;
            margin-top:15px;
            margin-bottom:15px;
            padding-bottom:10px;
            border-bottom: 1px solid #eee; 
        } 
        .article:first-child{
            border-top: 1px solid #eee;
        } 

        aside{ 
            float:left; 
            width:calc(20%-20px); 
            background:orange;
            min-height:500px;
            padding-left:10px;
            padding-right:10px;
            padding-top:20px;
        }

        footer{
            background:black;
            color:white;
            text-align:center;
            height:50px;
            line-height:50px;
        }
        """
        pass
    def css_to_ttkStyle():
        for k in self.files:
            if '*' in k:
                for rule in self.files[k]:
                    print(rule)
    def posicion(self,display='block',min_width=500,):
        """
        /* precomposed values */
        display: block;
        display: inline;
        display: inline-block;
        display: flex;
        display: inline-flex;
        display: grid;
        display: inline-grid;
        display: flow-root;

        /* box generation */
        display: none;
        display: contents;

        /* two-value syntax */
        display: block flow;
        display: inline flow;
        display: inline flow-root;
        display: block flex;
        display: inline flex;
        display: block grid;
        display: inline grid;
        display: block flow-root;

        /* other values */
        display: table;
        display: table-row; /* all table elements have an equivalent CSS display value */
        display: list-item;

        /* Global values */
        display: inherit;
        display: initial;
        display: revert;
        display: revert-layer;
        display: unset;
        """
        pass
class tkinterVar:
    """docstring for tkinterVar"""
    def __init__(self,*arg,**kw):
        self.tkVar={}
        self.tkValue={}
        self.idVar={}
        self.nextIdVar=str(len(self.idVar))
        self.typeVar = [
            [StringVar,str],
            [IntVar,int],
            [DoubleVar,float],
            [BooleanVar,bool]
            ]
        self.widgetVarKwarg={
            'entry':'textvariable',
            'lb':'textvariable',
            'Checkbutton':'variable',
            'Radiobutton':'variable'
            }
    def getVarID(self,n):
        '''Ejecuta: return tkinterVariable[n].get()'''
        return self.tkVar[self.idVar[n][0]][self.idVar[n][1]][self.idVar[n][2]][self.idVar[n][3]].get()
    def setVarID(self,n,value):
        '''Ejecuta: tkinterVariable[n].set(value)'''
        self.tkVar[self.idVar[n][0]][self.idVar[n][1]][self.idVar[n][2]][self.idVar[n][3]].set(value)
    def setTkinterVar(self,r,typeVar):
        '''agrega un tkinterVariable segun typeVar.__cass__, y asocia la ruta r
            self.setTkinterVar(
                [box,subbox,w_tk,name]:list,
                typeVar:[str/int/float/bool]
                ) -> ID:str
        '''
        for x in range( len(r) ):
            if not r[x] in V.get_iter( self.tkVar,keys=r[:x] ):
                V.get_iter( self.tkVar,keys=r[:x] )[r[x]]={}
        self.tkValue[self.nextIdVar] = typeVar
        typeVar = self.getTkinterVar(typeVar)
        self.tkVar[r[0]][r[1]][r[2]][r[3]]=typeVar(
            value=self.tkValue[self.nextIdVar],name=self.nextIdVar
            )
        self.tkVar[r[0]][r[1]][r[2]][r[3]].trace('w',self.updateVars)
        self.idVar[self.nextIdVar]=r
        self.nextIdVar=str(len(self.idVar))
        return self.nextIdVar
    def getTkinterVar(self,typeVar):
        #retorna la clase [StringVar,IntVar,DoubleVar,BooleanVar]
        return next(
            ( k[0] for k in self.typeVar if k[1] == typeVar.__class__ ), 
            self.typeVar[0][0] 
            )
    def updateVars(self,n,arg2,mod):
        #Actualizamos las 'self.tkValue[numero]' Automaticamente
        #print(n,arg2,mod)
        self.tkValue[n]=self.tkVar[self.idVar[n][0]][self.idVar[n][1]][self.idVar[n][2]][self.idVar[n][3]].get()
    def loadTkinterVar(self,w_tk,name,box,subbox,typeVar=None,**kw):
        ID = None
        if typeVar!=None and w_tk in self.widgetVarKwarg:
            ID=self.setTkinterVar(
                [box,subbox,w_tk,name],typeVar
                )
            kw[self.widgetVarKwarg[w_tk]]=V.get_iter(
                self.tkVar, [box,subbox,w_tk,name]
                )
        return ID, kw    
    def showVars(self,full=0):
        print('Mostrando las variables TypeVar:')
        for v in self.v:
            if full:
                print('TypeVar : %s '%(v))
                print('Valor = %s '%(self.v[v].get()))
                print('Valores = %s \n'%(self.valores[v]))
            else:
                print('(%s , %s , %s )'%(v,self.v[v].get(),self.valores[v]))
class seccionContenedor:
    """gestor de elementos block y inline"""
    def __init__(self,limites=(),**kw):
        self.bloquesSep=0
        self.bloques={}
        self.nextIdItem=None
        self.nextLine=True
        self.mas_x={}
        self.mas_y={}
        self.setBoxModel(**kw)
    def setBoxModel(self,x0=0,y0=0,width=500,height=500,margin=0,border=0,padding=0,display='block'):
        self.x0=x0
        self.y0=y0
        self._m=margin
        self._b=border
        self._p=padding
        self._W=width
        self._H=height
        self._display=display
    def config(self,x0=None,y0=None,width=None,height=None,margin=None,border=None,padding=None,display=None):
        if x0: self.x0=x0
        if y0: self.y0=y0
        if margin: self._m=margin
        if border: self._b=border
        if padding: self._p=padding
        if width: self._W=width
        if height: self._H=height
        if display: self._display=display
    def setItem(self,size,name,display='block',**kw):
        if display=='block':
            self.nextLine=True
            self.getBloque(display,**kw)
            self.bloques[self.nextIdItem]['line'][name]=size
        if display=='inline':
            if self.nextLine: self.getBloque(display,**kw)
            self.nextLine=False
            self.bloques[self.nextIdItem]['line'][name]=size
        if display=='inline-block':
            if self.nextLine: self.getBloque(display,**kw)
            self.nextLine=False
            self.bloques[self.nextIdItem]['line'][name]=size

        if display=='flex':
            #self.nextLine=True/False
            self.getBloque(display)
            self.bloques[self.nextIdItem]['line'][ID]=size
        if display=='inline-flex':
            #self.nextLine=True/False
            self.getBloque()
            self.bloques[self.nextIdItem]['line'][ID]=size
        if display=='grid':
            #self.nextLine=True/False
            self.getBloque()
            self.bloques[self.nextIdItem]['line'][ID]=size
        if display=='inline-grid':
            #self.nextLine=True/False
            self.getBloque()
            self.bloques[self.nextIdItem]['line'][ID]=size
        if display=='flow-root':
            self.getBloque()
            self.bloques[self.nextIdItem]['line'][ID]=size
    def getBloque(self,display,side="left" , fill="both",**kw):
        if self.nextIdItem==None:self.nextIdItem=0
        else: self.nextIdItem+=1
        self.bloques[self.nextIdItem]={
            'line':{},
            'place':{},
            'side':side,
            'fill':fill,
            'display':display,
            }
    def getPlace(self,name,x0=0,y0=0):
        for n in range(0,self.nextIdItem+1):
            if name in self.bloques[n]['line']:
                return [
                    self.bloques[n]['place'][name][0]+x0,
                    self.bloques[n]['place'][name][1]+y0
                    ]
    def getItemSide(self,n):
        if self.bloques[n]['side']=='left':
            return 0
        elif self.bloques[n]['side']=='center':
            return ((self._myWidth-self.mas_x[n])/2)
        elif self.bloques[n]['side']=='right':
            return self._myWidth-self.mas_x[n]
    def updatePLace(self):
        self.updateSize()
        y=0
        for n in self.bloques:
            x=self.getItemSide(n)
            if self.bloques[n]['display']=='block':
                for k in self.bloques[n]['line']:
                    self.bloques[n]['place'][k]=[x,y]
                    x += self.bloques[n]['line'][k][0]
            if self.bloques[n]['display']=='inline':
                for k in self.bloques[n]['line']:
                    self.bloques[n]['place'][k]=[
                        x,
                        y+(self.mas_y[n]-self.bloques[n]['line'][k][1])
                        ]
                    x+= self.bloques[n]['line'][k][0]
            y+= self.mas_y[n]
    def agregarBloque(self,n):
        desde=max(list(self.bloques.keys()))
        iterar=range(desde,n,-1)
        if desde==n:
            self.bloques[n+1]={**self.bloques[n]}
        for i in iterar:
            self.bloques[i+1]={**self.bloques[i]}
        self.bloques[n+1]['line']={}
        self.bloques[n+1]['place']={}
    def updateSize(self,n=0):
        self.mas_x={}
        self.mas_y={}
        while n in self.bloques:
            self.mas_x[n]=0
            self.mas_y[n]=0
            if self.bloques[n]['display']=='block':
                for size in self.bloques[n]['line'].values():
                    self.mas_x[n] = size[0]
                    self.mas_y[n] = size[1]
            if self.bloques[n]['display']=='inline':
                inline=list( self.bloques[n]['line'].keys() )
                for k in inline:
                    size=self.bloques[n]['line'][k]
                    if (self.x0+self.mas_x[n]+size[0]) >= self._W:
                        print(n,k,self.x0,self.mas_x[n],size[0],self._W)
                        self.agregarBloque(n)
                        key=list(self.bloques[n]['line'].keys())
                        for b in key[key.index(k):]:
                            self.bloques[n+1]['line'][b]=[*self.bloques[n]['line'][b]]
                            del self.bloques[n]['line'][b]
                        n+=1
                        self.nextIdItem+=1
                        self.mas_x[n]= size[0]
                        self.mas_y[n]= 0
                    else:
                        self.mas_x[n] += size[0]

                    if self.mas_y[n]<size[1]:
                        self.mas_y[n]=size[1]
                if n>0 and self.mas_x[n-1]+self.mas_x[n]+self.x0<self._W:
                    unir=True
                    for k in ['display','fill','side']:
                        if self.bloques[n][k]!=self.bloques[n-1][k]:
                            unir=False
                    if unir:
                        for b in self.bloques[n]['line']:
                            self.bloques[n-1]['line'][b]=self.bloques[n]['line'][b]
                        self.mas_x[n-1]+=self.mas_x[n]
                        if self.mas_y[n]>self.mas_y[n-1]:
                            self.mas_y[n-1]=self.mas_y[n]
                        n-=1
            n+=1
        self._myWidth=max( list(self.mas_x.values()) )
        self._myHeigth=sum( list(self.mas_y.values()) )
    def getSize(self):
        self.updatePLace()
        return [
            self._myWidth+self._m+self._b+self._p,
            self._myHeigth+self._m+self._b+self._p
            ]
class widgetUtils(tkinterCSS,tkinterVar):
    """
        metodos utiles para la gestion de los Widgets y graficos
    """
    def __init__(self, *arg,**kw):
        tkinterCSS.__init__(self,*arg,**kw)
        tkinterVar.__init__(self,*arg,**kw)
        self.size=descomprimir(**sizes)
        print(self.size.getSize())
        self.widgets={'default':{'default':{}}}
        self.contenedores={}
        self.class_tk={
            'radiobtn':Radiobutton,
            'checkbtn':Checkbutton,
            'btn':Button,
            'lb':Label,
            'entry':Entry,
            }
    def setContenedor(self,box,v,x=0,y=0,setElemento=None,**kw):
        if not box in self.widgets:
            self.widgets[box]={}
            self.contenedores[box]={'box':seccionContenedor(x0=x,y0=y,width=self.frameScrollWidth)}
        for e in v:
            if not e[0] in self.widgets[box]:
                self.widgets[box][e[0]]={}
            if setElemento != None: 
                self.contenedores[box][e[0]]=seccionContenedor(width=self.frameScrollWidth)
                setElemento(
                    e,box=box,subbox=e[0],
                    **kw
                    )
                self.contenedores[box]['box'].setItem(
                    self.contenedores[box][e[0]].getSize(),
                    e[0],display='inline')
        size=self.contenedores[box]['box'].getSize()
        for e in v:
            [x0,y0] = self.contenedores[box]['box'].getPlace(e[0],x0=x,y0=y)
            for w_tk in self.widgets[box][e[0]]:
                for name in self.widgets[box][e[0]][w_tk]:
                    [i,j]=self.contenedores[box][e[0]].getPlace(
                        f'{w_tk}_{name}',x0=x0,y0=y0)
                    self.widgets[box][e[0]][w_tk][name].place(x=i,y=j)

        return [size[0]+x,size[1]+y]
    def setWidget(self,w_tk,name,box='default',subbox='default',side="left" ,display='block',**kw):
        if w_tk in self.class_tk:
            #configuramos el estilo
            kw = self.loadStyle(w_tk,**kw)
            
            #instanciamos una objeto TkinterVar para este widget
            ID, kw = self.loadTkinterVar(w_tk,name,box,subbox,**kw)

            #medida del widget
            size, kw = self.loadSizes(w_tk,**kw)
            
            self.contenedores[box][subbox].setItem(
                size,f'{w_tk}_{name}',display=display,side=side,**kw
                )
            
            #creando el widget
            if not box in self.widgets: self.widgets[box]={subbox:{}}
            if not subbox in self.widgets[box]: self.widgets[box][subbox]={}
            if not w_tk in self.widgets[box][subbox]: self.widgets[box][subbox][w_tk]={}
            self.widgets[box][subbox][w_tk][name]=self.class_tk[w_tk](self,**kw)
            if ID!=None: return ID
        
        """
        elif myWidget['inputType']=='Radiobutton':
            p=myWidget['name']+'_'+[k for k in myWidget['radios']][0]
            #print([k for k in myWidget['radios']][0],p)
            self.Vars[p]=StringVar(value=str(myWidget['value']),name=p)
            x , y = 0 , 0
            if 'text' in myWidget:
                self.SetWidget(atributos={
                    'inputType':'Label',
                    'padre':myWidget['padre'],
                    'name':myWidget['name']+'_Label',
                    'xPlace':myWidget['xPlace']+x,
                    'yPlace':myWidget['yPlace']+y,
                    'ancho':self.anchoWidget(myWidget),
                    'alto':self.altoWidget(myWidget),
                    'fontSize':myWidget['fontSize'],
                    'fontType':myWidget['fontType'],
                    'fontColor':myWidget['fontColor'],
                    'bgColor':myWidget['bgColor'],
                    'text':myWidget['text']}
                    )
            x=self.atrb['fontSizeToAlto'][myWidget['fontType']][myWidget['fontSize']]
            #Creamos la lista de objetos Widget RadioButton()
            if 'radios' in myWidget:
                for r in myWidget['radios']:
                    y += (self.atrb['fontSizeToAlto'][myWidget['fontType']][myWidget['fontSize']])
                    myWidget['radios'][r]['inputType']=myWidget['inputType']
                    myWidget['radios'][r]['padre']=myWidget['padre']
                    myWidget['radios'][r]['name']=myWidget['name']+'_'+str(r)
                    myWidget['radios'][r]['xPlace']=myWidget['xPlace']+x
                    myWidget['radios'][r]['yPlace']=myWidget['yPlace']+y
                    myWidget['radios'][r]['bgColor']=myWidget['bgColor']
                    myWidget['radios'][r]['fontColor']=myWidget['fontColor']
                    myWidget['radios'][r]['fontType']=myWidget['fontType']
                    myWidget['radios'][r]['fontSize']=myWidget['fontSize']
                    myWidget['radios'][r]['ancho']=self.anchoWidget(myWidget)
                    myWidget['radios'][r]['alto']=self.altoWidget(myWidget)
                    #Instansiando 'Un' objeto Widget RadioButton()
                    myWidget['radios'][r]['widget']=Radiobutton(
                        self.widgets[myWidget['padre']]['widget'], 
                        text=myWidget['radios'][r]['text'],
                        bg=myWidget['radios'][r]['bgColor'],
                        fg=myWidget['radios'][r]['fontColor'], 
                        variable=self.Vars[p],
                        value=r,
                        font=(myWidget['radios'][r]['fontType'],myWidget['radios'][r]['fontSize']))
                    #le asignamos el comando desde 'self.command'
                    if 'command' in myWidget['radios'][r]:
                        myWidget['radios'][r]['widget'].config(command=self.command[myWidget['radios'][r]['command']])
                    self.widgets.setdefault(myWidget['radios'][r]['name'],myWidget['radios'][r])
            self.Vars[p].trace('w',lambda name,arg2,mod : self.updateVar(name,arg2,mod))
        """
    def responsive(self):
        '''ajustar la posicion de los widgets a la ventana'''
        x=10
        y=10
        for box in self.contenedores:
            self.contenedores[box]['box'].config(
                x0=x,y0=y,
                width=self.frameScrollWidth,
                height=self.frameScrollHeight
                )

            size=self.contenedores[box]['box'].getSize()
            if box=='box':continue

            for subbox in self.widgets[box]:
                #self.contenedores[box]['box'].updatePLace()
                [x0,y0] = self.contenedores[box]['box'].getPlace(
                    subbox,x0=x,y0=y
                    )
                for w_tk in self.widgets[box][subbox]:
                    for name in self.widgets[box][subbox][w_tk]:
                        [i,j]=self.contenedores[box][subbox].getPlace(
                            f'{w_tk}_{name}',x0=x0,y0=y0)
                        self.widgets[box][subbox][w_tk][name].place(x=i,y=j)
            x+=size[0]
            y+=size[1]
    def loadSizes(self,w_tk,size=True,contentSize=False,**kw):
        if w_tk in ['lb'] and size:
            #medidas de widgets que solo dependen del texto
            return self.getTextSize( kw['text'],*kw['font'] ,bd=kw['bd']),kw
        elif contentSize:
            pass
        elif w_tk in self.size.D[0]['inter'] and size:

            return self.widgetSize(w_tk,kw['width'],*kw['font'],bd=kw['bd']),kw
        else:
            return [0,0],kw
    def widgetSize(self,w,width,f,s,bd=0):
        #ancho del widget en pixeles
        #alto del widget en pixeles
        return [
            self.size.value( [w,f,'width',s,width] )+(2*bd),
            self.size.value( [w,f,'height',s] )+(2*bd)
            ]
class FrameScroll(Frame,widgetUtils):
    """docstring for tk_frame_scroll"""
    def __init__(self, padre,**kwargs):
        widgetUtils.__init__(self)
        # el objeto Tk(), que sera el PADRE de la instancia de este Frame
        self.frameScrollHeight = 400
        self.frameScrollWidth = 650
        self.paddingScrollBar=16
        self.kw_Frame={'bd':0,'highlightthickness':0}
        self.root=padre
        #frame que recive a los widgets canvas, scroll
        self.root_frame=Frame(self.root,relief='flat',**self.kw_Frame)
        #canvas para usar como area de Scroll
        self.root_frame_canvas=Canvas(self.root_frame,**self.kw_Frame)
        #barra de Scroll Vertical
        self.root_Yscroll=Scrollbar(
            self.root_frame, 
            orient='vertical',
            command=self.root_frame_canvas.yview
            )
        #barra de Scroll Horizontal
        self.root_Xscroll=Scrollbar(
            self.root_frame, 
            orient='horizontal',
            command=self.root_frame_canvas.xview
            )
        #instanciamos un Frame Scrolleado con el widget 'Canvas' ya que 
        #'super(FrameScroll, self)' pertenece a 'canvas', y 'canvas' a 
        #su ves esta siendo controlado con Scrollbar en X y en Y
        super(FrameScroll, self).__init__(self.root_frame_canvas)
        #Este evento se activa al girar la rueda del raton
        #self.root.bind("<MouseWheel>", self.scrollMe)
        self.root.bind("<Button-4>",self.scrollMe)
        self.root.bind("<Button-5>",self.scrollMe)
        #Configuramos todo para que 'self' quede con 
        #Scroll en X y en Y
        self.root_frame.bind("<Configure>",self.configureMe)
        #equivalente a 'self.pack()'
        self.root_frame_canvas.create_window(
            (0, 0),
            window=self,
            anchor="nw"
            )
        self.root_frame_canvas.configure(
            yscrollcommand=self.root_Yscroll.set,
            xscrollcommand=self.root_Xscroll.set
            )
        self.root_Yscroll.pack(side='right', fill='y')
        self.root_Xscroll.pack(side='bottom', fill='x')
        self.root_frame.pack(side='bottom', fill='both',expand=1)
        self.root_frame_canvas.pack(side="left" , fill="both", expand=True)
        self.conf(**kwargs)
        self.canvas=Canvas(self,bg=self.styleTk['color']['default']['default']['bg'])
        self.canvas.place(x=-1, y=-1)
    def scrollMe(self,event):
        
        if event.num == 5 or event.delta==120:
            self.root_frame_canvas.yview_scroll(5,"units")
        if event.num == 4 or event.delta==-120:
            self.root_frame_canvas.yview_scroll(-5,"units")
    def getEventType(self):
        '''retorna diccionario con los valores Type de cada evento'''
        if os.name == 'nt':
            return {
                'f_In':"FocusIn",
                'f_Out':"FocusOut",
                'btnPress':"ButtonPress",
                'move':"Motion",
                'mouseW':"MouseWheel"
                }
        elif 'ANDROID_ROOT' in os.environ:
            return {
                'f_In':"9",
                'f_Out':"10",
                'btnPress':"4",
                'move':"6",
                'mouseW':"38"
                } 
        elif os.name == 'posix':
            return {
                'f_In':"9",
                'f_Out':"10",
                'btnPress':"4",
                'move':"6",
                'mouseW':"38"
                }
        
    def configureMe(self,event):
        print(event.type,event.num,event)
        if self.frameScrollHeight!=event.height and self.frameScrollWidth!=event.width:
            self.root_frame_canvas.configure(
                scrollregion=self.root_frame_canvas.bbox("all")
                )
            self.frameScrollHeight=event.height
            self.frameScrollWidth=event.width
            self.configure(
                width = event.width, height=event.height
                )
            self.canvas.configure(
                width = event.width, height=event.height
                )
            #self.responsive()
            self.root.update()
    def conf(self, titulo='', icon='', geometry=(),color={},font=(),style={},**kw):
        # aplica cambios en el titulo, icono y la geometria de la ventana
        if self.root.__class__==I_am_Tk:
            self.root.conf(titulo=titulo, icon=icon, geometry=geometry)
        else:
            if icon :
                self.root.iconphoto(
                    False, 
                    PhotoImage(file=icon)
                    )
            if titulo: 
                self.root.title(titulo)
            if geometry:
                self.root.geometry("%sx%s+%s+%s"%geometry)
                self.frameScrollWidth = geometry[0]
                self.frameScrollHeight = geometry[1]
    def loop(self):
        print('self.root_frame_canvas.bbox("all")',self.root_frame_canvas.bbox("all"))
        if self.root.__class__==I_am_Tk:
            self.root.loop()
        else:
            self.root.update()
            self.root.mainloop()
    def updateScroll(self,w=0,h=0):
        if w!=0 and w < self.frameScrollWidth : w = self.frameScrollWidth
        if w == 0: w = self.frameScrollWidth
        if h!=0 and h < self.frameScrollHeight : h = self.frameScrollHeight
        if h == 0: h = self.frameScrollHeight
        
        self.configure(width = w, height=h)
        self.canvas.configure(width = w, height=h)
        self.root.update()
    def liberarCanvas(self,tag='all'):
        # limpiar canvas y liberar Memoria
        self.canvas.delete(tag)
class widget_IDE(FrameScroll):
    """docstring for widgetIDE"""
    def __init__(self,padre, **kwargs):
        super(widget_IDE, self).__init__(padre, **kwargs)
        self.textoPlanoPath = 'animacion_con_matplotlib.py'
        self.file = 'animacion_con_matplotlib.py'
        self.l=0 #line
        self.c=0 #caracter
        self.syntax='python'
        self.fontGround='#3030ff'
        self.fontColor='#ffffff'
        self.fontType='Andale Mono'
        self.fontSize=11
        self.letraWidth=8
        self.letraHight=28
        self.colores={
            'fc':self.fontColor,
            'fg':self.fontGround,
            'args':'#0ff00f',
            'BlockMagicName':'#8080f9',
            'BlockCall':'#0f0ff0',
            'BlockName':'#0ff00f',
            'value':'#ff00ff',
            'definicion':'#01019f',
            'operador':'#f90101',
            'control':'#f90f0f'
            }
        self.grupos={
            'value':['False', 'None', 'True'],
            'definicion':['async', 'class', 'def','lambda'],
            'operador':[
                'in','not','or','and','is','del','=',
                '*','/','+','-','&','|','!','@','<','>'
                ],
            'control':[
                'from', 'import','as', 'global', 'nonlocal', 
                'try', 'except', 'finally',
                'for', 'while', 'with', 'if', 'elif', 'else', 
                'pass', 'return', 'break', 'continue',
                'yield', 'await', 'raise', 'assert'
                ]
            }
        self.longitud=fontSizeWidth[self.fontType.replace(' ','_')][fontSizeWidth['Sizes'][self.fontSize]]
        
    def stringWidth(self,string):
        l=0.0
        for c in string: 
            if ord(c) in self.longitud:
                l+=self.longitud[ord(c)]
            else:
                print(ord(c),c)
        return l
    def setRet(self,k,t):
        #agregando instruccion para el grafico
        return [{'fill':self.colores[k],'width':self.stringWidth(t),'text':t}]
    def subBloque(self,line):
        #detectar inicio y fin de un bloque y luego darle formato
        indent='    '
        n=0
        while indent==file[self.line][:len(indent)]:
            n+=1
            indent+=indent
        #if file[self.line]
    def lineToFormat(self,line,format='canvas',indent='    '):

        #nivelar
        #agrupacion = {'orden':['{','[','(']}
        agrupacion = {'abierto': [[10,10]],'cerrado':[[5,3,5,10]],'l':10,'c':10}
        start=["{","(","[","'",'"']
        stop =["}",")","]","'",'"']
        nivel={0:''}
        n=0
        ret=[]
        if_in=lambda l,t: []!=[i for i in l if i in t]
        def formato(text,ret,grupo=''):
            indentacion=''
            if ' ' in text:
                n=0
                while text[n]==' ':
                    indentacion+=text[n]
                    n+=1
                ret+=setRet('fc',indentacion)
            if grupo=='args':
                if ',' in k:
                    for t in text.split(','):
                        if '=' in t:
                            ret+=setRet('args',t.split('=')[0])
                            ret+=setRet('operador','=')
                            if t[-1]!='=' :
                                ret=formato(t.split('=')[-1],ret)

                elif ('=' not in k):
                    pass
                if ('(' not in k):
                    pass
                if ('(' not in k) and (',' not in k):
                    pass
            for k in text.split(' '):
                k=k.split()
                grupo=''
                for g in self.grupos:
                    if k in self.grupos[g]:
                        grupo=g
                        ret+=setRet(g,k)
                
                if grupo=='definicion' and '(' in k:
                    name=k[:k.index('(')]
                    ret+=setRet('BlockName',name)
                    ret+=setRet('fc','(')
                    arg=k[k.index('(')+1:]
                    if arg:
                        ret=formato(arg,ret)
                elif (grupo!='definicion') and ('(' in k) and (',' in k):
                    name=k[:k.index('(')].split('.')[-1]
                    prefijo=k[:k.index('.'+name+'(')]

                elif grupo!='definicion' and '(' in k:
                    name=k[:k.index('(')].split('.')[-1]
                    prefijo=k[:k.index('.'+name+'(')]
                    ret+=setRet('fc',prefijo)
                    ret+=setRet('BlockCall',name)
                    ret+=setRet('fc','(')
                    arg=k[k.index('(')+1:]
                    if arg:
                        ret=formato(arg,ret)
                ret+=setRet('fc',' ')
            return ret
        #string=string.strip()
        codigo=''
        for c in line:
            if c == string and n:
                n-=1
                ret=formato(codigo,ret)
            elif c in ['"',"'"] and n==0:
                n=1
                string=c
            if n==0: codigo+=c
        codigo=None
        cu.create_text(xplace+int(ancho/2), yplace+int(alto/2),fill=fontColor,font=(fontType,fontSize), text=str(text))
    def ShowScript(self,lista=[],pwd=''):
        show=[]
        if lista:
            show=lista
        elif pwd:
            show=self.root.getFile(pwd)
        for l in range(len(show)):
            print(show[l])
            self.root_frame_canvas.create_text(
                int(self.stringWidth(show[l])/2)+50, 
                (l*15)+50,
                fill=self.fontColor,
                font=(self.fontType,self.fontSize), 
                text=show[l]
                )
class GUI(object,):
    """
        Clase de una GUI basado en Tkinter para crear y editar una GUI SIMPLE, 
        y posiblemente se pueda exportar una version .html con la logica en javascript 
        en un .js y sus estilos en un .css 
    """
    def __init__(self,bbdd={},AppName='No Hay Titulo...',comandos={},dbname='',tablas={},reset=0,pwd=os.getcwd(),**kwargs):
        self.pwd=pwd
        self.tablas={
            'atributos':["clave TEXT","valor TEXT"],
            'inputType':["clave TEXT","valor TEXT"],
            'Vars':["clave TEXT","valor TEXT"]
            }
        if tablas:
            for clave in tablas:
                self.tablas.setdefault(clave,tablas[clave])
        if bbdd:
            self.Sql=bbdd
        else:
            self.Sql=CRUD(sqlite3, self.tablas, query=query_sqLite3, campoAutoincrement='id', reset=reset,dbname=dbname)
        self.variablesEnSql=[]
        self.gitignore=[]
        self.menus={}
        self.Vars={}
        if reset:
            print(os.getcwd())
            import myVars as externo
            self.INPUTS_CONFIG=self.crearVariable("inputType",externo.inputsDefault)
            self.atrb=self.crearVariable("atributos",externo.atributos)
            del (externo)
            for tabla in self.tablas:
                if not tabla in self.Sql.tablas:
                    self.Sql.CrearTabla(tabla,self.tablas[tabla])
                    #print(tabla)
            #print(self.Sql.tablas)
        else:
            self.INPUTS_CONFIG=self.recuperarVariable("inputType")
            self.atrb=self.recuperarVariable("atributos")
        self.atrb['bbdd']=self.Sql.dbname
        self.atrb['campoAutoincrement']=self.Sql.campoID
        
        #lista de los widgetType que son creados automaticamente por y para esta clase al momento de declara un objeto de esta clase
        self.defaultWidgets=['Tk','myFrame','scrollCanvas','myCanvas','scrollbar','panel','Frame']
        #widgets que seran conectados automaticamente a variables de tipo IntVar(),StringVar(),DoubleVar(),BooleanVar()
        self.widgetConectadoaVars=['Radiobutton','Checkbutton','Entry']
        #Contendra todos los widgets tkinter, canvas, ttk, etc.
        #Cada elemento del diccionario, contendra el widget y todas las informaciones adicionales para poder configurar y manipular el widget
        self.widgets={}
        self.widgets.setdefault(
            'tk',
            {
                'widget':Tk(),
                'inputType':'Tk'
            }
        )
        self.widgets.setdefault('myFrame',{
                'widget':FrameScroll(
                    self.widgets['tk']['widget'],
                    bg=self.atrb['fondo'],**kwargs
                    ),
                'inputType':'myFrame'
                })
        #print(buscarFunciones("dictFunciones.py"))
        self.clickDerecho=[
            [0,500,0,500,"pruebaClickDerecho"]
            ]
        self.clickIzquierdo=[
            [0,500,0,500,"pruebaClickIzquierdo"]
            ]
        self.clickRueda=[
            [0,500,0,500,"pruebaClickRueda"]
            ]

        self.defaultCommand={
            'GUI_destroy':{'inputType':'Button','command':'GUI_destroy','text':'Salir'},
            'GUI_Aceptar':{'inputType':'Button','command':'GUI_Aceptar','text':'ACEPTAR'},
            'GUI_Guardar':{'inputType':'Button','command':'GUI_Guardar','text':'GUARDAR'},
            'GUI_Borrar':{'inputType':'Button','command':'GUI_Borrar','text':'BORRAR'},
            'GUI_Leer':{'inputType':'Button','command':'GUI_Leer','text':'Leer'},
            'GUI_Exportar_PY':{'inputType':'Button','command':'GUI_Exportar_PY','text':'Exportar a '+self.atrb['titulo']+'.py'},
            'GUI_Exportar_CSV':{'inputType':'Button','command':'GUI_Exportar_CSV','text':'Exportar a '+self.atrb['titulo']+'.csv'}
            }
        self.command={
            'GUI_destroy':lambda : self.widgets['tk']['widget'].destroy(),
            'GUI_Aceptar':lambda : print('Aceptar ',self.atrb['frameActivo']),
            'GUI_Guardar':lambda : self.comandoGuardar(),
            'GUI_Borrar':lambda : print('Borrar ',self.widgets['tk']['text']),
            'GUI_Leer':lambda : self.comandoLeer(),
            'GUI_Exportar_PY':lambda : self.comandoExportar(campoClave='id',file='',formato='.py',tabla=[]),
            'GUI_Exportar_CSV':lambda : self.comandoExportar(campoClave='id',file='',formato='.csv',tabla=[])
            }
        if comandos:
            for clave in comandos:
                self.command.setdefault(clave,comandos[clave])
    def title(self,titulo):
        self.atrb['titulo']=titulo
        self.widgets['tk']['widget'].title(self.atrb['titulo'])
    def loop(self):
        self.update()
        self.widgets['tk']['widget'].update()
        self.widgets['tk']['widget'].mainloop()
    def updateVar(self,name,arg2,mod):
        #print(name,arg2,mod)
        nombreSinPadre=name.replace(self.widgets[name]['padre']+'_','')
        if self.widgets[name]['inputType'] in ['Radiobutton']:
            ok_name=nombreSinPadre.replace('_'+nombreSinPadre.split('_')[-1],'')
        else:
            ok_name=nombreSinPadre
        self.widgets[self.widgets[name]['padre']]['value'][ok_name]=self.Vars[name].get()    
    def setVar(self,name,values={}):
        myVars=[]
        if self.widgets[name]['inputType'] in ['Frame','panel']:
            for w in self.widgets:
                if (self.widgets[w]['inputType'] not in self.defaultWidgets):
                    if (self.widgets[w]['padre'] == name) and (self.widgets[w]['inputType'] in self.widgetConectadoaVars):
                        myVars += [w]
            for buscar in [w for w in myVars if (self.widgets[w]['inputType'] in ['Radiobutton'])]:    
                    if buscar in self.Vars:
                        for v in values:
                            if str(name+'_'+v) in buscar:
                                self.Vars[buscar].set(values[v])
            for v in values:
                if str(name+'_'+v) in self.Vars:
                    self.Vars[name+'_'+v].set(values[v])
            if not values:
                for v in myVars:
                    if v in self.Vars:
                        self.Vars[v].set(self.INPUTS_CONFIG[self.widgets[v]['inputType']]['value'])
    def onkey(self,event):
        #print(event)
        pass
    def onclick(self,event):
        for w in self.widgets:
            if self.widgets[w]['widget']==event.widget:
                name = w
            if 'canvas' in self.widgets[w]:
                if self.widgets[w]['canvas']==event.widget:
                    name = w
        if name=='canvas':
            xReal=event.x
            yReal=event.y
        else:
            hijo=name
            padre=self.widgets[name]['padre']
            while padre!='tk':
                if 'padre' in self.widgets[hijo]['padre']:
                    padre=self.widgets[hijo]['padre']
                if self.widgets[hijo]['inputType'] in self.defaultWidgets:
                    padre='tk'
                else:
                    hijo=padre           
            #print('name:',name,'hijo:',hijo,'padre:',padre)
            xReal=int(self.widgets[hijo]['xPlace']+event.x)
            yReal=int(self.widgets[hijo]['yPlace']+event.y)
        #print(xReal,yReal)
        #print(event.x,event.y,event.state,event.num,event.widget)
        if '1'==event.num:
            for area in self.clickIzquierdo:
                if (area[0]<=event.x<=area[1]) and (area[2]<=event.y<=area[3]):
                    threading.Thread(target=self.command[area[-1]][0],args=self.command[area[-1]][1]).start()
        elif '2'==event.num:
            for area in self.clickRueda:
                if (area[0]<=event.x<=area[1]) and (area[2]<=event.y<=area[3]):
                    threading.Thread(target=self.command[area[-1]][0],args=self.command[area[-1]][1]).start()
        elif '3'==event.num:
            for area in self.clickDerecho:
                if (area[0]<=event.x<=area[1]) and (area[2]<=event.y<=area[3]):
                    threading.Thread(target=self.command[area[-1]][0],args=self.command[area[-1]][1]).start()
    def responsive(self,event):
        self.widgets['tk']['widget'].update()
        if (self.atrb['alto'] != self.widgets['tk']['widget'].winfo_height()) or (self.atrb['ancho']!= self.widgets['tk']['widget'].winfo_width()):
            self.atrb['alto'] = self.widgets['tk']['widget'].winfo_height()
            self.atrb['ancho']= self.widgets['tk']['widget'].winfo_width()
            self.update()
    def recuperarVariable(self,nombreVariable):
        #funcion que recupera variables de una tabla y los retorna como una variable original de este clase
        ret={}
        dictReturn=self.Sql.SelectAll(nombreVariable,typeSalida='dict',campoClave='clave')
        if nombreVariable in self.tablas:
            for clave in dictReturn:
                ret.setdefault(dictReturn[clave]['clave'],dictReturn[clave]['valor'])
        return ret
    def crearVariable(self,nombreVariable,variables):
        #nombreVariable: nombre de la variable en el programa
        #variables: variable tipo diccionario sera guardada en una tabla, y el nombre de la tabla sera 'nombreVariable'
        self.tablas.setdefault(nombreVariable,["clave TEXT","valor TEXT"])
        self.variablesEnSql+=[nombreVariable]
        self.Sql.CrearTabla(nombreVariable,self.tablas[nombreVariable])
        for clave in variables:
            self.Sql.Cargar(nombreVariable,self.tablas[nombreVariable],[clave, variables[clave] ])
        ret={}
        dictReturn=self.Sql.SelectAll(nombreVariable,typeSalida='dict',campoClave='clave')
        for clave in dictReturn:
            ret.setdefault(dictReturn[clave]['clave'],dictReturn[clave]['valor'])
        return ret
    def guardarVariable(self,nombreVariable,variables):
        for clave in variables:
            self.Sql.Cargar(nombreVariable,self.tablas[nombreVariable],[clave, variables[clave]]) 
    def update(self):
        self.widgets['tk']['widget'].geometry(f"{self.atrb['ancho']}x{self.atrb['alto']}")
        #print("update")
        #self.widgets['myFrame']['widget'].config(width = self.atrb['ancho'], height = self.atrb['alto'])
        #self.widgets['canvas']['widget'].config(width = self.atrb['ancho'], height = self.atrb['alto'])
        self.margenSuperior=0
        self.margenInferior=0
        self.margenIzquierdo=0
        self.margenDerecho=0
        espasioAlfinal=100
        altoTotal=0
        anchoTotal=0
        sandwishSuperior=[]
        sandwishInferior=[]
        sandwishDerecho=[]
        sandwishIzquierdo=[]
        #actualizamos los parametros 'command' de los widgets
        for w in self.widgets:
            if self.widgets[w]['inputType']=='Button':            
                self.widgets[w]['widget'].config(
                    command=self.command[self.widgets[w]['command']],
                    text=self.widgets[w]['text'],
                    width=self.widgets[w]['width'] if self.widgets[w]['width'] else None,
                    bg=self.widgets[w]['bgColor'],
                    fg=self.widgets[w]['fontColor'],
                    font=(self.widgets[w]['fontType'],self.widgets[w]['fontSize'])
                    )
            elif self.widgets[w]['inputType'] in ['Label','Checkbutton','Radiobutton']:
                self.widgets[w]['widget'].config(
                    text=self.widgets[w]['text'],
                    bg=self.widgets[w]['bgColor'],
                    fg=self.widgets[w]['fontColor'],
                    font=(self.widgets[w]['fontType'],self.widgets[w]['fontSize'])
                    )
            elif self.widgets[w]['inputType'] in ['Entry']:
                self.widgets[w]['widget'].config(
                    bg=self.widgets[w]['bgColor'],
                    width=self.widgets[w]['width'] if self.widgets[w]['width'] else None,  
                    fg=self.widgets[w]['fontColor'],
                    insertbackground=self.widgets[w]['fontColor'],
                    font=(self.widgets[w]['fontType'],self.widgets[w]['fontSize'])
                    )
                #self.widgets[w]['padre']+self.widgets[w]['']
                #[self.widgets[w]['name']+'_LabelCanvas']
                if self.widgets[w]['name']+'_LabelCanvas' in self.widgets[self.widgets[w]['padre']]['inputs']:
                    self.widgets[self.widgets[w]['padre']]['inputs'][self.widgets[w]['name']+'_LabelCanvas']['xPlace']=self.widgets[w]['xPlace']
                    self.widgets[self.widgets[w]['padre']]['inputs'][self.widgets[w]['name']+'_LabelCanvas']['yPlace']=self.widgets[w]['yPlace']
                    self.widgets[self.widgets[w]['padre']]['inputs'][self.widgets[w]['name']+'_LabelCanvas']['ancho']=self.anchoWidget(self.widgets[w])
                    self.widgets[self.widgets[w]['padre']]['inputs'][self.widgets[w]['name']+'_LabelCanvas']['alto']=self.altoWidget(self.widgets[w])*0.5
                    self.widgets[self.widgets[w]['padre']]['inputs'][self.widgets[w]['name']+'_LabelCanvas']['fontSize']=int(self.widgets[w]['fontSize']*0.7)
                    self.widgets[self.widgets[w]['padre']]['inputs'][self.widgets[w]['name']+'_LabelCanvas']['fontType']=self.widgets[w]['fontType']
                    self.widgets[self.widgets[w]['padre']]['inputs'][self.widgets[w]['name']+'_LabelCanvas']['fontColor']=self.widgets[w]['fontColor']
                    self.widgets[self.widgets[w]['padre']]['inputs'][self.widgets[w]['name']+'_LabelCanvas']['bgColor']=self.widgets[w]['bgColor']
                    self.widgets[self.widgets[w]['padre']]['inputs'][self.widgets[w]['name']+'_LabelCanvas']['text']=self.widgets[w]['text']
                            
        #calculamos espacios de los margenes que necesitaremos para ubicar en ellos los paneles laterales, superiores, inferiores
        for myWidget in self.widgets:
            if self.widgets[myWidget]['inputType']=='panel' and self.widgets[myWidget]['visible']:
                self.margenDerecho +=  ((11-self.widgets[myWidget]['fontSize'])+(self.widgets[myWidget]['width']+1)*(self.widgets[myWidget]['fontSize']-1)+(self.widgets[myWidget]['width']*self.atrb['fontSizeToCorrectorAncho'][self.widgets[myWidget]['fontType']][self.widgets[myWidget]['fontSize']])) if ('e'==self.widgets[myWidget]['anchor'][0]) else 0 
                self.margenIzquierdo +=  ((11-self.widgets[myWidget]['fontSize'])+(self.widgets[myWidget]['width']+1)*(self.widgets[myWidget]['fontSize']-1)+(self.widgets[myWidget]['width']*self.atrb['fontSizeToCorrectorAncho'][self.widgets[myWidget]['fontType']][self.widgets[myWidget]['fontSize']])+self.atrb['scrollVerticalAncho']) if ('o'==self.widgets[myWidget]['anchor'][0]) else 0 
                self.margenSuperior += (self.atrb['fontSizeToAlto'][self.widgets[myWidget]['fontType']][self.widgets[myWidget]['fontSize']]) if ('n'==self.widgets[myWidget]['anchor'][0]) else 0 
                self.margenInferior += self.atrb['scrollHorizontalAlto']+(self.atrb['fontSizeToAlto'][self.widgets[myWidget]['fontType']][self.widgets[myWidget]['fontSize']]) if ('s'==self.widgets[myWidget]['anchor'][0]) else 0

        for myWidget in self.widgets:
            if self.widgets[myWidget]['inputType'] in ['Frame','panel']:
                if self.widgets[myWidget]['visible']:
                    #menus[myWidget]={'anchor':self.widgets[myWidget]['anchor'],'':self.widgets[myWidget]['']}
                    #hallamos el espacio total en X y Y que ocuaran todos los widget dentro del 'frame' o 'panel'
                    ySuma,xSuma=0,0
                    for w in self.widgets:
                        if (self.widgets[w]['inputType'] not in self.defaultWidgets):
                            if (self.widgets[w]['padre'] == myWidget):
                                posicionfinalenY=self.widgets[w]['yPlace']+self.widgets[w]['alto']+self.atrb['scrollHorizontalAlto']+self.margenSuperior + espasioAlfinal
                                ySuma = posicionfinalenY if posicionfinalenY > ySuma else ySuma

                                posicionfinalenX=self.widgets[w]['xPlace']+self.widgets[w]['ancho']+self.atrb['scrollVerticalAncho']+self.margenIzquierdo
                                xSuma = posicionfinalenX if posicionfinalenX > xSuma else xSuma
                    
                    if self.widgets[myWidget]['inputType'] in ['Frame']:
                        self.widgets[myWidget]['ancho'] =(self.atrb['ancho'])-self.margenIzquierdo-self.margenDerecho
                        self.widgets[myWidget]['alto'] = ySuma
                        self.widgets[myWidget]['yPlace'] = self.margenSuperior
                        self.widgets[myWidget]['xPlace'] = self.margenIzquierdo 
                        self.atrb['frameActivo']=myWidget

                        if ySuma>altoTotal:
                            altoTotal=ySuma
                            #print(self.margenSuperior,self.margenInferior,self.margenIzquierdo,self.margenDerecho)
                            #print(ySuma,self.atrb['alto'])
                        if self.widgets['myFrame']['widget'].winfo_height()<altoTotal:
                            self.widgets['myFrame']['widget'].config(width=self.atrb['ancho'],height=altoTotal,bg=self.widgets[myWidget]['bgColor'])
                        if self.widgets['myFrame']['widget'].winfo_height()>self.widgets[myWidget]['alto']:
                            self.widgets['myFrame']['widget'].config(width=self.atrb['ancho'],height=self.atrb['alto'],bg=self.widgets[myWidget]['bgColor'])

                    if self.widgets[myWidget]['inputType'] in ['panel']:
                        self.widgets[myWidget]['ancho'] = ((11-self.widgets[myWidget]['fontSize'])+(self.widgets[myWidget]['width']+1)*(self.widgets[myWidget]['fontSize']-1)+(self.widgets[myWidget]['width']*self.atrb['fontSizeToCorrectorAncho'][self.widgets[myWidget]['fontType']][self.widgets[myWidget]['fontSize']])) if (('e'==self.widgets[myWidget]['anchor'][0]) or ('o'==self.widgets[myWidget]['anchor'][0])) else (self.atrb['ancho']-self.atrb['scrollVerticalAncho'])
                        self.widgets[myWidget]['alto'] = self.atrb['alto']-self.margenInferior-self.margenSuperior-self.atrb['scrollHorizontalAlto'] if (('e'==self.widgets[myWidget]['anchor'][0]) or ('o'==self.widgets[myWidget]['anchor'][0])) else (self.atrb['fontSizeToAlto'][self.widgets[myWidget]['fontType']][self.widgets[myWidget]['fontSize']])
                        self.widgets[myWidget]['yPlace']= self.margenSuperior if (('e'==self.widgets[myWidget]['anchor'][0]) or ('o'==self.widgets[myWidget]['anchor'][0])) else (self.atrb['alto']-self.widgets[myWidget]['alto']-self.atrb['scrollHorizontalAlto']-sum([self.widgets[ocupa]['alto'] for ocupa in sandwishInferior]) if ('s'==self.widgets[myWidget]['anchor'][0]) else sum([self.widgets[ocupa]['alto'] for ocupa in sandwishSuperior]))
                        self.widgets[myWidget]['xPlace']= 0 if (('n'==self.widgets[myWidget]['anchor'][0]) or ('s'==self.widgets[myWidget]['anchor'][0])) else (self.atrb['ancho']-self.widgets[myWidget]['ancho']-self.atrb['scrollVerticalAncho']-sum([self.widgets[ocupa]['ancho'] for ocupa in sandwishDerecho]) if ('e'==self.widgets[myWidget]['anchor'][0]) else sum([self.widgets[ocupa]['ancho'] for ocupa in sandwishIzquierdo]))
                        if ('n'==self.widgets[myWidget]['anchor'][0]):
                            sandwishSuperior += [myWidget]
                        elif ('s'==self.widgets[myWidget]['anchor'][0]): 
                            sandwishInferior += [myWidget]
                        elif ('e'==self.widgets[myWidget]['anchor'][0]): 
                            sandwishDerecho += [myWidget]
                        elif ('o'==self.widgets[myWidget]['anchor'][0]): 
                            sandwishIzquierdo += [myWidget]
                    if (self.widgets[myWidget]['ancho']!=self.widgets[myWidget]['widget'].winfo_width()) or (self.widgets[myWidget]['alto']!=self.widgets[myWidget]['widget'].winfo_height()) or (not (self.widgets[myWidget]['widget'].place_info())):
                        self.widgets[myWidget]['widget'].config(width=self.widgets[myWidget]['ancho'],height=self.widgets[myWidget]['alto'],bg=self.widgets[myWidget]['bgColor'])
                        self.widgets[myWidget]['canvas'].config(width=self.widgets[myWidget]['ancho'],height=self.widgets[myWidget]['alto'],bg=self.widgets[myWidget]['bgColor'])
                        if not (self.widgets[myWidget]['widget'].place_info()):
                            self.widgets[myWidget]['canvas'].place(x=0, y=0)
                        #gradient(poligono=[],x=0,y=0,height=0,width=0,rotacion=0,color1='#ffffff',color2='#000000')
                        if self.widgets[myWidget]['degradado']:
                            for line in gradient(width=self.widgets[myWidget]['ancho'],height=self.widgets[myWidget]['alto'],color1=self.widgets[myWidget]['bgColor'],color2=escalarHex(h=self.widgets[myWidget]['bgColor'],factor=0.05)):
                                self.widgets[myWidget]['canvas'].create_line(line[0],line[1],line[2],line[3],fill=line[4])
                        for w in self.widgets[myWidget]['inputs']:
                            if self.widgets[myWidget]['inputs'][w]['inputType'] in ['LabelCanvas']:
                                self.widgets[myWidget]['canvas'].create_text(
                                    self.widgets[myWidget]['inputs'][w]['xPlace']+(self.widgets[myWidget]['inputs'][w]['ancho']/2),
                                    self.widgets[myWidget]['inputs'][w]['yPlace']-(self.widgets[myWidget]['inputs'][w]['alto']/2),
                                    fill=self.widgets[myWidget]['inputs'][w]['fontColor'],
                                    font=(self.widgets[myWidget]['inputs'][w]['fontType'],self.widgets[myWidget]['inputs'][w]['fontSize']), 
                                    text=self.widgets[myWidget]['inputs'][w]['text']
                                )
                    self.widgets[myWidget]['widget'].place(x=self.widgets[myWidget]['xPlace'],y=self.widgets[myWidget]['yPlace'])
                        
                        
                    #self.widgets[myWidget]['canvas'].config(width=self.widgets[myWidget]['ancho'],height=self.widgets[myWidget]['alto'],bg=self.widgets[myWidget]['bgColor'])
                    #self.widgets[myWidget]['canvas'].place(x=0, y=0)
                else:
                    self.widgets[myWidget]['widget'].place_forget()
                    print(myWidget,'place_forget')
                
        for myWidget in self.widgets:
            if (self.widgets[myWidget]['inputType'] not in self.defaultWidgets):
                self.widgets[myWidget]['widget'].place(x=self.widgets[myWidget]['xPlace'],y=self.widgets[myWidget]['yPlace'])
        self.widgets['tk']['widget'].update()

    def anchoWidget(self,w):
        #calcula el ancho del widget en pixeles
        return int( (11-w['fontSize']) + ((w['width']+1)*(w['fontSize']-1)) + (w['width']*self.atrb['fontSizeToCorrectorAncho'][w['fontType']][w['fontSize']]) )
    def altoWidget(self,w):
        #calcula el alto del widget en pixeles
        return self.atrb['fontSizeToAlto'][w['fontType']][w['fontSize']]
    def comandoGuardar(self):
            if self.widgets[self.atrb['frameActivo']]['crearTabla']:
                print(self.atrb['frameActivo'],self.tablas[self.atrb['frameActivo']][1:],[self.widgets[self.atrb['frameActivo']]['value'][v.split(' ')[0]] for v in self.tablas[self.atrb['frameActivo']][1:]] )
                self.Sql.Cargar(self.atrb['frameActivo'],self.tablas[self.atrb['frameActivo']][1:],[self.widgets[self.atrb['frameActivo']]['value'][v.split(' ')[0]] for v in self.tablas[self.atrb['frameActivo']][1:]] ,dirCRUD=self.pwd+os.path.sep+self.atrb['transicion']+os.path.sep+self.atrb['transicion']+self.Sql.extencionCRUD)
                self.setVar(self.atrb['frameActivo'])
    def comandoLeer(self,campoClave='id'):
                if self.widgets[self.atrb['frameActivo']]['crearTabla']:
                    if [1 for ok in self.atrb['subtransicion']['aceptar'] if (ok in self.widgets[self.atrb['frameActivo']]['etiquetas'])]:
                        print(self.Sql.SelectAll(self.atrb['frameActivo'],typeSalida='dict',campoClave=campoClave,dirCRUD=self.pwd+os.path.sep+self.atrb['transicion']+os.path.sep+self.atrb['transicion']+self.Sql.extencionCRUD))
                        #self.setVar(w)
    def comandoExportar(self,campoClave='id',file='',formato='',tabla=[]):
        if self.widgets[self.atrb['frameActivo']]['crearTabla']:
            self.Sql.exportarTablas(
                tabla=[self.atrb['frameActivo']],
                formato=formato,
                campoClave=campoClave,
                file=self.pwd+os.path.sep+self.atrb['transicion']+os.path.sep+self.atrb['titulo'],
                dirCRUD=self.pwd+os.path.sep+self.atrb['transicion']+os.path.sep+self.atrb['transicion']+self.Sql.extencionCRUD
                )
            #self.setVar(w)
    def SetTkWidget(self,myWidget):
        if myWidget['inputType']=='Button':
            myWidget['widget']=Button(
                self.widgets[myWidget['padre']]['widget'],
                text=myWidget['text'],
                width=myWidget['width'] if myWidget['width'] else None,
                bg=myWidget['bgColor'],
                fg=myWidget['fontColor'],
                font=(myWidget['fontType'],myWidget['fontSize']),
                command=self.command[myWidget['command']]
                )
            myWidget['ancho']=self.anchoWidget(myWidget)
            myWidget['alto']=self.altoWidget(myWidget)
            self.widgets.setdefault(myWidget['name'],myWidget)
        elif myWidget['inputType']=='Label':
            myWidget['widget']=Label(
                self.widgets[myWidget['padre']]['widget'], 
                text=myWidget['text'],
                bg=myWidget['bgColor'],
                fg=myWidget['fontColor'],
                font=(myWidget['fontType'],myWidget['fontSize']))
            myWidget['ancho']=self.anchoWidget(myWidget)
            myWidget['alto']=self.altoWidget(myWidget)
            self.widgets.setdefault(myWidget['name'],myWidget)
        elif myWidget['inputType']=='LabelCanvas':
            self.widgets[myWidget['padre']]['canvas'].create_text(
                myWidget['xPlace']+(myWidget['ancho']/2),
                myWidget['yPlace']+(myWidget['alto']/2),
                fill=myWidget['fontColor'],
                font=(myWidget['fontType'],myWidget['fontSize']), 
                text=myWidget['text']
                )
        elif myWidget['inputType']=='Entry':
            TypeVar = {'str':0,'correo':0,'date':0,'nombre':0,'int':1,'edad':1,'float':2,'moneda':2,'magnitud':2,'Boolean':3,'bool':3}
            inputVar = [
                [StringVar,str],
                [IntVar,lambda x : int(flot(x))],
                [DoubleVar,float],
                [BooleanVar,bool]
                ]
            print(next(( k for k in TypeVar if k == myWidget['typeSalida'] ), 0))
            TypeVar=next(( inputVar[TypeVar[k]] for k in TypeVar if k == myWidget['typeSalida'] ), inputVar[0])
            self.Vars[myWidget['name']]=TypeVar[0](
                value=TypeVar[1](myWidget['value']),
                name=myWidget['name']
                )
            myWidget['widget']=Entry(
                self.widgets[myWidget['padre']]['widget'], 
                textvariable=self.Vars[myWidget['name']],
                width=myWidget['width'] if myWidget['width'] else None,  
                fg=myWidget['fontColor'],
                insertbackground=myWidget['fontColor'],
                bg=myWidget['bgColor'],
                font=(myWidget['fontType'],myWidget['fontSize'])
                )
            self.Vars[myWidget['name']].trace('w',lambda name,arg2,mod : self.updateVar(name,arg2,mod))
            self.widgets.setdefault(myWidget['name'],myWidget)
            self.updateVar(myWidget['name'],' ','w')
        elif myWidget['inputType']=='Checkbutton':
            if not 'value' in myWidget:
                myWidget['value']=''
            self.Vars[myWidget['name']]=BooleanVar(value=bool(myWidget['value']),name=myWidget['name'])
            
            myWidget['widget']=Checkbutton(
                self.widgets[myWidget['padre']]['widget'], 
                text=myWidget['text'],
                bg=myWidget['bgColor'],
                fg=myWidget['fontColor'], 
                variable=self.Vars[myWidget['name']],
                font=(myWidget['fontType'],myWidget['fontSize'])
                )
            self.Vars[myWidget['name']].trace('w',lambda name,arg2,mod : self.updateVar(name,arg2,mod))
            myWidget['ancho']=self.anchoWidget(myWidget)
            myWidget['alto']=self.altoWidget(myWidget)
            self.widgets.setdefault(myWidget['name'],myWidget)
            self.updateVar(myWidget['name'],' ','w')
        elif myWidget['inputType']=='Radiobutton':
            p=myWidget['name']+'_'+[k for k in myWidget['radios']][0]
            #print([k for k in myWidget['radios']][0],p)
            self.Vars[p]=StringVar(value=str(myWidget['value']),name=p)
            x , y = 0 , 0
            if 'text' in myWidget:
                self.SetWidget(
                    atributos={
                        'inputType':'Label',
                        'padre':myWidget['padre'],
                        'name':myWidget['name']+'_Label',
                        'xPlace':myWidget['xPlace']+x,
                        'yPlace':myWidget['yPlace']+y,
                        'ancho':self.anchoWidget(myWidget),
                        'alto':self.altoWidget(myWidget),
                        'fontSize':myWidget['fontSize'],
                        'fontType':myWidget['fontType'],
                        'fontColor':myWidget['fontColor'],
                        'bgColor':myWidget['bgColor'],
                        'text':myWidget['text']
                        }
                    )
            x=self.atrb['fontSizeToAlto'][myWidget['fontType']][myWidget['fontSize']]
            #Creamos la lista de objetos Widget RadioButton()
            if 'radios' in myWidget:
                for r in myWidget['radios']:
                    y += (self.atrb['fontSizeToAlto'][myWidget['fontType']][myWidget['fontSize']])
                    myWidget['radios'][r]['inputType']=myWidget['inputType']
                    myWidget['radios'][r]['padre']=myWidget['padre']
                    myWidget['radios'][r]['name']=myWidget['name']+'_'+str(r)
                    myWidget['radios'][r]['xPlace']=myWidget['xPlace']+x
                    myWidget['radios'][r]['yPlace']=myWidget['yPlace']+y
                    myWidget['radios'][r]['bgColor']=myWidget['bgColor']
                    myWidget['radios'][r]['fontColor']=myWidget['fontColor']
                    myWidget['radios'][r]['fontType']=myWidget['fontType']
                    myWidget['radios'][r]['fontSize']=myWidget['fontSize']
                    myWidget['radios'][r]['ancho']=self.anchoWidget(myWidget)
                    myWidget['radios'][r]['alto']=self.altoWidget(myWidget)
                    #Instansiando 'Un' objeto Widget RadioButton()
                    myWidget['radios'][r]['widget']=Radiobutton(
                        self.widgets[myWidget['padre']]['widget'], 
                        text=myWidget['radios'][r]['text'],
                        bg=myWidget['radios'][r]['bgColor'],
                        fg=myWidget['radios'][r]['fontColor'], 
                        variable=self.Vars[p],
                        value=r,
                        font=(myWidget['radios'][r]['fontType'],myWidget['radios'][r]['fontSize']))
                    #le asignamos el comando desde 'self.command'
                    if 'command' in myWidget['radios'][r]:
                        myWidget['radios'][r]['widget'].config(command=self.command[myWidget['radios'][r]['command']])
                    self.widgets.setdefault(myWidget['radios'][r]['name'],myWidget['radios'][r])
            self.Vars[p].trace('w',lambda name,arg2,mod : self.updateVar(name,arg2,mod))
            #myWidget['ancho']=((11-myWidget['fontSize'])+(myWidget['width']+1)*(myWidget['fontSize']-1)+(myWidget['width']*self.atrb['fontSizeToCorrectorAncho'][myWidget['fontType']][myWidget['fontSize']]))
            #myWidget['alto']=(self.atrb['fontSizeToAlto'][myWidget['fontType']][myWidget['fontSize']])
            #self.widgets.setdefault(myWidget['name'],myWidget)
            self.updateVar(p,' ','w')
    def SetWidget(self,atributos={}):
        myCommand={}
        #Combinamos el conjunto de datos que resive esta funcion en el parametro 'atributos', con el conjunto de datos que ya tenemos Predefenidos en 'myVars.py'
        if atributos['inputType'] != self.INPUTS_CONFIG:
            myWidget = { k:ret[k] for ret in [self.INPUTS_CONFIG[atributos['inputType']],atributos] for k in ret }
            if 'padre' in myWidget:
                if not myWidget['padre']:
                    myWidget['padre']='myFrame'
            else:
                myWidget['padre']='myFrame'
        else:
           myWidget={'inputType':'' }

        """
            esta parte del codigo genera el 'Frame Tkinter' los inputs y outputs dentro de este
            A cada 'Frame  Tkinter' se le asignara un widget padre que le heredara el comportamiento deseado,
            los widget padre solo son 'tk' y 'myFrame', estos widget son declarados en la funcion __init__ de esta clase,
            COMPORTAMIENTOS:
            'tk' es el objeto Tk() de tkinter, y sus hijos se comportaran de forma ESTATICA dentro del programa, los hijos de 'tk' no se mueven o desplazan dentro de la ventana del Programa, o sea no seran controlados por las 'barras de desplazamiento'(Scrollbar)
            'myFrame' es el Frame() de tkinter, pero esta 'posicionado' dentro de un 'Canvas()' que este a su ves es controlado por las 'barras de desplazamiento'(Scrollbar), y los hijos de 'myFrame' tambien seran controlados por las 'barras de desplazamiento'(Scrollbar)
            POSICIONAMIENTO:
            'tk' sera el padre del 'Frame Tkinter' si le pasamos inputType='panel', y los hijos de 'Frame Tkinter' seran posicionados con .place(x=posicion real en pantalla,y=posicion real en pantalla)
            'myframe' sera el padre del 'Frame Tkinter' si le pasamos inputType='Frame', como 'myFrame' puede tener una dimencion deferente de 'tk', este debe posicionar los widgets dentro del 'Frame Tkinter' calculando su posicion dentro 'myFrame'
        """
        if myWidget['inputType'] in ['Frame','panel']:
            if myWidget['inputType']=='Frame':
                myWidget['widget']=Frame(
                    self.widgets['myFrame']['widget'], 
                    width=myWidget['ancho'], 
                    height=myWidget['alto'],
                    bd=0,
                    highlightthickness=0
                    )
                myWidget['padre']='myFrame'
            if myWidget['inputType']=='panel':
                myWidget['widget']=Frame(
                    self.widgets['tk']['widget'], 
                    width=myWidget['ancho'], 
                    height=myWidget['alto'],
                    bg=myWidget['bgColor']
                    )
                myWidget['padre']='tk'
            
            myWidget['canvas']=Canvas(myWidget['widget'],bd=0,highlightthickness=0)
            myWidget['value']={}
            self.widgets.setdefault(myWidget['name'],myWidget)
            if 'inputs'in myWidget:
                inputs={}
                x,y=0,0
                saltoX,saltoY=0,0
                if 'text' in myWidget:
                    inputs[myWidget['name']+'_Label']={
                        'inputType':'Label',
                        'padre':myWidget['name'],
                        'name':myWidget['name']+'_Label',
                        'xPlace':x,
                        'yPlace':y,
                        'ancho':self.anchoWidget(myWidget),
                        'alto':self.altoWidget(myWidget)*0.3+2,
                        'fontSize':int(myWidget['fontSize']),
                        'fontType':myWidget['fontType'],
                        'fontColor':myWidget['fontColor'],
                        'bgColor':myWidget['bgColor'],
                        'text':myWidget['text']}
                    self.SetWidget(atributos=inputs[myWidget['name']+'_Label'])
                for btn in myWidget['inputs']:
                    if saltoX > 0:
                        x += saltoX
                        saltoX=0    
                    else:
                        x += self.anchoWidget(myWidget) if (('n'==myWidget['anchor'][0]) or ('s'==myWidget['anchor'][0])) else 0
                    if saltoY > 0:
                        y += saltoY
                        saltoY=0    
                    else:
                        y += self.altoWidget(myWidget)+self.atrb['espacioVerticalEntreWidgets']
                    myWidget['inputs'][btn].setdefault('name',myWidget['name']+'_'+btn)
                    myWidget['inputs'][btn].setdefault('padre',myWidget['name'])
                    myWidget['inputs'][btn].setdefault('width',myWidget['width'])
                    myWidget['inputs'][btn].setdefault('fontSize',myWidget['fontSize'])
                    myWidget['inputs'][btn].setdefault('fontType',myWidget['fontType'])
                    myWidget['inputs'][btn].setdefault('fontColor',(escalarHex(h=myWidget['fontColor'],factor=1.0/0.9) if myWidget['inputs'][btn]['inputType']=='Entry' else myWidget['fontColor']))
                    myWidget['inputs'][btn].setdefault('bgColor',(escalarHex(h=myWidget['bgColor'],factor=0.9) if myWidget['inputs'][btn]['inputType']=='Entry' else myWidget['bgColor']))
                    myWidget['inputs'][btn].setdefault('fgColor',myWidget['fgColor'])
                    myWidget['inputs'][btn].setdefault('xPlace',x)
                    if myWidget['inputs'][btn]['inputType'] in ['Entry']:
                        myWidget['inputs'][btn].setdefault('yPlace',y+(self.altoWidget(myWidget['inputs'][btn]) if 'text' in myWidget['inputs'][btn] else 0))
                    else:
                        myWidget['inputs'][btn].setdefault('yPlace',y)

                    if myWidget['inputs'][btn]['inputType'] in ['Radiobutton']:
                        myWidget['inputs'][btn]['alto']=self.altoWidget(myWidget['inputs'][btn])*(len(myWidget['inputs'][btn]['radios'])+1)
                        saltoY=myWidget['inputs'][btn]['alto']
                    if myWidget['inputs'][btn]['inputType'] in ['Entry']:
                        myWidget['inputs'][btn]['alto']=self.altoWidget(myWidget['inputs'][btn])*2
                        saltoY=myWidget['inputs'][btn]['alto']
                    
                    self.SetWidget(atributos=myWidget['inputs'][btn])
                    if myWidget['inputs'][btn]['inputType']=='Entry' and ('text' in myWidget['inputs'][btn]) :
                        inputs[myWidget['name']+'_'+btn+'_LabelCanvas']={
                            'inputType':'LabelCanvas',
                            'padre':myWidget['name'],
                            'name':myWidget['name']+'_'+btn+'_LabelCanvas',
                            'xPlace':x,
                            'yPlace':y,
                            'ancho':self.anchoWidget(myWidget),
                            'alto':self.altoWidget(myWidget)*0.3+10,
                            'fontSize':int(myWidget['fontSize']*0.7),
                            'fontType':myWidget['fontType'],
                            'fontColor':myWidget['fontColor'],
                            'bgColor':myWidget['bgColor'],
                            'text':myWidget['inputs'][btn]['text']}
                        #self.SetWidget(atributos=inputs[myWidget['name']+'_'+btn+'_LabelCanvas'])
            self.widgets[myWidget['name']]['inputs']=myWidget['inputs']
            for i in inputs:
                self.widgets[myWidget['name']]['inputs'][i]=inputs[i]
            
        elif myWidget['inputType']=='formIn':
            self.widgets.setdefault(myWidget['name'],myWidget)

        elif myWidget['inputType']=='formOut':
            self.widgets.setdefault(myWidget['name'],myWidget)
        elif myWidget['inputType']!='':
            self.SetTkWidget(myWidget)

        #self.INPUTS_CONFIG=self.recuperarVariable("inputType")
        #print(myWidget['name'],self.widgets[myWidget['name']]['name'])
        if 'crearTabla' in myWidget:
            if (myWidget['crearTabla']) and (not myWidget['name'] in self.tablas):
                campos = [i for i in myWidget['inputs'] if (myWidget['inputs'][i]['inputType'] in self.widgetConectadoaVars) ]
                self.tablas[myWidget['name']]=[self.Sql.campoID]+[campos[0]+' text not null UNIQUE']+campos[1:]
                print(myWidget['name'],self.tablas[myWidget['name']],self.Sql.extencionCRUD)
                print(self.pwd,myWidget['subProyecto'],myWidget['subProyecto'],self.Sql.extencionCRUD)
                self.Sql.CrearTabla(myWidget['name'],self.tablas[myWidget['name']],dirCRUD=self.pwd+os.sep+myWidget['subProyecto']+self.Sql.extencionCRUD)

        del myWidget
def get_style():
    """probar get_style"""
    css=Styles()
    print(css.files)
    css.scan_css()
    css.p(css.files,listar=1)
def GUI_mbarete():
    """prueba del GUI FULL"""
    from extras import widgets
    obj=object_mbarete(
        pwd='media',
        flags=['error','init','acceso_directo'],
        carpetas={
            'dir_media':'mbarete/media/',
            'web_servidor':'mbarete/servidor/'
            }
        )
    comandos={
        'inicio':print('command_INICIO'),
        'nuevo':print('command_INICIO'),
        'bbdd':print('command_INICIO'),
        'formulario':print('command_INICIO'),
        'crear':print('command_INICIO'),
        'borrar':print('command_INICIO'),
        'cancelar':print('command_INICIO'),
        'exportarCSV':print('command_INICIO'),
        'exportarPython':print('command_INICIO')
        }
    G=GUI(
        AppName='Tkinter_Mbarete',
        titulo='NO hAY tITULO',
        reset=1,
        dbname='PRUEBAS_GUI.SQL',
        comandos=comandos,
        pwd=os.getcwd(),
        icon=obj.pwd+'Logo-Mbarete.png',
        geometry=(500,500,50,0)
        )
    for widget in widgets: G.SetWidget(atributos=widgets[widget])
    G.loop()
def tkinter_mbarete_titulo():
    """widgets personalisados aplicando herencia"""
    #print(tk.pwd+'Logo-Mbarete.png')
    tk=I_am_Tk(
        pwd='media',
        carpetas={
            'dir_media':'mbarete/media/',
            'web_servidor':'mbarete/servidor/'
            },
        icon='Logo-Mbarete.png'
        )
    raiz=FrameScroll(tk)
    #raiz.root.iconphoto(False,PhotoImage(file=icon))
    raiz.loop()
def mbarete_IDE():
    """Editor de Texto WIDGET_IDE"""
    #editor de texto
    print({x:str(chr(int(x))) for x in range(0,127)})
    tk=I_am_Tk(
        pwd='media',
        flags=['error','init','paths_directos'],
        carpetas={
            'dir_modulos':'mbarete/modulos/',
            'dir_media':'mbarete/media/',
            'web_servidor':'mbarete/servidor/',
            },
        geometry=(500,300,500,100),
        icon='Logo-Mbarete.png'
        )
    #print(tk.pwd+'Logo-Mbarete.png')
    raiz=widget_IDE( tk )
    raiz.ShowScript(pwd=tk.carpetas['modulos']+raiz.file)
    #raiz.root.iconphoto( False, PhotoImage(file=icon))
    raiz.loop()
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
def gestor_de_pestañas():
    """Usar frame desde varias pestañas"""
    from tkinter import Tk, Frame,Button
    global G;G={}
    def cambio(m):
        global G
        for menu in ['1','2']:
            G[menu].forget()
        G[m].pack(expand=1,side='bottom',fill='both')
        G['r'].update()
    G['r']=Tk()
    frameBoton=Frame(G['r'],bg='#101039')
    frameBoton.pack(side='top',expand=1,fill='x')
    cerrar=Button(frameBoton,text="Destroy",command=G['r'].destroy)
    cerrar.pack(side='right')
    btnmenu1=Button(frameBoton,text="menu 1",command=lambda: cambio('1'))
    btnmenu1.pack(side='left')
    btnmenu2=Button(frameBoton,text="menu 2",command=lambda: cambio('2'))
    btnmenu2.pack(side='left')
    G['1']=Frame(G['r'],bg='#f01039')
    G['2']=Frame(G['r'],bg='#f1f1f1')
    cambio('1')
    btn1=Button(G['1'],text="botonio 1",command=lambda: btn1.config(text="hola"))
    btn1.pack()
    btn2=Button(G['2'],text="botonio 2",command=lambda: btn2.config(text="hello"))
    btn2.pack()
    G['r'].mainloop()
def ttk_Style_primer():
    """Ttk Style"""
    import tkinter
    from tkinter import ttk
    root = tkinter.Tk()
    print(ttk.Style().lookup("TButton", "font"))
    ttk.Style().configure(
        "TButton", 
        padding=6, 
        relief="flat",
        background="#ccc"
        )
    btn = ttk.Button(text="Sample")
    btn.pack()
    root.mainloop()
def ttk_Style_layout():
    """Ttk Style Layout"""
    from tkinter import ttk
    import tkinter
    root = tkinter.Tk()
    style = ttk.Style()
    style.layout("TMenubutton", [
        ("Menubutton.background", None),
        ("Menubutton.button", {
            "children":[(
                "Menubutton.focus", 
                {
                    "children":[
                        (
                            "Menubutton.padding", 
                            {
                                "children":[
                                    (
                                        "Menubutton.label", 
                                        {
                                            "side": "left", 
                                            "expand": 1
                                        }
                                    )
                                ]
                            }
                        )
                    ]
                }
            )]
        }),
    ])
    mbtn = ttk.Menubutton(text='Text')
    mbtn.pack()
    root.mainloop()
def animacion_con_matplotlib():
    import numpy as np
    import matplotlib.pyplot as plt
    from matplotlib.animation import FuncAnimation
    import random
    global xData, yData
    xData=[]
    yData=[]
    fig, ax = plt.subplots()
    ax.set_xlim(0,205)
    ax.set_ylim(0,12)
    line,= ax.plot(0,0)
    #random.randrange(10)*0.1
    def animationFrame(i):
        xData.append(i)
        yData.append((1.01**i)+(random.randrange(10)*0.1))
        line.set_xdata(xData)
        line.set_ydata(yData)
        return line,
    #np.arange(0,10,0.01)
    print(np.arange(0,100,1))
    animation = FuncAnimation(
        fig, func=animationFrame, interval=1, 
        frames=np.arange(0,205,1)
        )
    plt.show()


if 'main' in __name__:
    main_pruebas([
        tkinter_mbarete_titulo,get_style,mbarete_IDE,GUI_mbarete,
        ttk_Style_primer,ttk_Style_layout,gestor_de_pestañas,
        animacion_con_matplotlib
        ])