#!/usr/bin/env python
# -*- coding: latin-1 -*-
#curso apache introduccion
#https://books.google.com.py/books?id=Kg8bAgAAQBAJ&lpg=RA1-PA10&dq=%2Fetc%2Fapache2%2Fapache.conf%20en%20espa%C3%B1ol&pg=RA1-PA15#v=onepage&q=/etc/apache2/apache.conf%20en%20espa%C3%B1ol&f=false
import os
import sys
import socket
import threading
import glob
import json
#print(os.environ['HOME'] if ('HOME' in os.environ) else os.environ['HOMEPATH'] ,sys.argv)
global f
f={}
def getFile(f,full=1):
    file=open(f)
    ret=[]
    for line in file:
        #print(line.strip())
        if str(line.strip())!='':
            ret += [str(line if full else line.strip())]
    file.close()
    return ret if len(ret)>1 else ret[0]
def setFile(f,valor,echo=1):
    if echo:
        print('Archivo:',f)
    file=open(f,"wb")
    if 'list' in str(type(valor)):
        for line in valor:
            if echo:
                #line.encode()
                print(line.encode('latin-1'))
            file.write(line.encode('latin-1')+b'\n')    
    else:
        file.write(valor)
    file.close()
    
def aplicar_Fordward(conect):
    for ip in conect:
        salida='' if (conect[ip]['accion']!='add') else "connectaddress={0} connectport={1}".format(conect[ip]['direccion'][1],conect[ip]['puerto'][1])
        command="netsh interface portproxy {0} {1}  listenaddress={2} listenport={3} {4}".format(conect[ip]['accion'], conect[ip]['tipo'], conect[ip]['direccion'][0], conect[ip]['puerto'][0], salida)
        print(command)
        os.system(command)
    os.system("netsh interface portproxy show all")

def configProxy(file,ip_hyperV,ip_wsl_ip_window):
    ultimaConfig=[[line.split(" ")[:-1]+[line.split(" ")[-1].replace('_'," ")]] for line in getFile("ultimaConfig")]
    #cargarConfig=getFile()

def scraping(file):
    lines=getFile(file,full=0)
    print(range(len(lines)),lines)
    for y in range(0,len(lines),1):
        print(y,lines[y])
        l=lines[y]
        pre=0
        only=1
        for x in l:
            if (x==' ') and (only):
                pre +=1
            else:
                only=0
        lines=[pre,lines[y]]
    print(lines)
    return lines
f['scraping']=scraping

def rootCall(arg,kwarg):
    #print(arg,kwarg)
    goto = kwarg['goto'] if ('goto' in kwarg) else 'root'
    cmd = kwarg['cmd'] if ('cmd' in kwarg) else 'echo '
    go = kwarg['go'] if ('go' in kwarg) else os.environ['USERPROFILE']+'\\mbareteAdmin.cmd'
    actualPath=os.getcwd()
    actualDrive=os.path.splitdrive(os.getcwd())[0]
    goFile=[
        r'@ECHO off',
        actualDrive,
        'cd "'+actualPath+'"',
        cmd+" "+goto
    ]
    setFile(go,goFile,echo=0)
f['rootCall']=rootCall
def reglas(pwd,dnsPort=53,sshPort=22,httpPort=80,nombreServicio='Mbarete_Server',reset=0):
    #a=sys.argv[sys.argv.index('_')+1] if ('_' in sys.argv) else False
    sshArchivo= ('program= '+sys.argv[sys.argv.index('sshArchivo')+1]) if ('sshArchivo' in sys.argv) else ''
    sshPort=('localport= '+sys.argv[sys.argv.index('sshPort')+1]) if ('sshPort' in sys.argv) else ''
    dnsArchivo=('program= '+sys.argv[sys.argv.index('dnsArchivo')+1]) if ('dnsArchivo' in sys.argv) else ''
    dnsPort=('localport= '+sys.argv[sys.argv.index('dnsPort')+1]) if ('dnsPort' in sys.argv) else ''
    httpArchivo=('program= '+sys.argv[sys.argv.index('httpArchivo')+1]) if ('httpArchivo' in sys.argv) else ''
    httpPort=('localport= '+sys.argv[sys.argv.index('httpPort')+1]) if ('httpPort' in sys.argv) else ''
    file=sys.argv[sys.argv.index('file')+1] if ('file' in sys.argv) else "reglas.cmd"
    """
    netsh advfirewall firewall add rule 
    name="permitir explorador"
    dir=in 
    program="c:\archivos de programa\explorador\explorador.exe"
    security=authnoencap 
    action=allow
    """
    reglaDNS=f'netsh advfirewall firewall add rule name="Open Port {dnsPort} para DNS de {nombreServicio}" dir=in action=allow protocol=TCP {dnsPort} {dnsArchivo}\n'
    reglaSSH=f'netsh advfirewall firewall add rule name="Open Port {sshPort} para SSH de {nombreServicio}" dir=in action=allow protocol=TCP {sshPort} {dnsArchivo}\n'
    reglaHTTP=f'netsh advfirewall firewall add rule name="Open Port {httpPort} para HTTP de {nombreServicio}" dir=in action=allow protocol=TCP {httpPort} {dnsArchivo}\n'
    
    if (not (file in os.listdir(pwd[0]))) or reset:
        regla=open(pwd[0]+os.path.sep+file,"w")
        regla.write(reglaDNS)
        regla.write(reglaSSH)
        regla.write(reglaHTTP)
        regla.close()
f['reglas']=reglas
def regla(*arg,**kwargs):
    dnsPort=53
    sshPort=22
    httpPort=80
    nombreServicio='Mbarete_Server'
    reset=0
    #_=sys.argv[sys.argv.index('_')+1] if ('_' in sys.argv) else False
    archivo= ('program= '+sys.argv[sys.argv.index('archivo')+1]) if ('archivo' in sys.argv) else ''
    port=('localport= '+sys.argv[sys.argv.index('port')+1]) if ('port' in sys.argv) else ''
    file=httpPort=sys.argv[sys.argv.index('file')+1] if ('file' in sys.argv) else "reglas.cmd"
    """
    netsh advfirewall firewall add rule 
    name="permitir explorador"
    dir=in 
    program="c:\archivos de programa\explorador\explorador.exe"
    security=authnoencap 
    action=allow
    """
    archivo=f'netsh advfirewall firewall add rule name="Open Port {dnsPort} para DNS de {nombreServicio}" dir=in action=allow protocol=TCP {dnsPort} {dnsArchivo}\n'
    
    if (not (file in os.listdir(pwd[0]))) or reset:
        regla=open(pwd[0]+os.path.sep+file,"w")
        regla.write(archivo)
        regla.close()
f['regla']=regla

def dirProgram(program,drive='C:\\',exacta=0,carpetas=['Program Files','Program Files (x86)']):
    carpetas=[drive+d for d in carpetas]
    program=program.upper()
    #retorna la Ruta Absoluta del Programa o  del Nombre de la carpeta
    pwd=False
    for d in carpetas:
        if exacta:
            for p in os.listdir(d):
                if program == p.upper():
                    pwd=d+'\\'+p
        else:
            for p in os.listdir(d):
                if program in p.upper():
                    pwd=d+'\\'+p
    return pwd
def configBIND_win(arg):
    server_name= sys.argv[sys.argv.index('server_name')+1] if ('server_name' in sys.argv) else 'mbarete'
    #configuracion y generador de los archivos para la instalacion del servidoR BIND9 EN WINDOWS
    dirBIND=dirProgram('ISC BIND 9')
    if dirBIND:
        if 'etc' in os.listdir(dirBIND):
            conf=dirBIND+'\\etc\\'+server_name+'.conf'
            """
            options {
                // Working directory
                directory "/etc/namedb";
                forwarders {8.8.4.4;8.8.8.8;1.1.1.1;};
                listen-on {any;};
                // Do not allow access to cache
                allow-query-cache { none; };
                // This is the default
                allow-query { any; };
                // Do not provide recursive service
                //recursion no;
                };

                // Provide a reverse mapping for the loopback
                // address 127.0.0.1
                zone "0.0.127.in-addr.arpa" {
                type primary;
                file "localhost.rev";
                notify no;
                };
                // We are the primary server for example.com
                zone "example.com" {
                type primary;
                file "example.com.db";
                // IP addresses of secondary servers allowed to
                // transfer example.com
                allow-transfer {
                192.168.4.14;
                192.168.5.53;
                };
                };
                // We are a secondary server for eng.example.com
                zone "eng.example.com" {
                type secondary;
                file "eng.example.com.bk";
                // IP address of eng.example.com primary server
                masters { 192.168.4.12; };
                };
            """
    else:
        pass

f['configBIND_win']=configBIND_win  

def hostName(pwd='host'+os.path.sep):
    hosts = pwd+(sys.argv[2] if len(sys.argv)==3 else 'hosts')
    actualIpLocal=getFile(pwd+'actualIpLocal')
    ultimoIpLocal=getFile(pwd+'ultimoIpLocal')
    ultimoHostName=getFile(pwd+'ultimoHostName')
    ultimoComentario=getFile(pwd+'ultimoComentario')
    if actualIpLocal==ultimoIpLocal:
        print("No se encontro ningun cambio en la IP de esta maquina en la red local actual.")
    else:
        print("IP anterior:{0} \nIP Nueva:{1}".format(ultimoIpLocal,actualIpLocal))
    actualHostName= "#"+input("Ingrese el Nuevo Host Name:") if ('s' in input("El Host Name de esta Maquina es: {0}.\nDesea cambiarlo s/n?:".format(ultimoHostName)).lower()) else ultimoHostName
    actualComentario= "#"+input("Ingrese el Nuevo Comentario:") if ('s' in input("El Comentario de este Host Name es: {0}.\nDesea cambiarlo s/n?:".format(ultimoComentario)).lower()) else ultimoComentario
    #print('\n'+'\n'+'\n'+'\n'+'\n')
    ultimoLine='{0} {1} {2}'.format(ultimoIpLocal,ultimoHostName,ultimoComentario)
    actualLine='{0} {1} {2}'.format(actualIpLocal,actualHostName,actualComentario)  
    hostsFile=getFile(hosts)
    if ultimoLine in hostsFile:
        hostsFile[hostsFile.index(ultimoLine)]=actualLine
    else:
        hostsFile+=[actualLine]
    setFile(hosts,hostsFile)
    setFile(pwd+'ultimoIpLocal',actualIpLocal,echo=0)
    setFile(pwd+'ultimoHostName',actualHostName,echo=0)
    setFile(pwd+'ultimoComentario',actualComentario,echo=0)
f['hostName']=hostName

def conf():
    hosts = pwd+(sys.argv[2] if len(sys.argv)==3 else '\\servidor\\nginx\\conf\\')
    actualIpLocal=getFile(pwd+'actualIpLocal')
    ultimoIpLocal=getFile(pwd+'ultimoIpLocal')
    ultimoHostName=getFile(pwd+'ultimoHostName')
    ultimoComentario=getFile(pwd+'ultimoComentario')
    if actualIpLocal==ultimoIpLocal:
        print("No se encontro ningun cambio en la IP de esta maquina en la red local actual.")
    else:
        print("IP anterior:{0} \nIP Nueva:{1}".format(ultimoIpLocal,actualIpLocal))
    actualHostName= "#"+input("Ingrese el Nuevo Host Name:") if ('s' in input("El Host Name de esta Maquina es: {0}.\nDesea cambiarlo s/n?:".format(ultimoHostName)).lower()) else ultimoHostName
    actualComentario= "#"+input("Ingrese el Nuevo Comentario:") if ('s' in input("El Comentario de este Host Name es: {0}.\nDesea cambiarlo s/n?:".format(ultimoComentario)).lower()) else ultimoComentario
    #print('\n'+'\n'+'\n'+'\n'+'\n')
    ultimoLine='{0} {1} {2}'.format(ultimoIpLocal,ultimoHostName,ultimoComentario)
    actualLine='{0} {1} {2}'.format(actualIpLocal,actualHostName,actualComentario)  
    hostsFile=getFile(hosts)
    if ultimoLine in hostsFile:
        hostsFile[hostsFile.index(ultimoLine)]=actualLine
    else:
        hostsFile+=[actualLine]
    setFile(hosts,hostsFile)
    setFile(pwd+'ultimoIpLocal',actualIpLocal,echo=0)
    setFile(pwd+'ultimoHostName',actualHostName,echo=0)
    setFile(pwd+'ultimoComentario',actualComentario,echo=0)
f['conf']=conf


#enrrutar
def getIPv4():
    import socket
    s=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(('10.255.255.255',1))
    print(str(s.getsockname()[0]) )
f['getIPv4']=getIPv4

def enrrutar():
    #setHostsName('192.168.100.21','powerHost','#esto es un host Name de prueba')
    IP_local=getFile(sys.argv[2])
    IP_wsl=getFile(sys.argv[3])
    #IP_hyperV=getFile(sys.argv[4])
    ultimoIpLocal=getFile('ultimoIpLocal')
    print('IP_local=',IP_local,'IP_wsl=',IP_wsl)
    IP_wsl=input("Ingrese la IPv4 Actual de WSL:") if ('s' in input("La IPv4 de WSL es: {0}.\nDesea cambiarlo s/n?:".format(IP_wsl)).lower()) else IP_wsl
    IP_local=input("Ingrese la IPv4 Actual de esta maquina en la red local:") if ('s' in input("La IPv4 de esta maquina en la red local es: {0}.\nDesea cambiarlo s/n?:".format(IP_local)).lower()) else IP_local
    puertos={
        'apache2':[80,80],
        'ssh':[23,23],
        'postgresql':[5432,5432]
        }
    if IP_local != ultimoIpLocal:
        aplicar_Fordward({p:{'accion':'delete','tipo':'v4tov4','direccion':[ultimoIpLocal,IP_wsl],'puerto':puertos[p]} for p in puertos})
    aplicar_Fordward({p:{'accion':'add','tipo':'v4tov4','direccion':[IP_local,IP_wsl],'puerto':puertos[p]} for p in puertos})
    setFile('actualIpLocal',IP_local)
f['enrrutar']=enrrutar
def DNS_stop(*arg):
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
    DNS_host='0.0.0.0'
    DNS_port = 53
    server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server.bind((DNS_host, 53535))
    server.sendto(b'stop_full',(DNS_host, DNS_port))
f['DNS_stop']=DNS_stop

def DNS_start(arg,kwarg):
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
    pwd=sys.argv[sys.argv.index('pwd')+1]
    server_name=sys.argv[sys.argv.index('server_name')+1]
    server_ip=sys.argv[sys.argv.index('server_ip')+1]
    #server_=sys.argv[sys.argv.index('server_')+1]
    port_zone=80
    DNS_host='0.0.0.0'
    DNS_port = 53
    print((server_ip, port_zone))
    server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server.bind((DNS_host, DNS_port))
    #server.listen()
    global zonedata
    def crear_archivo_ZONE(archivo_zone,server_name,server_ip,port_zone):
        time='time'
        #if port_zone:
        #    server_ip+=':'+str(port_zone)+''
        archivo='{\n'
        archivo+='  "$origin":"'+str(server_name)+'.",\n'
        archivo+='  "$ttl":3600,\n'
        archivo+='  "soa":{\n'
        archivo+='      "mname":"ns1.'+str(server_name)+'.",\n'
        archivo+='      "rname":"admin.'+str(server_name)+'.",\n'
        archivo+='      "serial":"{time}",\n'
        archivo+='      "refresh":3600,\n'
        archivo+='      "retry":600,\n'
        archivo+='      "expire":604800,\n'
        archivo+='      "minimun":86400\n'
        archivo+='  },\n'
        archivo+='  "ns":[\n'
        archivo+='      {"host":"ns1.'+str(server_name)+'."},\n'
        archivo+='      {"host":"ns2.'+str(server_name)+'."}\n'
        archivo+='  ],\n'
        archivo+='  "a":[\n'
        archivo+='      {"name":"@","ttl":400,"value":"'+str(server_ip)+'"},\n'
        archivo+='      {"name":"@","ttl":400,"value":"'+str(server_ip)+'"},\n'
        archivo+='      {"name":"@","ttl":400,"value":"'+str(server_ip)+'"},\n'
        archivo+='      {"name":"@","ttl":400,"value":"0.0.0.0"},\n'
        archivo+='      {"name":"@","ttl":400,"value":"255.255.255.255"}\n'
        archivo+='  ]\n'
        archivo+='}\n'
        file=open(archivo_zone,'wb')
        file.write(archivo.encode())
        file.close()
    def load_zones():
        if not server_name+'.zone' in os.listdir(pwd):
            crear_archivo_ZONE(pwd+os.path.sep+server_name+'.zone',server_name,server_ip,port_zone)
        else:
            print(server_name+'.zone',"ya Existe")
        jsonzone={}
        zonefiles=glob.glob(pwd+'/*.zone')
        for zone in zonefiles:
            with open(zone) as zonedata:
                data=json.load(zonedata)
                zonename = data["$origin"]
                jsonzone[zonename]=data
        for zone in jsonzone:
            print(zone,jsonzone[zone])
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
        if data==b'stop_full':
            return False
        else:
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
            return dnsheader+dnsquestion+dnsbody
    print('servidor DNS esta en Linea')
    while True:
        data, address = server.recvfrom(512)
        r=buildresponse(data)
        if r==False:
            break
        else:
            print(address,r)
            server.sendto(r,address)
f['DNS_start']=DNS_start  
#DNS_server("media"+os.path.sep+"servidor"+os.path.sep+'zones',server_name="ElectroZone",server_ip='192.168.100.21',port_zone='80')


#Open the Firewall
#netsh advfirewall firewall add rule name=”Open Port 2222 for WSL2” dir=in action=allow protocol=TCP localport=2222


#Forward Ports into WSL2
#netsh interface portproxy add v4tov4  listenaddress=192.168.100.21 listenport=7373 connectaddress=172.30.168.253 connectport=7373


#You can list all your portproxy rules like this if you're concerned:
#netsh interface portproxy show all

#You can remove them all if you want with
#netsh int portproxy reset all
def prueba(arg,kwarg):
    print(arg,kwarg)
f['prueba']=prueba
def help(arg,kwarg):
    print(f)

f['help']=help
def argvToParametros(prefijo='-'):
    kw=[]
    p = sys.argv
    arg=[]
    kwarg={}
    for i in range(0,len(sys.argv)):
        if prefijo in p[i][0]:
            kw+=[i,i+1]
            kwarg[p[i][1:]]=p[i+1]
        else:
            if not i in kw:
                arg+=[p[i]]
    return (arg,kwarg)

if 1<len(sys.argv):
    f[sys.argv[1]](*argvToParametros())
