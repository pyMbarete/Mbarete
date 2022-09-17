#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Modulos importados
import time,datetime
import os
#Declaracion de las funciones
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
def strToVar(strng,type_class=None):
    divisorDate = str(datetime.date.today())[4]
    string = str(strng).strip()
    start = ["{","(","[","'",'"']
    stop = ["}",")","]","'",'"']
    formato=type_class
    nivel=0
    try:
        if "-" in string:
            ret=float(string[1:])
            formato="negativo"
        if ("." in string) and ("-" not in string):
            ret=float(string)
            formato="float"
        if "." not in string and ("-" not in string):
            ret=int(float(string))
            formato="int"
    except Exception as e:
        formato=type_class
    if not formato:
        try:
            if (divisorDate in string):
                if (":" in string) and ( ":"==string.split(" ")[1][2]) and ( ":"==string.split(" ")[1][5]) and ( "."==string.split(" ")[1][8]):
                    formato="time"
                elif (-1 < int(string.split(divisorDate)[0])) and (-1 < int(string.split(divisorDate)[1])) and (-1 < int(string.split(divisorDate)[2])):
                    formato="date"
        except Exception as e:
            formato=type_class
    if string=="":
        return string
    elif formato == "date":
        #retorna datetime.date(int dia, int mes, int año) 
        ret=datetime.date(int(string.split("-")[0]),int(string.split("-")[1]),int(string.split("-")[2]))
        return ret
    elif formato == "time":
        #retorna datetime(año,mes,dia,hora,minutos,segundos,milisegundos) 
        ret=datetime.datetime(int(string[0:4]),int(string[5:7]),int(string[8:10]),int(string[11:13]),int(string[14:16]),int(string[17:19]),int(string[20:]))
        return ret
    elif (string[0]=="{") and (string[-1]=="}"):
        #retorna dict
        ret ={}
        string=string[1:-1]
        comasDivisores=[-1]
        dosPuntos=[]
        comilla=0
        for x in range(0,len(string),1):
            if string[x] in start:
                if string[x] not in ['"',"'"]:
                    nivel += 1
                if string[x]==comilla:
                    nivel -= 1
                    comilla = 0
                elif (string[x] in ['"',"'"]) and (comilla not in ['"',"'"]):
                    nivel += 1
                    comilla=string[x]
            elif string[x] in stop:
                nivel -= 1
            if (string[x]==",") and (nivel==0):
                comasDivisores.append(x)
            if (string[x]==":") and (nivel==0):
                dosPuntos.append(x)
        for x in range(1,len(comasDivisores),1):
            ret.setdefault(strToVar(string[comasDivisores[x-1]+1:dosPuntos[x-1]]),strToVar(string[dosPuntos[x-1]+1:comasDivisores[x]]))
        ret.setdefault(strToVar(string[comasDivisores[-1]+1:dosPuntos[-1]]),strToVar(string[dosPuntos[-1]+1:]))
        return ret
    elif (string[0]=="[") and (string[-1]=="]"):
        ret =[]
        string=string[1:-1]
        comasDivisores=[-1]
        comilla=0
        for x in range(0,len(string),1):
            if string[x] in start:
                if string[x] not in ['"',"'"]:
                    nivel += 1
                if string[x]==comilla:
                    nivel -= 1
                    comilla = 0
                elif (string[x] in ['"',"'"]) and (comilla not in ['"',"'"]):
                    nivel += 1
                    comilla=string[x]
            elif string[x] in stop:
                nivel -= 1
            if (string[x]==",") and (nivel==0):
                comasDivisores.append(x)
        for x in range(1,len(comasDivisores),1):
            ret.append(strToVar(string[comasDivisores[x-1]+1:comasDivisores[x]]))
        ret.append(strToVar(string[comasDivisores[-1]+1:]))
        return ret
    elif (string[0]=="(") and (string[-1]==")"):
        #retornatupla
        ret =[]
        string=string[1:-1]
        comasDivisores=[-1]
        for x in range(0,len(string),1):
            if string[x] in start:
                nivel += 1
            if string[x] in stop:
                nivel -= 1
            if (string[x]==",") and (nivel==0):
                comasDivisores.append(x)
        for x in range(1,len(comasDivisores),1):
            ret.append(strToVar(string[comasDivisores[x-1]+1:comasDivisores[x]]))
        ret.append(strToVar(string[comasDivisores[-1]+1:]))
        return tuple(ret)
    elif (string=="True") or (string=="False"):
        return True if string=="True" else False
    elif  (formato=="negativo"):    
        return -1*float(string.replace('-',''))
        
    elif  (formato=="float"):        
        #retornamos un float
        return float(string)
    elif formato=="int":
        #retornamos un int
        return int(float(string))
    elif ((formato!="int") and (formato!="float") and (formato!="date") and (formato!="negativo")):
        #retornamos un str
        if (string[0] in start) and (string[-1] in stop):
            return string[1:-1]
        else:
            return string
    else:
        print("NO HAY FORMATO")
        return string

class clienteSQL(object):
    def __init__(self,padre,dbname='postgres',user='postgres',password='secret666',host='localhost',port='5432'):
        self.sql=padre
        self.connect_kwarg = {
            'dbname':dbname,
            'user':user,
            'password':password,
            'host':host,
            'port':port
        }
        self.dbname=dbname
        self.status=0
    def connect(self,dirCRUD=''):
        if not self.status:
            if dirCRUD:
                self.con = self.sql.connect(dirCRUD)
            elif self.query['name']=='sqLite3':
                self.con = self.sql.connect(self.dbname)
            else:
                self.con = self.sql.connect(**self.connect_kwarg)
            self.cursor = self.con.cursor()
            self.status=1
    def execute(self,comandoSQL,**kwargs):
        self.connect(**kwargs)
        self.cursor.execute(comandoSQL)
    def execute_commit(self,comandoSQL,**kwargs):
        self.connect(**kwargs)
        self.cursor.execute(comandoSQL)
        self.con.commit()
    def execute_close(self,comandoSQL,**kwargs):
        self.connect(**kwargs)
        self.cursor.execute(comandoSQL)
        self.con.commit()
        self.close()
    def close(self):
        self.cursor.close()
        self.status=0

#SELECT name FROM (SELECT * FROM sqlite_schema UNION ALL SELECT * FROM sqlite_temp_schema) WHERE type='table' ORDER BY name
query_sqLite3={
    'name':'sqLite3',
    'encode':0,
    'NoneType':lambda c: "%s Byte"%(c),
    'bytes':lambda c: "%s Byte"%(c),
    'bool':lambda c: "%s boolean"%(c),
    'float':lambda c: "%s double"%(c),
    'str':lambda c: "%s text"%(c),
    'int':lambda c: "%s integer"%(c),
    'primary_key':lambda c: "%s integer not null primary key autoincrement"%(c),
    'insert_into':lambda t,c,v: "insert into %s %s values %s"%(t,c,v),
    'create_table':lambda t,c: "CREATE TABLE IF NOT EXISTS %s %s"%(t,c),
    'select_all':lambda t: "SELECT * FROM '%s'"%(str(t)),
    'delete_from_where':lambda t,c,v: "DELETE FROM %s WHERE %s='%s'"%(t,c,v),
    'show_bbdd':"SELECT * FROM sqlite_master",
    'show_schema':"SELECT name FROM (SELECT * FROM sqlite_master UNION ALL SELECT * FROM sqlite_temp_master) WHERE type='table' ORDER BY name",
    'use_show_tables':lambda BBDD: "SELECT name FROM sqlite_master WHERE type='table' ORDER BY name;",
    'use_describe_table':lambda BBDD,t: "USE %s ;DESCRIBE %s"%(BBDD,t),
    'drop_table_if_exists':lambda BBDD,t: "USE %s ;DROP TABLE IF EXISTS %s"%(BBDD,t),
    'truncate_table':lambda BBDD,t: "USE %s ;TRUNCATE TABLE %s"%(BBDD,t),
    'rename_table':lambda BBDD,t0,t: "USE %s ;RENAME TABLE %s TO %s"%(BBDD,t0,t)
    }


query_postgres={
    'name':'postgres',
    'encode':0,
    'NoneType':lambda c: "%s Byte"%(c),
    'bytes':lambda c: "%s Byte"%(c),
    'bool':lambda c: "%s boolean"%(c),
    'float':lambda c: "%s double"%(c),
    'str':lambda c: "%s text"%(c),
    'int':lambda c: "%s int"%(c),
    'primary_key':lambda c: "%s Serial"%(c),
    'insert_into':lambda t,c,v: "INSERT INTO %s%s VALUES %s;"%(t,c,v),
    'create_table':lambda t,c: "CREATE TABLE IF NOT EXISTS %s%s;"%(t,c),
    'select_all':lambda t: "SELECT * FROM %s;"%(str(t)),
    'delete_from_where':lambda t,c,v: "DELETE FROM %s WHERE %s='%s';"%(t,c,v),
    'show_bbdd':"SHOW DATABASE",
    'use_show_tables':lambda BBDD: "USE %s ;SHOW TABLES"%(BBDD),
    'use_describe_table':lambda BBDD,t: "USE %s ;DESCRIBE %s"%(BBDD,t),
    'drop_table_if_exists':lambda BBDD,t: "USE %s ;DROP TABLE IF EXISTS %s"%(BBDD,t),
    'truncate_table':lambda BBDD,t: "USE %s ;TRUNCATE TABLE %s"%(BBDD,t),
    'rename_table':lambda BBDD,t0,t: "USE %s ;RENAME TABLE %s TO %s"%(BBDD,t0,t)
    }
query_MySQL={
    'name':'MySQL',
    'encode':0,
    'NoneType':lambda c: "%s Byte"%(c),
    'bytes':lambda c: "%s Byte"%(c),
    'bool':lambda c: "%s boolean"%(c),
    'float':lambda c: "%s double"%(c),
    'str':lambda c: "%s text"%(c),
    'int':lambda c: "%s int"%(c),
    'primary_key':lambda c: "%s Serial"%(c),
    'insert_into':lambda t,c,v: "INSERT INTO %s%s VALUES %s;"%(t,c,v),
    'create_table':lambda t,c: "CREATE TABLE IF NOT EXISTS %s%s;"%(t,c),
    'select_all':lambda t: "SELECT * FROM %s;"%(str(t)),
    'delete_from_where':lambda t,c,v: "DELETE FROM %s WHERE %s='%s';"%(t,c,v),
    'show_bbdd':"SHOW DATABASE",
    'use_show_tables':lambda BBDD: "USE %S ;SHOW TABLES"%(BBDD),
    'use_describe_table':lambda BBDD,t: "USE %S ;DESCRIBE %s"%(BBDD,t),
    'drop_table_if_exists':lambda BBDD,t: "USE %S ;DROP TABLE IF EXISTS %s"%(BBDD,t),
    'truncate_table':lambda BBDD,t: "USE %S ;TRUNCATE TABLE %s"%(BBDD,t),
    'rename_table':lambda BBDD,t0,t: "USE %S ;RENAME TABLE %s TO %s"%(BBDD,t0,t)
    }

class CRUD(clienteSQL):
    """
        La clase para administrar la base de datos 
            estructura del diccionario de tablas:
                tablas={
                    'nombreTabla':{'campoID':['campoID','campo1','campo2','campo3','campo4','campo5']}
                }
    """
    def __init__(self,padre, tabla, query=query_sqLite3, campoAutoincrement='id', reset=0,**kwargs):
        super(CRUD, self).__init__(padre, **kwargs)
        """
        bb='Mbarete.sql' nombre de la base de datos y del archivo que sera el contenedor del gestor de base de datos Sqlite3
        reset=1 borrara el archivo con el nombre 'miBaseDeDatos.sql' que le pases como parametro en dirCRUD='miBaseDeDatos.sql', 'Mbarete.sql' es el archivo que se crea por defecto si no se asigna un nombre diferente a 'dirCRUD'
        reset=0 no eliminara el archivo 'Mbarete.sql' y ejecutara los comandos SQL  en el archivo, si hacemos cambios en la estructura de una tabla en la base de datos debemois resetar el archivo para poder
        """
        self.query=query
        self.query['getCampo']=lambda c,r:self.query[str(r.__class__)[8:-2]](c)
        if (' ' in campoAutoincrement):
            self.campoID=campoAutoincrement 
        else: 
            self.campoID=self.query['primary_key'](campoAutoincrement)

        self.reset=reset
        if not '.' in self.dbname.split(os.sep)[-1]:
            self.extencionCRUD='.sql'
        else:
            self.extencionCRUD='.'+self.dbname.split('.')[-1]

        self.tablas=tabla
        if self.reset:
            if (os.path.exists(self.dbname)):
                os.remove(self.dbname)
            for tabl in self.tablas:
                self.CrearTabla(tabl,self.tablas[tabl])

    def infoSQL(self,**kwargs):
        """ De dbname obtenemos lista de tablas, descripcion de las tablas """
        """From within a C/C++ program (or a script using 
        Tcl/Ruby/Perl/Python bindings) you can get access to table and 
        index names by doing a SELECT on a special table named 
        "SQLITE_SCHEMA". Every SQLite database has an 
        SQLITE_SCHEMA table that defines the schema for the database. 
        The SQLITE_SCHEMA table looks like this:
            CREATE TABLE sqlite_schema (
              type TEXT,
              name TEXT,
              tbl_name TEXT,
              rootpage INTEGER,
              sql TEXT
            );
        To get a list of all tables, both permanent and temporary, 
        one can use a command similar to the following: 
            SELECT name FROM 
               (SELECT * FROM sqlite_schema UNION ALL
                SELECT * FROM sqlite_temp_schema)
            WHERE type='table'
            ORDER BY name
        """
        print('show_bbdd:')
        self.execute_commit(
            self.query['show_bbdd'],
            **kwargs
            )
        for fila in self.cursor.fetchall():
            print(fila)
        print('show_schema:')
        self.execute_commit(
            self.query['show_schema'],
            **kwargs
            )
        for fila in self.cursor.fetchall():
            print(fila)
        print('use_show_tables:')
        self.execute_commit(
            self.query['use_show_tables'](self.dbname),
            **kwargs
            )
        for fila in self.cursor.fetchall():
            print(fila)
        """
            self.execute_commit(
                self.query['use_describe_table'](self.dbname,fila[0]),
                **kwargs
                )
            for fila in self.cursor.fetchall():
                (fila)
        self.execute_commit(
            self.query['select_all'](nombreTabla),
            **kwargs
            )
        for fila in self.cursor.fetchall():
            (fila)
        """
        self.close()
    def CrearTabla(self,nombreTabla,columnas,autoincrement=0,**kwargs):
        # nombre_tabla="miTabla"
        # columnas=["primer_campo TEXT","segundo_campo TEXT","tercer_campo TEXT","cuarto_campo TEXT"]
        # Comprueba si la tabla "nombre_tabla" existe, en caso de no existir la creara
        # cursor.execute("""CREATE TABLE IF NOT EXISTS  ( TEXT, TEXT)""")
        """
        CrearTabla("Nombre_de_la_tabla",["primer_campo TEXT","segundo_campo TEXT","tercero_campo TEXT","cuarto_campo TEXT"])
        CREATE TABLE IF NOT EXISTS nombre_de_la_tabla (variable TEXT, valor TEXT)
        """
        campo_id=self.campoID.split(' ')[0]
        if campo_id in columnas:
            columnas[columnas.index(campo_id)]=self.campoID
        if not self.reset :
            self.tablas.setdefault(
                nombreTabla,
                columnas
            )
        colum,val=self.columnas_valores(columnas, [], create_table=1)
        comando = self.query['create_table'](nombreTabla,colum)
        self.execute_close(comando,**kwargs)

    def SelectAll(self,nombreTabla,typeSalida="dict",campoClave="id",**kwargs):
        campos=[key.split(' ')[0] for key in self.tablas[nombreTabla]]
        self.execute_commit(
            self.query['select_all'](nombreTabla),
            **kwargs
            )
        if (campoClave in campos):
            campoClave=campos.index(campoClave)
        else:
            campoClave=0

        if typeSalida=="dict":
            ret={}
            for registro in self.fetchall(nombreTabla):
                pasar={campos[i]:registro[i] for i in range(len(campos))}
                ret.setdefault(registro[campoClave],pasar)
        else:
            ret=[campos]+self.fetchall(nombreTabla)
        self.close()
        return ret
    def fetchall(self,nombreTabla):
        noModificar=[]
        if (self.campoID in self.tablas[nombreTabla]):
            noModificar=[self.tablas[nombreTabla].index(self.campoID)]
        r=[]
        for fila in self.cursor.fetchall():
            r+=[[]]
            for n in range(0,len(fila),1):
                if (not n in noModificar) and self.query['encode']:
                    r[-1]+=[strToVar(unicodeToStr(fila[n]))]
                else: 
                    r[-1]+=[fila[n]]
        return r            
    def columnas_valores(self,columnas,valores,create_table=0):
        colum="("
        if create_table and columnas:
            for c in range(0,(len(columnas)-1),1):
                colum+=columnas[c]+","
            colum+=columnas[-1]+")"
        elif columnas:
            for col in range(0,(len(columnas)-1),1):
                if self.campoID[:len(columnas[col])]!=columnas[col]:
                    colum+=str(columnas[col].split(' ')[0])+","
            colum+=str(columnas[-1].split(' ')[0])+")"
        else:
            colum+=")"
        val="("
        if self.query['encode'] and valores:
            for v in range(0,(len(valores)-1),1):
                val+="'"+strToUnicode(valores[v])+"',"
            val+="'"+strToUnicode(valores[-1])+"')"
        elif valores:
            for v in range(0,(len(valores)-1),1):
                val+=self.add_value(valores[v])+", "
            val+=self.add_value(valores[-1])+")"
        else:
            val+=")"
        return colum,val
    def add_value(self,v):
        if str==v.__class__: return "'"+v+"'"
        else: return str(v)
    def Cargar(self,nombreTabla,columnas,valores,**kwargs):
        colum,val=self.columnas_valores(columnas,valores)
        comandoSQL = self.query['insert_into'](nombreTabla,colum,val)
        self.execute_close(comandoSQL,**kwargs)
    def Modificar(self,nombreTabla,columnas,valores,**kwargs):
        """ sin terminar """
        colum,val=self.columnas_valores(columnas,valores)
        comandoSQL=self.query['delete_from_where'](
            nombreTabla,
            columnas[0].split(' ')[0],
            strToUnicode(valores[0])
        )
        self.execute_commit(comandoSQL,**kwargs)
        comandoSQL=self.query['insert_into'](nombreTabla,colum,val)
        self.execute_close(comandoSQL,**kwargs)
        
    def Elimina(self,nombreTabla,columnas,valores,**kwargs):
        """ """
        self.execute_close(
            self.query['delete_from_where'](
                nombreTabla,
                columnas[0].split(' ')[0],
                strToUnicode(valores[0])
            ),
            **kwargs
        )
        
    def exportarTablas(self,tablas=[],formato="shell",campoClave="",file="",**kwargs):
        """ guardara las tablas que estan guardadas en la base de datos en formato ["shell","csv","py","js"] """
        ret={}
        self.connect(**kwargs)
        if not tablas: tablas=self.tablas
        for tabl in tablas:
            ret.setdefault(
                tabl,
                [[campo.split(" ")[0] for campo in self.tablas[tabl]]]
            )
            self.execute(self.query['select_all'](tabl),**kwargs)
            ret[tabl]+=self.fetchall(tabl)
            self.con.commit()
        self.close()
        if formato.lower() in "shell consola":
            f='en consola'
            for clave in ret:
                print('Nombre de la tabla:',clave,'\n','Numero de Registros:',len(ret[clave]))
                for i in ret[clave]:
                    print(" ",i)
        elif formato.lower() in ".csv":
            f=(file if file else self.dirCRUD[:-len(self.extencionCRUD)])+".csv"
            file=open(f,"w")
            for clave in ret:
                file.write('Nombre de la tabla:'+";"+str(clave)+'\n')
                file.write('Numero de Registros:'+";"+str(len(ret[clave]))+'\n')
                for i in ret[clave]:
                    registro=""
                    for x in i:
                        registro+=';'+str(x) 
                    file.write(" "+";"+str(registro)+""+'\n')
                file.write('\n'+'\n'+'\n'+'\n'+'\n')
        elif formato.lower() in ".py":
            f=(file if file else self.dirCRUD[:-len(self.extencionCRUD)])+".py"
            file=open(f,"w")
            file.write(str(r'#!/usr/bin/env python'+'\n'))
            file.write(str(r'# -*- coding: latin-1 -*-'+'\n'))
            for clave in ret:
                campos=[campo.split(" ")[0] for campo in self.tablas[clave]]
                myClave=campoClave if campoClave in campos else campos[0]
                if 1<len(ret[clave]):
                    file.write(str(clave)+'={\n')
                    for reg in range(1,len(ret[clave]),1):
                        file.write("    '"+str(ret[clave][reg][campos.index(myClave)])+"':{\n")
                        for x in range(0,len(ret[clave][reg])-1,1):
                            file.write("        '"+str(campos[x])+"':"+( '"'+ret[clave][reg][x]+'"' if "str" in str(type(ret[clave][reg][x])) else str(ret[clave][reg][x]) )+",\n")
                        file.write("        '"+str(campos[-1])+"':"+( '"'+ret[clave][reg][-1]+'"' if "str" in str(type(ret[clave][reg][-1])) else str(ret[clave][reg][-1]) )+"\n")
                        file.write("    }\n" if len(ret[clave][1:])==reg else "    },\n" )
                    file.write('}\n'+'\n')
            file.close()
        print("Fue exportado Exitosamente ,",f)
    def command(self,comandoSQL,ret=0,**kwargs):
        self.execute_commit(comandoSQL,**kwargs)
        rtrn=self.cursor.fetchall()
        self.close()
        if ret:
            return rtrn

if 'main' in __name__:
    from pruebas import main_pruebas
    pruebas=[
        #{'titulo':" :",'f':}
        ]
    main_pruebas(pruebas,sys.argv)
            