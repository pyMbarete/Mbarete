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
print(('\n'+'@'*10)*6)

import os,sys,csv
from extras import object_mbarete
from pruebas import deco


class object_servidor(object_mbarete):
    """ SERVIDOR COMPLETO PARA TODO TIPO DE PROYECTOS WEB """
    def __init__(self,puerto=8080,host='0.0.0.0',pwd='servidor',carpetas={},**kwargs):
        carpetas.setdefault('pwd_servidor','servidor/')
        super(object_servidor, self).__init__(pwd=pwd,carpetas=carpetas,**kwargs)
        import socket,json
        from datetime import datetime
        from threading import Thread
        self.t=Thread
        self.j=json
        self.dt=datetime
        self.s=socket
        s=self.s.socket(self.s.AF_INET, self.s.SOCK_DGRAM)
        s.connect(('10.255.255.255',1))
        ip=s.getsockname()
        s.close()
        self.info['lan_ipv4']=ip[0]
        self.port =  puerto #puerto en donde va a estar escuchando este servidor
        self.host = host    #ipV4 en donde va a estar escuchando este servidor, la direccion '0.0.0.0' es ideal para servir en la red local
        self.format_encode=self.code #la funcion encode comvertira todos los datos que lleguen por los puertos a este formato de texto
        self.porcion= 1024*5      #cantidad de bytes que seran leidos cada ves que se use .recv(bytes)
        self.status= True         #indica que el servidor debe seguir funcionando
        self.pwd_js=self.pwd+os.sep+'js'+os.sep
        self.pwd_upload=self.pwd+os.sep+'download'+os.sep
        self.pwd_download= self.pwd+os.sep
        self.action_close= b'POST /cerrar HTTP/1.1\r\n' 
        self.action_download='/download/'
        self.action_upload='/subir/'
        self.action_borrar='/borrar/'
        self.p(f"Red Local url: 'http://{self.info['lan_ipv4']}:{self.port}/'",flag='init')
    def carpetas_web(self):
        #obtener informacion de los archivos en estas carpetas
        pass
    def file_download_js(self):
        self.media=self.media_me(self.pwd_upload)
        #creando un .js que contiene un objeto array con todos los elementos del directorio
        javascript=open(self.pwd_js+'files.download.js',"w")
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
        count=0
        for f in media:
            try:
                if 'media_me'!=f:
                    print(media[f])
                    javascript.write('files['+str(count)+'] = new registrar("'+media[f]['name']+'","'+f+'",'+str(media[f]['size'])+','+media[f]['modificado']+','+str(count)+'); \n')
                    count+=1
            except Exception as e:
                errorWrite[f]={'pwd':media[f]['path']}
                raise e
        javascript.close()
        self.servidor_archivos = [ media[f]['path'] for f in media if 'media_me'!=f]
    def requestToDictionary(self,request,add={}):
        if b'\r\n\r\n' in request:
            post=[ request.split(b'\r\n\r\n')[-1] ]
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
            
        if add:
            for a in add:
                ret[a]=add[a]
        return ret
    def get_header(myfile,sub_dominio):
        try:
            self.p('myfile:',myfile,flag='mimetype')
            header='HTTP/1.1 200 OK\n'
            ext='.'+myfile.split('.')[-1]
            mimetype={
                '.jpg':'Content-Type: image/jpg',
                '.css':'Content-Type: text/css',
                '.js':'Content-Type: text/javascript',
                '.pdf':'Content-Type: application/pdf',
                '.mp4':'Content-Type: video/mp4'
                }
            if ext in mimetype:
                mimetype=mimetype[ext]
            elif self.action_download in sub_dominio[:len(self.action_download)]:
                myfile=sub_dominio[len(self.action_download):].replace('/',os.path.sep).replace('%20',' ')
                self.p(myfile,self.dt.now(),flag='mimetype')
                """
                Server: MBARETE_PYTHON
                Date: Tue, 28 Sep 2021 00:03:17 GMT
                Connection: close
                Accept-Ranges: bytes
                Content-transfer-encoding: binary
                Content-Length: 3942042048
                Cache-Control: no-store
                X-Robots-Tag:noindex, nofollow
                Content-Disposition: attachment; filename="Black - PS2 by Videogames SCZ.pkg"
                Content-Type: application/octet-stream
                """
                #mimetype ='Server: MBARETE_PYTHON\n'
                #mimetype+='Date: '+str(datetime.datetime.now())+'\n'
                #mimetype+='Connection: close\n'
                mimetype='Accept-Ranges: bytes\n'
                mimetype+='Content-transfer-encoding: binary\n'
                mimetype+='Content-Length: '+str(os.path.getsize(myfile))+'\n'#3942042048
                mimetype+='Cache-Control: no-store\n'
                #mimetype+='X-Robots-Tag:noindex, nofollow\n'
                mimetype+='Content-Disposition: attachment; filename="'+sub_dominio.split('/')[-1]+'"\n'
                mimetype+='Content-Type: application/octet-stream\n'
                mimetype+='\n'
                self.p('mimetype:',mimetype,flag='mimetype')
            else: 
                mimetype='Content-Type: text/html'
            header += str(mimetype)+'\n\n'
        except Exception as e:
            self.p(e,myfile,sub_dominio,flag='error')
            header='HTTP:/1.1 404 Not Found \n\n'
        return header.encode(self.format_encode)
    def auto_send(self,client):
        #funcion que se ejecuta automaticamente despues de "client, address = self.server.accept()"
        pass
    def auto_recv(self,client):
        #funcion que se ejecuta automaticamente despues de "client.connect(( self.host_ip, self.port))"
        pass
    def hilo_start(self):
        self.server = self.s.socket(self.s.AF_INET, self.s.SOCK_STREAM)
        self.server.bind((self.host, self.port))
        self.server.listen()
        self.p(f"\nServidor HTTP corriendo en la direccion 'http://{self.info['lan_ipv4']}:{self.port}/'",flag='init')
        while self.status:
            client, address = self.server.accept()
            self.auto_send(client)
            datos_Bytes=client.recv(self.porcion)
            if (self.action_close in datos_Bytes):
                client.close()
                self.server.close()  
                self.status=False 
            else:
                thread = self.t(target=self.respond, args=( client, address, datos_Bytes))
                thread.start()
        self.p('Servidor Apagado',flag='init')
    def stop(self):
        self.p( self.info['lan_ipv4'], self.port,flag='init')
        try:
            client_closer = self.s.socket(self.s.AF_INET, self.s.SOCK_STREAM)
            client_closer.connect(( self.info['lan_ipv4'], self.port))
            self.p(self.auto_recv(client_closer),flag='init')
            client_closer.send(self.action_close)
            client_closer.close()
            self.p("cerrado:",( self.s.gethostname(), self.port),flag='init')
        except Exception as e:
            self.p(e,flag='error')
    def stop():
        ip=input('IP del Servidor:')
        port=int(input('Puerto del Servidor:'))
        action_close=input('action_close del Servidor:').encode('utf-8')+b'\r\n'
        print(action_close)
        import socket
        print( ip, port)
        try:
            client_closer = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client_closer.connect(( ip, port))
            print(client_closer.recv(1024))
            client_closer.send(action_close)
            client_closer.close()
            print("cerrado:",( ip, port))
        except Exception as e:
            print('ERROR:',e)
    def start(self):
        thread = self.t(target=self.hilo_start)
        thread.start()
class nodo_python(object_servidor):
    """
        docstring for nodo_python
    """
    def __init__(self,name='cross',pwd='nodo',ignore=[],carpetas={},IP_clase_C='192.168.100.',dispositivos='1-30',**kwargs):
        self.nodo_home = 'home'
        ignore+=[self.nodo_home]
        carpetas.setdefault('pwd_nodo','modulos/')
        super(nodo_python, self).__init__(pwd=pwd,carpetas=carpetas,ignore=ignore,**kwargs)
        self.action_close=b'CLOSE\r\n'
        self.IP_C=IP_clase_C
        self.dispositivos=dispositivos
        #self.code=format_encode
        self.sepUser= '_'
        self.media=self.media_me(self.pwd,prefijo=name,sep='_')
        self.clients = {}
        self.scan_async()
    def crear_cliente(self,med,address):
        self.media['media_me']['address']=med['media_me']['address']
        med['media_me']['address']=tuple(address)
        #home de nuestro nodo
        home=self.pwd+os.sep+self.nodo_home
        name=med['media_me']['name']
        for e in med:
            if 'media_me' != e:
                med[e]['path'] = self.nodo_home+os.sep+name+med[e]['path']
        self.clients[name]=med
        if not name in os.listdir(home): os.mkdir(home+os.sep+name)
        #home del cliente dentro de nuestro nodo
        home=home+os.sep+name
        for d in med['media_me']['home']:
            if not d in os.listdir(home): 
                os.mkdir(home+os.sep+d)
        self.p(med['media_me'],flag='auto')
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
        #canal para los otros nodods
        pass
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
    @deco(flag='tiempo',msj='scan:')
    def scan(self):
        #b'JSONin'
        inicio,fin=map(int,self.dispositivos.split('-'))
        for c in range(inicio,fin+1):
            client = self.s.socket(self.s.AF_INET, self.s.SOCK_STREAM)
            try:
                if not (c in self.ignore):
                    msj,address=b'',(self.IP_C+str(c),self.port)
                    client.connect(address)
                    msj=client.recv(self.porcion)
                    if b'nodo_python' in msj:
                        med=self.media
                        med['media_me']['address']=address
                        msj=self.j.dumps(med).encode(self.code)
                        client.send(b'JSONin\r\n'+msj+b'\r\n\r\n')
                        datos_Bytes=client.recv(self.porcion)
                        j=datos_Bytes
                        while datos_Bytes:
                            datos_Bytes=client.recv(self.porcion)
                            j+=datos_Bytes
                        msj=j.split(b'\r\n')[1].decode(self.code)
                        client_media=self.j.loads(msj)
                        self.crear_cliente(client_media,address)
            except Exception as e:
                self.p('ERROR:',address,e,flag='error')
            client.close()
    @deco(flag='tiempo',msj='scan_async:')
    def scan_async(self):
        import asyncio
        async def io_operation(msj,address):
            self.p(
                f'Inicio de escaneo en {address} ... scan Async',
                flag='scan_async'
            )
            try:
                #Asynchronous version of socket.connect(address)
                reader, writer = await asyncio.open_connection(*address)
                # Asynchronous version of socket.recv(self.porcion).
                msj= await reader.read(self.porcion)
                if b'nodo_python' in msj:
                    med=self.media
                    med['media_me']['address']=address
                    msj=self.j.dumps(med).encode(self.code)
                    #client.send(b'JSONin\r\n'+msj+b'\r\n\r\n')
                    writer.write(b'JSONin\r\n'+msj+b'\r\n\r\n')
                    datos_Bytes= await reader.read(self.porcion)
                    j=datos_Bytes
                    while datos_Bytes:
                        datos_Bytes= await reader.read(self.porcion)
                        j+=datos_Bytes
                    msj=j.split(b'\r\n')[1].decode(self.code)
                    c_m=self.j.loads(msj) #Client_Media
                    self.crear_cliente(c_m,address)
                    self.p(
                        'Conectado ',c_m['media_me']['name'],
                        flag='scan_async'
                    )
            except Exception as e:
                self.p('ERROR:',address,e,flag='error')
            else:
                writer.close()
            #await writer.wait_closed()
            self.p(f'Fin de escaneo en {address}',flag='scan_async')
        async def main():
            inicio,fin=map(int,self.dispositivos.split('-'))
            # Ciclo de eventos
            args=[]
            for c in range(inicio,fin+1): 
                if not (c in self.ignore):
                    #Return a Task object
                    args+=[
                        io_operation(
                            b'',
                            (self.IP_C+str(c),self.port)
                        )
                    ]
            await asyncio.gather(*args)
        loop = asyncio.get_event_loop() 
        loop.run_until_complete( main() )
            
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
    def auto_send(self,client):
        #mensaje enviado automaticamente al recivir una coneccion
        client.send(b'nodo_python')
    def auto_recv(self,client):
        #mensaje recivido automaticamente cuando hacemos connect()
        self.p(client.recv(1024),flag='init')
            
class servidor_web(object_servidor):
    """ SERVIDOR COMPLETO PARA TODO TIPO DE PROYECTOS WEB """
    def __init__(self,index='index.html',**kwargs):
        super(servidor_web, self).__init__(**kwargs)
        self.index=index
        self.file_download_js()
        print(self.servidor_archivos)

    def respond(self,client, address,datos_Bytes):
        global servidor_archivos
        responder=False
        request=b''
        ok=True
        cabezera=True
        binario=None
        info={}
        while ok:
            try:
                datos_Bytes=client.recv(self.porcion)
                print(datos_Bytes)
            except:
                ok=False
            if (b'Android' in datos_Bytes) and (b'boundary' in datos_Bytes):
                request+=datos_Bytes
                info=self.requestToDictionary(datos_Bytes)
                datos_Bytes=client.recv(self.porcion)
            if (porcion > len(datos_Bytes)) and (b'\r\n' in datos_Bytes):
                ok = False
            if b'' == datos_Bytes:
                ok = False
            if cabezera:
                if ((b'\r\n\r\n' in datos_Bytes) or info):
                    cabezera=False
                    if 'boundary' in info:
                        boundary=b'--'+info['boundary'].encode(self.format_encode)
                        if boundary in datos_Bytes.split(b'\r\n'):
                            binario=datos_Bytes.split(boundary+b'\r\n')[-1].split(b'\r\n')[2]
                    elif (b'boundary=----' in datos_Bytes) and (b'\r\n\r\n' in datos_Bytes):
                        print('############## 2 BIUNDARY',datos_Bytes)
                        request+=datos_Bytes.split(b'\r\n\r\n')[0]+b'\r\n\r\n'
                        info=self.requestToDictionary(datos_Bytes.split(b'\r\n\r\n')[0])
                        boundary=b'--'+info['boundary'].encode(self.format_encode)
                        form_data=datos_Bytes.split(boundary+b'\r\n')[-1].split(b'\r\n\r\n')[0]
                        request+= boundary+b'\r\n'+form_data
                        info=self.requestToDictionary(form_data,add=info)
                        binario=datos_Bytes.split(form_data+b'\r\n\r\n')[-1]
                    if binario:
                        boundary+=b'--\r\n'
                        #request=datos_Bytes.split(binario)[0]
                        #info=requestToDictionary(request,add=info)
                        subiendo = open(self.pwd_upload+info['form_data']['filename'],"wb")
                        if boundary in datos_Bytes:
                            subiendo.write(binario.split(boundary)[0])
                            request+=boundary+binario.split(boundary)[-1]
                        else:
                            subiendo.write(binario)
                            while binario:
                                datos_Bytes=client.recv(self.porcion)
                                if boundary in datos_Bytes:
                                    subiendo.write(datos_Bytes.split(boundary)[0])
                                    request+=boundary+datos_Bytes.split(boundary)[-1]
                                    binario=None
                                else:
                                    subiendo.write(datos_Bytes)
                        subiendo.close()
                        print("Subido:",info['form_data']['filename'])
                        self.file_download_js()
                        ok=False
                    else:
                        request+=datos_Bytes
                else:
                    request+=datos_Bytes
            else:
                request+=datos_Bytes
        self.p('request:',request,flag='respond')
        info = self.requestToDictionary(request,add=info)
        if ''!= request:
            self.p(info,flag='respond')
            myfile=pwd+os.sep
            if '/socket.io/?' in info['sub_dominio']:
                io={}
                for k in info['sub_dominio'].replace('/socket.io/?','').split('&'):
                    io[k.split('=')[0]]=k.split('=')[1]                
                myfile += 'socket_'+info['method']+'.io.html'
                file=open(myfile,'wb')
                file.write(str(io).encode())
                #file.write(request)
                file.close()
            if ('GET' in info['method']):
                if '/' ==  info['sub_dominio']:
                    myfile += self.index
                elif info['sub_dominio'].replace('/',os.path.sep).replace('%20',' ') in self.servidor_archivos:
                    myfile += info['sub_dominio'].replace('/',os.path.sep).replace('%20',' ')
                    print('method GET full:',myfile)
                else:
                    myfile += 'GET.html'
                    file=open(myfile,'wb')
                    file.write(b'<h1>Archivo No Encontrado</h1>')
                    file.write(request)
                    file.close()
            elif ('HEAD' in info['method']):
                if '/' ==  info['sub_dominio']:
                    myfile += self.index
                elif info['sub_dominio'].replace('/',os.sep) in servidor_archivos:
                    myfile += info['sub_dominio'].replace('/',os.sep)
                    print('method HEAD:',myfile)
                if '/socket.io/?' in info['sub_dominio']:
                    io={}
                    for k in info['sub_dominio'].replace('/socket.io/?','').split('&'):
                        io[k.split('=')[0]]=k.split('=')[1] 
                    #print(io)
                    #print({k.split('=')[0]:k.split('=')[1] for k in info['sub_dominio'].replace('/socket.io/?','').split('&')})
                    myfile += 'socket_GET.io.html'
                    file=open(myfile,'wb')
                    file.write(str({k.split('=')[0]:k.split('=')[1] for k in info['sub_dominio'].replace('/socket.io/?','').split('&')}).encode())
                    #file.write(request)
                    file.close()
                else:
                    myfile += 'GET.html'
                    file=open(myfile,'wb')
                    file.write(b'<h1>Archivo No Encontrado</h1>')
                    file.write(request)
                    file.close()
            elif ('POST' in info['method']):
                if '/subir' in info['sub_dominio']:
                    myfile += 'subido.html'
                    file=open(myfile,'wb')
                    file.write(b'<h1>Archivo Subido con Exito </h1>')
                    file.write(request)
                    file.close()
                else:
                    myfile += 'POST.html'
                    file=open(myfile,'wb')
                    file.write(request)
                    file.close()
            #80029563
            header=self.get_header(myfile,info['sub_dominio'])
            if '/download/' in info['sub_dominio'][:len('/download/')]:
                client.send(header)
                #for linea in pesca.iter_content(100000):
                file = open(myfile,'rb')
                part=file.read(porcion*20)
                while part:
                    client.send(part)
                    part=file.read(porcion*20)
                file.close()
            else:
                client.send(header)
                file=open(myfile,'rb')
                client.send(file.read())
                file.close()
        client.close()
        print("fin de coneccion")            
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
class servidor_API_threading(object_servidor):
    """docstring for servidor_API"""
    def __init__(self, command, subProyectos, carpetas={'dir_servidor':'/mbarete/servidor'}, pwd='servidor', **kwargs):
        super(servidor_API, self).__init__(**kwargs)
        self.metricas={}
        self.command=command #todas las funciones que seran recividas desde los sub proyectos
        self.cola=cola()         #lista de todas las instrucciones que seran recividas en este servidor
        self.tiempo_backend=1000       #para poder llevar la cuenta de cuantos procesos ya se estan ejecutando
        self.ID_Procesos=0       #para poder llevar la cuenta de cuantos procesos ya se estan ejecutando
        self.hilos={}            #lista de todas las funciones que esteran ejecutando en segundo plano
        self.limite_hilos=10     #cantidad de procesos que pueden ser ejecutados al mismos tiempo
        self.responds={}         #salida que corresponde a cada proceso ya ejecutado y terminado
        self.subProyectos=subProyectos #info de cada subProyecto necesario para poder configurara los datos para cadad funcion
        self.clients = {}        #coneccones que seran mantenidas
        self.usernames = {}      #cada ves que alguien se conecte se le asignara un username+
        #servidor_archivos=self.download()
    def check(self):
        self.p("check en linea",flag='check')
        f=self.cola.frente()
        while True: 
            self.p('self.cola.frente():',f,flag='check')
            while (f<0) and (self.status):
                time.sleep(0.1)
                f=self.cola.frente()
            if f >= 0:
                m=self.cola.cola[f]['parametros']
                self.hilos[m['ID_Proceso']] = threading.Thread(
                    target=self.hilo, 
                    args=(
                        m['ID_Proceso'],
                        m['funcion'],
                        m['arg'],
                        m['kwargs'],
                    ) 
                )
                self.hilos[m['ID_Proceso']].start()
                self.cola.desencolar(f)
                self.p( self.cola.cola, self.cola.prioridad ,flag='check')
            while (len(self.hilos) >= self.limite_hilos) and (self.status):
                time.sleep(0.1)
            f=self.cola.frente()
            if not self.status:
                break
    def hilo(self,ID,f,args,kwargs):
        self.p('ejecutando:',f)
        T0=time.time()
        self.responds[ID]= self.command[f]( *args, **kwargs )
        T=time.time()-T0
        if funcion in self.metricas:
            if self.metricas[f]['min_tiempo']<T :
                self.metricas[f]['min_tiempo']= self.metricas[f]['min_tiempo']  
            else: 
                self.metricas[f]['min_tiempo']= T

            if self.metricas[f]['max_tiempo'] > T :
                self.metricas[f]['max_tiempo'] = self.metricas[f]['max_tiempo'] 
            else: 
                self.metricas[f]['max_tiempo'] = T

            self.metricas[f]['suma_tiempo']+=T
            self.metricas[f]['ejecuciones']+=1.0
            self.metricas[f]['promedio']=self.metricas[f]['suma_tiempo']/self.metricas[f]['ejecuciones']
        else:
            self.metricas[f]={}
            self.metricas[f]['min_tiempo']= T
            self.metricas[f]['max_tiempo']= T
            self.metricas[f]['suma_tiempo']=T
            self.metricas[f]['ejecuciones']=1.0
            self.metricas[f]['promedio']=self.metricas[f]['suma_tiempo']
        del self.hilos[ID]
    def respond(self,client, address,datos_Bytes):
        info=self.requestToDictionary(datos_Bytes)
        if 'parametros' in info:
            self.p('Content-Type',info,flag='respond')
            if 'ID_Proceso' in info['parametros']:
                if 'inicio' in info['parametros']['ID_Proceso']:
                    self.p('ID_Proceso',info['parametros']['ID_Proceso'],flag='respond')
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
                    respon=[p for p in info['parametros']['ID_Proceso'] if p in self.responds]
                    if respon:
                        header='HTTP/1.1 200 OK\n'+'Content-Type: application/javascript\n\n ' + json.dumps({p:self.responds[p] for p in respon}) +' \n '
                        for p in respon:
                            del self.responds[p]
                            del self.hilos[p]
                        client.send((header).encode(self.format_encode))
                    else:
                        ejecutando=[p for p in info['parametros']['ID_Proceso'] if p in self.hilos]
                        header=f'HTTP/1.1 200 OK\nContent-Type: application/javascript\n\n'+ json.dumps({'ejecutando':ejecutando}) +'; \n'
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
            self.p('Servidor Apagado',flag='respond')
        client.close()
        self.p("fin de coneccion con ",address,flag='respond')

    def servidor_HTTP_python(self):
        def receive_connections():    
            thread_check = self.t(target=self.check)
            thread_check.start()
            try:
                while self.status:
                    client, address = self.server.accept()
                    thread = self.t(target=self.respond, args=(client, address))
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
def hijo_web():
    web=servidor_web(
        pwd='servidor',
        carpetas={'dir_servidor':'/mbarete/servidor/'},
        puerto=666,
        index='indexsocket.html',
        flags=['init','error','respond',],
        name='mbarete'
    )
    web.log=0
    web.hilo_start()
def nodo_PC():
    import time
    reloj=['~',r'\ ','|','/','~',r'\ ','|','/']
    x=7
    n=nodo_python(
        dispositivos='3-38',
        ignore=[21],
        puerto=8002,
        name='cross',
        flags=['init','metodo','error','scan_async','media_me'],
        pwd='modulos',
        carpetas={'pwd_modulos':'mbarete/modulos/'}
        )
    #n.p('clients:',[c for c in n.clients])
    #n.p('n.media:',n.media)
    #print(n.media)
    n.start()
    for client in n.clients:
        files=[f for f in n.clients[client] if client in f]
        n.get(files)
    files=[f for f in n.media if n.media['media_me']['name'] in f]
    for client in n.clients:
        n.set(client,files)
    while 'sigue' in os.listdir(n.pwd):
        time.sleep(1)
        #print(reloj[x%7],end='\r')
        x= 7 if x==70 else x+1
    n.p(n.all_flags)
def servidor_stop():
    object_servidor.stop()

def nodoAndroi():
    import time
    reloj=['~',r'\ ','|','/','~',r'\ ','|','/']
    x=7
    if not 'sigue' in os.listdir():os.mkdir('sigue')
    n=nodo_python(dispositivos='20-22',ignore=['192.168.100.7'],username='android',pwd='/storage/emulated/0/0_PYTHON')
    n.p('clients:',[c for c in n.clients])
    n.p('n.media:',n.media)
    #print(n.media)
    n.start()
    for client in n.clients:
        files=[f for f in n.clients[client] if client in f]
        n.get(files)
    files=[f for f in n.media if n.media['media_me']['username'] in f]
    for client in n.clients:
        n.set(client,files)



if 'main' in __name__:
    import sys
    from pruebas import main_pruebas
    pruebas=[
        {'titulo':"Servidor Socket Python",'f':servidor_CHAT_socket_python},
        {'titulo':"Cliente Socket Python",'f':cliente_CHAT_socket_python},
        {'titulo':"DNS SERVER",'f':DNS_server},
        {'titulo':"NODO_PYTHON",'f':nodo_PC},
        {'titulo':"Servidor web 2.0",'f':hijo_web},
        {'titulo':"Para DETENER un Servidor",'f':servidor_stop}
        ]
    main_pruebas(pruebas,sys.argv)
            