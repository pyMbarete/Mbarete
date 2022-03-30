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
import os
d={
    'img':os.getcwd()+os.path.sep+"media"+os.path.sep,
    'audio':os.getcwd()+os.path.sep+"media"+os.path.sep
    }
canvas_width = 1100
canvas_height =1000


"""Cómo se construye una dirección IP:
    En estos cuatro bloques, los tres primeros constituyen las distintas capas de 
    la red a la que estamos conectados, mientras que el último es el que 
    se asigna a nuestro dispositivo.
    Es decir, en una IP 230.143.089.001, somos el dispositivo número 
    1 de la red '230.143.089'. 
    Como la red se construye por capas, la estructura sería la siguiente 
    (usando el mismo ejemplo).
        230. Identificador de la red principal.
        143. Identificador de la primera sub-red.
        089. Identificador de la segunda sub-red.
        001. Identificador de nuestro dispositivo en la red general.
    Pero esto sólo es así en las redes de clase C, pues existen otras dos clases de 
    redes IP que quedan de la siguiente manera:
        Clase A: Red.Dispositivo.Dispositivo.Dispositivo.
        Clase B: Red.Red.Dispositivo.Dispositivo.
        Clase C: Red.Red.Red.Dispositivo.
    Las redes que nos interesan son las de clase C, que son las que afectan a 
    ordenadores, móviles, tablets, televisores, relojes y demás dispositivos 
    que se conectan a Internet de forma clásica.
    Como hemos comentado antes, existen dos direcciones IP para cada dispositivo que 
    tengamos conectado en el hogar, una IP privada y una IP pública. La privada tiene un 
    formato similar a 192.168.0.1, pues las redes 192 son las reservadas para este uso. 
    Pero cuando salimos a Internet, a nuestro dispositivo se le asigna una IP pública y 
    es más fácil de lo que parece saber cuál es en cada momento.
"""



def red():
    from mbarete import internet
    ip=internet()
    print('ip.lan_ip:',ip.lan_ip,'ip.wan_ip:',ip.wan_ip)
class nodo_python(object):
    """docstring for nodo_python"""
    def __init__(self,IP_clase_C='192.168.100.',dispositivos='2-30',host = "",port = 30000,format_encode='utf-8',username='',infodir=['mbarete','consolas']):
        super(nodo_python, self).__init__()
        import os,sys,csv,time
        from datetime import datetime
        import socket
        from threading import Thread
        self.t=Thread
        self.status=True
        self.infodir=''
        for d in infodir: self.infodir+=d+'\\'
        self.username='cross_username'
        self.ruta_app = os.getcwd()
        self.host='0.0.0.0'
        self.port=port
        self.IP_C=IP_clase_C
        self.dispositivos=dispositivos
        self.code=format_encode
        self.porcion=1024*5
        self.media=self.media_me()
        #self.=
        #self.=
        print(self.host, self.port)
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind((self.host, self.port))
        self.server.listen()
        self.clients = []
        self.scan()

    def media_me(self):
        from  datetime import datetime
        media={}
        total = 0
        num_archivos = 0
        formato = '%d-%m-%y %H:%M:%S'
        for ruta, directorios, archivos in os.walk(self.ruta_app, topdown=True):
            for elemento in archivos:
                num_archivos += 1
                archivo = ruta + os.sep + elemento
                media[self.username+'_'+str(num_archivos)]={'path':archivo,'name':elemento}
                estado = os.stat(archivo)
                tamanho = estado.st_size
                ult_acceso = datetime.fromtimestamp(estado.st_atime)
                modificado = datetime.fromtimestamp(estado.st_mtime)
                ult_acceso = ult_acceso.strftime(formato)
                modificado = modificado.strftime(formato)
                total += tamanho
                media[self.username+'_'+str(num_archivos)]['modificado']=modificado
                media[self.username+'_'+str(num_archivos)]['ult_acceso']=ult_acceso
                media[self.username+'_'+str(num_archivos)]['size']=tamanho
        media['media_me']={'num_archivos':num_archivos,'peso_total_kb':round(total/1024, 1),'username':self.username,'address':(self.host,self.port)}
        return media
        
    def scan(self):
        #b'JSONin'
        import socket
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        inicio,fin=map(int,self.dispositivos.split('-'))
        for c in range(inicio,fin+1):
            med=self.media
            try:
                med['media_me']['host']=self.IP_C+str(c)
                client.connect((self.IP_C+str(c), self.port))
                client.send(b'JSONin\r\n'+ json.dumps(med).encode(self.code)+b'\r\n\r\n')
                datos_Bytes=client.recv(self.porcion)
                j=datos_Bytes
                while not (b'\r\n\r\n' in datos_Bytes):
                    datos_Bytes=client.recv(self.porcion)
                    j+=datos_Bytes
                client_media=json.loads(j.split(b'\r\n')[1].decode(self.code))
                self.clients[client_media['media_me']['username']]=client_media
            except Exception as e:
                print('ERROR:',(self.IP_C+str(c), self.port))
            client.close()

    def respond(self,client, address):
        request=b''
        ok=True
        cabezera=True
        binario=None
        info={}
        datos_Bytes=client.recv(self.porcion)
        if (b'JSONin' in datos_Bytes):
            j=datos_Bytes
            while not (b'\r\n\r\n' in datos_Bytes):
                datos_Bytes=client.recv(self.porcion)
                j+=datos_Bytes
            client_media=json.loads(j.split(b'\r\n')[1].decode(self.code))
            #f'JSONout\n'+ json.dumps(media) +'\n'
            print(client_media['media_me'])
            self.clients[client_media['media_me']['username']]=client_media
            client.send(b'JSONout\r\n'+ json.dumps(self.media).encode(self.code) +b'\r\n\r\n')
        elif (b'GET' in datos_Bytes):
            boundary=datos_Bytes.split(b'\r\n')[1].decode(self.code)
            file=open(media[boundary]['filename'],'rb')
            client.send(file.read())
            file.close()
        elif (b'CLOSE' in datos_Bytes):
            print('Servidor Apagado')
            client.close()
            self.server.close()  
            self.status=False      
        else:
            boundary=datos_Bytes.split(b'\r\n')[0]
            if boundary.decode(self.code) in media:
                binario=datos_Bytes.split(boundary+b'\r\n')[0]
                guardando = open(media[boundary.decode(self.code)]['filename'],"wb")
                #guardando.write(numerosMagicos[binario]['inicio']+datos_Bytes.split(numerosMagicos[binario]['inicio'])[-1])
                while binario:
                    if boundary+b'--' in binario:
                        guardando.write(binario.split(boundary+b'--')[0])
                        #request=info['boundary'].encode(format_encode)+datos_Bytes.split(info['boundary'].encode(format_encode))[-1]
                        #binario=False
                    else:
                        guardando.write(binario)
                    binario=client.recv(porcion)
                guardando.close()
                print("recivido:",media[boundary.decode(self.code)]['filename'])
            else:
                print('el elemento no esta registrado:',boundary)
        client.close()
        print("fin de coneccion")
    def start(self):
        print(f"\nServidor HTTP corriendo en la direccion 'http://{self.host}:{self.port}/'")
        while self.status:
            client, address = self.server.accept()
            thread = self.t(target=self.respond, args=(client, address))
            thread.start()
        print("fin de servicio")
    
def nodo():
    n=nodo_python()
    print(n.clients)
    #print(n.media)
    n.start()
    n.server.close()

def CLOSE():
    #b'JSONin'
    import socket
    print( socket.gethostname(), 30000)
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        client.connect(( socket.gethostname(), 30000))
        client.send(b'CLOSE\r\n')
        """
        datos_Bytes=client.recv(self.porcion)
        j=datos_Bytes
        while not (b'\r\n\r\n' in datos_Bytes):
            datos_Bytes=client.recv(self.porcion)
            j+=datos_Bytes
        client_media=json.loads(j.split(b'\r\n')[1].decode(self.code))
        self.clients[client_media['media_me']['username']]=client_media
        """
    except Exception as e:
        print(e)
    client.close()


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
            