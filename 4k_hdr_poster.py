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
plextvdvlibrary = (server["TVDVLIBRARY"])
ppath = (server["PLEXPATH"])
mpath = (server["MOUNTEDPATH"])
pbak = (server["POSTER_BU"])
plex = PlexServer(baseurl, token)
films = plex.library.section(plexlibrary)
television = plex.library.section(plextvlibrary)
televisiondv = plex.library.section(plextvdvlibrary)
dvfilms = plex.library.section(plexdvlibrary)
banner_4k = Image.open("4K-Template.png")
banner_hdr = Image.open("hdr-poster.png")
banner_4k_hdr = Image.open("4k-hdr-poster.png")
banner_4k_dv = Image.open("4k-dv-poster.png")
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
    i.addLabel("Overlay")
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
    i.addLabel("Overlay")
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
    i.addLabel("Overlay")
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
    i.addLabel("Overlay")
    os.remove('poster.png') 

def poster_4ktvdv():   
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
    background.paste(banner_4k_dv, (0, 0), banner_4k_dv)
    background.save('poster.png')
    i.uploadPoster(filepath="poster.png")
    i.addLabel("Overlay")
    os.remove('poster.png')     
    
for i in films.search(**{"sort": titleSort, "hdr": True, "label!": "Overlay"}):
    poster_4k_hdr()
#for i in films.search(**{"hdr": False, "label!": "Overlay"}):
#    poster_4k()
#for i in dvfilms.search(**{"hdr": True, "label!": "Overlay"}):
#    poster_4k_dv() 
#for i in dvfilms.search(**{"hdr": False, "label!": "Overlay"}):
#    poster_4k_dv()
#for i in television.search(**{"addedAt>>": "label!": "Overlay"}):
#    poster_4ktv()
#for i in televisiondv.search(**{"label!": "Overlay"}):
#    poster_4ktvdv()    
