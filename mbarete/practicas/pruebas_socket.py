#!/usr/bin/env python
# -*- coding: latin-1 -*-

"""
    b'POST /subir HTTP/1.1'
    b'Host: 127.0.0.1:8080'
    b'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:90.0) Gecko/20100101 Firefox/90.0'
    b'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'
    b'Accept-Language: es-ES,es;q=0.8,en-US;q=0.5,en;q=0.3'
    b'Accept-Encoding: gzip, deflate'
    b'Content-Type: multipart/form-data; boundary=---------------------------1262949829386019333586660223'
    b'Content-Length: 225'
    b'Origin: http://127.0.0.1:8080'
    b'Connection: keep-alive'
    b'Referer: http://127.0.0.1:8080/'
    b'Upgrade-Insecure-Requests: 1'
    b'Sec-Fetch-Dest: document'
    b'Sec-Fetch-Mode: navigate'
    b'Sec-Fetch-Site: same-origin'
    b'Sec-Fetch-User: ?1'
    b''
    b'-----------------------------1262949829386019333586660223'
    b'Content-Disposition: form-data; name="archivo"; filename=""'
    b'Content-Type: application/octet-stream'
    b''
    b''
    b'-----------------------------1262949829386019333586660223--'

"""
import os,sys,csv
from pruebas import object_prueba
d={
    'img':os.getcwd()+os.path.sep+"media"+os.path.sep,
    'audio':os.getcwd()+os.path.sep+"media"+os.path.sep
    }

class nodo_python(object_prueba):
    """docstring for nodo_python"""
    def __init__(self,IP_clase_C='192.168.100.',dispositivos='1-30',ignore=[],port = 8002,format_encode='utf-8',name='cross',pwd='',flags=['init','log','error']):
        super(nodo_python, self).__init__()
        import socket,json
        from datetime import datetime
        from threading import Thread
        self.t=Thread
        self.j=json
        self.dt=datetime
        self.s=socket
        self.name = name
        self.port=port
        self.IP_C=IP_clase_C
        self.dispositivos=dispositivos
        #self.code=format_encode
        self.flags=['']+flags
        self.status=True
        self.sepUser='_'
        self.home='home'
        self.ignore=ignore+['__pycache__',self.home]
        self.pwd = pwd if pwd else os.getcwd()
        if not self.home in os.listdir(self.pwd):
            os.mkdir(self.pwd+os.sep+self.home)
            self.setFile(self.pwd+os.sep+self.home+os.sep+'__init__.py',valor=['#!/usr/bin/env python','# -*- coding: '+self.code+' -*-'])
        self.host='0.0.0.0'
        self.porcion=1024*5
        self.media=self.media_me()
        self.p(self.host, self.port,flag='init')
        self.server = self.s.socket(self.s.AF_INET, self.s.SOCK_STREAM)
        self.clients = {}
        self.scan()
    def crear_cliente(self,med,address):
        self.media['media_me']['address']=med['media_me']['address']
        med['media_me']['address']=tuple(address)
        home=self.pwd+os.sep+self.home
        name=med['media_me']['name']
        for e in med:
            if 'media_me' != e:
                med[e]['path'] = os.sep+self.home+os.sep+name+med[e]['path']
        self.clients[name]=med
        if not name in os.listdir(home): os.mkdir(home+os.sep+name)
        home=home+os.sep+name
        for d in med['media_me']['home']:
            if not d in os.listdir(home): 
                os.mkdir(home+os.sep+d)
        self.p(med['media_me'],flag='auto')
    def media_me(self):
        media={}
        total = 0
        num_archivos = 0
        formato = '%d-%m-%y %H:%M:%S'
        home=[]
        for ruta, directorios, archivos in os.walk(self.pwd, topdown=True):
            ruta='' if ruta==self.pwd else ruta.replace(self.pwd+os.sep,'')
            self.p(ruta,not ruta.split(os.sep)[0] in self.ignore,flag='init')
            if not ruta.split(os.sep)[0] in self.ignore:
                if not ruta in home: home+=[ruta]
                for elemento in archivos:
                    num_archivos += 1
                    archivo = ruta+os.sep+elemento if ruta else elemento
                    self.p(archivo,flag='init')
                    estado = os.stat(archivo)
                    tamanho = estado.st_size
                    name=self.name+self.sepUser+str(num_archivos)
                    media[name]={'path':os.sep+archivo,'name':elemento}
                    ult_acceso = self.dt.fromtimestamp(estado.st_atime)
                    modificado = self.dt.fromtimestamp(estado.st_mtime)
                    ult_acceso = ult_acceso.strftime(formato)
                    modificado = modificado.strftime(formato)
                    total += tamanho
                    media[name]['modificado']=modificado
                    media[name]['ult_acceso']=ult_acceso
                    media[name]['size']=tamanho
        home=[d.replace(self.pwd,'') for d in home if d]
        home.sort(reverse=False,key=lambda x: len(x.strip(os.sep)))
        media['media_me']={'num_archivos':num_archivos,'peso_total_kb':round(total/1024, 1),'name':self.name,'address':(self.host,self.port),'pwd':self.pwd,'home':home}
        return media
    def get(self,files):
        while files:
            f=files[-1].split(self.sepUser)[0]
            cli_files=[]
            for x in range(len(files)-1,-1,-1):
                if f in files[x]:
                    cli_files+=[files[x]]
                    files.pop(x)
            if (f in self.clients):
                cli=self.clients[f]
                for f in cli_files:
                    try:
                        file = cli[f]['path']
                        client = self.s.socket(self.s.AF_INET, self.s.SOCK_STREAM)
                        client.connect(cli['media_me']['address'])
                        msj=client.recv(self.porcion)
                        if b'nodo_python' in msj:
                            client.send(b'GET\r\n'+f.encode(self.code)+b'\r\n\r\n')
                            binario=client.recv(self.porcion)
                            guardando = open(self.pwd+file,"wb")
                            while binario:
                                guardando.write(binario)
                                binario=client.recv(self.porcion)
                            guardando.close()
                            self.p("recivido:",file,flag='metodo')
                        client.close()
                    except Exception as e:
                        self.p('ERROR:',e,flag='error')
            self.p('GET len(files):',len(files),flag='metodo')
    def connect(self,name):


    def set(self,username,files):
        cli=self.clients[username]
        for boundary in files:
            try:
                client = self.s.socket(self.s.AF_INET, self.s.SOCK_STREAM)
                client.connect(cli['media_me']['address'])
                msj=client.recv(self.porcion)
                if b'nodo_python' in msj:
                    file=open(self.pwd+self.media[boundary]['path'],'rb')
                    client.send(boundary.encode(self.code)+b'\r\n'+file.read())
                    file.close()
                    self.p("enviado:",self.media[boundary]['path'],flag='metodo')
                client.close()
            except Exception as e:
                self.p('ERROR:',e,flag='error')
        self.p('SET len(files):',len(files),flag='metodo')
    def scan(self):
        #b'JSONin'
        inicio,fin=map(int,self.dispositivos.split('-'))
        for c in range(inicio,fin+1):
            client = self.s.socket(self.s.AF_INET, self.s.SOCK_STREAM)
            try:
                if not (c in self.ignore):
                    msj=b''
                    client.connect((self.IP_C+str(c),self.port))
                    msj=client.recv(self.porcion)
                    if b'nodo_python' in msj:
                        med=self.media
                        med['media_me']['address']=(self.IP_C+str(c),self.port)
                        client.send(b'JSONin\r\n'+self.j.dumps(med).encode(self.code)+b'\r\n\r\n')
                        datos_Bytes=client.recv(self.porcion)
                        j=datos_Bytes
                        while datos_Bytes:
                            datos_Bytes=client.recv(self.porcion)
                            j+=datos_Bytes
                        client_media=self.j.loads(j.split(b'\r\n')[1].decode(self.code))
                        self.crear_cliente(client_media,(self.IP_C+str(c),self.port))
            except Exception as e:
                self.p('ERROR:',(self.IP_C+str(c), self.port),e,flag='error')
            client.close()
    def respond(self,client, address,datos_Bytes):
        try:
            if (b'JSONin\r\n' in datos_Bytes):
                j=datos_Bytes
                while not b'\r\n\r\n' in datos_Bytes:
                    datos_Bytes=client.recv(self.porcion)
                    j+=datos_Bytes
                client_media=self.j.loads(j.split(b'\r\n')[1].decode(self.code))
                med=self.media
                med['media_me']['address']=(address[0],self.port)
                client.send(b'JSONout\r\n'+self.j.dumps(med).encode(self.code) +b'\r\n\r\n')
                self.crear_cliente(client_media,(address[0],self.port))

            elif (b'GET\r\n' in datos_Bytes):
                boundary=datos_Bytes.split(b'\r\n')[1].decode(self.code)
                file=open(self.pwd+self.media[boundary]['path'],'rb')
                client.send(file.read())
                file.close()
            else:
                #b'SET'
                boundary=datos_Bytes.split(b'\r\n')[0].decode(self.code)
                cli=boundary.split(self.sepUser)[0]
                if cli in self.clients:
                    file=self.pwd+self.clients[cli][boundary]['path']
                    boundary=boundary.encode(self.code)
                    binario=datos_Bytes[len(boundary+b'\r\n'):]
                    guardando = open(file,"wb")
                    while binario:
                        guardando.write(binario)
                        binario=client.recv(self.porcion)
                    guardando.close()
                    self.p("recivido:",file,flag='auto')
                else:
                    self.p('el elemento no esta registrado:',boundary,flag='auto')
        except Exception as e:
            self.p(e,flag='error')
        client.close()
    def hilo_start(self):
        self.server.bind((self.host, self.port))
        self.server.listen()
        while self.status:
            client, address = self.server.accept()
            client.send(b'nodo_python')
            datos_Bytes=client.recv(self.porcion)
            if (b'CLOSE\r\n' in datos_Bytes):
                client.close()
                self.server.close()  
                self.status=False 
            else:
                thread = self.t(target=self.respond, args=( client, address, datos_Bytes))
                thread.start()
        self.p('Servidor Apagado',flag='init')
    def stop(self):
        self.p( self.s.gethostname(), 8002,flag='init')
        try:
            client = self.s.socket(self.s.AF_INET, self.s.SOCK_STREAM)
            client.connect(( self.s.gethostname(), self.port))
            self.p(client.recv(1024),flag='init')
            client.send(b'CLOSE\r\n')
            client.close()
            self.p("cerrado:",( self.s.gethostname(), self.port),flag='init')
        except Exception as e:
            self.p(e,flag='error')
        
    def start(self):
        thread = self.t(target=self.hilo_start)
        thread.start()
        self.p(f"\nServidor HTTP corriendo en la direccion 'http://{self.host}:{self.port}/'",flag='init')
    
def nodo():
    import time
    reloj=['~',r'\ ','|','/','~',r'\ ','|','/']
    x=7
    if not 'sigue' in os.listdir():os.mkdir('sigue')
    n=nodo_python(dispositivos='6-8',ignore=[21],name='cross',flags=['init','metodo','error'],pwd='/home/mbarete/Escritorio/0_PYTHON/Mbarete/mbarete/practicas')
    print('clients:',[c for c in n.clients])
    print('n.media:',n.media)
    #print(n.media)
    n.start()
    for client in n.clients:
        files=[f for f in n.clients[client] if client in f]
        n.get(files)
    files=[f for f in n.media if n.media['media_me']['name'] in f]
    for client in n.clients:
        n.set(client,files)
    while 'sigue' in os.listdir():
        time.sleep(1)
        #print(reloj[x%7],end='\r')
        x= 7 if x==70 else x+1
    print("cerrando:",n.media['media_me']['address'])
    n.stop()
def nodoAndroi():
    import time
    reloj=['~',r'\ ','|','/','~',r'\ ','|','/']
    x=7
    if not 'sigue' in os.listdir():os.mkdir('sigue')
    n=nodo_python(dispositivos='20-22',ignore=['192.168.100.7'],username='android',pwd='/storage/emulated/0/0_PYTHON')
    print('clients:',[c for c in n.clients])
    print('n.media:',n.media)
    #print(n.media)
    n.start()
    for client in n.clients:
        files=[f for f in n.clients[client] if client in f]
        n.get(files)
    files=[f for f in n.media if n.media['media_me']['username'] in f]
    for client in n.clients:
        n.set(client,files)
def CLOSE():
    if 'sigue' in os.listdir():os.rmdir('sigue')


def DNS_server():
    import socket   
    import threading
    host = '127.0.0.1'
    port = 53
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((host, port))
    while True:
        data, address = server.recvfrom(512)
        print(data)
        if b'/cerrar' in data:
            break
def servidor_CHAT_socket_python():
    import socket   
    import threading
    host = '192.168.43.134'
    port = 8080
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((host, port))
    server.listen()
    print(f"Servidor corriendo en la direccion {host}:{port}")
    clients = []
    usernames = []
    def broadcast(message, _client):
        for client in clients:
            if client != _client:
                client.send(message)
    def handle_messages(client):
        while True:
            try:
                message = client.recv(1024)
                broadcast(message, client)
            except:
                index = clients.index(client)
                username = usernames[index]
                broadcast(f"ChatBot: {username} se desconecto".encode('utf-8'), client)
                clients.remove(client)
                usernames.remove(username)
                client.close()
                break
    def receive_connections():
        while True:
            client, address = server.accept()
            client.send("@username".encode("utf-8"))
            username = client.recv(1024).decode('utf-8')
            clients.append(client)
            usernames.append(username)
            print(f"{username} esta conectado desde {str(address)}")
            message = f"ChatBot: {username} se unio al chat!".encode("utf-8")
            broadcast(message, client)
            thread = threading.Thread(target=handle_messages, args=(client,))
            thread.start()

    receive_connections()
def cliente_CHAT_socket_python():
    import socket   
    import threading
    #username = input("Ingresa tu nombre de usuario: ")
    username = "Ingresa"
    host = '192.168.43.134'
    port = 8080
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((host, port))
    def receive_messages():
        while True:
            try:
                message = client.recv(1024).decode('utf-8')
                if message == "@username":
                    client.send(username.encode("utf-8"))
                else:
                    print('\n'+message+'\n<<< Tu:',end='')
            except:
                print("Houston! Tenemos Problemas")
                client.close()
                break
    def write_messages():
        while True:
            tu=input('<<< Tu:')
            if tu=='salir':
                client.close()
                break
            else:
                message = f"{username}: {tu}"
                client.send(message.encode('utf-8'))
    receive_thread = threading.Thread(target=receive_messages)
    receive_thread.start()
    write_thread = threading.Thread(target=write_messages)
    write_thread.start()
class cola(object):
    """clase para gestionar los pedidos masivos desde el servidor hacia nuestras funciones"""
    def __init__(self):
        super(cola, self).__init__()
        self.crear()
    def crear(self):
        self.cola = []
        self.prioridad = []
    def encolar(self,prioridad,elemento):
        self.cola+=[elemento]
        self.prioridad+=[int(prioridad)]

    def desencolar(self,indice):
        if (self.cola and self.prioridad):
            self.cola.pop(indice)
            self.prioridad.pop(indice)
            return 1
        else:
            return 0
    def frente(self):
        if (self.cola and self.prioridad):
            return self.prioridad.index(min(self.prioridad))
        else:
            return -1
    def vaciar(self):
        self.cola = []
        self.prioridad = []
class servidor(object):
    """docstring for servidor"""
    def __init__(self,pwd, command,subProyectos,puerto=8080):
        super(servidor, self).__init__()
        self.metricas_command={}
        self.command=command #todas las funciones que seran recividas desde los sub proyectos
        self.cola=cola()         #lista de todas las instrucciones que seran recividas en este servidor
        self.tiempo_backend=1000       #para poder llevar la cuenta de cuantos procesos ya se estan ejecutando
        self.ID_Procesos=0       #para poder llevar la cuenta de cuantos procesos ya se estan ejecutando
        self.hilos={}            #lista de todas las funciones que esteran ejecutando en segundo plano
        self.limite_hilos=10     #cantidad de procesos que pueden ser ejecutados al mismos tiempo
        self.responds={}         #salida que corresponde a cada proceso ya ejecutado y terminado
        self.subProyectos=subProyectos #info de cada subProyecto necesario para poder configurara los datos para cadad funcion
        self.pwd=pwd #ruta absoluta de donde se esta ejecutando el servidor
        self.host = '0.0.0.0'    #ipV4 en donde va a estar escuchando este servidor, la direccion '0.0.0.0' es ideal para servir en la red local
        self.port = puerto       #puerto en donde va a estar escuchando este servidor
        self.format_encode='utf-8' #la funcion encode comvertira todos los datos que lleguen por los puertos a este formato de texto
        self.porcion=1024*5      #cantidad de bytes que seran leidos cada ves que se use .recv(bytes)
        self.status=True         #indica que el servidor debe seguir funcionando
        self.clients = {}        #coneccones que seran mantenidas
        self.usernames = {}      #cada ves que alguien se conecte se le asignara un username
        self.action_download='/download/' #posible programa dentro del proyecto debe ser resuelto mas adelante
        self.action_upload='/subir/'    #posible programa dentro del proyecto debe ser resuelto mas adelante
        self.action_borrar='/borrar/'   #posible programa dentro del proyecto debe ser resuelto mas adelante
        self.pwd_js=self.pwd+'\\js\\'   #carpeta de destino para la informacion JavaScript generada por los subproyectos
        self.pwd_upload=self.pwd+'\\download\\' #carpeta de destino para todo lo que sea subido al sitio
        self.pwd_download=self.pwd+'\\'         #carpeta desde donde se puede descargar todo lo que contenga, en este caso la carpeta raiz del proyecto
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind((self.host, self.port))
        self.server.listen()
        print(f"\nServidor HTTP corriendo en la direccion 'http://{self.host}:{self.port}/'")
        #servidor_archivos=self.download()
    def check(self):
        print("check en linea")
        f=self.cola.frente()
        while True: 
            print('self.cola.frente():',f)
            while (f<0) and (self.status):
                time.sleep(0.1)
                f=self.cola.frente()
            if f >= 0:
                m=self.cola.cola[f]
                self.hilos[m['parametros']['ID_Proceso']] = threading.Thread(target=self.hilo, args=(m,) )
                self.hilos[m['parametros']['ID_Proceso']].start()
                self.cola.desencolar(f)
                print(self.cola.cola,self.cola.prioridad)
            while (len(self.hilos) >= self.limite_hilos) and (self.status):
                time.sleep(0.1)
            f=self.cola.frente()
            if not self.status:
                break
        """
        try:
            f=self.cola.frente()
            while True: 
                m=self.cola.cola[f]
                self.hilos[m['ID_Proceso']] = threading.Thread(target=self.hilo, args=(m['args'],m['parametros']), kwargs=(m['kwargs'],) )
                self.hilos[m['ID_Proceso']].start()
                self.cola.desencolar(f)
                while len(self.hilos) >= self.limite_hilos:
                    time.sleep(0.5)
                f=self.cola.frente()
                while f<=0:
                    time.sleep(0.5)
                    f=self.cola.frente()
        except Exception as e:
            print("Error en la funcion Check():",e)
        """
    def hilo(self,info):
        print('ejecutando:',info['parametros']['funcion'])
        T0=time.time()
        self.responds[info['parametros']['ID_Proceso']]=self.command[info['parametros']['funcion']](*info['parametros']['args'],**info['parametros']['kwargs'])
        T=time.time()-T0
        if info['parametros']['funcion'] in self.metricas_command:
            self.metricas_command[info['parametros']['funcion']]['min_tiempo']= self.metricas_command[info['parametros']['funcion']]['min_tiempo'] if self.metricas_command[info['parametros']['funcion']]['min_tiempo']<T else T
            self.metricas_command[info['parametros']['funcion']]['max_tiempo']= self.metricas_command[info['parametros']['funcion']]['max_tiempo'] if self.metricas_command[info['parametros']['funcion']]['max_tiempo']>T else T
            self.metricas_command[info['parametros']['funcion']]['suma_tiempo']+=T
            self.metricas_command[info['parametros']['funcion']]['ejecuciones']+=1.0
            self.metricas_command[info['parametros']['funcion']]['promedio']=self.metricas_command[info['parametros']['funcion']]['suma_tiempo']/self.metricas_command[info['parametros']['funcion']]['ejecuciones']
        else:
            self.metricas_command[info['parametros']['funcion']]={}
            self.metricas_command[info['parametros']['funcion']]['min_tiempo']= T
            self.metricas_command[info['parametros']['funcion']]['max_tiempo']= T
            self.metricas_command[info['parametros']['funcion']]['suma_tiempo']=T
            self.metricas_command[info['parametros']['funcion']]['ejecuciones']=1.0
            self.metricas_command[info['parametros']['funcion']]['promedio']=self.metricas_command[info['parametros']['funcion']]['suma_tiempo']/self.metricas_command[info['parametros']['funcion']]['ejecuciones']
    def arboldearchivos(self,pwd=''):
        ret=[]
        if not pwd:
            pwd = os.getcwd()
        for check in os.listdir(pwd):
            if os.path.isfile(pwd+os.path.sep+check):
                ret += [pwd+os.path.sep+check]
            else:
                ret += self.arboldearchivos(pwd+os.path.sep+check)
        return ret
    def download(self,pwd_js,pwd_upload):
            index=[{'name':file,'size':os.path.getsize(pwd_upload+file),'fecha':os.path.getmtime(pwd_upload+file),'pwd':str(pwd_upload+file).replace(' ','%20').replace(os.path.sep,'/')} for file in os.listdir(pwd_upload)]
            #creando un .js que contiene un objeto array con todos los elementos del directorio
            javascript=open(pwd_js+'files.download.js',"w")
            javascript.write('var files = new Array();'+'\n')
            javascript.write('function registrar (name,pwd,size,fecha,id){'+'\n')
            javascript.write('  this.name = name;'+'\n')
            javascript.write('  this.pwd = pwd;'+'\n')
            javascript.write('  this.size = size;'+'\n')
            javascript.write('  this.fecha = fecha;'+'\n')
            javascript.write('  this.id = id;'+'\n')
            javascript.write('  return this;'+'\n')
            javascript.write('  }'+'\n')
            errorWrite={}
            mayor=0
            for f in range(len(index)):
                try:
                    javascript.write('files['+str(f)+'] = new registrar("'+str(index[f]['name'])+'","'+str(index[f]['pwd'].replace(' ','%20').replace(os.path.sep,'/'))+'",'+str(index[f]['size'])+','+str(index[f]['fecha'])+','+str(f)+'); \n')
                except Exception as e:
                    errorWrite[f]={'pwd':index[f]['pwd']}
                    raise e
            javascript.close()
            return self.arboldearchivos(pwd)
    def requestToDictionary(self,request,add={}):
        #print(request)
        if b'\r\n\r\n' in request:
            post=request.split(b'\r\n\r\n')[-1].decode(self.format_encode)
            #print(post)
        requ=[r.decode(self.format_encode) for r in request.split(b'\r\n')]
        ret={}
        for i in requ:
            if ('POST' in i) or ('GET' in i) or ('HEAD' in i):
                ret['method']=i.split(' ')[0]
                ret['sub_dominio']=i.split(' ')[1]
                ret['http']=i.split(' ')[2]
            if 'User-Agent:' in i:
                ret['User_Agent']=i[len('User_Agent: '):-1]
            if 'Content-Disposition:' in i:
                ret['form_data']={
                    'name':i.split('form-data; ')[-1].split(';')[0][len('name='):-1],
                    'filename':i.split('form-data; ')[-1].split(';')[1][len(' filename="'):-1]
                }
            if 'Content-Type: multipart/form-data; boundary' in i:
                ret['boundary']=i.split('boundary=')[-1]
            elif 'Content-Type:' in i:
                ret['Content-Type']=i.split('Content-Type:')[-1].strip()
                if ('application/x-www-form-urlencoded' in ret['Content-Type']) and post :
                    ret['parametros']={k.split('=')[0].strip():k.split('=')[1].strip() for k in post.split('&')}
                if ('application/json' in ret['Content-Type']) and post :
                    ret['parametros']=json.loads(post)
                    #ret['parametros']={k.split(':')[0].strip():k.split(':')[1].strip() for k in post.split('&')}
                
            if 'Content-Length:' in i:
                ret['Content-Length']=int(i.split('Content-Length:')[-1])
            if 'Origin:' in i:
                ret['Origin']=i.split('Origin:')[-1]
            if 'Referer:' in i:
                ret['Referer']=i.split('Referer:')[-1]
            
            #if ':' in i:
            #    ret['']=i.split(':')[-1]
            #
        if add:
            for a in add:
                ret[a]=add[a]
        return ret
    def respond(self,client, address):
        #80029563
        info=self.requestToDictionary(client.recv(self.porcion))
        #header='HTTP:/1.1 404 Not Found \n\n'
        if 'parametros' in info:
            print('Content-Type',info)
            if 'ID_Proceso' in info['parametros']:
                if 'inicio' in info['parametros']['ID_Proceso']:
                    print('ID_Proceso',info['parametros']['ID_Proceso'])
                    self.ID_Procesos+=1
                    info['parametros']['ID_Proceso']=self.ID_Procesos
                    #self.clients[self.ID_Procesos]=client
                    j={
                        'ID_Proceso':self.ID_Procesos,
                        'status':'encolado', 
                        'funcion':info['parametros']['funcion'],
                        'args':info['parametros']['args'],
                        'kwargs':info['parametros']['kwargs'],
                        'prioridad':info['parametros']['prioridad'],
                        'user':info['parametros']['user']
                    }
                    self.cola.encolar(info['parametros']['prioridad'],info)
                    header=f'HTTP/1.1 200 OK\nContent-Type: application/javascript\n\n'
                    header+=json.dumps(j)
                    client.send((header).encode(self.format_encode))
                else:
                    print('self.responds: ',self.responds)
                    respon=[p for p in info['parametros']['ID_Proceso'] if p in self.responds]
                    if respon:
                        header='HTTP/1.1 200 OK\n'+'Content-Type: application/javascript\n\n ' + json.dumps({p:self.responds[p] for p in respon}) +' \n '
                        for p in respon:
                            del self.responds[p]
                            del self.hilos[p]
                        print(header)
                        client.send((header).encode(self.format_encode))
                    else:
                        ejecutando=[p for p in info['parametros']['ID_Proceso'] if p in self.hilos]
                        header=f'HTTP/1.1 200 OK\nContent-Type: application/javascript\n\n'+ json.dumps({'ejecutando':ejecutando}) +'; \n'
                        print(header)
                        client.send((header).encode(self.format_encode))
            #if info['parametros']['funcion'] in self.command:
            #    header='HTTP/1.1 200 OK\n\n'

        if '/test' == info['sub_dominio']:
            client.send(('HTTP/1.1 200 OK\n'+'Content-Type: text/html\n\n').encode(self.format_encode))
            file=open(self.pwd+os.path.sep+'index.html','rb')
            client.send(file.read())
            file.close()
        elif '/cerrar' ==  info['sub_dominio']:
            client.close()
            self.server.close()
            self.status=False
            print('Servidor Apagado')
        client.close()
        """
        except Exception as e :
            print('ERROR:',e)
            client.send(('HTTP:/1.1 404 Not Found\n'+'Content-Type: text/html \n\n'+str(e)).encode(self.format_encode))
            client.close()
        """
        print("fin de coneccion")            

    def servidor_HTTP_python(self):
        def receive_connections():    
            thread_check = threading.Thread(target=self.check)
            thread_check.start()
            try:
                while self.status:
                    client, address = self.server.accept()
                    thread = threading.Thread(target=self.respond, args=(client, address))
                    thread.start()
            except Exception as e:
                print('ERROR receive_connections():', e) 
                
        receive_connections()
        print('self.responds:',self.responds)
        print('self.cola.cola:',self.cola.cola)
        print('self.metricas_command:',self.metricas_command)
        print('self.ID_Procesos:',self.ID_Procesos)
        print(':',)
        self.server.close()

if 'main' in __name__:
    import sys
    from pruebas import main_pruebas
    pruebas={           
        1:{'titulo':"Servidor Socket Python",'f':servidor_CHAT_socket_python},
        2:{'titulo':"Cliente Socket Python",'f':cliente_CHAT_socket_python},
        3:{'titulo':"DNS SERVER",'f':DNS_server},
        4:{'titulo':"NODO_PYTHON",'f':nodo},
        5:{'titulo':"CERRAR NODO",'f':CLOSE}
        }
    main_pruebas(pruebas,sys.argv)
            