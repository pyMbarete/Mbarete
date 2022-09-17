import math,os,sys
from pruebas import deco

def strMetodosParaMatematicas():
    print("'2146.54'.isdigit()",'2146.54'.isdigit())
    print("'4.5'.isnumeric()",'4.5'.isnumeric())

def multiplicarMatriz(factor,Matriz):
    for x in range(len(Matriz)):
        if Matriz[x].__class__ == list:
            Matriz[x]=multiplicarMatriz(factor,Matriz[x])
        elif Matriz[x].__class__ == [int,float]:
            Matriz[x]=Matriz[x]*factor
    return Matriz
class calc:
    """geometria,calculo,vectores,estadistica"""
    EJE_X=1.0
    EJE_Y=1.0
    #decimales a tener en cuenta
    d=4
    def promedio(l,key=None):
        p=0
        for e in l :
            p+= key(e) if key!=None else e
        return p/len(l)
    def varianza(l,key=None):
        p=calc.promedio(l,key=key)
        v=0
        if key != None:
            for e in l: v+= abs(p-key(e)) 
        else:
            for e in l: v+= abs(p-e) 
        return v
    @deco(flag='geo')
    def esColineales(A,B,C):
        AB=calc.resta(B,A)
        AC=calc.resta(C,A)
        if int((AB[0]/AB[1])*(10**calc.d))==int((AC[0]/AC[1])*(10**calc.d)):
            return True
        else:
            return False
    @deco(flag='geo')
    def modulo(A): return (((A[0])**2)+((A[1])**2)+((A[2])**2))**(1/2)
    @deco(flag='geo')
    def vectorUnitario(A):
        m=calc.modulo(A)
        return [A[0]/m,A[1]/m,A[2]/m]
    def hypotenusa(catA,catB): return (((catA)**(2))+((catB)**(2)))**(1/2)
    @deco(flag='geo')
    def dist(A,B):
        #calcula la dsitancia entre A y B
        return (((A[0]-B[0])**2)+((A[1]-B[1])**2)+((A[2]-B[2])**2))**(1/2)
    @deco(flag='geo')
    def coseno(A,B):
        #retorna el valor del coseno del angulo formado entre los vectores A y B
        divisor=(((((A[0])**2)+((A[1])**2)+((A[2])**2))**(1/2))*((((B[0])**2)+((B[1])**2)+((B[2])**2))**(1/2)))
        if divisor!=0.0:
            return ((A[0]*B[0]+A[1]*B[1]+A[2]*B[2])/divisor)
        else:
            return 3.1416/2
    def angRad(A,B): return math.acos(calc.coseno(A,B))
    def ang(A,B):return math.degrees(math.acos(calc.coseno(A,B)))
    @deco(flag='geo')
    def resta(A,B):
        #retorna el vector AB o B-A
        return [B[0]-A[0],B[1]-A[1],B[2]-A[2]]
    @deco(flag='geo')
    def suma(A,B):
        #retorna el vector A+B.
        return [B[0]+A[0],B[1]+A[1],B[2]+A[2]]
    @deco(flag='geo')
    def medio(A,B):
        #retorna el vector A+B.
        return [(B[0]+A[0])/2,(B[1]+A[1])/2,(B[2]+A[2])/2]
    @deco(flag='geo')
    def alt(A,B,C):
        #retorna el 'punto de origen' del segmento que 
        #define la altura del triangulo A,B,C. 
        #Considerando al lado BC como la base del triangulo.
        ab=calc.dist(A,B)
        bc=calc.dist(B,C)
        BA=calc.resta(B,A)
        BC=calc.resta(B,C)
        cosB=calc.coseno(BA,BC)
        x=((BC[0]/bc)*(cosB*ab))+B[0]
        y=((BC[1]/bc)*(cosB*ab))+B[1]
        z=((BC[2]/bc)*(cosB*ab))+B[2]
        return  [x,y,z]
    def rotar(rad,P,O=[0.0,0.0]):
        #sobre el origen, rotar el angulo 'rad' dado en 
        #sentido antiorario el punto P 
        #OP=calc.resta(O,P)
        x=(P[0]-O[0])*math.cos(rad)-(P[1]-O[1])*math.sin(rad)
        y=(P[0]-O[0])*math.sin(rad)+(P[1]-O[1])*math.cos(rad)
        return [O[0]+x,O[1]+y]
    @deco(flag='geo')
    def trasladar(O,P):
        #trasladar el punto P, al nuevo origen O
        return P[0]+O[0], P[1]+O[1] ,P[2]+O[2]
    def rectaAB(A,B,x=None,y=None):
        '''ecuacion de la recta definada por los puntos A y B
            rectaAB([xa,ya],[xb,yb],x:float) -> y:float
            rectaAB([xa,ya],[xb,yb],y:float) -> x:float
        '''
        if x!=None:
            return ( ((B[1]-A[1])*(x-A[0]))/(B[0]-A[0]) )+A[1]
        if y!=None:
            return ( ((B[0]-A[0])*(y-A[1]))/(B[1]-A[1]) )+A[0]
    def rectaAm(A,m,x=None,y=None):
        '''ecuacion de la recta definada por el punto A y la pendiente m
            rectaAm([x,y],m,x:float) -> y:float
            rectaAm([x,y],m,y:float) -> x:float
        '''
        if x!=None:
            return (m*(x-A[0]))+A[1]
        if y!=None:
            return ((y-A[1])/m)+A[0]
def globo_terraqueo(diametro=100):
    #formula para generar plano de corte para globo terraqueo
    arco_maximo=45.0
    cortes=12.0
    r=diametro/2.0
    arco=360.0/cortes
def calcular_sueldo():
    sueldo=0
    dia={
        'pasajes':10500,
        'saldo':5000,
        'comida':20000,
        'fotocopias':3000
        }
    mes={
        'luz':100000,
        'internet':100000,
        'cuota':150000,
        'limpieza_personal':100000,
        'tinta':15000,
        'farmacia':50000,
        'herramientas':100000,
        'materiales':200000
        }
    for k in dia:sueldo+=dia[k]*30
    for k in mes:sueldo+=mes[k]
    print('Sueldo:',sueldo)
def brasos_contrapesos(brasos=[],carga=5.0,densidad=2.7):
    if not brasos:
        brasos=[
            [0.2,0.2,0.3],
            [0.5,0.5,0.4]
        ]
    contra_pesos=[]
    suma=carga
    for b in brasos:
        contra_pesos += [ (b[0]*suma + (b[0]/2.0)*b[1])/b[2] ]
        suma += suma + b[1] + contra_pesos[-1]
    vol=sum(contra_pesos)/densidad
    print(suma,contra_pesos,vol)
    return suma,contra_pesos,vol
def brasos_articulado_contrapesos(brasos=[],carga=5.0,densidad={'aluminio':2.7,'acero':7.7}):
    #
    b={
        'peso_objetivo':carga,
        'peso_muerto':2.0,
        'largo_util':1.5,
        'masa_util':1.0,
        'masa_braso_2':0.4,
        'largo_braso_2':0.6,
        'largo_contrapeso_2':0.1
        }
    [ p, m0, lu, mu, mb2, lb2, lc2 ] = [b[k] for k in b]
    mc2 = (lb2*m0 + (lb2/2.0)*mb2)/lc2
    lc2_p = (lb2*(m0+p) + (lb2/2.0)*mb2)/mc2
    lb1 = lu*(lb2/(lb2+lc2))
    lb1_p = lu*(lb2/(lb2+lc2_p))
    b['masa_contrapeso_2']=mc2
    b['largo_contrapeso_2_con_peso']=lc2_p
    b['largo_braso_1']=lb1
    b['largo_braso_1_con_peso']=lb1_p
    b['masa_contrapeso_1'] = ((((lb1_p**2)-((lu-lb1_p)**2))/2)*(mu/lu))/((lu-lb1_p)/2)
    b['largo_contrapeso_1'] = ((lb1/2)*lb1*(mu/lu))/b['masa_contrapeso_1']
    b['largo_contrapeso_1_con_peso'] = lu - lb1
    b['masa_total']=mc2+p+m0+mu+mb2+b['masa_contrapeso_1']
    for d in densidad:b['vol_'+d]=b['masa_total']/densidad[d]
    for k in b:print(k+':',b[k])
    return b
def pascal_piramid(nivel=20):
    triangulo=[[1]]
    for i in range(nivel):
        print(triangulo[-1])
        e=[0]+triangulo[-1]+[0]
        triangulo+=[[ e[x]+e[x+1] for x in range(len(e)-1)]]
def primos_menores(entero,primos=[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]):
    ultimo=max(primos)+1
    if ultimo>=entero:
        x=0
        menor=[]
        while primos[x]<entero:
            menor+=[primos[x]]
            x+=1
        return menor
    else:
        while ultimo<entero:
            add=1
            for p in primos[:-1]:
                if ultimo%p == 0:add=0
            if add: primos+=[ultimo]
            else:ultimo+=1
        return primos
def primo_mayor(primos):
    ultimo=max(primos)+1
    add=0
    while add==0:
        add=1
        for p in primos:
            if ultimo%p == 0:add=0
        if add: primos+=[ultimo]
        else: ultimo+=1
    return ultimo
def shift_fact(entero):
    """
        Retorna un diccionario con los factores de un numero entero 
        si es entero. Sino solamente retorna el signo del numero.
        return { 'signo':+-1, base:exponente, ... , baseN:exponenteN }
    """
    (signo,entero)=(-1,-1*entero) if entero<0.0 else (1,entero)
    #lista de factores
    f=['signo'] 
    if entero.__class__ == int:
        x=2
        while x<=entero:
            while entero%x==0:
                f+=[x]
                entero=entero/x
            x+=1
    #convertir esa lista a diccionario
    return { f:signo if f=='signo' else f.count(f) for f in set(f) }

def shift_quebrado(numero):
    precision=16
    entero,decimales=str(numero).split('.')
    if len(decimales)>=precision:
        decimales=decimales[:-1]
    periodo = next((decimales[:x] for x in range(1,len(decimales)) if decimales in decimales[:x]*len(decimales)), None)
    mixto=[]
    for x in range(1,len(decimales)):
        for m in range(1,len(decimales)-x):
            scan=decimales[m:m+x]
            if scan*2 in decimales: mixto+=[{'periodo':scan,'index':m}]
    mixto.sort(reverse=False,key=lambda x: x['index'])
    for x in range(len(mixto)):
        if mixto.__class__ == str: continue
        else: e=mixto[x]
        if decimales==(decimales[:e['index']]+e['periodo']*(((len(decimales)-e['index'])//len(e['periodo']))+1))[:len(decimales)]:
            mixto=e['periodo']
    #¿es periodica? 
    if periodo:
        abc=sum([9*(10**x) for x in range(len(periodo))])
        entero,decimales=map(int,[entero,decimales])
        numerador=shift_fact(int(periodo)+entero*abc)
    elif mixto.__class__ == str:
        periodo=mixto
        noperiodo=decimales.split(mixto)[0]
        abc=sum([9*(10**x) for x in range(len(mixto))])*(10**(len(noperiodo)))
        numerador=shift_fact(int(noperiodo+mixto)-int(noperiodo))
    else:
        abc=10**(len(decimales))
        numerador=shift_fact(int(numero*abc))
    denominador=shift_fact(abc)
    numerador,denominador=reducir(numerador,denominador)
    return factores_to_entero(numerador), factores_to_entero(denominador)
def factores_to_entero(d,signo=1):
    d = [f for f in d for x in range(d[f]) if f != 'signo']+[d['signo']]
    return math.prod(d)
def reducir(N,D):
    for f in N:
        if f in D and f != 'signo':
            if N[f]>D[f]:
                N[f]=N[f]-D[f]
                D[f]=0
            else:
                D[f]=D[f]-N[f]
                N[f]=0
    return N,D
def strToMathViejo(string='',variable='x',dy=0,p=0,c=None,decimales=4,signo=None,v=0,composicion=0):
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
            print('division:',string,signoDivision)
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
class constante(object):
    """numero operador aritmetico"""
    def __init__(self,numero,D=1,N=1):
        super(constante, self).__init__()
        if None==numero:
            self.D=D
            self.N=N
        else:
            self.set(numero)
            self.D=self.D
            self.N=self.N
    def __str__(self):
        return str(self.N)+'/'+str(self.D)
    def set(self,numero):
        numero=float(numero) if numero.__class__==str else numero
        if float == numero.__class__:
            self.N,self.D = shift_quebrado(numero)
        else:
            self.N,self.D = int(numero) ,1
    def __repr__(self):
        return self.N
    def __call__(self):
        return self.N
    def __add__(self, other):
        #suma
        if other.__class__==int or other.__class__==float:
            N=shift_fact(self.N+(self.D*other))
            D=shift_fact(self.D)
        else:
            N=shift_fact(self.N*other.D+self.D*other.N)
            D=shift_fact(self.D*other.D)
        N,D=reducir(N,D)
        return constante(None,N=factores_to_entero(N),D=factores_to_entero(D))

    def __sub__(self, other):
        #resta
        if other.__class__==int or other.__class__==float:
            N=shift_fact(self.N-(self.D*other))
            D=shift_fact(self.D)
        else:
            N=shift_fact(self.N*other.D-self.D*other.N)
            D=shift_fact(self.D*other.D)
        N,D=reducir(N,D)
        return constante(None,N=factores_to_entero(N),D=factores_to_entero(D))

    def __mul__(self, other):
        #multiplicacion
        if other.__class__==int or other.__class__==float:
            N=shift_fact(self.N*other)
            D=shift_fact(self.D)
        else:
            N=shift_fact(self.N*other.N)
            D=shift_fact(self.D*other.D)
        N,D=reducir(N,D)
        return constante(None,N=factores_to_entero(N),D=factores_to_entero(D))

    def __truediv__(self, other):
        #division
        if other.__class__==int or other.__class__==float:
            N=shift_fact(self.N)
            D=shift_fact(self.D*other)
        else:
            N=shift_fact(self.N*other.D)
            D=shift_fact(self.D*other.N)
        N,D=reducir(N,D)
        return constante(None,N=factores_to_entero(N),D=factores_to_entero(D))
class Vector():
    def __init__(self, data):
        self._data = data
    
    def __repr__(self):
        return self._data
    def __str__(self):
        return f"The values are: {self._data}"
    def __len__(self):
        return len(self._data)
    
    def __getitem__(self, pos):
        return self._data[pos]
    
    def __setitem__(self, pos, value):
        self._data[pos] = value
    
    def __get__(self):
        return self._data
    
    def __set__(self, value):
        print(value)
        self._data = value
    
    def __iter__(self):
        for pos in range(0, len(self._data)):
            yield f"Value[{pos}]: {self._data[pos]}"

    def __add__(self, other):
        #suma
        result = [None] * len(self._data)
        for pos in range(len(self._data)):
            result[pos] = self._data[pos] + other._data[pos]
        return Vector(result)
    def __sub__(self, other):
        result = [None] * len(self._data)
        #resta
        return Vector(result)
    def __mul__(self, other):
        #multiplicacion
        result = [None] * len(self._data)
        return Vector(result)
    def __truediv__(self, other):
        #division
        result = [None] * len(self._data)
        return Vector(result)
class ecuacion(object):
    """las ecuaciones seran objetos con diferentes metodos, para ser operados,derivados,simplificados,etc,etc..."""
    def __init__(self, extras):
        super(ecuacion, self).__init__()
        self.extras = extras
        self.simplificado=0
        self.ret='y'
        self.op='y'
        self.f={}
        self.g={'c':None}
        self.c={}
    def __call__(self,x,extras={}):
        #extras[''] = extras[''] if '' in extras else self.extras['']
        extras['signo'] = self.extras['signo']
        ret = extras['ret'] if 'ret' in extras else self.extras['ret']
        op = extras['op'] if 'op' in extras else self.extras['op']
        extras['mostrarSigno'] = extras['mostrarSigno'] if 'mostrarSigno' in extras else self.extras['mostrarSigno']
        extras['decimales'] = extras['decimales'] if 'decimales' in extras else self.extras['decimales']
        if ret == 'print':
            if extras['mostrarSigno']:
                s='+' if extras['signo']>0.0 else '-'
            else:
                s=''
        else:
            s=0.0
        extras['mostrarSigno'] = self.extras['mostrarSigno']
        if self.extras['c']:
            return self.extras['signo']*self.c[op][ret] if ret=='y' else s+self.c[op][ret]
        else:
            return self.extras['signo']*self.f[op][ret](x,extras=extras,g=self.g) if ret=='y' else s+self.f[op][ret](x,extras=extras,g=self.g)

    def set(self,f):
        self.f=f
        self.extras['c']=self.isConstante(self.g)
        if self.extras['c']:
            extras={'decimales':6,'signo':self.extras['signo']}
            self.c['dy']={
                'print':str(self.f['dy']['y'](None,extras={'op':'dy','decimales':6,'signo':self.extras['signo']},g=self.g)),
                'y':self.f['dy']['y'](None,extras={'op':'dy','decimales':6,'signo':self.extras['signo']},g=self.g)
                }
            self.c['y']={
                'print':str(self.f['y']['y'](None,extras={'decimales':6,'signo':self.extras['signo']},g=self.g)),
                'y':self.f['y']['y'](None,extras={'decimales':6,'signo':self.extras['signo']},g=self.g)
                }
            print(self.extras['ecuacion'],self.c)
    def isConstante(self,obj):
        ret=1
        if obj.__class__ == dict:
            for ecu in obj:
                if obj[ecu].__class__ == list:
                    for i in obj[ecu]:
                        if not i.extras['c']: ret=0
                if obj[ecu].__class__ == ecuacion:
                    if not obj[ecu].extras['c']: ret=0
        if {'c':None} == obj: ret=0
        return ret
def validar(string='',v=0,composicion=0):
    if v:
        print('validando',string,composicion)
    if ' ' in string:
        s=''
        for c in string: 
            if ' '!=c: s+=c
        string=s
    composicion += 1
    nivel=0
    comas=[0]
    op=''
    signos={}
    signos['suma']=[0]
    signos['producto']=[0]
    signos['division']=[0]
    signos['exponente']=[0]
    signos['resto']=[0]
    operador=1
    monomio=1
    parentesis=1
    sig=1.0
    nivelar=lambda c,n: n+1 if (c=='(') else (n-1 if c==')' else n)
    string=string.strip()
    for fondo in range(3):
        monomio=1
        parentesis=1
        for x in range(0,len(string),1):
            nivel=nivelar(string[x],nivel)
            if string[x] in '-+' and nivel==0: 
                if x>0: monomio=0
            if string[x] in '-+*/%' and nivel==0: 
                if x>0: parentesis=0
        if monomio:
            if string[0] in '-' and nivel==0: sig=-1.0*sig
            if string[0] in '+-' and nivel==0: string=string[1:].strip()
        if parentesis:        
            if ('(' in string[0]) and (')' in string[-1]):
                string=string[1:-1].strip()

    for x in range(0,len(string),1):
        nivel=nivelar(string[x],nivel)
        if nivel!=0: continue
        if (string[x] in ',') : comas += [x]
        if (string[x] == '%') : op='resto'
        if (string[x] in '/') : op='division'
        if (string[x] in '-+') and (x>0): op='suma'
        if (string[x] == '*') and ( '*' == string[x+1]) : op='exponente'
        if (string[x] == '*') and ( '*' != string[x+1]) and ( '*' != string[x-1]):  op='producto'
        if (string[x] in '-+%*/') and ( '*' != string[x-1]) and op:
            signos[op] += [x]
            operador=(1 if monomio else 0) if op=='suma' else 0
    return string,op,signos,operador,nivel,sig,comas,composicion
class igualdad(object):
    """
        objeto para poder resolver igualdades
    """
    def __init__(self,l,r):
        self.r=r
        self.l=l
        self.simplificables=['producto','division','suma','exponente','','','']
    def simplificar(self,e):
        simple=1
        while simple:
            simple=0
            if not e.simplificado:
                if 'constante' == e.extras['ecuacion']:
                    factores=[]
def strToMath(string='',extras={'variable':'x','mostrarSigno':0,'c':None,'decimales':4,'signo':None,'v':0,'composicion':0}):
    constantes={'e':math.e,'pi':3.1416,'g':9.8182}
    if 'constantes' in extras:
        for c in extras['constantes']: constantes[c]=extras['constantes'][c]
    operadores=['w','sen','cos','tg','log','ln','lambert','dy','sec','cosec','cotag','arcsen','arccos','arctg','round','floor','ceil','signo','abs']
    simbolos=['*','(',')','/','+','-','.','%']
    string,op,signos,operador,nivel,sig,comas,comp=validar(string=string,v=extras['v'],composicion=extras['composicion'])
    f=ecuacion(extras={
        'string':string,
        'variable':extras['variable'],
        'mostrarSigno':extras['mostrarSigno'],
        'c':None,
        'decimales':extras['decimales'],
        'signo':sig,
        'v':extras['v'],
        'composicion':comp,
        'op':'y',
        'ret':'y'})
    if operador:
        operador = next((o for o in operadores if o in (string[:len(o)] if len(o)<len(string) else '')), None)
        if operador and nivel==0:
            print(operador+':',string,signos[op])
            f.extras['mostrarSigno']=1
            f.extras['ecuacion']=op
            if operador in 'w':
                f.extras['ecuacion']='NO DEFINIDA'
                def dy_print(x,extras={},g={}):
                    return '0.0'
                def dy_y(x,extras={},g={}):
                    return 0.0
                def y_print(x,extras={},g={}):
                    return '0.0'
                def y_y(x,extras={},g={}):
                    return 0.0
            if operador in 'dy':
                f.extras['ecuacion']='NO DEFINIDA'
                def dy_print(x,extras={},g={}):
                    return '0.0'
                def dy_y(x,extras={},g={}):
                    return 0.0
                def y_print(x,extras={},g={}):
                    return '0.0'
                def y_y(x,extras={},g={}):
                    return 0.0
            if operador in 'log':
                #math.log(x,base)
                f.g['parteReal']=strToMath(string=string[len('log'):comas[1]],extras=extras)
                if len(comas)==1:
                    f.g['base']=strToMath(string='10.0',extras=extras)
                else:
                    f.g['base']=strToMath(string=string[comas[1]+1:-1],extras=extras)
                def dy_print(x,extras={},g={}):
                    numerador='(('+g['parteReal'](x,extras=extras)+'/'+g['parteReal'](x,extras={'ret':'print'})+')-('+g['parteReal'](x,extras=extras)+'/'+g['parteReal'](x,extras={'ret':'print'})+'))'
                    return '('+numerador+'/'+g['parteReal'](x,extras={'ret':'print'})+')'
                def dy_y(x,extras={},g={}):
                    numerador=signo*((g['parteReal'](x,extras=extras)/g['parteReal'](x))-(g['base'](x,extras=extras)/g['base'](x)))
                    return numerador/((math.log(g['base'](x,extras=extras)))**2)
                def y_print(x,extras={},g={}):
                    return 'ln('+g['parteReal'](x,extras=extras)+','+g['base'](x,extras=extras)+')'
                def y_y(x,extras={},g={}):
                    return math.log(g['parteReal'](x),g['base'](x))
            if operador in 'ln':
                #math.log(x,base)
                f.g['parteReal']=strToMath(string=string[len('ln'):],extras=extras)
                def dy_print(x,extras={},g={}):
                    return '('+g['parteReal'](x,extras=extras)+'/'+g['parteReal'](x,extras={'ret':'print'})+')'
                def dy_y(x,extras={},g={}):
                    return g['parteReal'](x,extras=extras)/g['parteReal'](x)
                def y_print(x,extras={},g={}):
                    return 'ln('+g['parteReal'](x,extras=extras)+')'
                def y_y(x,extras={},g={}):
                    return math.log(g['parteReal'](x))
            if operador in 'abs':
                #math.fabs(-66.43)
                f.g['valor']=strToMath(string=string[len(''):],extras=extras)
                def dy_print(x,extras={},g={}):
                    return '(('+g['valor'](x,extras={'ret':'print'})+'/abs('+g['valor'](x,extras={'ret':'print'})+'))*('+g['valor'](x,extras=extras)+'))'
                def dy_y(x,extras={},g={}):
                    return (g['valor'](x)/math.fabs(g['valor'](x)))*g['valor'](x,extras=extras)
                def y_print(x,extras={},g={}):
                    return 'abs('+g['valor'](x,extras=extras)+')'
                def y_y(x,extras={},g={}):
                    return math.fabs(g['valor'](x))                
            if operador in 'tg':
                #math.tan()
                f.g['radian']=strToMath(string=string[len(operador):],extras=extras)
                def dy_print(x,extras={},g={}):
                    return '((1+tg('+g['radian'](x,extras={'ret':'print'})+')**2)*('+g['radian'](x,extras=extras)+'))'
                def dy_y(x,extras={},g={}):
                    return (1+math.tan(g['radian'](x))**2)*g['radian'](x,extras={'op':'dy'})
                def y_print(x,extras={},g={}):
                    return 'tg('+g['radian'](x,extras=extras)+')'
                def y_y(x,extras={},g={}):
                    return math.tan(g['radian'](x))
            if operador in 'sen':
                #math.sin()
                f.g['radian']=strToMath(string=string[len(operador):],extras=extras)
                def dy_print(x,extras={},g={}):
                    return '(cos('+g['radian'](x,extras={'ret':'print'})+')*('+g['radian'](x,extras=extras)+'))'
                def dy_y(x,extras={},g={}):
                    return math.cos(g['radian'](x))*g['radian'](x,extras={'op':'dy'})
                def y_print(x,extras={},g={}):
                    return 'sen('+g['radian'](x,extras={'ret':'print'})+')'
                def y_y(x,extras={},g={}):
                    return math.sin(g['radian'](x))
            if operador in 'cos':
                #math.cos()
                f.g['radian']=strToMath(string=string[len(operador):],extras=extras)
                def dy_print(x,extras={},g={}):
                    return '(sen('+g['radian'](x,extras={'ret':'print'})+')*('+g['radian'](x,extras=extras)+'))'
                def dy_y(x,extras={},g={}):
                    return -1*signo*math.sin(g['radian'](x))*g['radian'](x,extras=extras)
                def y_print(x,extras={},g={}):
                    return 'cos('+g['radian'](x,extras=extras)+')'
                def y_y(x,extras={},g={}):
                    return signo*math.cos(g['radian'](x))
            if operador in 'arcsen':
                #math.asin()
                pass
            if operador in 'arccos':
                #math.acos()
                pass
            if operador in 'arctg':
                #math.atan()
                pass
            if operador in 'signo':
                #detecta el signo
                pass
            if operador in 'entero':
                #retorna el entero del la funcion
                pass
            if operador in 'decimal':
                #retorna la parte decimal
                pass
            if operador in 'round':
                f.g['round']=strToMath(string=string[len(operador):],extras=extras)
                def dy_print(x,extras={},g={}):
                    return '0.0'
                def dy_y(x,extras={},g={}):
                    return 0.0
                def y_print(x,extras={},g={}):
                    return 'round('+g['round'](x,extras=extras)+')'
                def y_y(x,extras={},g={}):
                    return math.round(g['round'](x))
            if operador in 'floor':
                f.g['floor']=strToMath(string=string[len(operador):],extras=extras)
                def dy_print(x,extras={},g={}):
                    return '0.0'
                def dy_y(x,extras={},g={}):
                    return 0.0
                def y_print(x,extras={},g={}):
                    return 'floor('+g['floor'](x,extras=extras)+')'
                def y_y(x,extras={},g={}):
                    return math.floor(g['floor'](x))
            if operador in 'ceil':
                f.g['ceil']=strToMath(string=string[len(operador):],extras=extras)
                def dy_print(x,extras={},g={}):
                    return '0.0'
                def dy_y(x,extras={},g={}):
                    return 0.0
                def y_print(x,extras={},g={}):
                    return 'ceil('+g['ceil'](x,extras=extras)+')'
                def y_y(x,extras={},g={}):
                    return math.ceil(g['ceil'](x))
        else:
            if string in constantes:
                f.g['c']=constantes[string]
            elif sum([1 for l in string if ((48<=ord(l)<=57) or (ord(l)==46))])==len(string):
                f.g['c']=float(string)
            if f.g['c']:
                f.extras['ecuacion']='constante'
                f.extras['c']=1
                def dy_print(x,extras={},g={}):
                    return '0.0'
                def dy_y(x,extras={},g={}):
                    return 0.0
                def y_print(x,extras={},g={}):
                    return str(g['c'])[:extras['decimales']]
                def y_y(x,extras={},g={}):
                    return g['c']*extras['signo']
                
            if string==extras['variable']:
                f.extras['ecuacion']='variable'
                def dy_print(x,extras={},g={}):
                    return '1.0'
                def dy_y(x,extras={},g={}):
                    return 1.0
                def y_print(x,extras={},g={}):
                    return str(x)[:extras['decimales']]
                def y_y(x,extras={},g={}):
                    return x*extras['signo']
    else:
        #parentecis,exponente/radicales,multiplicacion/division,suma/resta
        print(op+':',string,signos[op])
        f.extras['ecuacion']=op
        if op=='suma':
            if len(signos[op])==1:
                f.g['sumandos']=[strToMath(string=string[1:],extras=extras)]
            else:
                f.g['sumandos']=[]
                for sumando in range(0,len(signos[op])-1,1):
                    f.g['sumandos']+=[strToMath(string=string[signos[op][sumando]:signos[op][sumando+1]],extras=extras)]
                f.g['sumandos']+=[strToMath(string=string[signos[op][-1]:],extras=extras)]
            def dy_print(x,extras={},g={}):
                ret = '('
                for sumando in g['sumandos']:
                    ret += ' '+sumando(x,extras=extras)
                return ret+' )'
            def dy_y(x,extras={},g={}):
                return sum([sumando(x,extras=extras) for sumando in g['sumandos']])
            def y_print(x,extras={},g={}):
                ret = '('
                for sumando in g['sumandos']:
                    ret += ' '+sumando(x,extras={'ret':'print','mostrarSigno':1})
                return ret+' )'
            def y_y(x,extras={},g={}):
                ret = 0.0
                for sumando in g['sumandos']:
                    ret += sumando(x)
                return ret
            
        elif op=='division':
            signos[op]+=[]
            f.g['nume']=strToMath(string=string[0:signos[op][1]],extras=extras)
            f.g['deno']=strToMath(string=string[signos[op][1]+1:],extras=extras)
            def dy_print(x,extras={},g={}):
                return '(('+g['nume'](x,extras=extras)+')*('+g['deno'](x,extras={'ret':'print'})+')-('+g['nume'](x,extras={'ret':'print'})+')*('+g['deno'](x,extras=extras)+'))/(('+g['deno'](x,extras={'ret':'print'})+')**2)'
            def dy_y(x,extras={},g={}):
                return extras['signo']*((g['nume'](x,extras=extras)*g['deno'](x))-(g['nume'](x)*g['deno'](x,extras=extras)))/(g['deno'](x)**2)
            def y_print(x,extras={},g={}):
                return '('+g['nume'](x,extras=extras)+'/'+g['deno'](x,extras=extras)+')'
            def y_y(x,extras={},g={}):
                return extras['signo']*g['nume'](x,extras=extras)/g['deno'](x,extras=extras)
        elif op=='resto':
            signos[op]+=[]
            f.g['nume']=strToMath(string=string[0:signos[op][1]],extras=extras)
            f.g['deno']=strToMath(string=string[signos[op][1]+1:],extras=extras)
            def dy_print(x,extras={},g={}):
                return ''
            def dy_y(x,extras={},g={}):
                return None
            def y_print(x,extras={},g={}):
                return '('+g['nume'](x,extras=extras)+'%'+g['deno'](x,extras=extras)+')'
            def y_y(x,extras={},g={}):
                return extras['signo']*g['nume'](x,extras=extras)%g['deno'](x,extras=extras)
            
        elif op=='producto':
            f.g['factores']=[]
            for factor in range(0,len(signos[op])-1,1):
                f.g['factores']+=[strToMath(string=string[signos[op][factor]+(1 if 0<factor else 0 ):signos[op][factor+1]],extras=extras)]
            f.g['factores']+=[strToMath(string=string[signos[op][-1]+1:],extras=extras)]
            def dy_print(x,extras={},g={}):
                ret='('
                factor='('
                for derivar in range(0,len(g['factores']),1):
                    factor=g['factores'][derivar](x,extras=extras)
                    for escalar in range(0,len(g['factores']),1):
                        if not (derivar == escalar):
                            factor += '*'+g['factores'][escalar](x,extras={'ret':'print'})
                    ret += factor+')+'
                return ret[:-1]+')'
            def dy_y(x,extras={},g={}):
                ret=0.0
                factor=1.0
                for derivar in range(0,len(g['factores']),1):
                    factor=g['factores'][derivar](x,extras=extras)
                    for escalar in range(0,len(g['factores']),1):
                        if not (derivar == escalar):
                            factor*=g['factores'][escalar](x,extras={'op':'y'})
                    ret += factor
                return extras['signo']*ret
            def y_print(x,extras={},g={}):
                ret = '('+g['factores'][0](x,extras=extras)
                for factor in g['factores'][1:]:
                    ret += '*'+factor(x,extras=extras)
                return ret+')'
            def y_y(x,extras={},g={}):
                ret = 1.0
                for factor in g['factores']:
                    ret *= factor(x)
                return extras['signo']*ret
            
        elif op=='exponente':
            signos[op]+=[]
            f.g['base']=strToMath(string=string[0:signos[op][1]],extras=extras)
            f.g['exponente']=strToMath(string=string[signos[op][1]+2:],extras=extras)
            def dy_print(x,extras={},g={}):
                return '((('+g['exponente'](x,extras={'ret':'print'})+'*('+g['base'](x,extras={'ret':'print'})+'**('+g['exponente'](x,extras={'ret':'print'})+'-1))*'+g['base'](x,extras=extras)+') + ('+g['exponente'](x,extras=extras)+'*('+g['base'](x,extras={'ret':'print'})+'**'+g['exponente'](x,extras={'ret':'print'})+')*ln('+g['base'](x,extras={'ret':'print'})+'))))'
            def dy_y(x,extras={},g={}):
                ret = g['exponente'](x)*(g['base'](x)**(g['exponente'](x)-1))*g['base'](x,extras=extras) + g['exponente'](x,extras=extras)*(g['base'](x)**g['exponente'](x))*math.log(g['base'](x))
                return extras['signo']*ret
            def y_print(x,extras={},g={}):
                return g['base'](x,extras={'ret':'print'})+'**('+g['exponente'](x,extras={'ret':'print','mostrarSigno':1})+')'
            def y_y(x,extras={},g={}):
                return extras['signo']*g['base'](x)**g['exponente'](x)
            
    f.set({'dy':{'print':dy_print,'y':dy_y},'y':{'print':y_print,'y':y_y}})
    #print(string,op,signos,operador,nivel,extras,comas)
    return f  
def algebra():
    a=constante(1/5)
    b=constante(5/45)
    c=constante(500)
    print(a,b,c)
    op=[lambda a,b:print(a,'+',b,'=',a+b),lambda a,b:print(a,'-',b,'=',a-b),lambda a,b:print(a,'/',b,'=',a/b),lambda a,b:print(a,'*',b,'=',a*b)]
    for f in op:
        f(a,9*b())
        f(a,c)
        f(b,c)
    v = Vector([1,2])
    w = Vector([2,2])
     
    print(v + w)
"""
Ecuación general y completa de segundo grado
Ax2 + Bxy + Cy2 + Dx + Ey + F = 0 
"""

if 'main' in __name__:
    from pruebas import main_pruebas
    pruebas=[
        {'titulo':"Piramide de pascal",'f':pascal_piramid},
        {'titulo':"primo mayor a [2, 3, 5, 7, 11, 13, 17, 19, 23] ",'f':lambda: print(primo_mayor([2, 3, 5, 7, 11, 13, 17, 19, 23]))},
        {'titulo':"primos menores de 500 ",'f':lambda: print( primos_menores(500))},
        {'titulo':"lista con los factores de 5000000",'f':lambda: print( shift_fact(5000000) )},
        {'titulo':"generatriz de 0.0451451451  ",'f':lambda: print( shift_quebrado(0.0451451451))},
        {'titulo':"Contrapesos de un braso articulado  ",'f':brasos_articulado_contrapesos},
        {'titulo':"Calcular sueldo segun gasto semanal y mensual  ",'f':calcular_sueldo}        
        ]
    main_pruebas(pruebas,sys.argv)