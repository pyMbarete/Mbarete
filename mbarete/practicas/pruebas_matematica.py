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
