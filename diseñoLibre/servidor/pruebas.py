#!/usr/bin/env python
# -*- coding: utf-8 -*-
# archivo generado por Diseño Libre para servidor

#Modulos importados
import socket, glob, json  
import threading
import os,datetime
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
def arboldearchivos(pwd=''):
    ret=[]
    if not pwd:
        pwd = os.getcwd()
    for check in os.listdir(pwd):
        if os.path.isfile(pwd+os.path.sep+check):
            ret += [pwd+os.path.sep+check]
        else:
            ret += arboldearchivos(pwd+os.path.sep+check)
    return ret

canal={}
def servidor_eventos(puerto=5050,host='0.0.0.0'):
    pass

def reglas_para_el_sevidor(pwd,dnsPort=53,sshPort=22,httpPort=80,nombreServicio='Mbarete_Server',reset=0):
    file="reglas.cmd"
    reglaDNS=f'netsh advfirewall firewall add rule name=”Open Port {dnsPort} para DNS de {nombreServicio}” dir=in action=allow protocol=TCP localport={dnsPort}\n'
    reglaSSH=f'netsh advfirewall firewall add rule name=”Open Port {sshPort} para SSH de {nombreServicio}” dir=in action=allow protocol=TCP localport={sshPort}\n'
    reglaHTTP=f'netsh advfirewall firewall add rule name=”Open Port {httpPort} para HTTP de {nombreServicio}” dir=in action=allow protocol=TCP localport={httpPort}\n'
    
    if (not (file in os.listdir(pwd))) or reset:
        regla=open(pwd+os.path.sep+file,"w")
        regla.write(reglaDNS)
        regla.write(reglaSSH)
        regla.write(reglaHTTP)
        regla.close()

fileZillaPort=14148
def DNS_server(pwd,archivo_zone='mbaretePro.zone',dominio_zone="web.mbarete.",ipv4_zone='127.0.0.1',port_zone=80):
    """
    if LAN:
        s=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('10.255.255.255',1))
        ip=s.getsockname()
        s.close()
        host = ip[0]
    else:
        host = '0.0.0.0'
    """
    DNS_host=ipv4_zone
    DNS_port = 53
    print((ipv4_zone, port_zone))
    server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server.bind((DNS_host, DNS_port))
    global zonedata
    def crear_archivo_ZONE(archivo_zone,dominio_zone,ipv4_zone,port_zone):
        time='time'
        #if port_zone:
        #    ipv4_zone+=':'+str(port_zone)+''
        archivo='{\n'
        archivo+='  "$origin":"'+str(dominio_zone)+'.",\n'
        archivo+='  "$ttl":3600,\n'
        archivo+='  "soa":{\n'
        archivo+='      "mname":"ns1.'+str(dominio_zone)+'.",\n'
        archivo+='      "rname":"admin.'+str(dominio_zone)+'.",\n'
        archivo+='      "serial":"{time}",\n'
        archivo+='      "refresh":3600,\n'
        archivo+='      "retry":600,\n'
        archivo+='      "expire":604800,\n'
        archivo+='      "minimun":86400\n'
        archivo+='  },\n'
        archivo+='  "ns":[\n'
        archivo+='      {"host":"ns1.'+str(dominio_zone)+'."},\n'
        archivo+='      {"host":"ns2.'+str(dominio_zone)+'."}\n'
        archivo+='  ],\n'
        archivo+='  "a":[\n'
        archivo+='      {"name":"@","ttl":400,"value":"0.0.0.0"},\n'
        archivo+='      {"name":"@","ttl":400,"value":"255.255.255.255"},\n'
        archivo+='      {"name":"@","ttl":400,"value":"127.0.0.1"},\n'
        archivo+='      {"name":"@","ttl":400,"value":"'+str(ipv4_zone)+'"},\n'
        archivo+='      {"name":"@","ttl":400,"value":"'+str(ipv4_zone)+'"}\n'
        archivo+='  ]\n'
        archivo+='}\n'
        file=open(archivo_zone,'wb')
        file.write(archivo.encode())
        file.close()
    def load_zones():
        if not dominio_zone+'.zone' in os.listdir(pwd):
            crear_archivo_ZONE(pwd+os.path.sep+dominio_zone+'.zone',dominio_zone,ipv4_zone,port_zone)
        jsonzone={}
        zonefiles=glob.glob(pwd+'/*.zone')
        for zone in zonefiles:
            with open(zone) as zonedata:
                data=json.load(zonedata)
                zonename = data["$origin"]
                jsonzone[zonename]=data
        print(jsonzone)
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
                qbytes+=ord(char).to_bytes(1,byteorder='big')
        if rectype =='a':
            qbytes+=(1).to_bytes(2,byteorder='big')
        qbytes+=(1).to_bytes(2,byteorder='big')
        return qbytes

    def rectobytes(domainname,rectype,recttl,recval):
        rbytes=b'\xc0\x0c'
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
      
#DNS_server("media"+os.path.sep+"servidor"+os.path.sep+'zones',archivo_zone='mbaretePro.zone',dominio_zone="ElectroZone",ipv4_zone='192.168.100.21',port_zone='80')

def servidor_HTTP_python(dominio="electrozone.local",pwd="media"+os.path.sep+"servidor",dns=1):
    global status,recieve,servidor_archivos
    host = '0.0.0.0'
    port = 80
    format_encode='utf-8'
    status=True
    clients = []
    usernames = []
    action_download='/download/'
    action_upload='/subir/'
    action_borrar='/borrar/'
    pwd_js=pwd+'\\js\\'
    pwd_upload=pwd+'\\download\\'
    pwd_download=pwd+'\\'
    s=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(('10.255.255.255',1))
    ip=s.getsockname()
    s.close()
    host_DNS = ip[0]
    reglas_para_el_sevidor(pwd,dnsPort=53,sshPort=22,httpPort=80,nombreServicio='Mbarete_Server',reset=0)
    #servidor_DNS = threading.Thread(target=DNS_server, args=(pwd+os.path.sep+'zones',), kwargs={'archivo_zone':'ElectroZone.zone','dominio_zone':dominio,'ipv4_zone':host_DNS,'port_zone':port})
    #servidor_DNS.start()
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((host, port))
    server.listen()
    print(f"\nServidor HTTP corriendo en la direccion 'http://{host_DNS}:{port}/'")
    def download():
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
        return arboldearchivos(pwd)

    servidor_archivos=download()

    print(servidor_archivos)
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
            
        if add:
            for a in add:
                ret[a]=add[a]
        return ret
    def respond(client, address):
        global servidor_archivos
        responder=False
        request=b''
        ok=True
        cabezera=True
        porcion=1024*5
        binario=None
        info={}
        while ok:
            try:
                datos_Bytes=client.recv(porcion)
                print(datos_Bytes)
            except:
                ok=False
            if (b'Android' in datos_Bytes) and (b'boundary' in datos_Bytes):
                request+=datos_Bytes
                info=requestToDictionary(datos_Bytes)
                datos_Bytes=client.recv(porcion)
            if (porcion > len(datos_Bytes)) and (b'\r\n' in datos_Bytes):
                ok = False
            if b'' == datos_Bytes:
                ok = False
            if cabezera:
                if ((b'\r\n\r\n' in datos_Bytes) or info):
                    cabezera=False
                    if 'boundary' in info:
                        boundary=b'--'+info['boundary'].encode(format_encode)
                        if boundary in datos_Bytes.split(b'\r\n'):
                            binario=datos_Bytes.split(boundary+b'\r\n')[-1].split(b'\r\n')[2]
                    elif (b'boundary=----' in datos_Bytes) and (b'\r\n\r\n' in datos_Bytes):
                        print('############## 2 BIUNDARY',datos_Bytes)
                        request+=datos_Bytes.split(b'\r\n\r\n')[0]+b'\r\n\r\n'
                        info=requestToDictionary(datos_Bytes.split(b'\r\n\r\n')[0])
                        boundary=b'--'+info['boundary'].encode(format_encode)
                        form_data=datos_Bytes.split(boundary+b'\r\n')[-1].split(b'\r\n\r\n')[0]
                        print(form_data)
                        request+= boundary+b'\r\n'+form_data
                        info=requestToDictionary(form_data,add=info)
                        binario=datos_Bytes.split(form_data+b'\r\n\r\n')[-1]
                    if binario:
                        boundary+=b'--\r\n'
                        #request=datos_Bytes.split(binario)[0]
                        #info=requestToDictionary(request,add=info)
                        subiendo = open(pwd_upload+info['form_data']['filename'],"wb")
                        if boundary in datos_Bytes:
                            subiendo.write(binario.split(boundary)[0])
                            request+=boundary+binario.split(boundary)[-1]
                        else:
                            subiendo.write(binario)
                            while binario:
                                datos_Bytes=client.recv(porcion)
                                if boundary in datos_Bytes:
                                    subiendo.write(datos_Bytes.split(boundary)[0])
                                    request+=boundary+datos_Bytes.split(boundary)[-1]
                                    binario=None
                                else:
                                    subiendo.write(datos_Bytes)
                        subiendo.close()
                        print("Subido:",info['form_data']['filename'])
                        servidor_archivos=download()
                        ok=False
                    else:
                        request+=datos_Bytes
                else:
                    request+=datos_Bytes
            else:
                request+=datos_Bytes
            print('ok:',ok)
        print('request:',request)
        info = requestToDictionary(request,add=info)
        if ''!= request:
            print(info)
            if '/cerrar' in  info['sub_dominio']:
                print('Servidor Apagado')
                client.close()
                server.close()
                #servidor_DNS.close()
                status=False
                os.system("curl http://"+host+":"+str(port)+"/cerrar")
            elif ('GET' in info['method']):
                if '/' ==  info['sub_dominio']:
                    myfile = pwd+os.path.sep+'index.html'
                elif pwd+info['sub_dominio'].replace('/',os.path.sep).replace('%20',' ') in servidor_archivos:
                    myfile=pwd+info['sub_dominio'].replace('/',os.path.sep).replace('%20',' ')
                    print('method GET full:',myfile)
                elif '/socket.io/?' in info['sub_dominio']:
                    io={}
                    for k in info['sub_dominio'].replace('/socket.io/?','').split('&'):
                        io[k.split('=')[0]]=k.split('=')[1] 
                    #print(io)
                    #print({k.split('=')[0]:k.split('=')[1] for k in info['sub_dominio'].replace('/socket.io/?','').split('&')})
                    myfile=pwd+os.path.sep+'socket_GET.io.html'
                    file=open(myfile,'wb')
                    file.write(str({k.split('=')[0]:k.split('=')[1] for k in info['sub_dominio'].replace('/socket.io/?','').split('&')}).encode())
                    #file.write(request)
                    file.close()
                else:
                    myfile=pwd+os.path.sep+'GET.html'
                    file=open(myfile,'wb')
                    file.write(b'<h1>Archivo No Encontrado</h1>')
                    file.write(request)
                    file.close()
            elif ('HEAD' in info['method']):
                if '/' ==  info['sub_dominio']:
                    myfile = pwd+os.path.sep+'index.html'
                elif pwd+info['sub_dominio'].replace('/',os.path.sep) in servidor_archivos:
                    myfile=pwd+info['sub_dominio'].replace('/',os.path.sep)
                    print('method HEAD:',myfile)
                elif '/socket.io/?' in info['sub_dominio']:
                    io={}
                    for k in info['sub_dominio'].replace('/socket.io/?','').split('&'):
                        io[k.split('=')[0]]=k.split('=')[1] 
                    #print(io)
                    #print({k.split('=')[0]:k.split('=')[1] for k in info['sub_dominio'].replace('/socket.io/?','').split('&')})
                    myfile=pwd+os.path.sep+'socket_GET.io.html'
                    file=open(myfile,'wb')
                    file.write(str({k.split('=')[0]:k.split('=')[1] for k in info['sub_dominio'].replace('/socket.io/?','').split('&')}).encode())
                    #file.write(request)
                    file.close()
                else:
                    myfile=pwd+os.path.sep+'GET.html'
                    file=open(myfile,'wb')
                    file.write(b'<h1>Archivo No Encontrado</h1>')
                    file.write(request)
                    file.close()
            elif ('POST' in info['method']):
                if '/subir' in info['sub_dominio']:
                    myfile=pwd+os.path.sep+'subido.html'
                    file=open(myfile,'wb')
                    file.write(b'<h1>Archivo Subido con Exito </h1>')
                    file.write(request)
                    file.close()
                elif '/socket.io/?' in info['sub_dominio']:
                    myfile=pwd+os.path.sep+'socket_POST.io.html'
                    file=open(myfile,'wb')
                    file.write(str({k.split('=')[0]:k.split('=')[1] for k in info['sub_dominio'].replace('/socket.io/?','').split('&')}).encode())
                    #file.write(request)
                    file.close()
                else:
                    myfile=pwd+os.path.sep+'POST.html'
                    file=open(myfile,'wb')
                    file.write(request)
                    file.close()
            #80029563
            try:
                print('myfile',myfile)
                header='HTTP/1.1 200 OK\n'
                if myfile.endswith('.jpg'): 
                    mimetype='Content-Type: image/jpg'
                elif myfile.endswith('.css'): 
                    mimetype='Content-Type: text/css'
                elif myfile.endswith('.js'): 
                    mimetype='Content-Type: text/javascript'
                elif myfile.endswith('.pdf'): 
                    mimetype='Content-Type: application/pdf'
                elif myfile.endswith('.mp4'): 
                    mimetype='Content-Type: video/mp4'
                elif '/download/' in info['sub_dominio'][:len('/download/')]:
                    myfile=info['sub_dominio'][len('/download/'):].replace('/',os.path.sep).replace('%20',' ')
                    print(myfile,os.path.getsize(myfile),datetime.datetime.now()) 
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
                    mimetype+='Content-Disposition: attachment; filename="'+info['sub_dominio'].split('/')[-1]+'"\n'
                    mimetype+='Content-Type: application/octet-stream\n'
                    mimetype+='\n'
                    print('mimetype:',mimetype)
                else: 
                    mimetype='Content-Type: text/html'
                header += str(mimetype)+'\n\n'
                """
                if ('GET' in info['method']):
                
                 if '/descargar' ==  info['sub_dominio']:
                        header = '200 OK \nContent-Type: text/html; charset=utf-8 \nContent-Disposition: attachment; filename="genial.html"\nContent-Length: 22\n<HTML>Guárdame!</HTML>'
                """
            except Exception as e:
                print(e)
                header='HTTP:/1.1 404 Not Found \n\n'
                response=f'<html><body>Error 404: File NOt Found<br> {e} </body></html>'.encode(format_encode)
            header=header.encode(format_encode)
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
    def receive_connections():
        while status:
            client, address = server.accept()
            thread = threading.Thread(target=respond, args=(client, address))
            thread.start()
        print("fin de servicio")
    
    receive_connections()
    server.close()

servidor_HTTP_python()

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
