#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os, sys, csv, shutil
import requests
import re
import argparse
from bs4 import BeautifulSoup
from time import sleep
from PIL import * 
from PIL import Image
from pruebas import object_pruebas

class GoogleSearch():
	def __init__(self,*arg,**kwargs):
		super(GoogleSearch).__init__(*arg,**kwargs)

		self.domain = "https://www.google.com/"
	def __request(self, url,results=[]):
		response = requests.get(url)
		soup = BeautifulSoup(response.text, 'html.parser')
		data = soup.find_all("div", {"class":"kCrYT"})
		if data:
			title= "null"
			link= "null"
			for d in data[3:]:
				d=next((d.split(e) for e in ["/url?q=","/search?ie"] if e in d),[1])
				a = d
				if len(d)>1:
					a = d[1].split(r'&amp;')[0].replace(r'%3Fv%3D',"?v=")
					if "%3Fid" in a:
						a = a.split(r'%3Fid')[0]
					
				link = self.__parse_ulr(a)
				title = d
				if "/search?ie" in link:
					link = self.domain + link
				if d != [1]:
					results.append(link)
		return soup, results

	def __pagination(self, soup, page):
		try:
			link = self.domain + self.__parse_url(soup.find_all( "a",{"class":"fl"} )[page].get("href"))
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
			results.extend(r)
		print("Total de resultados: {}".format(len(results)))
		return results

test=object_pruebas(pwd=os.getcwd())
test.go_pwd(self,pwd='',mkdir=test.info['ignorar']+__file__,reset=0)
buscar ="producto "+input("BUSCAR: ")

os.system("mkdir "+buscar.replace(" ","_"))
buscar1=buscar
url1 =  "https://www.google.com/"+ 'search?q=' + buscar.replace(" ","%20") + '&oq='+buscar.replace(" ","%20")+'amp;&btnG=Buscar&tbm=isch&ie=UTF-8&source=lnms&tbs=isz:l'
buscar=buscar.replace(" ","%20")+r"%20imagen%20producto"
gs = GoogleSearch()
results = gs.request_data(buscar, 5, 5)
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
	urls = [ img.get('src') for img in img_tags]
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
			d=url.split("://")[1]
			d=gs.str_to_key(d,remplazar=[([".jpg"],"finallity"),(["."],"_")])
			d=dominio.replace(".","_")+d.replace("finallity",".jpg")
			shutil.copy("colchom.html",d)
			imagen= open(d,"wb")
			for linea in pesca.iter_content(100000):
				imagen.write(linea)
			imagen.close()
			#print("se guardo "+dominio+d)
			shutil.move(d,buscar1.replace(" ","_"))	
#print(results1)
final=len(results1)
contador=0
import os, shutil, glob, sys 
print(os.listdir())
#shutil.copy("resultadoso.py","resultado.py")
#shutil.move("resultado.py",buscar1.replace(" ","_"))
#shutil.move("codigo.txt",buscar1.replace(" ","_"))
os.chdir(buscar1.replace(" ","_"))
archivos_pesos = []
midir=os.listdir()
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
			Image.open(str(peso)+"_"+archivo+".jpg")
			Image.save(str(peso)+"_"+archivo+".png")
		except IOError:
			print("No se puede convertir la imagen")
	if ".jpg" in str(archivo):
		try:
			Image.open(str(peso)+"_"+archivo)
			Image.save(str(peso)+"_"+archivo.replace(".jpg",".png"))
			os.delete(str(peso)+"_"+archivo)
		except IOError:
			print("No se puede convertir la imagen")

if 'main' in __name__:
    from pruebas import main_pruebas
    pruebas={           
        1:{'titulo':"Nombre del script:",'f':lambda: print(__file__)},
        2:{'titulo':"Nombre del script:",'f':}
        }
    main_pruebas(pruebas,sys.argv)