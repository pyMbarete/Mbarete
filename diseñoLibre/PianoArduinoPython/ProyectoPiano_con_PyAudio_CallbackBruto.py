#::=()[]''""_+;<>!\% esto es un commentario

import pyaudio
import wave
import time
import sys
import serial
import os
import shutil

global reproduciendo
global wav
global sonando
global samplers
global leido

global stream_0, wf0
global stream_1, wf1
global stream_2, wf2
global stream_3, wf3
global stream_4, wf4
global stream_5, wf5
global stream_6, wf6
global stream_7, wf7
global stream_8, wf8
global stream_9, wf9
global stream_10, wf10
global stream_11, wf11
global stream_12, wf12
global stream_13, wf13

reproduciendo=True
wav=[]
direccion=os.getcwd()+"//media//packs//"
file=direccion+"silencio.wav"
# instantiate PyAudio (1)
p1 = pyaudio.PyAudio()

wf0 = wave.open(file, 'rb')
wf1 = wave.open(file, 'rb')
wf2 = wave.open(file, 'rb')
wf3 = wave.open(file, 'rb')
wf4 = wave.open(file, 'rb')
wf5 = wave.open(file, 'rb')
wf6 = wave.open(file, 'rb')
wf7 = wave.open(file, 'rb')
wf8 = wave.open(file, 'rb')
wf9 = wave.open(file, 'rb')
wf10 = wave.open(file, 'rb')
wf11 = wave.open(file, 'rb')
wf12 = wave.open(file, 'rb')

def archivos(direccion):
    global wav
    global leido
    wav=[]
    packs=[]
    leido = []
    os.chdir(direccion)
    midir=[d for d in os.listdir() if not d in ['silencio.wav']]
    for instrumento in midir:
        os.chdir(instrumento)
        packs.append([instrumento,"octetos"])
        octetos=[]
        hay_notas=[0,0,0,0,0,0,0,0,0,0]
        notas=os.listdir()
        for x in range(0,10):
            octeto=[]
            hay_nota=False
            if str(x)+"C.wav" in notas :
                octeto.append(str(x)+"C.wav")
                hay_nota=True
            else:
                octeto.append("silencio.wav")
            if str(x)+"C#.wav" in notas :
                octeto.append(str(x)+"C#.wav")
                hay_nota=True
            else:
                octeto.append("silencio.wav")
            if str(x)+"D.wav" in notas :
                octeto.append(str(x)+"D.wav")
                hay_nota=True
            else:
                octeto.append("silencio.wav")
            if str(x)+"D#.wav" in notas :
                octeto.append(str(x)+"D#.wav")
                hay_nota=True
            else:
                octeto.append("silencio.wav")
            if str(x)+"E.wav" in notas :
                octeto.append(str(x)+"E.wav")
                hay_nota=True
            else:
                octeto.append("silencio.wav")
            if str(x)+"F.wav" in notas :
                octeto.append(str(x)+"F.wav")
                hay_nota=True
            else:
                octeto.append("silencio.wav")
            if str(x)+"F#.wav" in notas :
                octeto.append(str(x)+"F#.wav")
                hay_nota=True
            else:
                octeto.append("silencio.wav")
            if str(x)+"G.wav" in notas :
                octeto.append(str(x)+"G.wav")
                hay_nota=True
            else:
                octeto.append("silencio.wav")
            if str(x)+"G#.wav" in notas :
                octeto.append(str(x)+"G#.wav")
                hay_nota=True
            else:
                octeto.append("silencio.wav")
            if str(x)+"A.wav" in notas :
                octeto.append(str(x)+"A.wav")
                hay_nota=True
            else:
                octeto.append("silencio.wav")
            if str(x)+"A#.wav" in notas :
                octeto.append(str(x)+"A#.wav")
                hay_nota=True
            else:
                octeto.append("silencio.wav")
            if str(x)+"B.wav" in notas :
                octeto.append(str(x)+"B.wav")
                hay_nota=True
            else:
                octeto.append("silencio.wav")
            
            if hay_nota:
                hay_notas[x]=1
            octetos.append(octeto)
        packs[-1]=[instrumento,octetos,hay_notas]
        os.chdir("..")
    os.chdir("..")
    for x in range(0,len(packs)):
        notas=": "
        for n in range(0,len(packs[x][2])):
            if 1==packs[x][2][n]:
                notas=notas+str(n)+" "
        print(packs[x][0],x,notas)
    instrumentos=input("ingrese el numero del INSTRUMENTO para cada octeto, separado por COMAS:").split(',')
    octetos=input("ingrese el numero de la ESCALA DEL INSTRUMENTO segun este disponible para cada octeto, separado por COMAS:").split(',')
    for n in range(0,4):
        for x in range(0,12):
            wav.append(direccion+packs[int(instrumentos[n])][0]+"/"+packs[int(instrumentos[n])][1][int(octetos[n])][x])
            leido.append("0")

archivos(direccion)
def callback_0(in_data, frame_count, time_info, status):
    try:
        data = wf0.readframes(frame_count)
        return (data, pyaudio.paContinue)
    except:
        reproduciendo=False
def callback_1(in_data, frame_count, time_info, status):
    try:
        data = wf1.readframes(frame_count)
        return (data, pyaudio.paContinue)
    except:
        reproduciendo=False
def callback_2(in_data, frame_count, time_info, status):
    data = wf2.readframes(frame_count)
    return (data, pyaudio.paContinue)
def callback_3(in_data, frame_count, time_info, status):
    data = wf3.readframes(frame_count)
    return (data, pyaudio.paContinue)
def callback_4(in_data, frame_count, time_info, status):
    data = wf4.readframes(frame_count)
    return (data, pyaudio.paContinue)
def callback_5(in_data, frame_count, time_info, status):
    data = wf5.readframes(frame_count)
    return (data, pyaudio.paContinue)
def callback_6(in_data, frame_count, time_info, status):
    data = wf6.readframes(frame_count)
    return (data, pyaudio.paContinue)
def callback_7(in_data, frame_count, time_info, status):
    data = wf7.readframes(frame_count)
    return (data, pyaudio.paContinue)
def callback_8(in_data, frame_count, time_info, status):
    data = wf8.readframes(frame_count)
    return (data, pyaudio.paContinue)
def callback_9(in_data, frame_count, time_info, status):
    data = wf9.readframes(frame_count)
    return (data, pyaudio.paContinue)
def callback_10(in_data, frame_count, time_info, status):
    data = wf10.readframes(frame_count)
    return (data, pyaudio.paContinue)
def callback_11(in_data, frame_count, time_info, status):
    data = wf11.readframes(frame_count)
    return (data, pyaudio.paContinue)
def callback_12(in_data, frame_count, time_info, status):
    data = wf12.readframes(frame_count)
    return (data, pyaudio.paContinue)

# open stream_n using callback_n (3)
stream_0 = p1.open(format=p1.get_format_from_width(wf0.getsampwidth()),
                channels=wf0.getnchannels(),
                rate=wf0.getframerate(),
                output=True,
                stream_callback=callback_0)
stream_1 = p1.open(format=p1.get_format_from_width(wf1.getsampwidth()),
                channels=wf1.getnchannels(),
                rate=wf1.getframerate(),
                output=True,
                stream_callback=callback_1)
stream_2 = p1.open(format=p1.get_format_from_width(wf2.getsampwidth()),
                channels=wf2.getnchannels(),
                rate=wf2.getframerate(),
                output=True,
                stream_callback=callback_2)
stream_3 = p1.open(format=p1.get_format_from_width(wf3.getsampwidth()),
                channels=wf3.getnchannels(),
                rate=wf3.getframerate(),
                output=True,
                stream_callback=callback_3)
stream_4 = p1.open(format=p1.get_format_from_width(wf4.getsampwidth()),
                channels=wf4.getnchannels(),
                rate=wf4.getframerate(),
                output=True,
                stream_callback=callback_4)
stream_5 = p1.open(format=p1.get_format_from_width(wf5.getsampwidth()),
                channels=wf5.getnchannels(),
                rate=wf5.getframerate(),
                output=True,
                stream_callback=callback_5)
stream_6 = p1.open(format=p1.get_format_from_width(wf6.getsampwidth()),
                channels=wf6.getnchannels(),
                rate=wf6.getframerate(),
                output=True,
                stream_callback=callback_6)
stream_7 = p1.open(format=p1.get_format_from_width(wf7.getsampwidth()),
                channels=wf7.getnchannels(),
                rate=wf7.getframerate(),
                output=True,
                stream_callback=callback_7)
stream_8 = p1.open(format=p1.get_format_from_width(wf8.getsampwidth()),
                channels=wf8.getnchannels(),
                rate=wf8.getframerate(),
                output=True,
                stream_callback=callback_8)
stream_9 = p1.open(format=p1.get_format_from_width(wf9.getsampwidth()),
                channels=wf9.getnchannels(),
                rate=wf9.getframerate(),
                output=True,
                stream_callback=callback_9)
stream_10 = p1.open(format=p1.get_format_from_width(wf10.getsampwidth()),
                channels=wf10.getnchannels(),
                rate=wf10.getframerate(),
                output=True,
                stream_callback=callback_10)
stream_11 = p1.open(format=p1.get_format_from_width(wf11.getsampwidth()),
                channels=wf11.getnchannels(),
                rate=wf11.getframerate(),
                output=True,
                stream_callback=callback_11)
stream_12 = p1.open(format=p1.get_format_from_width(wf12.getsampwidth()),
                channels=wf12.getnchannels(),
                rate=wf12.getframerate(),
                output=True,
                stream_callback=callback_12)

stream_0.start_stream()
stream_1.start_stream()
stream_2.start_stream()
stream_3.start_stream()
stream_4.start_stream()
stream_5.start_stream()
stream_6.start_stream()
stream_7.start_stream()
stream_8.start_stream()
stream_9.start_stream()
stream_10.start_stream()
stream_11.start_stream()
stream_12.start_stream()

#::=()[]''""_+;<>!\% esto es un commentario
def stop_all():
    global sonando
    global samplers
    global stream_0, wf0
    global stream_1, wf1
    global stream_2, wf2
    global stream_3, wf3
    global stream_4, wf4
    global stream_5, wf5
    global stream_6, wf6
    global stream_7, wf7
    global stream_8, wf8
    global stream_9, wf9
    global stream_10, wf10
    global stream_11, wf11
    global stream_12, wf12
    sonando=[0,0,0,0,0,0,0,0,0,0,0,0,0]
    samplers=["","","","","","","","","","","","",""]
    leido = ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0']
    stream_0.stop_stream()
    stream_0.close()
    wf0.close()
    stream_1.stop_stream()
    stream_1.close()
    wf1.close()
    stream_2.stop_stream()
    stream_2.close()
    wf2.close()
    stream_3.stop_stream()
    stream_3.close()
    wf3.close()
    stream_4.stop_stream()
    stream_4.close()
    wf4.close()
    stream_5.stop_stream()
    stream_5.close()
    wf5.close()
    stream_6.stop_stream()
    stream_6.close()
    wf6.close()
    stream_7.stop_stream()
    stream_7.close()
    wf7.close()
    stream_8.stop_stream()
    stream_8.close()
    wf8.close()
    stream_9.stop_stream()
    stream_9.close()
    wf9.close()
    stream_10.stop_stream()
    stream_10.close()
    wf10.close()
    stream_11.stop_stream()
    stream_11.close()
    wf11.close()
    stream_12.stop_stream()
    stream_12.close()
    wf12.close()
def play(x):
    global wav
    global sonando
    global samplers
    global presionado
    global stream_0, wf0
    global stream_1, wf1
    global stream_2, wf2
    global stream_3, wf3
    global stream_4, wf4
    global stream_5, wf5
    global stream_6, wf6
    global stream_7, wf7
    global stream_8, wf8
    global stream_9, wf9
    global stream_10, wf10
    global stream_11, wf11
    global stream_12, wf12
    libre="null"
    y_final="null"
    if sum(presionado)==0:
        presionado[0]=1
        libre=0
    elif x in samplers:
        libre = samplers.index(x)
        presionado[libre]=1
    else:
        for y in range(0,6):
            if (12*(y))<=x and x<(12*(y+1)):
                y_final=y
                for son in range(12*(y),12*(y+1)):
                    if (son in samplers) :
                        if (0==presionado[samplers.index(son)]):
                            libre=samplers.index(son)
        if libre!="null":
            presionado[libre]=1
        else:
            for son in range(12*(int(y_final)-2),12*(int(y_final)+3)):
                if (son in samplers) :
                    if (0==presionado[samplers.index(son)]):
                        libre=samplers.index(son)
            if libre=="null":
                libre=presionado.index(0)
            presionado[libre]=1
    if libre==0:
        sonando[libre]=1
        samplers[libre]=x

        if stream_0.is_active()== True:
            
            stream_0.stop_stream()
            stream_0.close()
        else:
            stream_0.close()
        wf0 = wave.open(wav[x], 'rb')
        stream_0 = p1.open(format=p1.get_format_from_width(wf0.getsampwidth()),
                        channels=wf0.getnchannels(),
                        rate=wf0.getframerate(),
                        output=True,
                        stream_callback=callback_0)
        stream_0.start_stream()
    elif libre==1:
        sonando[libre]=1
        samplers[libre]=x
        if stream_1.is_active():
            stream_1.stop_stream()
            stream_1.close()
        else:
            stream_1.close()
        wf1 = wave.open(wav[x], 'rb')
        stream_1 = p1.open(format=p1.get_format_from_width(wf1.getsampwidth()),
                        channels=wf1.getnchannels(),
                        rate=wf1.getframerate(),
                        output=True,
                        stream_callback=callback_1)
        stream_1.start_stream()
    elif libre==2:
        sonando[libre]=1
        samplers[libre]=x
        if stream_2.is_active():
            stream_2.stop_stream()
            stream_2.close()
        else:
            stream_2.close()
        wf2 = wave.open(wav[x], 'rb')
        stream_2 = p1.open(format=p1.get_format_from_width(wf2.getsampwidth()),
                        channels=wf2.getnchannels(),
                        rate=wf2.getframerate(),
                        output=True,
                        stream_callback=callback_2)
        stream_2.start_stream()
    elif libre==3:
        sonando[libre]=1
        samplers[libre]=x
        if stream_3.is_active():
            stream_3.stop_stream()
            stream_3.close()
        else:
            stream_3.close()
        wf3 = wave.open(wav[x], 'rb')
        stream_3 = p1.open(format=p1.get_format_from_width(wf3.getsampwidth()),
                        channels=wf3.getnchannels(),
                        rate=wf3.getframerate(),
                        output=True,
                        stream_callback=callback_3)
        stream_3.start_stream()
    elif libre==4:
        sonando[libre]=1
        samplers[libre]=x
        if stream_4.is_active():
            stream_4.stop_stream()
            stream_4.close()
        else:
            stream_4.close()
        wf4 = wave.open(wav[x], 'rb')
        stream_4 = p1.open(format=p1.get_format_from_width(wf4.getsampwidth()),
                        channels=wf4.getnchannels(),
                        rate=wf4.getframerate(),
                        output=True,
                        stream_callback=callback_4)
        stream_4.start_stream()
    elif libre==5:
        sonando[libre]=1
        samplers[libre]=x
        if stream_5.is_active():
            stream_5.stop_stream()
            stream_5.close()
        else:
            stream_5.close()
        wf5 = wave.open(wav[x], 'rb')
        stream_5 = p1.open(format=p1.get_format_from_width(wf5.getsampwidth()),
                        channels=wf5.getnchannels(),
                        rate=wf5.getframerate(),
                        output=True,
                        stream_callback=callback_5)
        stream_5.start_stream()
    elif libre==6:
        sonando[libre]=1
        samplers[libre]=x
        if stream_6.is_active():
            stream_6.stop_stream()
            stream_6.close()
        else:
            stream_6.close()
        wf6 = wave.open(wav[x], 'rb')
        stream_6 = p1.open(format=p1.get_format_from_width(wf6.getsampwidth()),
                        channels=wf6.getnchannels(),
                        rate=wf6.getframerate(),
                        output=True,
                        stream_callback=callback_6)
        stream_6.start_stream()
    elif libre==7:
        sonando[libre]=1
        samplers[libre]=x
        if stream_7.is_active():
            stream_7.stop_stream()
            stream_7.close()
        else:
            stream_7.close()
        wf7 = wave.open(wav[x], 'rb')
        stream_7 = p1.open(format=p1.get_format_from_width(wf7.getsampwidth()),
                        channels=wf7.getnchannels(),
                        rate=wf7.getframerate(),
                        output=True,
                        stream_callback=callback_7)
        stream_7.start_stream()
    elif libre==8:
        sonando[libre]=1
        samplers[libre]=x
        if stream_8.is_active():
            stream_8.stop_stream()
            stream_8.close()
        else:
            stream_8.close()
        wf8 = wave.open(wav[x], 'rb')
        stream_8 = p1.open(format=p1.get_format_from_width(wf8.getsampwidth()),
                        channels=wf8.getnchannels(),
                        rate=wf8.getframerate(),
                        output=True,
                        stream_callback=callback_8)
        stream_8.start_stream()
    elif libre==9:
        sonando[libre]=1
        samplers[libre]=x
        if stream_9.is_active():
            stream_9.stop_stream()
            stream_9.close()
        else:
            stream_9.close()
        wf9 = wave.open(wav[x], 'rb')
        stream_9 = p1.open(format=p1.get_format_from_width(wf9.getsampwidth()),
                        channels=wf9.getnchannels(),
                        rate=wf9.getframerate(),
                        output=True,
                        stream_callback=callback_9)
        stream_9.start_stream()
    elif libre==10:
        sonando[libre]=1
        samplers[libre]=x
        if stream_10.is_active():
            stream_10.stop_stream()
            stream_10.close()
        else:
            stream_10.close()
        wf10 = wave.open(wav[x], 'rb')
        stream_10 = p1.open(format=p1.get_format_from_width(wf10.getsampwidth()),
                        channels=wf10.getnchannels(),
                        rate=wf10.getframerate(),
                        output=True,
                        stream_callback=callback_10)
        stream_10.start_stream()
    elif libre==11:
        sonando[libre]=1
        samplers[libre]=x
        if stream_11.is_active():
            stream_11.stop_stream()
            stream_11.close()
        else:
            stream_11.close()
        wf11 = wave.open(wav[x], 'rb')
        stream_11 = p1.open(format=p1.get_format_from_width(wf11.getsampwidth()),
                        channels=wf11.getnchannels(),
                        rate=wf11.getframerate(),
                        output=True,
                        stream_callback=callback_11)
        stream_11.start_stream()
    elif libre==12:
        sonando[libre]=1
        samplers[libre]=x
        if stream_12.is_active():
            stream_12.stop_stream()
            stream_12.close()
        else:
            stream_12.close()
        wf12 = wave.open(wav[x], 'rb')
        stream_12 = p1.open(format=p1.get_format_from_width(wf12.getsampwidth()),
                        channels=wf12.getnchannels(),
                        rate=wf12.getframerate(),
                        output=True,
                        stream_callback=callback_12)
        stream_12.start_stream()
def presion_off(x):
    global samplers
    global wav
    global presionado
    if x in samplers:
        libre = samplers.index(x)
        presionado[libre]=0   
def stop(x):
    global samplers
    global sonando
    global wav
    global presionado
    global stream_0, wf0
    global stream_1, wf1
    global stream_2, wf2
    global stream_3, wf3
    global stream_4, wf4
    global stream_5, wf5
    global stream_6, wf6
    global stream_7, wf7
    global stream_8, wf8
    global stream_9, wf9
    global stream_10, wf10
    global stream_11, wf11
    global stream_12, wf12
    libre = samplers.index(wav[x])
    if libre==0:
        sonando[libre]=0
        samplers[libre]=100
        if stream_0.is_active():
            stream_0.stop_stream()
    elif libre==1:
        sonando[libre]=0
        samplers[libre]=100
        if stream_1.is_active():
            stream_1.stop_stream()
    elif libre==2:
        sonando[libre]=0
        samplers[libre]=100
        if stream_2.is_active():
            stream_2.stop_stream()
    elif libre==3:
        sonando[libre]=0
        samplers[libre]=100
        if stream_3.is_active():
            stream_3.stop_stream()
    elif libre==4:
        sonando[libre]=0
        samplers[libre]=100
        if stream_4.is_active():
            stream_4.stop_stream()
    elif libre==5:
        sonando[libre]=0
        samplers[libre]=100
        if stream_5.is_active():
            stream_5.stop_stream()
    elif libre==6:
        sonando[libre]=0
        samplers[libre]=100
        if stream_6.is_active():
            stream_6.stop_stream()
    elif libre==7:
        sonando[libre]=0
        samplers[libre]=100
        if stream_7.is_active():
            stream_7.stop_stream()
    elif libre==8:
        sonando[libre]=0
        samplers[libre]=100
        if stream_8.is_active():
            stream_8.stop_stream()
    elif libre==9:
        sonando[libre]=0
        samplers[libre]=100
        if stream_9.is_active():
            stream_9.stop_stream()
    elif libre==10:
        sonando[libre]=0
        samplers[libre]=100
        if stream_10.is_active():
            stream_10.stop_stream()
    elif libre==11:
        sonando[libre]=0
        samplers[libre]=100
        if stream_11.is_active():
            stream_11.stop_stream()
    elif libre==12:
        sonando[libre]=0
        samplers[libre]=100
        if stream_12.is_active():
            stream_12.stop_stream()

presionado=[0,0,0,0,0,0,0,0,0,0,0,0,0]
sonando=[0,0,0,0,0,0,0,0,0,0,0,0,0]
samplers=["","","","","","","","","","","","",""]
lee=""
leyendo = ["","","","","","","","",""]
try:
    print("Conectando al puerto /dev/ttyACM0")
    arduino = serial.Serial("/dev/ttyACM0", 9600)
except :
    print("Fallo la coneccion al puerto /dev/ttyACM0")
    arduino = serial.Serial('COM3', 9600)
while reproduciendo:
    leyendo = ["","","","","","","","",""]
    arduino.inWaiting()
    leer = str(arduino.readline())[2:-6].split(',')
    print(leer)
    for x in range(0,6):
        if leer[x] != '':
            leer[x]=int(leer[x])
            leer[x]=("0"*(11-len(bin(leer[x])))+(bin(leer[x])[2:len(bin(leer[x]))]))
            for n in range(0,9):
                leyendo[n]=leyendo[n]+leer[x][n]
    leer=""
    for x in range(0,9):
        leer=leer+leyendo[x]
    leer=leer[0:48]
    print(leer)
    for x in range(0,len(leer)):
        if ("0" in leer[x]) and ("1" in leido[x]) :
            leido[x] = leer[x]
            presion_off(x)
        elif ("0" in leer[x]) and ("0" in leido[x]) :
            leido[x] = leer[x]
        elif("1" in leer[x]) and ("0" in leido[x]):
            if 13 >= sum(sonando) :
                leido[x] = leer[x]
                play(x)
            
arduino.close()
p1.terminate()
#::=()[]''""_+;<>=!\% esto es un commentario
