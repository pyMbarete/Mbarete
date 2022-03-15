#!/usr/bin/env python
# -*- coding: utf-8 -*-
# archivo generado por Diseño Libre para servidor

#Modulos importados
import socket, glob, json  
import threading
import os,datetime,time
def f1(*a,**k):
    return datetime.datetime.now()
f1()

def f2(*a,**k):
    return str(datetime.datetime.now())
f2()

def f3(*a,**k):
    return datetime.datetime.now()
f3()
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

funciones={
    'f1':f1,
    'f2':f2,
    'f3':f3
}
pwd=os.getcwd()+'\\media\\servidor'
subProyectos={
    'a':{'pwd':pwd+'\\'+'a','name':'a'},
    'b':{'pwd':pwd+'\\'+'b','name':'b'},
    'c':{'pwd':pwd+'\\'+'c','name':'c'},
    'd':{'pwd':pwd+'\\'+'d','name':'d'}
    }
#api=servidor(pwd, funciones,subProyectos,puerto=666)
#api.servidor_HTTP_python()

def servidor_CHAT_socket_python():
    import socket   
    import threading
    host = '0.0.0.0'
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
    username = user_name if (user_name:=input("Ingresa tu nombre de usuario: "))!='' else "No_Name"
    host = '192.168.43.134'
    port = 8080
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((host, port))
    def read_messages():
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
    receive_thread = threading.Thread(target=read_messages)
    receive_thread.start()
    write_thread = threading.Thread(target=write_messages)
    write_thread.start()


def command(admin,G,info,ec,geo):
    print(info['subProyecto'])
    print('Info:',info['info'])
    print('Widgest:',info['widget'])
    print('Comandos',info['command']) 
    G.command[info['command']['manager']]=lambda : admin.transicion(G,admin.manager)


print(__name__)
if 'main' in __name__:
    import sys
    pruebas={           
        0:{'titulo':":",'f':print("")},
        1:{'titulo':"servidor_CHAT_socket_python",'f':servidor_CHAT_socket_python},
        2:{'titulo':"cliente_CHAT_socket_python",'f':cliente_CHAT_socket_python},
        3:{'titulo':"salir",'f':lambda : p(('hello',21,True))},
        4:{'titulo':"salir",'f':lambda : p(('hello',21,True),console=0)},
        5:{'titulo':"salir",'f':exit}
        }
    def f(num):
        print('######################################################################')
        print("PRUEBA Inicianda: "+pruebas[num]['titulo'])
        print('######################################################################'+'\n')

        #llamamos a la funcion
        pruebas[num]['f']()

        #esperamos que termine
        
        #Aviso de que la funcion termino.
        print('\n'+"PRUEBA Terminada...")
        print('\n')
    if len(sys.argv)>1:
        f(int(sys.argv[1]))
        exit()        
    num=1
    while num > 0:
        num=0
        for prueba in pruebas:
            print(str(prueba)+'. '+pruebas[prueba]['titulo'])
        inpu=input('Ingrese el numero de la siguiente prueba: ').split(' ')
        num=int(inpu[0] if inpu[0] != '' else 0)
        if num > 0:
            f(num)
        else:
            exit()
