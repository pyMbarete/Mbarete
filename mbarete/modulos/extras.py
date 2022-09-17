#!/usr/bin/env python
# -*- coding: latin-1 -*-
__all__=["tiempos","comprimir","descomprimir","V","C"]
import os,sys,time
# Registros, Logs, tiempos
class tiempos:
    _total=0
    def medirTiempo():
        if tiempos._total==0: tiempos.setTotal(10)
        else: return next( tiempos._generar_tiempos )
    def setTotal(total):
        tiempos._total=total
        tiempos._generar_tiempos=tiempos._generador()
    def _generador():
        t=0
        suma=0.0
        t0=time.time()
        T=t0
        while t < tiempos._total:
            T=time.time()
            suma += round(T-t0,4)
            yield 'T%s:%s, suma:%s'%(t,T-t0,suma)
            t+=1
            t0=T

class operador_comprimido:
    """docstring for operador_comprimido"""
    def value(self,R):
        #R=['font','Albertus','width',24,36]
        #print(R)
        l=len(R)
        #unificado
        g=V.get_iter(
            self.var[self.name],
            [self.D[x]['inter'][R[x]] for x in self.D if x < self.nivel]
            )
        for i in range(self.nivel,l):
            #pertenece a alguna ruta
            for r in self.rutas:
                if i==len(self.rutas[r]):
                    esRuta=True
                    for x in range(i):
                        if x>=len(self.rutas[r]): continue
                        elif self.rutas[r][x]==[]: pass
                        elif R[x] in self.rutas[r][x]: pass
                        else: esRuta=False
                else: esRuta=False

                if esRuta:
                    if (r in self.indexs) :
                        g = self.indexs[r][ g ]

                    if g.__class__ in [ tuple, list, dict ]:
                        if (r in self.grupos):
                            g = g[ self.grupos[r][ R[i] ] ]
                        elif self.D[i]['unificable']:
                            g = g[ self.D[i]['inter'][R[i]] ]
                        else:
                            g = g[ R[i] ]
        return g
    def getSize(self):
        #retorna el peso de la instancia, en memoria
        return f'{V.get_size([self.D,self.grupos,self.indexs,self.rutas,self.name,self.var,self.nivel])/1024}KB'
    def guardar(self,**kw):
        V.saveVars(
            [
                [
                    self.name,
                    {
                        'D':self.D,
                        'var':self.var,
                        'grupos':self.grupos,
                        'indexs':self.indexs,
                        'rutas':self.rutas,
                        'name':self.name,
                        'nivel':self.nivel
                        }
                    ]
                ],
            file=f'{self.name}.py',deep=[4],**kw
            )
class comprimir(operador_comprimido):
    """docstring for dimensiones"""
    __slots__=('indexs','grupos','D','rutas','name','var','lenR','nivel')
    def __init__(self, name,var,**kw):
        self.D={}
        self.nivel=0
        self.grupos={}
        self.indexs={}
        self.rutas={}
        self.name=name
        self.var={name:var}
        self.sub_dimension(self.var,0,**kw)
    def generador_multidimensional(self,rutas,d=0):
        if self.D[d]['unificable'] and rutas:
            if rutas[d]!=[]:
                iterar=rutas[d]
            else:            
                iterar=self.D[d]['inter']
            for k in iterar:
                if d+1==len(rutas):
                    yield [k]
                else:
                    for sub in self.generador_multidimensional(rutas,d=d+1):
                        yield [k]+sub
    def indexar_dimension(self,name,rutas,grupo={},**kw):
        self.rutas[name]=rutas
        self.indexs[name]=[]
        if grupo!={}:
            self.grupos[name]=grupo
        for r in self.generador_multidimensional(rutas):
            self.var[self.name], self.indexs[name] = C.indexado(
                    self.var[self.name], self.indexs[name],
                    keys_get=r,keys_set=r,**kw
                    )
        ordenado = [ [k,self.rutas[k]] for k in self.rutas ]
        ordenado.sort(reverse=False,key=lambda r : len(r[1]))
        self.rutas={ r[0]:r[1] for r in ordenado }
        self.lenR={ r:len(self.rutas[r]) for r in self.rutas}
    def unificar(self,d,var={},n=0):
        if var=={}:
            self.nivel=d
            var=self.var
        if n<d: 
            for i in var: 
                var[i]= { k:var[i][k] for k in self.D[n]['inter'] }
                self.unificar(d,var=var[i],n=n+1)
                var[i]=[ var[i][k] for k in self.D[n]['inter'] ]
    def sub_dimension(self,var,num,ignore=[],**kw):
        if var.__class__ == dict:
            if not num in self.D:
                self.D[num]={'unificable':True}

            if self.D[num]['unificable']:
                self.D[num]['unificable'],inter=self.esIguales(var,ignore=ignore,**kw)
                if 'inter' in self.D[num] :
                    if self.D[num]['inter'] != inter:
                        self.D[num]['unificable']=False
                else:
                    self.D[num]['inter'] = inter
            if self.D[num]['unificable']:
                for v in var:
                    if not v in ignore:
                        self.sub_dimension(var[v],num+1,ignore=ignore,**kw)
        else:
            self.D[num]={'unificable':False}
    def esIguales(self,dicts,ignore=[],normal=False,**kw):
        l=len(dicts)
        for e in ignore:
            if e in dicts:
                l-=1
        iguales=True
        inter=[]
        #condicion para las 'claves interseccion' entre los diccionarios
        ok=lambda k: (not k in ignore) and (inter.count(k)==l)
        #agrupamos todas las claves
        for e in dicts:
            if not e in ignore:
                if dicts[e].__class__ == dict:
                    inter += list(dicts[e])
                else:
                    return False,{}
        #claves que si estan en la interseccion
        inter = [ k for k in set(inter) if ok(k) ]
        #ordenamos
        inter.sort()
        #convertimos la lista a diccionario
        if normal:
            inter={i:inter[i] for i in range(len(inter))}
        else:
            inter={inter[i]:i for i in range(len(inter))}
        #todos los diccionarios tienen el mismo orden y claves
        for e in dicts:
            if not e in ignore:
                l=(len(dicts[e])-sum([1 for i in ignore if i in dicts[e]]))
                if l!=len(inter):
                    iguales=False
        return iguales,inter
class descomprimir(operador_comprimido):
    """docstring for comprimido"""
    __slots__=('indexs','grupos','D','rutas','name','var','lenR','nivel')
    def __init__(self,D={},grupos={},indexs={},rutas={},name='comprimido',var=[],nivel=0):
        self.D=D
        self.grupos=grupos
        self.indexs=indexs
        self.rutas=rutas
        self.name=name
        self.var=var
        self.nivel=nivel
        self.lenR={ r:len(self.rutas[r]) for r in self.rutas }
    def __call__(self,*ruta):
        return self.value(ruta)
class V:
    """Clase no instanciable, para [int,float,str,tuple,list,dict]"""
    def saveV(file,var,f=None,name='',n=0,ignore=[],m='w',deep=3):
        #saveVar('nombreScript.py',variable,name='varName',f=None,n=0,ignore=[],m='w',deep=3)
        indent='    '*n
        if f != None:
            if var.__class__ in [str]:
                f.write('"%s"'%(var))
            elif var.__class__ in [int,float,bool,bytes]:
                f.write("%s"%(var))
            if n>=deep and (var.__class__ in [list,tuple,dict]):
                #print(var)
                f.write("%s"%(var,))
            elif var.__class__ in [tuple]:
                f.write("(\n")
                for v in var:
                    f.write('%s'%(indent))
                    V.saveV(file,v,f=f,n=n+1,deep=deep)
                    f.write(",\n")
                f.write('%s)'%(indent))
            elif var.__class__ in [list]:
                f.write("[\n")
                for v in var:
                    f.write('%s'%(indent))
                    V.saveV(file,v,f=f,n=n+1,deep=deep)
                    f.write(",\n")
                f.write('%s]'%(indent))
            elif var.__class__ in [dict]:
                f.write("{\n")
                for v in var:
                    f.write("%s%s:"%(indent,"%s"%(v) if v.__class__==int else "'%s'"%(v)))
                    V.saveV(file,var[v],f=f,n=n+1,deep=deep)
                    f.write(",\n")
                f.write('%s}'%(indent))
        else:
            if not name:name=var.__name__
            f=open(file,m)
            f.write('%s='%(name))
            V.saveV(file,var,f=f,n=n+1,deep=deep)
            f.write("\n")
            f.close()
            if not 'print' in ignore:
                print('Guardado:%s en "%s"'%(name,file))
    def saveVars(l,file='ColeccionVar.py',m='a',deep=[],**kw):
        #saveColeccionVar(listaDeVariables,file='ColeccionVar.py',m='a',**kw)
        if deep==[]:
            deep=[3 for v in l]
        f=open(file,'w')
        f.write('#!/usr/bin/env python\n# -*- coding: latin-1 -*-\n')
        f.close()
        for x in range(len(l)):
            V.saveV(file,l[x][1],name=l[x][0],f=None,m=m,deep=deep[x],**kw)
    def get_size(obj, seen=None):
        """Recursivamente, encuentra el tamaño en memoria del objeto"""
        size = sys.getsizeof(obj)
        if seen is None:
            seen = set()
        obj_id = id(obj)
        if obj_id in seen:
            return 0
        # Marcar el objeto como 'visto' *antes* de entrar en recursion
        seen.add(obj_id)
        if isinstance(obj, dict):
            size += sum([V.get_size(v, seen) for v in obj.values()])
            size += sum([V.get_size(k, seen) for k in obj.keys()])
        elif hasattr(obj, '__dict__'):
            size += V.get_size(obj.__dict__, seen)
        elif hasattr(obj, '__iter__') and not isinstance(obj, (str, bytes, bytearray)):
            size += sum([V.get_size(i, seen) for i in obj])
        return size
    def igualar_dict(dicts,ignore=[],**kw):
        l=len(dicts)
        inter=[]
        #condicion para las 'claves interseccion' entre los diccionarios
        ok=lambda k: (not k in ignore) and (inter.count(k)==l)
        #agrupamos todas las claves
        for e in range(l): inter += list(dicts[e])
        #claves que si estan en la interseccion
        inter = [ k for k in set(inter) if ok(k) ]
        #ordenamos
        inter.sort()

        #convertimos la lista a diccionario
        inter={inter[i]:i for i in range(len(inter))}

        #todos los diccionarios tienen el mismo orden y claves
        for e in range(l):
            dicts[e] = {k:dicts[e][k] for k in inter}
        return dicts,inter

    def set_iter(var,value,keys=[]):
        if keys:
            var[keys[0]]=V.set_iter(var[keys[0]],value,keys=keys[1:])
        else:
            var=value
        return var
    def get_iter(var,keys=[]):
        if keys:
            return V.get_iter(var[keys[0]],keys=keys[1:])
        else:
            return var
    def toText(t,case='camel',sep=' '):
        ret=''
        split={'snake':'_','kebab':'-'}
        if case=='camel':
            for c in t:
                if ret=='': ret+=c.upper()
                elif c.islower(): ret+=c
                else: ret+=sep+c

        elif case in split:
            for word in t.strip().split(split[case]):
                word[0]=word[0].upper()
                ret+=word+sep

        return ret.strip()
    def toNameCase(t,case,sep=' '):
        ret=''
        split={'snake':'_','kebab':'-'}
        if case=='camel':
            for word in t.strip().split(sep):
                word[0]=word[0].upper()
                ret+=word
            ret[0]=ret[0].lower()
            return ret
        elif case in split:
            return t.lower().strip().replace(sep,split[case])    
class C:
    """
        Compresor:
        Funciones para compresion de variables estructurales dict,list
    """
    def get_keys(item):
        if item.__class__ == tuple: return list(range(len(item)-1))
        elif item.__class__ == dict: return list(item.keys())
        else: return item
    def get_values(item):
        if item.__class__ == tuple: return list(item)
        elif item.__class__ == dict: return list(item.values())
        else: return item
    def filtro_mono(x,g,item,grupos):
        v = round( varianza(item),4 )
        if v==0.0:
            grupos[g+'_mono'][x]=round( promedio(item),4 )
            return True
        else:
            return False
    def filtro_indexado(cmd,g,filtrar,lista,grupos,indexs):
        nivel=[{cmd:[]}]
        for grupo in ['mono']:
            if grupo in filtrar:
                nivel[0][cmd]+=[g+'_'+grupo]
                grupos[g+'_'+grupo]={}
        for index in ['index']:
            if index in filtrar:
                index=g+'_'+index
                nivel[0][cmd]+= [index]
                grupos[index] = {}
                indexs[index] = []
        if 'keyOrd' in filtrar:
            grupos[g+'_keyOrd']=list(lista[0].keys())
            grupos[g+'_keyOrd']= { grupos[g+'_keyOrd'][x]:x for x in range(len(grupos[g+'_keyOrd'])) }
            nivel += [ { 'keys':[g+'_keyOrd'] } ]
        for x in range(len(lista)):
            item=C.get_values( lista[x] )
            if 'mono' in filtrar and C.filtro_mono(x,g,item,grupos):
                pass
            elif 'index' in filtrar:
                grupos[g+'_index'][x]=len( indexs[g+'_index'] )
                indexs[g+'_index']+=[item]

        return nivel    
        
    def item_to_index(item,index,def_set=None,def_get=None,keys_set=None,keys_get=None,**kw):
        if keys_get:u=V.get_iter( item ,keys=keys_get )
        else: u=item
        if def_get:u=def_get(u)
        if u in index: i=index.index(u)
        else:
            i=len(index)
            index+=[u]
        if def_set: i=def_set(i)
        if keys_set: item=V.set_iter( item,i,keys=keys_set )
        else: item= i
        return item,index

    def if_iterar(item,iterar):
        if iterar:
            if item.__class__ == list: return item.indexs()
            elif item.__class__ == dict: return item.keys()
            else: return []
        else:
            return False
        
    def indexado(item,index,iterar=0,**kw):
        iterar=C.if_iterar(item,iterar)
        if iterar==False:
            return C.item_to_index(item,index,**kw)
            
        for e in iterar:
            item[e],index=C.item_to_index(item[e],index,**kw)
        return item,index

    def get_rutas(item,rutas,iterar=0,**kw):
        iterar=C.if_iterar(item,iterar)
        if iterar==False:
            if rutas.__class__ ==list:
                return [ V.get_iter(item,keys=r) for r in rutas ]
            else:
                return [ V.get_iter(item,keys=rutas[r]) for r in rutas ]
            
        for e in iterar:
            item[e]=[ V.get_iter(item[e],keys=rutas[r]) for r in rutas ]  
        return item

    def enrutar( g,dicts, grupos,indexs,rutas={},filtrar=[],iterar=1,**kw ):
        nivel=[{'values':[g]}]
        grupos[g]=[k for k in dicts]
        if iterar :
            dicts,grupos[g+'_iterar'] = V.igualar_dict( list(dicts.values()),**kw )
            nivel+=[{'keys':[g+'_iterar']}]
            if 'keyOrd' in filtrar:
                grupos[g+'_keyOrd']=dicts[0][list(dicts[0])[0]]
        else:
            if 'keyOrd' in filtrar:
                grupos[g+'_keyOrd']=dicts[list(dicts)[0]]
        n=0
        nivel+=[{'pass':[g+'_ruta']}]
        grupos[ g+'_ruta' ] = {}
        nivel+=[{ 'k_i':[g+'_ruta_index'] }]
        grupos[g+'_ruta_index']={}
        for r in rutas:
            grupos[ g+'_ruta' ][r]=n
            grupos[ g+'_ruta_index'][r] = []
            n+=1
        if 'keyOrd' in filtrar:
            grupos[g+'_keyOrd']=[V.get_iter( grupos[g+'_keyOrd'] ,keys=rutas[r] ) for r in rutas]
            _,grupos[g+'_keyOrd'] = V.igualar_dict( grupos[g+'_keyOrd'] )
            nivel+=[{'keys':[g+'_keyOrd']}]
        for i in range(len(dicts)):
            for r in rutas:
                dicts[i],grupos[g+'_ruta_index'][r] = C.indexado(
                    dicts[i], grupos[g+'_ruta_index'][r],
                    keys_get=rutas[r],
                    keys_set=rutas[r],
                    iterar=iterar,
                    **kw
                    )
            dicts[i] = C.get_rutas( dicts[i],rutas,iterar=iterar )
            if dicts[i].__class__ == dict:
                # convertimos el diccionario a lista
                dicts[i]=list( dicts[i].values() )
        grupos[g]={grupos[g][i]:dicts[i] for i in range(len(grupos[g]))}
        return nivel
    def enrutar_a_index( g,dicts, grupos,indexs,rutas=[],filtrar=[],iterar=1,**kw ):
        nivel=[{keys:[g]}]
        grupos[g]=[k for k in dicts]

        if iterar :
            dicts,grupos[g+'_iterar'] = V.igualar_dict( list(dicts.values()),**kw )
            nivel+=[{'keys':[g+'_iterar']}]
            if 'keyOrd' in filtrar:
                grupos[g+'_keyOrd']=dicts[0][list(dicts[0])[0]]
        else:
            if 'keyOrd' in filtrar:
                grupos[g+'_keyOrd']=dicts[list(dicts)[0]]

        n=0
        nivel+=[{'pass':[g+'_ruta']}]
        grupos[ g+'_ruta' ] = {}
        nivel+=[{ 'k_i':[g+'_ruta_index'] }]
        grupos[g+'_ruta_index']={}
        for r in rutas:
            grupos[ g+'_ruta' ][r]=n
            grupos[ g+'_ruta_index'][r] = []
            n+=1
        if 'keyOrd' in filtrar:
            grupos[g+'_keyOrd']=[V.get_iter( grupos[g+'_keyOrd'] ,keys=rutas[r] ) for r in rutas]
            _,grupos[g+'_keyOrd'] = V.igualar_dict( grupos[g+'_keyOrd'] )
            nivel+=[{'keys':[g+'_keyOrd']}]
        for i in range(len(dicts)):
            for r in rutas:
                dicts[i],grupos[g+'_ruta_index'][r] = C.indexado(
                    dicts[i], grupos[g+'_ruta_index'][r],
                    keys_get=rutas[r],
                    keys_set=rutas[r],
                    iterar=iterar,
                    **kw
                    )
            dicts[i] = C.get_rutas( dicts[i],rutas,iterar=iterar )
            if dicts[i].__class__ == dict:
                # convertimos el diccionario a lista
                dicts[i]=list( dicts[i].values() )
        grupos[g]={grupos[g][i]:dicts[i] for i in range(len(grupos[g]))}
        return nivel

    """
    Proyecto para comprimir listas de 2 dimensiones.
    Reemplazando las secciones [x0:xf] mas repetidas por 
    numeros enteros int. Esta seccion sera guardada 
    dentro de la variable 'index', los 'int' representan 
    la posicion de la seccion en  la variable 'index'
    """
    def veces_seccion(s,m,l=6,end=0):
        """
            veces_seccion(lista_a_buscar,lista_donde_buscar)
            lista de pares [inicio,fin] de numero indice de cada 
            parte donde se repite la seccion 's' en la lista 'm'
            Ejemplo:
                s=[5,8,48]

                #    0   1  2  3  4 5 6 7 8  9  10 11 12 13 14 15 16 
                m=[  4, 54, 5, 8,48,6,5,5,8,48,654, 0, 6, 4, 5, 8,48]
                #  -17 -16  .  .  . . . . .  .   .  . -5 -4 -3 -2 -1 

                return [[2,5], [7,10], [14,-1]]
        """
        memo=[]
        if not end: end=len(m)
        for j0 in range(l,end):
            if s == m[j0-l:j0]:
                if not memo:
                    memo+=[[j0-l,j0]]
                elif  memo[-1][1]<=j0-l:
                    memo+=[[j0-l,-1]] if (end-1)==j0 else [[j0-l,j0]]
        return memo

    def reemplazar_s(m,k,memo):
        ret=[]
        #k=-float(k)
        if 0==memo[0][0]:
            ret+=[k]
        else:
            ret+=m[0:memo[0][0]]+[k]
        for j0 in range(len(memo)-1):
            if memo[j0][1]!=memo[j0+1][0]:
                ret+=m[memo[j0][1]:memo[j0+1][0]]+[k]
            elif memo[j0][1]==memo[j0+1][0]:
                ret+=[k]
        if len(m)!=memo[-1][-1]:
            ret+=m[memo[-1][-1]:]
        return ret

    def comprimir_niveles(lista,niveles=[12,8,7,6,5,4,3],index=[]):
        t=[]
        for n in niveles:
            lista,index,p = C.comprimir_List(lista,index=index,l=n)
            t+=[p]
        return lista,index

    def scan_List(lista,index=[],l=6,cont={}):
        #hallando las seccion mas repetida
        for i in range(len(lista)):
            for i0 in range(l,len(lista[i])):
                s=lista[i][i0-l:i0]
                repe= s in index
                if repe: x=index.index(s)
                else: x=len(index)
                for j in range(len(lista)):
                    memo=C.veces_seccion(s,lista[j],l=l)
                    if memo:
                        memo=len(memo)
                        if repe: cont[x]+=memo
                        else:
                            cont[x]=memo
                            index+=[s]
                            repe = True    
        #ordenando las seccion mas repetida
        return index,cont

    def comprimir_List(lista,index_test=[],l=6,cont=None,repeMinimo=3):
        items = sum([ len(k) for k in lista ])
        items+= sum([ len(k) for k in index_test ])
        if cont==None :
            print(
                """ERROR:'cont' no Declarado. 
                Escaneando la lista y agregando al index_test
                scan_list(lista,index=index_test,l=l)...
                """
                )
            index_test,cont=C.scan_List(lista,index=index_test,l=l)
        print("Convertimos 'cont' a list()... len(cont):",len(cont))
        cont=[{'k':c,'n':cont[c]} for c in cont if cont[c]>=repeMinimo]
        end=len(cont)
        print(f'len(cont):{end}\ncont.sort(reverse=True,key= ... )... ')
        cont.sort(reverse=True,key=lambda e : e['n'])
        print('Seccion mas repetida:',cont[0]['n'])
        index_ok=[]
        for s in range(end):
            print((s/end)*100,'%     ',end='\r')
            s = index_test[cont[s]['k']]
            ok = False
            for i in range(len(lista)):
                m=C.veces_seccion(s,lista[i],l=l)
                if m:
                    if not ok:
                        ok=True
                        x=len(index_ok)
                        index_ok+=[s]
                    lista[i]=C.reemplazar_s(lista[i],x,m)
        p(f'\nFueron remplazadas {len(index_ok)} secciones de {end}')
        items_out= sum([len(k) for k in lista])
        items_out+=sum([len(k) for k in index_ok])
        #print(items_out,items,items_out/items)
        return lista,index_ok,(items,items_out,items_out/items)
class infoPWD:
    """docstring for infoSystem"""
    def __init__(self, carpetas={},*arg,**kw):
        super(infoPWD, self).__init__(*arg,**kw)
        self.arg = arg
class p:
    """docstring for p"""
    conf={
        'all_flags':[],
        'prnt':True,
        'logFile':__file__+'.log',
        'flags':['error'],
        'log':False,
        'code':'latin-1'
        }
    def __init__(self,*arg,**kw):
        pass
    def __call__(*arg,**kw):
        p._p(*arg,**kw)
    def config(*arg,**kw):
        if kw=={}:
            return p.conf
        else:
            for k in kw:
                p.conf[k]=kw[k]
    def _p(p,*args,end='\n',sep=' ',flush=True,flag='',command=None,listar=0):
        if not (flag in p.all_flags):
            p.all_flags+=[flag]
        if p.prnt and (flag in p.flags):
            if listar:
                print(flag, p.flags)
                for var in [*args]:
                    print('#'*10+' LISTANDO '+'#'*10+' '+flag)
                    if var.__class__==dict :
                        for k in var:print(k,':',var[k])
                    elif var.__class__ in [list,tuple]:
                        for k in var:print(k)
                    else:
                        print(var,end=end,sep=sep,flush=flush)
                    print()
            else:
                print(*args,end=end,sep=sep,flush=flush)
        if p.log or (command != None):
            valor=''
            for e in [*args]: valor+=str(e)+sep
            valor+=end
            if (command != None): command([*args])
            if p.log:
                V.setFile(
                    p.logFile,
                    valor=valor.encode(p.code),
                    echo='log' in p.flags,
                    modo='ab'
                )
    def getFile( name, full=1,code='',modo='rb',join=None,sep='',prefijo='',buscar=[],campos_list=[]):
        if not code: code=p.conf['code']
        file=open(name,modo)
        ret=[]
        for line in file:
            line=line.decode(code)[:-1]
            if line.strip()!='':
                line=line if full else line.strip()
                if sep :
                    if sep in line: ret += [line.split(sep)]
                else:
                    ret += [line]
        file.close()
        if ret:
            if join==None:
                    return ret if len(ret)>1 else ret[0]
            elif join.__class__ == dict:
                if not sep:sep=':'
                for k in ret:
                    clave=k[0].strip()
                    if buscar:
                        if clave in buscar:
                            join[prefijo+clave]=k[1].strip()
                    else:
                        join[prefijo+clave]=k[1].strip()
                return join
            elif join.__class__ == list:
                if campos_list:
                    for x in range(len(ret)):
                        l=ret[x]
                        ret[x]={campos_list[i]:l[i] for i in range(len(l))}
                return join+ret
            elif join == 'json':
                if campos_list:
                    for x in range(len(ret)):
                        l=ret[x]
                        ret[x]={campos_list[i]:l[i] for i in range(len(l))}
                return join+ret
        else:
            return []
    def setFile(name,valor=[],echo=1,code='',modo='wb'):
        if not code: code=p.conf['code']
        file=open(name,modo)
        if echo: print('Archivo:',name)
        if list == valor.__class__:
            for line in valor:
                if echo: print( line.encode(code) )
                file.write(line.encode(code)+b'\n')    
        else:
            if echo: print(valor)
            file.write(valor+b'\n')
        file.close()  
class object_mbarete:

    """esta clase sera heredada a todas las clases de las demas practicas"""
    def __init__(self,pwd='repo_path',logFile=__file__+'.log',flags=['error'],open_modo='wb',code='utf-8',ignore=[],carpetas={},**kwargs):
        #super(object_mbarete, self).__init__()
        
        #ruta absoluta de donde se esta ejecutando este objeto
        self.pwd = pwd 
        self.historial_pwd=[0,[self.pwd]]
        self.log=False
        self.prnt=True
        self.code=code
        self.logFile=logFile
        self.flags=['']+flags
        self.all_flags=['']+flags
        self.open_modo=open_modo
        self.info_system(carpetas)
        self.info_git()
        self.ignore = ignore+['__pycache__',self.info['file']]
        self.paths_directos()
        if self.pwd in self.carpetas:
            self.pwd=self.carpetas[self.pwd]
        elif os.path.lexists(self.pwd):
            pass
        elif os.path.lexists(os.getcwd()+os.sep+self.pwd):
            self.pwd=os.getcwd()+os.sep+self.pwd
        elif 'git_repo_path' in self.info :
            if os.path.lexists(self.info['git_repo_path']+os.sep+self.pwd): 
                self.pwd=self.info['git_repo_path']+os.sep+self.pwd
        else:
            self.pwd = self.carpetas[self.pwd]
        
    def download_content(self,url,file='descargado_Con_Object_Mbarete'):
        import requests
        url=url.replace("\/","/") 
        try:
            content = requests.get(url)
            binario= open(file,"wb")
            for datos_byte in content.iter_content(100000):
                binario.write(datos_byte)
            binario.close()
        except:
            self.p("ERROR al conectar con el archivo: "+url,flag='error') 
    def if_exist_split(self,exist,t,sino=None):
        #busca que un 'str' de 'exist' que este en 'string' para aplicar 'return string.split(str)', sino encuntra coincidencias 'return sino' 
        return next((t.split(e) for e in exist if e in t),sino)
    def is_extend(self,list_files,list_extens):
        ret=[]
        for f in list_files:
            if f.split('.')[-1] in list_extens:
                ret+=[f]
        return ret
    def paths_directos(self):
        self.carpetas={}
        prefijos={'dir_':4,'web_':4,'pwd_':4,'git_repo_path':4}
        if 'git_repo_path' in self.info :
            repo_path=self.info['git_repo_path'] 
        else:
            repo_path=self.info['dir_repo_path']

        for k in self.info:
            if k[:4] in ['dir_','web_','pwd_']: 
                self.info[k] = repo_path+self.info[k]

        for k in self.info:
            pre=next( ( p for p in prefijos if p==k[:len(p)] ), None )
            if pre in prefijos: 
                self.carpetas[k[prefijos[pre]:]]=self.info[k]

        self.p(self.carpetas,flag='paths_directos',listar=1)

        return self.carpetas
    def go_pwd(self,pwd='',mkdir='',scan=[]):
        #sin terminar
        if os.path.lexists(pwd):
            if mkdir:
                if not mkdir in os.listdir(pwd): 
                    os.mkdir(pwd+os.sep+mkdir)
            os.chdir(pwd+os.sep+mkdir)
            self.historial_pwd[0]+=1
            self.historial_pwd[1]+=[pwd+os.sep+mkdir]
        self.p(os.getcwd())
    def back_pwd(self,pwd=''):
        #historial de navegacion entre directorios
        self.p(os.getcwd())
    def ret_system(self,command,**kw):
        os.system(command+" > "+self.info['home']+'mbarete_tmp')
        ret = self.getFile(
            self.info['home']+'mbarete_tmp',
            **kw
            )
        os.remove(self.info['home']+'mbarete_tmp')
        return ret
    def info_system(self,arg):
        ignorar='.auto.'
        info={
            'file':'info'+ignorar,
            'prefijo':'cross_',
            'file_tmp':'temp_mbarete.',
            'ignorar':ignorar,
            **arg
            }
        if os.name == 'nt':
            import platform
            info={
                **info,
                'OS':'windows',
                'V':os.environ['OS'],
                'tmp':os.environ['TEMP']+os.sep,
                'home':os.environ['USERPROFILE']+os.sep
                }
            info['uname_sysname'] ,info['uname_nodename'] ,info['uname_release'] ,info['uname_version'] ,info['uname_machine'] ,info['uname_processor'] = platform.uname()
            info['uname_version']='"'+info['uname_version']+'"'
        elif 'ANDROID_ROOT' in os.environ:
            info={
                **info,
                'OS':'android',
                'V':os.environ['SHELL'],
                'tmp':'/tmp/',
                'home':os.environ['HOME']+os.sep
                }
        elif os.name == 'posix':
            info=self.getFile(
                '/etc/os-release',
                {
                    **info,
                    'OS':'linux',
                    'tmp':'/tmp/',
                    'home':os.environ['HOME']+os.sep
                    },
                sep='=',
                prefijo='OS_',
                buscar=['VERSION','ID','ID_LIKE','PRETTY_NAME']
            )
            info['uname_sysname'] ,info['uname_nodename'] ,info['uname_release'] ,info['uname_version'] ,info['uname_machine'] = os.uname()
            info['V']='"'+info['OS_ID']+', '+info['OS_PRETTY_NAME'][1:-1]+'"'
            info['uname_version']='"'+info['uname_version']+'"'
        info['sys_prefix']='"'+sys.prefix+'"'
        info['sys_platform']=sys.platform
        info['sys_version']='"'+sys.version.replace('\n',' ')+'"'
        return info
    
    def info_git(self):
        buscar=['git_repo_path','git_repo_name','git_branch','pwd_consolas','pwd_modulos','pwd_servidor']
        buscar=[ self.info['prefijo']+b for b in buscar ]
        self.info['git_branch']=next(
            (e[2:] for e in self.ret_system("git branch") if '*' in e[0]),
            None
            )
        tmp_git=self.info['file_tmp']+self.info['file']
        myTMP=[]
        for file in os.listdir(self.info['home']): 
            if tmp_git in file[:len(tmp_git)]:
                myTMP+=[file]
        self.mis_repos = {}
        for repo in myTMP:
            self.mis_repos[repo[len(tmp_git):]]=self.getFile(
                self.info['home']+repo ,
                join={},
                buscar=buscar,
                sep=':'
            )
        self.p(self.mis_repos,flag='info_git',listar=1)
        if self.info['git_branch']:
            #buscamos la direccion raiz de este repositorio
            h=[os.getcwd()]
            while not '.git' in os.listdir():
                os.chdir('..')
                h+=[os.getcwd()]
            self.info['git_repo_path']=h[-1]+os.sep
            os.chdir(h[0])
            # obtenemos la lista de configuracion de git global y local
            git=self.ret_system("git config --list",join={},sep='=')
            self.p(git,flag='info_git',listar=1)
            config={
                'email':'user.email',
                'username':'user.name'
            }
            for g in config:
                if config[g] in git:
                    self.info['git_'+g]= git[config[g]] 
                else:
                    self.info['git_'+g]=input(f'Ingrese su {g} de github:')
            if 'remote.origin.url' in git:
                (self.info['git_repo_username'],self.info['git_repo_name'])=git['remote.origin.url'].split('/')[-2:]
        else:
            pass
            """
                estos codigos deberian estar generados con 
                la clase consola

            codigo para:
            *instalar git
            *activar git en este proyecto, 'git init'
            *crear cuenta en github
            *metodos de autenticacion del usuario
            *conectar este repositorio con Github
            """
        if not 'git_repo_path' in self.info :
            #esta sera la ruta 'repo_path' de self.carpetas
            self.info['dir_repo_path']=os.getcwd()+os.sep
        self.p(self.info,listar=1,flag='info_git')
    def media_me(self,pwd,ret='media',prefijo='media',sep='_'):
        media={}
        total = 0
        num_archivos = 0
        formato = '%d-%m-%y %H:%M:%S'
        home=[]
        self.p('media_me en ',pwd,self.ignore,flag='media_me')
        for ruta, directorios, archivos in os.walk(pwd, topdown=True):
            ruta='' if ruta==pwd else ruta.replace(pwd,'')
            self.p(ruta,not ruta.split(os.sep)[0] in self.ignore,flag='media_me')
            if not ruta.split(os.sep)[0] in self.ignore:
                if not ruta in home: home+=[ruta]
                for elemento in archivos:
                    num_archivos += 1
                    archivo = ruta+os.sep+elemento if ruta else elemento
                    self.p(archivo,flag='media_me')
                    estado = os.stat(pwd+os.sep+archivo)
                    tamanho = estado.st_size
                    name=prefijo+sep+str(num_archivos)
                    media[name]={
                        'path':os.sep+archivo,
                        'name':elemento,
                        'size':tamanho
                    }
                    ult_acceso = self.dt.fromtimestamp(estado.st_atime)
                    modificado = self.dt.fromtimestamp(estado.st_mtime)
                    ult_acceso = ult_acceso.strftime(formato)
                    modificado = modificado.strftime(formato)
                    total += tamanho
                    media[name]['modificado']=modificado
                    media[name]['ult_acceso']=ult_acceso
        home=[d.replace(pwd,'') for d in home if d]
        home.sort(reverse=False,key=lambda x: len(x.strip(os.sep)))
        if ret=='media':
            media['media_me']={
                'num_archivos':num_archivos,
                'peso_total_kb':round(total/1024, 1),
                'name':prefijo,
                'address':(self.host,self.port),
                'pwd':pwd,
                'home':home
                }
            return media
        elif ret=='lista':
            return [ media[f]['path'] for f in media]
    def p(self,*args,end='\n',sep=' ',flush=True,flag='',command=None,listar=0):
        """
        end='\n'
            Con el parámetro end podemos modificar esto por el valor que queramos.
            print( “Hola”, end = “ @ ”)
            print(“Mundo”)
            El resultado es:
            “Hola @ Mundo”
            No se fue a la siguiente línea.
        sep=' '
            Con el parámetro sep, podemos escribir algo entre esos valores.
            print( “Tengo una”, “ ¿Quieres una ”,  “?”, sep = “Manzana”)
            El resultado sería:
            “Tengo 1 Manzana ¿Quieres una Manzana?”
            Nota: Funciona con variables int y float sin necesidad de convertirlas a String.
        flush=True
            Se recomienda usarlo cuando usamos el comando end. Ya que al usarlo el buffer ya 
            no se vacía (flush), por lo tanto para asegurar que el comando print imprima en 
            cuanto lo llamemos, se recomienda usar el comando flush = True.
            Esto se entiende mejor si contamos elementos pero con un tiempo de espera, así 
            veremos que sin Flush=True, el comando print se actualizará hasta el final.
            import time
            print("Números: ")
            for i in range(8):
                time.sleep(0.5)
                print(i, end=" ",  flush=True)
            Ese código pruébalo con flush=True y flush = False y ahí versa la diferencia.
        """
        if not (flag in self.all_flags):
            self.all_flags+=[flag]
        if self.prnt and (flag in self.flags):
            if listar:
                print(flag, self.flags)
                for var in [*args]:
                    print('#'*10+' LISTANDO '+'#'*10+' '+flag)
                    if var.__class__==dict :
                        for k in var:print(k,':',var[k])
                    elif var.__class__ in [list,tuple]:
                        for k in var:print(k)
                    else:
                        print(var,end=end,sep=sep,flush=flush)
                    print()
            else:
                print(*args,end=end,sep=sep,flush=flush)
        if self.log or (command != None):
            valor=''
            for e in [*args]: valor+=str(e)+sep
            valor+=end
            if (command != None): command([*args])
            if self.log:
                self.setFile(
                    self.logFile,
                    valor=valor.encode(self.code),
                    echo='log' in self.flags,
                    modo='ab'
                )
    def getFile(self, name, full=1,code='',modo='rb',join=None,sep='',prefijo='',buscar=[],campos_list=[]):
        if not code: code=self.code
        file=open(name,modo)
        ret=[]
        for line in file:
            line=line.decode(code)[:-1]
            if line.strip()!='':
                line=line if full else line.strip()
                if sep :
                    if sep in line: ret += [line.split(sep)]
                else:
                    ret += [line]
        file.close()
        if ret:
            if join==None:
                    return ret if len(ret)>1 else ret[0]
            elif join.__class__ == dict:
                if not sep:sep=':'
                for k in ret:
                    clave=k[0].strip()
                    if buscar:
                        if clave in buscar:
                            join[prefijo+clave]=k[1].strip()
                    else:
                        join[prefijo+clave]=k[1].strip()
                return join
            elif join.__class__ == list:
                if campos_list:
                    for x in range(len(ret)):
                        l=ret[x]
                        ret[x]={campos_list[i]:l[i] for i in range(len(l))}
                return join+ret
            elif join == 'json':
                if campos_list:
                    for x in range(len(ret)):
                        l=ret[x]
                        ret[x]={campos_list[i]:l[i] for i in range(len(l))}
                return join+ret
        else:
            return []
    def setFile(self,name,valor=[],echo=1,code='',modo='wb'):
        if not code: code=self.code
        file=open(name,modo)
        if echo: print('Archivo:',name)
        if list == valor.__class__:
            for line in valor:
                if echo: print( line.encode(code) )
                file.write(line.encode(code)+b'\n')    
        else:
            if echo: print(valor)
            file.write(valor+b'\n')
        file.close()  

if 'main' in __name__:
    import pruebas
    pruebas=[]
    main_pruebas(pruebas)
d={
    'img':os.getcwd()+os.sep+"media"+os.sep,
    'audio':os.getcwd()+os.sep+"media"+os.sep
    }
flatpak_status= [
    {'Nombre': 'KDE Application Platform', 'AppID': 'org.kde.Platform', 'Version': '', 'Branch': '5.15', 'Installation': 'system', 'ID': 'org.kde.Platform', 'Referencia': 'runtime/org.kde.Platform/x86_64/5.15', 'Arquitectura': 'x86_64', 'Rama': '5.15', 'License': 'GPL-2.0+', 'Origen': 'flathub', 'Collection': 'org.flathub.Stable', 'Installed': 1024, 'Commit': 'dc1c3d01cc95b500c9c334e7e54cf80e2179ac5ab53f2e3fbc63cc7e34ecd448', 'Parent': '1cb4374f4cc2438ca9674ae683b38fb1dbe74704d28cd8508349c81f6228b3d3', 'Subject': 'build of org.kde.Sdk, Fri 11 Feb 2022 03', 'Date': '2022-02-11 23', 'autoremove': 1}, 
    {'Nombre': 'ONLYOFFICE Desktop Editors', 'AppID': 'org.onlyoffice.desktopeditors', 'Version': '7.0.1', 'Branch': 'stable', 'Installation': 'system', 'ID': 'org.onlyoffice.desktopeditors', 'Referencia': 'app/org.onlyoffice.desktopeditors/x86_64/stable', 'Arquitectura': 'x86_64', 'Rama': 'stable', 'License': 'AGPL-3.0-only', 'Origen': 'flathub', 'Collection': 'org.flathub.Stable', 'Installed': 1000, 'Runtime': 'org.freedesktop.Platform/x86_64/20.08', 'Sdk': 'org.freedesktop.Sdk/x86_64/20.08', 'Commit': '37830664975b3e1cd4458b208b3796fcf55f81b7d3066104b68d921332d65628', 'Parent': '59283778536e5ab0c763b91a22b4bbf188d8785785673767eeae836d2dfce38b', 'Subject': 'Fix bug #44321 (#56) (7941a8c4)', 'Date': '2022-03-09 14', 'autoremove': 1}, 
    {'Nombre': 'GNOME Application Platform version 41', 'AppID': 'org.gnome.Platform', 'Version': '', 'Branch': '41', 'Installation': 'system', 'ID': 'org.gnome.Platform', 'Referencia': 'runtime/org.gnome.Platform/x86_64/41', 'Arquitectura': 'x86_64', 'Rama': '41', 'License': 'GPL-2.0+', 'Origen': 'flathub', 'Collection': 'org.flathub.Stable', 'Installed': 768, 'Commit': '6603dc6b728731bbaa7f1f1abbae3007cc3f029f72c40a9f1c43c7ff3c799b4f', 'Parent': 'b0aed9b5fb8b5e3e1e1badc8711fa34667760cf5ce79b2727b8d8c21d4772577', 'Subject': 'Export org.gnome.Platform', 'Date': '2022-03-05 08', 'autoremove': 1}, 
    {'Nombre': 'Freedesktop Platform', 'AppID': 'org.freedesktop.Platform', 'Version': '20.08.18', 'Branch': '20.08', 'Installation': 'system', 'ID': 'org.freedesktop.Platform', 'Referencia': 'runtime/org.freedesktop.Platform/x86_64/20.08', 'Arquitectura': 'x86_64', 'Rama': '20.08', 'License': 'GPL-2.0+', 'Origen': 'flathub', 'Collection': 'org.flathub.Stable', 'Installed': 743, 'Commit': '0e5f59c847f90b344208dc0f2b67bc27c9e4f3ab1a1a78fa56cdd0fb81c35274', 'Parent': '2857bbad6f429653e6bb3534568e1900eac395196bcac7641ef21f7950eb9898', 'Subject': 'Export org.freedesktop.Platform', 'Date': '2022-02-12 15', 'autoremove': 1}, 
    {'Nombre': 'Mesa', 'AppID': 'org.freedesktop.Platform.GL.default', 'Version': '21.3.6', 'Branch': '21.08', 'Installation': 'system', 'ID': 'org.freedesktop.Platform.GL.default', 'Referencia': 'runtime/org.freedesktop.Platform.GL.default/x86_64/21.08', 'Arquitectura': 'x86_64', 'Rama': '21.08', 'License': 'MIT', 'Origen': 'flathub', 'Collection': 'org.flathub.Stable', 'Installed': 387, 'Commit': 'de4df0d5f0e86d0b03baf4616d5686851a53d38c1d8b89f34d220c062655ae1b', 'Parent': 'e9fde4c03364608fdad1f6bd5d794089e4c41e37e40ec496a49d15c290b682a6', 'Subject': 'Export org.freedesktop.Platform.GL.default', 'Date': '2022-03-02 19', 'autoremove': 1}, 
    {'Nombre': 'Mesa', 'AppID': 'org.freedesktop.Platform.GL.default', 'Version': '21.1.8', 'Branch': '20.08', 'Installation': 'system', 'ID': 'org.freedesktop.Platform.GL.default', 'Referencia': 'runtime/org.freedesktop.Platform.GL.default/x86_64/20.08', 'Arquitectura': 'x86_64', 'Rama': '20.08', 'License': 'MIT', 'Origen': 'flathub', 'Collection': 'org.flathub.Stable', 'Installed': 313, 'Commit': '7cd6707e605cd492e251c4414020c4dfe6d6ca317032be35cd0604a1b2e9eb00', 'Parent': '20aba59249164e809da18f80f162d1a3d1ed8832df969d51dc9eba653c66bd03', 'Subject': 'Export org.freedesktop.Platform.GL.default', 'Date': '2022-02-12 15', 'autoremove': 1}, 
    {'Nombre': 'Kiwix', 'AppID': 'org.kiwix.desktop', 'Version': '2.2.1', 'Branch': 'stable', 'Installation': 'system', 'ID': 'org.kiwix.desktop', 'Referencia': 'app/org.kiwix.desktop/x86_64/stable', 'Arquitectura': 'x86_64', 'Rama': 'stable', 'License': 'GPL-3.0+', 'Origen': 'flathub', 'Collection': 'org.flathub.Stable', 'Installed': 174, 'Runtime': 'org.kde.Platform/x86_64/5.15', 'Sdk': 'org.kde.Sdk/x86_64/5.15', 'Commit': '83f98eae80001d0c2b152cdb6ca7c9fc512bebb23a1ee7147d365de61de0daa1', 'Parent': '2233c497681e6a9be980fd79642b6b057e21b832d24c00712c59226887fac74c', 'Subject': 'Update to version 2.2.1 (87f0c47e)', 'Date': '2022-03-11 16', 'autoremove': 1}, 
    {'Nombre': 'AbiWord', 'AppID': 'com.abisource.AbiWord', 'Version': '3.0.5', 'Branch': 'stable', 'Installation': 'system', 'ID': 'com.abisource.AbiWord', 'Referencia': 'app/com.abisource.AbiWord/x86_64/stable', 'Arquitectura': 'x86_64', 'Rama': 'stable', 'License': 'GPL-2.0-or-later', 'Origen': 'flathub', 'Collection': 'org.flathub.Stable', 'Installed': 76, 'Runtime': 'org.gnome.Platform/x86_64/41', 'Sdk': 'org.gnome.Sdk/x86_64/41', 'Commit': 'f3763378d6e6b54e8de4d56310b3e86d36d863a6f282911a069f43c0b5ea7656', 'Parent': '58451d4b5b83e0410fbc682ea4549c02b547b700383353dc28b191190dda76bf', 'Subject': 'Update libwmf to 0.2.12 (456ffae2)', 'Date': '2021-12-21 02', 'autoremove': 1}, 
    {'Nombre': 'Intel', 'AppID': 'org.freedesktop.Platform.VAAPI.Intel', 'Version': '', 'Branch': '20.08', 'Installation': 'system', 'ID': 'org.freedesktop.Platform.VAAPI.Intel', 'Referencia': 'runtime/org.freedesktop.Platform.VAAPI.Intel/x86_64/20.08', 'Arquitectura': 'x86_64', 'Rama': '20.08', 'Origen': 'flathub', 'Collection': 'org.flathub.Stable', 'Installed': 46, 'Commit': 'ae904b9978a9f36d2812c7c9afb366e5da3d376d956725136bbf0ba7354f6444', 'Parent': '231db1962d03a83867da2aff086f5aa2e099eb3b377a458d2454e37979b07320', 'Subject': 'Export org.freedesktop.Platform.VAAPI.Intel', 'Date': '2022-02-12 15', 'autoremove': 1}, 
    {'Nombre': 'Intel', 'AppID': 'org.freedesktop.Platform.VAAPI.Intel', 'Version': '', 'Branch': '21.08', 'Installation': 'system', 'ID': 'org.freedesktop.Platform.VAAPI.Intel', 'Referencia': 'runtime/org.freedesktop.Platform.VAAPI.Intel/x86_64/21.08', 'Arquitectura': 'x86_64', 'Rama': '21.08', 'Origen': 'flathub', 'Collection': 'org.flathub.Stable', 'Installed': 46, 'Commit': '1bc1f826fcae6ece0a9674ef0c8ab0607b815f9e339b3f6df561ded8711b0b19', 'Parent': '45d65f23e5f7fa198a50b45049418aed8e17ee6069dc60c3ecbba75c3d1ff74c', 'Subject': 'Export org.freedesktop.Platform.VAAPI.Intel', 'Date': '2022-03-02 19', 'autoremove': 1}, 
    {'Nombre': 'Adwaita theme', 'AppID': 'org.kde.KStyle.Adwaita', 'Version': '', 'Branch': '5.15', 'Installation': 'system', 'ID': 'org.kde.KStyle.Adwaita', 'Referencia': 'runtime/org.kde.KStyle.Adwaita/x86_64/5.15', 'Arquitectura': 'x86_64', 'Rama': '5.15', 'Origen': 'flathub', 'Collection': 'org.flathub.Stable', 'Installed': 17, 'Commit': '9eec9ea75af698fd44a2f987502bf32c8108e4f599564383b3bd54ab1e44efed', 'Parent': '02860ce9758a0f06f12c33baa2b84d0b8a571176cf67cabbe004c7c2059f065f', 'Subject': 'Update to 1.4.1 (97db0efb)', 'Date': '2022-01-12 08', 'autoremove': 1}, 
    {'Nombre': 'Adwaita theme', 'AppID': 'org.kde.KStyle.Adwaita', 'Version': '', 'Branch': '5.15-21.08', 'Installation': 'system', 'ID': 'org.kde.KStyle.Adwaita', 'Referencia': 'runtime/org.kde.KStyle.Adwaita/x86_64/5.15-21.08', 'Arquitectura': 'x86_64', 'Rama': '5.15-21.08', 'Origen': 'flathub', 'Collection': 'org.flathub.Stable', 'Installed': 16, 'Commit': 'ba4fc825c4849595ae9384d14b9687b05f7f6539faa0acd1a64cb1f0bb2a46bf', 'Parent': 'f4e139ecde7fbc0b2f739fa8f511666b17589c3980a5be0ada97a64b0977a026', 'Subject': 'Update to 1.4.1 (c6da3ec0)', 'Date': '2022-01-12 08', 'autoremove': 1}, 
    {'Nombre': 'ffmpeg-full', 'AppID': 'org.freedesktop.Platform.ffmpeg-full', 'Version': '', 'Branch': '21.08', 'Installation': 'system', 'ID': 'org.freedesktop.Platform.ffmpeg-full', 'Referencia': 'runtime/org.freedesktop.Platform.ffmpeg-full/x86_64/21.08', 'Arquitectura': 'x86_64', 'Rama': '21.08', 'Origen': 'flathub', 'Collection': 'org.flathub.Stable', 'Installed': 11, 'Commit': 'fa66f4ef14fb4d14e42877785f844d0cdad2afd2c7c4728fc052c02034a15da0', 'Parent': '6e8bc383622e6c05a83cae95cd2676ea64946b5eae965ffa1999819a58815f1f', 'Subject': 'Export org.freedesktop.Platform.ffmpeg-full', 'Date': '2022-01-08 13', 'autoremove': 1}, 
    {'Nombre': 'openh264', 'AppID': 'org.freedesktop.Platform.openh264', 'Version': '2.1.0', 'Branch': '2.0', 'Installation': 'system', 'ID': 'org.freedesktop.Platform.openh264', 'Referencia': 'runtime/org.freedesktop.Platform.openh264/x86_64/2.0', 'Arquitectura': 'x86_64', 'Rama': '2.0', 'License': 'LicenseRef-proprietary=https', 'Origen': 'flathub', 'Collection': 'org.flathub.Stable', 'Installed': 1, 'Commit': '73f998362a6fc0d57e0c7e83e928d32b0ec14d10d0d94291033976bdcecc6b6b', 'Parent': '15266352ca7587793d013fdb17530a24d728e09be4f4cf315dc5bf99ad4323e8', 'Subject': 'Export org.freedesktop.Platform.openh264', 'Date': '2020-06-18 15', 'autoremove': 1}
    ]
tabla_automatica=[{
    'Nombre':'Lucas Mathias',
    'mes':5,
    'year':1995,
    'dia':21,
    'peso':90,
    'altura':1.73,
    'pasa':False,
    'tecla':b'\n\r',
    'nadaDeNada':None
    }]
widgets={
        'nav':{
            'inputType':"panel",
            "etiquetas":['id','default','panel'],#AUTOMATICO/OBLIGATORIO
            "typeSalida":"command",#OPCIONAL
            "name":'menu',#OBLIGATORIO
            "text":'Menu',#OBLIGATORIO
            'anchor':'o', 
            'fontSize':15,
            'width':15,
            'bgColor':'#f00904',
            'degradado':0, 
            'inputs':{
                'inicio':{
                    'inputType':'Button',
                    'command':'inicio',
                    'text':'Lista de Proyectos'
                },
                'nuevo':{
                    'inputType':'Button',
                    'command':'nuevo',
                    'text':'Nuevo Proyecto'
                },
                'bbdd':{
                    'inputType':'Button',
                    'command':'bbdd',
                    'text':'Base de Datos'
                },
                'formulario':{
                    'inputType':'Button',
                    'command':'formulario',
                    'text':'Cargar Datos'
                }
            }
        },
        'nuevo':{
            'inputType':"Frame",
            "etiquetas":['id','Nuevo','Frame','menu'],#AUTOMATICO/OBLIGATORIO
            "typeSalida":"command",#OPCIONAL
            "name":'nuevo',#OBLIGATORIO
            "text":'Nuevo Proyecto',#OBLIGATORIO
            'fontSize':12,
            'visible':0,
            'bgColor':'#080904',
            'degradado':0, 
            'inputs':{
                'autor':{
                    'inputType':'Entry',
                    'descripcion':'',
                    'text':'Autor:',
                    'value':'Lucas Mathias Villalba Diaz'
                },
                'name':{
                    'inputType':'Entry',
                    'descripcion':'',
                    'text':'Nombre CamelCase:',
                    'value':'BorrarAhora'
                },
                'text':{
                    'inputType':'Entry',
                    'descripcion':'',
                    'text':'Nombre normal:',
                    'value':'Borrar'
                },
                'descripcionBreve':{
                    'inputType':'Entry',
                    'descripcion':'',
                    'text':'Descripcion breve:',
                    'value':''
                },
                'descripcionLarga':{
                    'inputType':'Entry',
                    'descripcion':'',
                    'text':'Descripcion larga:',
                    'value':''
                },
                'img':{
                    'inputType':'Entry',
                    'descripcion':'',
                    'text':'Imagen del proyecto:',
                    'value':'logo.png'
                },
                'enlace':{
                    'inputType':'Entry',
                    'descripcion':'',
                    'text':'Enlace o link para Contacto:',
                    'value':'mathiaslucasvidipy@gmail.com'
                },
                'etiquetas':{
                    'inputType':'Entry',
                    'descripcion':'practicas Matplotlib,graficos',
                    'text':'Etiquetas para este proyecto, separadas por comas (,):',
                    'value':'default,inicio'
                },
                'media':{
                    'inputType':'Checkbutton',
                    'text':'Crear Carpeta [ media ]',
                    'value':1.0
                },
                'dirmedia':{
                    'inputType':'Entry',
                    'descripcion':'carpeta 1,carpeeta 2, etc...',
                    'text':'Nombre para las carpetas dentro de la carpeta [ media ], separadas por comas (,):',
                    'value':'img,js,css,txt,audio'
                },
                'biblio':{
                    'inputType':'Checkbutton',
                    'text':'Crear Carpeta [ bibliografia ]',
                    'value':1.0
                },
                'dirbiblio':{
                    'inputType':'Entry',
                    'descripcion':'carpeta 1,carpeeta 2, etc...',
                    'text':'Nombre para las carpetas en la carpeta [ bibliografia ], separadas por comas (,):',
                    'value':'pdf,img,audio,webSites,txt'
                },
                'backup':{
                    'inputType':'Checkbutton',
                    'text':'Crear Carpeta [ Copias_de_Seguridad ]',
                    'value':1.0
                },
                'dirbackup':{
                    'inputType':'Entry',
                    'descripcion':'carpeta 1,carpeta 2, etc...',
                    'text':'Nombre para las carpetas en la carpeta [ Copias_de_Seguridad ], separadas por comas (,):',
                    'value':'Tablas,Sql,txt'
                },
                'panelUbicacion':{
                        'inputType':"Radiobutton",
                        'text':'Ubicacion del Panel de Inicio',#OBLIGATORIO
                        'radios':{
                            'n':'Superior','s':'Inferior',
                            'e':'Derecha','o':'Izquierda'
                            }
                },
                'frame':{
                    'inputType':'Checkbutton',
                    'text':'Crear un widget Frame por default',
                    'value':1.0
                },
                'os':{'inputType':'Checkbutton','text':'import os','value':0.0},
                'sys':{'inputType':'Checkbutton','text':'import sys','value':0.0},
                'math':{'inputType':'Checkbutton','text':'import math','value':0.0},
                'time':{'inputType':'Checkbutton','text':'import time','value':0.0},
                'datetime':{'inputType':'Checkbutton','text':'import datetime','value':0.0},
                'threading':{'inputType':'Checkbutton','text':'import threading','value':0.0},
                'sqlite':{'inputType':'Checkbutton','text':'import sqlite3','value':0.0},
                'PIL':{'inputType':'Checkbutton','text':'from PIL import Image, ImageTk','value':0.0},
                'crear':{
                    'inputType':'Button',
                    'command':'crear',
                    'text':'Crear Proyecto'
                },
                'borrar':{
                    'inputType':'Button',
                    'command':'borrar',
                    'text':'Borrar Todo'
                },
                'cancelar':{
                    'inputType':'Button',
                    'command':'cancelar',
                    'text':'Cancelar'
                }
            }
        },
        'bbdd':{
            'inputType':"Frame",
            "etiquetas":['id','bbdd','Frame','menu'],#AUTOMATICO/OBLIGATORIO
            "typeSalida":"command",#OPCIONAL
            "name":'bbdd',#OBLIGATORIO
            "text":'Base de Datos',#OBLIGATORIO
            'width':25,
            'fontSize':10,
            'bgColor':'#080904', 
            'degradado':0, 
            'inputs':{
                'filesql':{
                    'inputType':'Entry',
                    'descripcion':'FICHERO.sql',
                    'text':'Fichero Sqlite3:',
                    'value':''
                },
                'filepy':{
                    'inputType':'Entry',
                    'descripcion':'FICHERO.py',
                    'text':'Script Python:',
                    'value':''
                },
                'filecsv':{
                    'inputType':'Entry',
                    'descripcion':'FICHERO.csv',
                    'text':'Fichero CSV:',
                    'value':''
                },
                'crearPY':{
                    'inputType':'Button',
                    'command':'exportarPython',
                    'text':'Exportar a Script.py'
                },
                'crearCSV':{
                    'inputType':'Button',
                    'command':'exportarCSV',
                    'text':'Exportar a CSV'
                }
            }
        },
        'formulario':{
            'inputType':"Frame",
            "etiquetas":['id','formulario','Frame','menu'],#AUTOMATICO/OBLIGATORIO
            "typeSalida":"command",#OPCIONAL
            "name":'formulario',#OBLIGATORIO
            "text":'Cargar Datos',#OBLIGATORIO
            'width':25,
            'fontSize':10,
            'crearTabla':1,
            'bgColor':'#080904',
            'subProyecto':'prueba_gui_full',
            'degradado':0, 
            'inputs':{
                'nombres':{
                    'inputType':'Entry',
                    'descripcion':'Nombres',
                    'text':'Nombre:',
                    'value':''
                },
                'apellidos':{
                    'inputType':'Entry',
                    'descripcion':'Apellidos',
                    'text':'Apellidos:',
                    'value':''
                },
                'direccion':{
                    'inputType':'Entry',
                    'descripcion':'Donde vives?',
                    'text':'Direccion Actual:',
                    'value':''
                }
            }
        },
        'subProyectos':{
            'inputType':"Frame",
            "etiquetas":['id','Inicio','Frame'],#AUTOMATICO/OBLIGATORIO
            "typeSalida":"command",#OPCIONAL
            "name":'inicio',#OBLIGATORIO
            "text":'Lista de Los Sub Proyectos',#OBLIGATORIO
            'fontSize':15,
            'visible':0,
            'bgColor':'#f00904',
            'degradado':0, 
            'inputs':{}
        }
    }

