from pathlib import Path
from PIL import Image
from plexapi.server import PlexServer
import numpy as np
import requests
import shutil
import os
import re
import stat
from configparser import ConfigParser
import platform


config_object = ConfigParser()
config_object.read("config.ini")
server = config_object["PLEXSERVER"]
baseurl = (server["PLEX_URL"])
token = (server["TOKEN"])
plexlibrary = (server["FILMSLIBRARY"])
plextvlibrary = (server["TVLIBRARY"])
plexdvlibrary = (server["DVLIBRARY"])
plexde4klibrary = (server["DE4KLIBRARY"])
plexdelibrary = (server["DELIBRARY"])
plexdetvlibrary = (server["DETVLIBRARY"])
plexdklibrary = (server["DKLIBRARY"])
plexnllibrary = (server["NLLIBRARY"])
plexbollywood = (server["HILIBRARY"])
plexbollywoodtv = (server["HITVLIBRARY"])
plexasian = (server["ASIANLIBRARY"])
ppath = (server["PLEXPATH"])
mpath = (server["MOUNTEDPATH"])
pbak = (server["POSTER_BU"])
plex = PlexServer(baseurl, token)
films = plex.library.section(plexlibrary)
television = plex.library.section(plextvlibrary)
dvfilms = plex.library.section(plexdvlibrary)
defilms = plex.library.section(plexdelibrary)
dkfilms = plex.library.section(plexdklibrary)
nlfilms = plex.library.section(plexnllibrary)
de4kfilms = plex.library.section(plexdelibrary)
detelevision = plex.library.section(plexdetvlibrary)
bollywood = plex.library.section(plexbollywood)
bollywoodtv = plex.library.section(plexbollywoodtv)
asiantv = plex.library.section(plexasian)
banner_4k = Image.open("4K-Template.png")
banner_hdr = Image.open("hdr-poster.png")
banner_4k_hdr = Image.open("4k-hdr-poster.png")
banner_4k_dv = Image.open("4k-dv-poster.png")
banner_4k_de = Image.open("4k-de-poster.png")
banner_de = Image.open("DE-template.png")
banner_dk = Image.open("dk-poster.png")
banner_nl = Image.open("nl-poster.png")
banner_hi = Image.open("bollywood_poster.png")
banner_asian = Image.open("asian_poster.png")
size = (911,1367)
 

def poster_4k_hdr():
    print(i.title + ' 4k HDR')    
    if platform.system() == 'Windows':
        newdir = os.path.dirname(re.sub(ppath, mpath, i.media[0].parts[0].file))+"\\" 
    else:
        newdir = os.path.dirname(re.sub(ppath, mpath, i.media[0].parts[0].file))+'/'
    backup = os.path.exists(newdir+'poster_bak.png')  
    imgurl = i.posterUrl
    img = requests.get(imgurl, stream=True)
    filename = "poster.png"
    if pbak == True: 
        if backup == True: 
            print('Backup File Exists, Skipping...')    
        else:
            print('Creating a backup file')
            dest = shutil.copyfile(filename, newdir+'poster_bak.png')
            os.chown(newdir+'poster_bak.png', 99, 100)
            os.chmod(newdir+'poster_bak.png', 0o0666)

    if img.status_code == 200:
        img.raw.decode_content = True
        with open(filename, 'wb') as f:
            shutil.copyfileobj(img.raw, f)

    print('creating poster')    
    background = Image.open('poster.png')
    background = background.resize(size,Image.ANTIALIAS)
    background.paste(banner_4k_hdr, (0, 0), banner_4k_hdr)
    background.save('poster.png')
    i.uploadPoster(filepath="poster.png")
    os.remove('poster.png') 
    
def poster_4k_dv():
    print(i.title + ' 4k DV')    
    if platform.system() == 'Windows':
        newdir = os.path.dirname(re.sub(ppath, mpath, i.media[0].parts[0].file))+"\\" 
    else:
        newdir = os.path.dirname(re.sub(ppath, mpath, i.media[0].parts[0].file))+'/'
    backup = os.path.exists(newdir+'poster_bak.png')  
    imgurl = i.posterUrl
    img = requests.get(imgurl, stream=True)
    filename = "poster.png"
    if pbak == True: 
        if backup == True: 
            print('Backup File Exists, Skipping...')    
        else:
            print('Creating a backup file')
            dest = shutil.copyfile(filename, newdir+'poster_bak.png')
            os.chown(newdir+'poster_bak.png', 99, 100)
            os.chmod(newdir+'poster_bak.png', 0o0666)

    if img.status_code == 200:
        img.raw.decode_content = True
        with open(filename, 'wb') as f:
            shutil.copyfileobj(img.raw, f)

    print('creating poster')    
    background = Image.open('poster.png')
    background = background.resize(size,Image.ANTIALIAS)
    background.paste(banner_4k_dv, (0, 0), banner_4k_dv)
    background.save('poster.png')
    i.uploadPoster(filepath="poster.png")
    os.remove('poster.png') 
    
def poster_4k_de():
    print(i.title + ' 4k DE')    
    if platform.system() == 'Windows':
        newdir = os.path.dirname(re.sub(ppath, mpath, i.media[0].parts[0].file))+"\\" 
    else:
        newdir = os.path.dirname(re.sub(ppath, mpath, i.media[0].parts[0].file))+'/'
    backup = os.path.exists(newdir+'poster_bak.png')  
    imgurl = i.posterUrl
    img = requests.get(imgurl, stream=True)
    filename = "poster.png"
    if pbak == True: 
        if backup == True: 
            print('Backup File Exists, Skipping...')    
        else:
            print('Creating a backup file')
            dest = shutil.copyfile(filename, newdir+'poster_bak.png')
            os.chown(newdir+'poster_bak.png', 99, 100)
            os.chmod(newdir+'poster_bak.png', 0o0666)

    if img.status_code == 200:
        img.raw.decode_content = True
        with open(filename, 'wb') as f:
            shutil.copyfileobj(img.raw, f)

    print('creating poster')    
    background = Image.open('poster.png')
    background = background.resize(size,Image.ANTIALIAS)
    background.paste(banner_4k_de, (0, 0), banner_4k_de)
    background.save('poster.png')
    i.uploadPoster(filepath="poster.png")
    os.remove('poster.png') 
           
def poster_4k():   
    print(i.title + " 4K Poster")
    if platform.system() == 'Windows':
        newdir = os.path.dirname(re.sub(ppath, mpath, i.media[0].parts[0].file))+"\\" 
    else:
        newdir = os.path.dirname(re.sub(ppath, mpath, i.media[0].parts[0].file))+'/'
    backup = os.path.exists(newdir+'poster_bak.png')    
    imgurl = i.posterUrl
    img = requests.get(imgurl, stream=True)
    filename = "poster.png"
    if pbak == True: 
        if backup == True: 
            print('Backup File Exists, Skipping...')    
        else:
            print('Creating a backup file')
            dest = shutil.copyfile(filename, newdir+'poster_bak.png')
            os.chown(newdir+'poster_bak.png', 99, 100)
            os.chmod(newdir+'poster_bak.png', 0o0666)

    if img.status_code == 200:
        img.raw.decode_content = True
        with open(filename, 'wb') as f:
            shutil.copyfileobj(img.raw, f)

    print('creating poster')    
    background = Image.open('poster.png')
    background = background.resize(size,Image.ANTIALIAS)
    background.paste(banner_4k, (0, 0), banner_4k)
    background.save('poster.png')
    i.uploadPoster(filepath="poster.png")
    os.remove('poster.png') 

def poster_4ktv():   
    print(i.title + " 4K Poster")
    imgurl = i.posterUrl
    img = requests.get(imgurl, stream=True)
    filename = "poster.png"
    if img.status_code == 200:
        img.raw.decode_content = True
        with open(filename, 'wb') as f:
            shutil.copyfileobj(img.raw, f)

    print('creating poster')    
    background = Image.open('poster.png')
    background = background.resize(size,Image.ANTIALIAS)
    background.paste(banner_4k, (0, 0), banner_4k)
    background.save('poster.png')
    i.uploadPoster(filepath="poster.png")
    os.remove('poster.png') 

           
def poster_hdr():
    print(i.title + " HDR Poster")
    if platform.system() == 'Windows':
        newdir = os.path.dirname(re.sub(ppath, mpath, i.media[0].parts[0].file))+"\\" 
    else:
        newdir = os.path.dirname(re.sub(ppath, mpath, i.media[0].parts[0].file))+'/'
    backup = os.path.exists(newdir+'poster_bak.png')    
    imgurl = i.posterUrl
    img = requests.get(imgurl, stream=True)
    filename = "poster.png"
    if pbak == True: 
        if backup == True: 
            print('Backup File Exists, Skipping...')    
        else:
            print('Creating a backup file')
            dest = shutil.copyfile(filename, newdir+'poster_bak.png')
            os.chown(newdir+'poster_bak.png', 99, 100)
            os.chmod(newdir+'poster_bak.png', 0o0666)

    if img.status_code == 200:
        img.raw.decode_content = True
        with open(filename, 'wb') as f:
            shutil.copyfileobj(img.raw, f)

    print('creating poster')    
    background = Image.open('poster.png')
    background = background.resize(size,Image.ANTIALIAS)
    background.paste(banner_hdr, (0, 0), banner_hdr)
    background.save('poster.png')
    i.uploadPoster(filepath="poster.png")
    os.remove('poster.png') 
    
def poster_de():   
    print(i.title + " DE Poster")
    imgurl = i.posterUrl
    img = requests.get(imgurl, stream=True)
    filename = "poster.png"
    if img.status_code == 200:
        img.raw.decode_content = True
        with open(filename, 'wb') as f:
            shutil.copyfileobj(img.raw, f)

    print('creating poster')    
    background = Image.open('poster.png')
    background = background.resize(size,Image.ANTIALIAS)
    background.paste(banner_de, (0, 0), banner_de)
    background.save('poster.png')
    i.uploadPoster(filepath="poster.png")
    os.remove('poster.png') 
    
def poster_dk():   
    print(i.title + " DE Poster")
    if platform.system() == 'Windows':
        newdir = os.path.dirname(re.sub(ppath, mpath, i.media[0].parts[0].file))+"\\" 
    else:
        newdir = os.path.dirname(re.sub(ppath, mpath, i.media[0].parts[0].file))+'/'
    backup = os.path.exists(newdir+'poster_bak.png')    
    imgurl = i.posterUrl
    img = requests.get(imgurl, stream=True)
    filename = "poster.png"
    if pbak == True: 
        if backup == True: 
            print('Backup File Exists, Skipping...')    
        else:
            print('Creating a backup file')
            dest = shutil.copyfile(filename, newdir+'poster_bak.png')
            os.chown(newdir+'poster_bak.png', 99, 100)
            os.chmod(newdir+'poster_bak.png', 0o0666)

    if img.status_code == 200:
        img.raw.decode_content = True
        with open(filename, 'wb') as f:
            shutil.copyfileobj(img.raw, f)

    print('creating poster')    
    background = Image.open('poster.png')
    background = background.resize(size,Image.ANTIALIAS)
    background.paste(banner_dk, (0, 0), banner_dk)
    background.save('poster.png')
    i.uploadPoster(filepath="poster.png")
    os.remove('poster.png') 
     
def poster_nl():   
    print(i.title + " NL Poster")
    if platform.system() == 'Windows':
        newdir = os.path.dirname(re.sub(ppath, mpath, i.media[0].parts[0].file))+"\\" 
    else:
        newdir = os.path.dirname(re.sub(ppath, mpath, i.media[0].parts[0].file))+'/'
    backup = os.path.exists(newdir+'poster_bak.png')    
    imgurl = i.posterUrl
    img = requests.get(imgurl, stream=True)
    filename = "poster.png"
    if pbak == True: 
        if backup == True: 
            print('Backup File Exists, Skipping...')    
        else:
            print('Creating a backup file')
            dest = shutil.copyfile(filename, newdir+'poster_bak.png')
            os.chown(newdir+'poster_bak.png', 99, 100)
            os.chmod(newdir+'poster_bak.png', 0o0666)

    if img.status_code == 200:
        img.raw.decode_content = True
        with open(filename, 'wb') as f:
            shutil.copyfileobj(img.raw, f)

    print('creating poster')    
    background = Image.open('poster.png')
    background = background.resize(size,Image.ANTIALIAS)
    background.paste(banner_nl, (0, 0), banner_nl)
    background.save('poster.png')
    i.uploadPoster(filepath="poster.png")
    os.remove('poster.png')

for i in films.search(**{"hdr": True, "addedAt>>": "70m"}):
    poster_4k_hdr()
for i in films.search(**{"hdr": False, "addedAt>>": "70m"}):
    poster_4k()

for i in dvfilms.search(**{"hdr": True, "addedAt>>": "70m"}):
    poster_4k_dv() 
for i in dvfilms.search(**{"hdr": False, "addedAt>>": "70m"}):
    poster_4k_dv()
  
for i in television.search(**{"addedAt>>": "70m"}):
    poster_4ktv()
  
for i in de4kfilms.search(**{"hdr": True, "addedAt>>": "70m"}):
    poster_4k_de() 
for i in de4kfilms.search(**{"hdr": False, "addedAt>>": "70m"}):
    poster_4k_de() 
  
  
for i in dkfilms.search(**{"addedAt>>": "70m"}):
    poster_dk()
for i in nlfilms.search(**{"addedAt>>": "70m"}):
    poster_nl()
  
for i in .search(**{"addedAt>>": "70m"}):
    poster_nl()
  
for i in bollywood.search(**{"addedAt>>": "70m"}):
    poster_hi()
for i in bollywoodtv.search(**{"addedAt>>": "70m"}):
    poster_hi()
for i in asiantv.search(**{"addedAt>>": "70m"}):
    poster_asian() 
  
for i in detelevision.search(**{"addedAt>>": "70m"}):
    poster_de()  
  
#all_tv_shows = plex.library.section("TV Shows - 4K").all()
#for i in all_tv_shows:
#    #poster_4ktv()
