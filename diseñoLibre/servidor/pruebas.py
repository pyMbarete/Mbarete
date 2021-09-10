#!/usr/bin/env python
# -*- coding: utf-8 -*-
# archivo generado por Diseño Libre para servidor

#Modulos importados
import socket, glob, json  
import threading
import os
info={
    'autor':'Lucas Mathias Villalba Diaz',
    'name':'servidor',
    'text':'Servidor HTTP Python',
    'descripcionBreve':'servidor http para  hacer correr como una API rest Full en red, para nuestros proyectos Mbarete',
    'descripcionLarga':'Servidor HTTP montado con Socket y threading , falta la integracion para que funcione de forma automatica dentro de nuestros proyectos mbarete, cargar logica del proyecto en el servidor y luego generar los response desde la clase mbarete del modulo mbarete',
    'img':'logo.png',
    'enlace':'mathiaslucasvidipy@gmail.com',
    'etiquetas':['default', 'inicio', 'servidor', 'HTTP_server', 'socket', 'APIrest Full', 'html', 'css', 'javascript', 'typescript', 'BBDD','DNS_server']
}
widgets={
    'servidorPanel':{
        'inputType':'panel',#OBLIGATORIO
        'etiquetas':['id','Inicio','default','panel','servidor'],
        'name':'servidor',#OBLIGATORIO
        'text':'Inicio Servidor HTTP Python',#OBLIGATORIO
        'anchor':'e',
        'inputs':{
            'inicio':{
                'inputType':'Button',
                'command':'manager',
                'text':'Administrador'
            }
        }
    },
    'servidorFrame':{
        'inputType':'Frame',#OBLIGATORIO
        'etiquetas':['id','Inicio','Frame','servidor'],
        'name':'servidorFrame',#OBLIGATORIO
        'text':'Frame Servidor HTTP Python',#OBLIGATORIO
        'inputs':{
            'inicio':{
                'inputType':'Button',
                'command':'manager',
                'text':'Administrador'
            }
        }
    }
}

def servidor_HTTP_python(pwd="",dns=1):
    if dns:
        s=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('10.255.255.255',1))
        ip=s.getsockname()
        s.close()
        host = ip[0]
    else:
        host = '0.0.0.0'
    host = '0.0.0.0'
    port = 8080
    format_encode='utf-8'
    numerosMagicos={
        'png':{'inicio':b'\x89PNG\r\n'},
        'gif1':{'inicio':b'GIF89a'},
        'gif2':{'inicio':b'GIF87a'},
        'jpg1':{'inicio':b'\xff\xd8\xff\xdb'},
        'jpg2':{'inicio':b'\xff\xd8\xff\xe0'},
        'jpg':{'inicio':b'\xff\xd8\xff\xee'},
        'webp':{'inicio':b'RIFF\xb0y\x00\x00WEBPVP8'},
        'exe':{'inicio':b'MZ'},
        'pdf':{'inicio':b'%PDF-'},
        'OggS':{'inicio':b'OggS'},
        'matroska':{'inicio':b'\x1a\x45\xdf\xa3'},
        'script':{'inicio':b'#!'},
        'sql':{'inicio':b'SQLite format 3'},
        'faxx':{'inicio':b'FORM????FAXX'},
        'zip1':{'inicio':b'\x50\x4b\x03\x04'},
        'zip2':{'inicio':b'\x50\x4b\x05\x06'},
        #'zip3':{'inicio':b'PK␅␆'},
        #'rar':{'inicio':b'Rar!␚␇␀'},
        #'windowMedia':{'inicio':b'0&²uŽfÏ␑¦Ù␀ª␀bÎl'},
        #'Photoshop':{'inicio':b'8BPS'},
        'wav':{'inicio':b'RIFF????WAVE'},
        #'avi':{'inicio':b'RIFF????AVI␠'},
        #'1mp3':{'inicio':b'ÿû'},
        #'2mp3':{'inicio':b'ÿó'},
        #'3mp3':{'inicio':b'ÿò'},
        'mp3':{'inicio':b'ID3'},
        'CD_DVD':{'inicio':b'CD001'},
        'midi':{'inicio':b'MThd'},
        #'MicrosoftOffice':{'inicio':b'ÐÏ␑à¡±␚á'},
        #'debutante':{'inicio':b'!␊'},
        'webpGoogle':{'inicio':b'RIFF????WEBP'},
        'mp4':{'inicio':b'ftypisom'},
        'blender':{'inicio':b'BLENDER'}
        }
        #'':{'inicio':b''},
        #'':{'inicio':b''}
    global status,recieve
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((host, port))
    server.listen()
    print(f"\nServidor HTTP corriendo en la direccion 'http://{host}:{port}/'")
    status=True
    clients = []
    usernames = []
    def requestToDictionary(request,add={}):
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
        if b'\r\n\r\n' in request:
            post=[ request.split(b'\r\n\r\n')[-1]]
        requ=[r.decode(format_encode) for r in request.split(b'\r\n')]
        ret={}
        for i in requ:
            if ('POST' in i) or ('GET' in i):
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
            if 'Content-Type: multipart/form-data;' in i:
                ret['boundary']=i.split('boundary=')[-1]
            
        if add:
            for a in add:
                ret[a]=add[a]
        return ret
    def respond(client, address):
        responder=False
        request=b''
        ok=True
        cabezera=True
        porcion=1024*5
        binario=None
        info={}
        while ok:
            datos_Bytes=client.recv(porcion)
            if (b'Android' in datos_Bytes) and (b'boundary' in datos_Bytes):
                info=requestToDictionary(datos_Bytes)
                datos_Bytes=client.recv(porcion)
            if (porcion > len(datos_Bytes)) and (b'\r\n' in datos_Bytes):
                ok = False
            if cabezera:
                if (b'\r\n\r\n' in datos_Bytes) or info:
                    cabezera=False
                    for b in numerosMagicos:
                        if numerosMagicos[b]['inicio'] in datos_Bytes:
                            binario=b
                    if binario:
                        request=datos_Bytes.split(numerosMagicos[binario]['inicio'])[0]
                        info=requestToDictionary(request,add=info)
                        subiendo = open(info['form_data']['filename'],"wb")
                        subiendo.write(numerosMagicos[binario]['inicio']+datos_Bytes.split(numerosMagicos[binario]['inicio'])[-1])
                        while binario:
                            datos_Bytes=client.recv(porcion)
                            if info['boundary'].encode(format_encode) in datos_Bytes:
                                subiendo.write(datos_Bytes.split(info['boundary'].encode(format_encode))[0])
                                request=info['boundary'].encode(format_encode)+datos_Bytes.split(info['boundary'].encode(format_encode))[-1]
                                binario=False
                            else:
                                subiendo.write(datos_Bytes)
                        subiendo.close()
                        print("Subido:",info['form_data']['filename'])
                    else:
                        request+=datos_Bytes
                else:
                    request+=datos_Bytes
            else:
                request+=datos_Bytes
        print('request:',request)
        info = requestToDictionary(request,add=info)
        if ''!= request:
            print(info)
            if '/cerrar' in  info['sub_dominio']:
                print('Servidor Apagado')
                client.close()
                server.close()
                status=False
            elif ('GET' in info['method']):
                if '/' ==  info['sub_dominio']:
                    myfile = 'index.html'
                elif 'pruebaGet' in info['sub_dominio']:
                    myfile='index.html' 
                elif 'video' in info['sub_dominio']:
                    myfile='bibliografia/ONE_PUNCH_PARTE_9.mp4'
                else:
                    myfile='media/GET.html'
                    file=open(myfile,'wb')
                    file.write(request)
                    file.close()
            elif ('POST' in info['method']):
                if 'pruebaPost' in info['sub_dominio']:
                    myfile='media/pruebaPost.html'
                    file=open(myfile,'wb')
                    file.write(request)
                    file.close()
                else:
                    myfile='media/POST.html'
                    file=open(myfile,'wb')
                    file.write(request)
                    file.close()

            try:
                print('myfile',myfile)
                header='HTTP/1.1 200 OK\n'
                if myfile.endswith('.jpg'): 
                    mimetype='image/jpg'
                elif myfile.endswith('.css'): 
                    mimetype='text/css'
                elif myfile.endswith('.pdf'): 
                    mimetype='application/pdf'
                elif myfile.endswith('.mp4'): 
                    mimetype='video/mp4'
                else: 
                    mimetype='text/html'
                header += 'Content-Type: '+str(mimetype)+'\n\n'
            except Exception as e:
                header='HTTP:/1.1 404 Not Found \n\n'
                response=f'<html><body>Error 404: File NOt Found<br> {e} </body></html>'.encode(format_encode)
            header=header.encode(format_encode)
            client.send(header)
            file=open(myfile,'rb')
            client.send(file.read())
            file.close()
        client.close()
        print("fin de coneccion")            
    def receive_connections():
        while status:
            client, address = server.accept()
            thread = threading.Thread(target=respond, args=(client, address))
            thread.start()
        print("fin de servicio")
    (target=receive_connections)
    server.close()

servidor_HTTP_python()
def DNS_server(url="web.mbarete.",ip_v4='127.0.0.1',port=8080):
    if LAN:
        s=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('10.255.255.255',1))
        ip=s.getsockname()
        s.close()
        host = ip[0]
    else:
        host = '0.0.0.0'
    port = 53
    print((host, port))
    server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server.bind((host, port))
    global zonedata
    def load_zones():
        jsonzone={}
        zonefiles=glob.glob('zones/*.zone')
        for zone in zonefiles:
            with open(zone) as zonedata:
                data=json.load(zonedata)
                zonename = data["$origin"]
                jsonzone[zonename]=data
        return jsonzone
    zonedata=load_zones()
    def getflags(flags):
        byte1=bytes(flags[:1])
        byte2=bytes(flags[1:2])
        rflags=''
        QR='1'
        OPCODE=''
        for bit in range(1,5):
            OPCODE+=str(ord(byte1)&(1<<bit))
        AA='1'
        TC='0'
        RD='0'
        #Byte 2
        RA='0'
        Z='000'
        RCODE='0000'
        return int(QR+OPCODE+AA+TC+RD,2).to_bytes(1,byteorder='big')+int(RA+Z+RCODE,2).to_bytes(1,byteorder='big')
    def getquestiondomain(data):
        state=0
        expectedlength=0
        domainstring=''
        domainparts=[]
        x=0
        y=0

        for byte in data:
            if state == 1:
                if byte != 0:
                    domainstring += chr(byte)
                x+=1
                if x == expectedlength:
                    domainparts.append(domainstring)
                    domainstring = ''
                    state=0
                    x=0
                if byte == 0:
                    domainparts.append(domainstring)
                    break
            else:
                state=1
                expectedlength=byte
            y+=1
        questiontype = data[y:y+2]
        return (domainparts,questiontype)
    def getzone(domain):
        global zonedata
        zone_name = '.'.join(domain)
        return zonedata[zone_name]
    def getrecs(data):
        domain,questiontype=getquestiondomain(data)
        qt=''
        if questiontype==b'\x00\x01':
            qt='a'
        zone=getzone(domain)
        return (zone[qt],qt,domain)
    def buildquestion(domainname,rectype):
        qbytes=b''
        for part in domainname:
            length=len(part)
            qbytes+=bytes([length])
            for char in part:
                qbytes=ord(char).to_bytes(1,byteorder='big')
            if rectype =='a':
                qbytes+=(2).to_bytes(1,byteorder='big')
            qbytes+=(1).to_bytes(1,byteorder='big')

        return qbytes
    def rectobytes(domainname,rectype,recttl,recval):
        rbytes=b''
        if rectype=='a':
            rbytes=rbytes+bytes([0])+bytes([1])
        rbytes=rbytes+bytes([0])+bytes([1])
        rbytes+=int(recttl).to_bytes(4,byteorder='big')
        if rectype=='a':
            rbytes=rbytes+bytes([0])+bytes([4])
            for part in recval.split('.'):
                rbytes+=bytes([int(part)])
        return rbytes
    def buildresponse(data):
        #Transaction ID
        TransactionID=data[:2]
        #Get the Flags
        Flags = getflags(data[2:4])

        # Question Count
        QDCOUNT = b'\x00\x01'

        #Answer Count
        ANCOUNT = len(getrecs(data[12:])[0]).to_bytes(2,byteorder='big')

        # Name Server
        NSCOUNT=(0).to_bytes(2,byteorder='big')

        # Additional Count
        ARCOUNT=(0).to_bytes(2,byteorder='big')

        dnsheader=TransactionID+Flags+QDCOUNT+ANCOUNT+NSCOUNT+ARCOUNT 

        #Create DNS BODY
        dnsbody=b''
        #Get answer for query
        records,rectype,domainname=getrecs(data[12:])
        dnsquestion=buildquestion(domainname,rectype)
        for record in records:
           dnsbody += rectobytes(domainname,rectype,record["ttl"],record["value"]) 
        print(dnsheader)
        return dnsheader+dnsquestion+dnsbody
    print('servidor DNS esta en Linea')
    while True:
        data, address = server.recvfrom(512)
        print(data)
        r=buildresponse(data)
        server.sendto(r,address)
      
#DNS_server()
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

def command(admin,G,info,ec,geo):
    print(info['subProyecto'])
    print('Info:',info['info'])
    print('Widgest:',info['widget'])
    print('Comandos',info['command']) 
    G.command[info['command']['manager']]=lambda : admin.transicion(G,admin.manager)
