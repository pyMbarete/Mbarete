#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from tkinter import*
os.system("pip3 install --upgrade pip")
os.system("pip3 install --upgrade setuptools")
os.system("pip3 install --upgrade wheel")

try:
	import setuptools
	import wheel
except:
	os.system("pip3 install setuptools")
	os.system("pip3 install wheel")
	import setuptools
	import wheel
try:
	from PIL import Image
except:
	os.system("pip3 install Pillow")
	
try:
	from bs4 import BeautifulSoup

except :
	os.system("pip3 install beautifulsoup4-4.8.1-py3-none-any.whl")
	os.system("pip3 install beautifulsoup4-4.8.1.tar.gz")
	from bs4 import BeautifulSoup
try:
	import requests
	import argparse
	import re
except :
	os.system("pip3 install requests")
	os.system("pip3 install argparse")
	import requests, argparse, re
	
"""

os.system("pip3 install beautifulsoup4-4.8.1-py3-none-any.whl")
os.system("pip3 install beautifulsoup4-4.8.1.tar.gz")
os.system("")
os.system("")
os.system("")
os.system("pip3 install setuptools")
os.system("pip3 install wheel")
os.system("pip3 update")
os.system("pip3 upgrade")
os.system("")
os.system("pip3 install requests")
os.system("pip3 install argparse")
"""
import os, sys, csv, shutil
import requests
from requests import *
import re
import argparse
from bs4 import BeautifulSoup
from time import sleep
from PIL import * 
from tkinter import Tk
from PIL import Image
class GoogleSearch:
	global results1,results,buscar1
	results1 =results = []
	def __init__(self):
		self.domain = "https://www.google.com/"
		

	def __request(self, url):
		global buscar1
		global results1
		response = requests.get(url)
		#print(response,"response")
		soup = BeautifulSoup(response.text, 'html.parser')
		data = soup.find_all("div", {"class":"kCrYT"})
		#final=len(data)
		#contador=3
		#while final>contador:
		#	linkear=str(data[contador]).split("/url?q=")
		#	puente = linkear[1].split(r'&amp;')
		#	data[contador] = puente[0].replace(r'"',"")
		#	print(data[contador])
		#	contador=1+contador
		#print(data,"data")
		#data = soup.find_all("div", {"class":"ZINbbc xpd O9g5cc uUPGi"})
		#print(data,"data")
		#print(len(data))
		if data:
			final=len(data)
			contador=3
			title= "null"
			link= "null"
			while final>contador:
				d= [1]
				if "/url?q=" in str(data[contador]):
					d = linkear=str(data[contador]).split("/url?q=")
				elif "/search?ie" in str(data[contador]):
					d = linkear=str(data[contador]).split("/search?ie")
				a = d
				if len(d)>1:
					a = d[1].split(r'&amp;')
					a = a[0].replace(r'%3Fv%3D',"?v=")
					if "%3Fid" in a:	
						a = a.split(r'%3Fid')
						a = a[0]
					#print(a[0].replace(r'%3Fv%3D',"?v="),contador)

				link = self.__parse_ulr(a)
				title = d
				if "/search?ie" in link:
					link = self.domain + link
				if d != [1]:
					results1.append(link)
				contador=1+contador
			results.append([title,link])
			
			
			#print({title:link})
		return soup, results

	def __pagination(self, soup, page):
		try:
			link = self.domain + self.__parse_url(soup.find_all("a",{"class":"fl"})[page].get("href"))
			#print(link)
		except:
			link = None
		return link

	def __parse_ulr(self, url):
		
		try:
			return url.replace("/url?q=","").split("&sa=")[0]
		except:
			return url
	def request_data(self, search, pages, pause):
		print("Buscando...")
		print("Maxima paginacion: {}".format(pages))
		url = self.domain + 'search?q=' + search + '&oq='+search 
		soup, results = self.__request(url)
		total_results = soup.find(id="resultStats")
		total_results = soup.getText()
		"""print("Resultados encontrados en google: {}".format(total_results))"""
		#print(soup)
		doc= open("resultadosindex.html","w")
		doc.write(str(soup))
		doc.close()
		for i in range(1, pages):
			sleep(pause)
			url = self.__pagination(soup, i)
			if url is None:
				print(pages)
				break
			s, r = self.__request(url)
			results.extend(s,r)
		print("Total de resultados: {}".format(len(results)))
		return results
global results1, buscar1
buscar ="producto "
buscare= open("buscar.txt","r")
for linea in buscare:
        buscar = buscar+linea.strip()
buscare.close()
buscare=os.listdir()
for linea in buscare:
    if buscar.replace(" ","_")==linea:
    	os.chdir(buscar.replace(" ","_"))
    	archivos=os.listdir()
    	for archivo1 in archivos:
    		os.remove(archivo1)
    	os.chdir("..")
    	os.rmdir(buscar.replace(" ","_"))

os.system("mkdir "+buscar.replace(" ","_"))
buscar1=buscar
url1 =  "https://www.google.com/"+ 'search?q=' + buscar.replace(" ","%20") + '&oq='+buscar.replace(" ","%20")+'amp;&btnG=Buscar&tbm=isch&ie=UTF-8&source=lnms&tbs=isz:l'
buscar=buscar.replace(" ","%20")+r"%20imagen%20producto"
gs = GoogleSearch()
results = gs.request_data(buscar, 5, 5)
#print(results1)
#print(url1)
if "://" in str(url1) :
	linkear=str(url1).split("://")
	d = linkear[1].split("/")
	dominio=str(d[0].upper())
	#print(url1)
	try:
		resp = requests.get(url1)
		soup = BeautifulSoup(resp.text, 'html.parser')
		img_tags = soup.find_all('img')	
	except:
		print("error al conectar con el sitio "+dominio)
		img_tags = []
	
	#if ".aspx" in str(results1[contador]) :
	#print(soup)
	#print(img_tags)
	urls = [ img.get('src') for img in img_tags]
	#print(urls)
	for url in urls:
			
			# if "?" in str(url) :
			# 	d=url.split("?")
			# 	url=d[0]
			
		if 'http' in str(url) and ('facebook' not in str(url)):
	            # sometimes an image source can be relative 
	            # if it is provide the base url which also happens 
	            # to be the site variable atm.
			url=url.replace("\/","/") 
			try:
				pesca = requests.get(url)
			except:
				print("error al conectar con el archivo") 
				break
			url=url.replace("/","/")
			d=url.split("://")
			d=d[1].replace("/","_")
			d=d.replace(".jpg","finallity")
			d=d.replace(".","_")
			d=d.replace("finallity",".jpg")
			d=d.replace("finallity",".jpg")
			d=d.replace("(","_")
			d=d.replace(")","_")
			d=d.replace("?","_")
			d=d.replace("&","_")
			d=d.replace(" ","_")
			d=d.replace("=","_")
			d=d.replace("*","_")
			d=d.replace("+","_")
			d=d.replace("-","_")
			d=d.replace("!","_")
			d=d.replace(",","_")
			d=d.replace(":","_")
			d=d.replace(" ","_")
			dominio=dominio.replace(".","_")
			shutil.copy("colchom.html",dominio+d)
			imagen= open(dominio+d,"wb")
			for linea in pesca.iter_content(100000):
				imagen.write(linea)
			imagen.close()
			#print("se guardo "+dominio+d)
			shutil.move(dominio+d,buscar1.replace(" ","_"))	
#print(results1)
final=len(results1)
contador=0
doc= open("colchom.html","w")
doc.write("este documento es de solo para colchon de las imagenes q seran descargadas")
doc.close()											
"""esta parte del codigo descarga las imagenes de los sitios que muestran en el resultado de la busqueda
while final>contador:
	print(results1[contador])
	if "://" in str(results1[contador]) :
		linkear=str(results1[contador]).split("://")
		d = linkear[1].split("/")
		dominio=str(d[0].upper())
		print(dominio)
		site=results1[contador]
		try:
			resp = requests.get(results1[contador])
		except:
			print("error al conectar con sitio "+dominio) 
			break
		soup = BeautifulSoup(resp.text, 'html.parser')
		#if ".aspx" in str(results1[contador]) :
		#	print(soup)
		img_tags = soup.find_all('img')
		
		urls = [ img.get('src') for img in img_tags]
		
		for url in urls:
			
			if "?" in str(url) :
				d=url.split("?")
				url=d[0]
			
			if (('http' in str(url)) and (('.jpg' in str(url)) or ('.png' in str(url)))) and ('tarjetas' not in str(url)) and ( 'facebook' not in str(url)) and ( 'youtube' not in str(url)) and ( 'logo' not in str(url)) and ( 'mejorpatineteelectrico' not in str(url)) and ( 'FACEBOOK' not in str(dominio)):
		            # sometimes an image source can be relative 
		            # if it is provide the base url which also happens 
		            # to be the site variable atm.
				url=url.replace("\/","/") 
				try:
					pesca = requests.get(url)
				except:
					print("error al conectar con el archivo")
					break 
				
				
				url=url.replace("/","/")
				d=url.split("://")

				d=d[1].replace("/","_")
				d=d.replace(".jpg","finallityjpg")
				d=d.replace(".png","finallitypng")
				d=d.replace(".","_")
				d=d.replace("finallityjpg",".jpg")
				d=d.replace("finallitypng",".png")
				d=d.replace("(","_")
				d=d.replace(")","_")
				d=d.replace("?","_")
				d=d.replace("&","_")
				d=d.replace(" ","_")
				d=d.replace("=","_")
				d=d.replace("*","_")
				d=d.replace("*","_")
				d=d.replace("+","_")
				d=d.replace("-","_")
				d=d.replace("!","_")
				d=d.replace(",","_")
				d=d.replace(":","_")
				dominio=dominio.replace(".","_")
				os.system("cp colchom.html "+dominio+d)
				imagen= open(dominio+d,"wb")
				for linea in pesca.iter_content(100000):
					imagen.write(linea)
				imagen.close()
				print("se guardo "+dominio+d)
				os.system("mv "+dominio+d+" "+buscar1.replace(" ","_"))

	contador=contador+1 
"""
import os, shutil, glob, sys 
#os.system("ls")
shutil.copy("resultadoso.py","resultado.py")
shutil.move("resultado.py",buscar1.replace(" ","_"))
shutil.move("codigo.txt",buscar1.replace(" ","_"))
os.chdir(buscar1.replace(" ","_"))
archivos_pesos = []
midir=os.listdir()
#os.system("ls")
for archivo in midir:
	if ("resultado.py" not in archivo) and ("codigo.txt" not in archivo):
		peso=os.path.getsize(str(archivo))
		#print(archivo,"pesa", peso)
		previa=(10-len(str(peso)))*"0"
		peso=previa+str(peso)
		archivos_pesos.append([archivo, peso])
		os.rename(archivo,str(peso)+"_"+archivo)
	if "GOOGLE" in str(archivo):
		os.rename(str(peso)+"_"+archivo,str(peso)+"_"+archivo+".jpg")
		try:
			Image.open(str(peso)+"_"+archivo+".jpg").resize((200,200)).save(str(peso)+"_"+archivo+".png")
		except IOError:
			print("No se puede convertir la imagen")
	if ".jpg" in str(archivo):
		try:
			Image.open(str(peso)+"_"+archivo).resize((200,200)).save(str(peso)+"_"+archivo.replace(".jpg",".png"))
			os.delete(str(peso)+"_"+archivo)
		except IOError:
			print("No se puede convertir la imagen")

#os.system("ls")
midir=os.listdir()
final=len(midir)

contador=0
fila=0
columna=0
largo=int(final/5)+1
doc= open("resultado.py","a")
doc.write(" "+'\n')
doc.write("largo="+str(int(largo*200))+'\n')
while final>contador:
    if ("codigo.txt" not in midir[contador]) and ("resultado.py" not in midir[contador]) and (".jpg" not in midir[contador]) and (".gif" not in midir[contador]):
        peso=midir[contador].split("_")
        doc.write("try:"+'\n')
        doc.write("    img"+str(contador)+" = Image.open("+r'"'+str(midir[contador])+r'"'+").resize((100,100)).save('imagen"+str(contador)+".png','png')"+'\n')
        doc.write("    img"+str(contador)+" =  PhotoImage(file="+r'"imagen'+str(contador)+r'.png"'+")"+'\n')
        doc.write("    botonNuevo"+str(contador)+" = Button(root, image=img"+str(contador)+", text="+r'"'+str(peso[0])+r'"'+", compound="+r'"'+"top"+r'"'+",bd=0 ,command=lambda:seleccion("+r'"'+str(midir[contador])+r'") )'+'\n')
        doc.write("    botonNuevo"+str(contador)+".place(x="+str(columna*120)+", y="+str(fila*130)+")"+'\n')
        doc.write("except:"+'\n')
        doc.write("    botonNuevo"+str(contador)+" = Button(root, text="+r'"'+"imagen dañada"+r'"'+")"+'\n')
        doc.write("    botonNuevo"+str(contador)+".place(x="+str(columna*120)+", y="+str(fila*130)+")"+'\n')
    if columna==8:
        fila=fila+1
        columna=-1
    columna=columna+1
    if ".jpg" in str(midir[contador]):
        try:
            os.remove(str(midir[contador]))
        except IOError:
            print("No se puede eliminar la imagen")
    contador=contador+1
doc.write("largo="+str(int((fila*200)+200))+'\n')
doc.write("root.configure(width = 1200, height=largo)"+'\n')
doc.write("miFrameinicio.geometry("+r'"'+"1200x600"+r'"'+")"+'\n')
doc.write("c.config(scrollregion=c.bbox("+r'"'+"all"+r'"'+"))"+'\n')
doc.write("miFrameinicio.title("+r'"'+str(buscar1)+r'"'+")"+'\n')
doc.write("root.update()"+'\n')
doc.write("root.mainloop()"+'\n')
doc.close()	 
os.system("python3 resultado.py")
#import resultado
