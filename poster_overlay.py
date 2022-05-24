#!/usr/local/bin/python3
from pathlib import Path
from PIL import Image, ImageChops
from plexapi.server import PlexServer
import numpy as np
import requests
import shutil
import os
import re
import stat
from configparser import ConfigParser
import platform
from colorama import Fore, Back, Style
from requests.api import get
from requests.models import REDIRECT_STATI
from datetime import datetime

# Do not edit these, use the config file to make any changes

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
pbak = str.lower((server["POSTER_BU"]))
plex = PlexServer(baseurl, token)
films = plex.library.section(plexlibrary)
television = plex.library.section(plextvlibrary)
televisiondv = plex.library.section(plextvdvlibrary)
dvfilms = plex.library.section(plexdvlibrary)
banner_4k = Image.open("4K-Template.png")
banner_4k_hdr = Image.open("4k-hdr-poster.png")
banner_4k_dv = Image.open("4k-dv-poster.png")
size = (911,1367)

now = datetime.now()
current_time = now.strftime("%H:%M:%S")
print(current_time, ": 4k HDR poster script starting now.")          

def add_banner4k():
    background = Image.open('poster.png')
    background = background.resize(size,Image.Resampling.LANCZOS)
    background.paste(banner_4k, (0, 0), banner_4k)
    background.save('poster.png')
    i.uploadPoster(filepath="poster.png")

def add_banner_4k_hdr():
    background = Image.open('poster.png')
    background = background.resize(size,Image.Resampling.LANCZOS)
    background.paste(banner_4k_hdr, (0, 0), banner_4k_hdr)
    background.save('poster.png')
    i.uploadPoster(filepath="poster.png")
    
def add_banner_4k_dv():
    background = Image.open('poster.png')
    background = background.resize(size,Image.Resampling.LANCZOS)
    background.paste(banner_4k_dv, (0, 0), banner_4k_dv)
    background.save('poster.png')
    i.uploadPoster(filepath="poster.png")    

def get_poster():
    newdir = os.path.dirname(re.sub(ppath, mpath, i.media[0].parts[0].file))+'/'
    backup = os.path.exists(newdir+'poster_bak.png')
    imgurl = i.posterUrl
    img = requests.get(imgurl, stream=True)
    filename = "poster.png"

    if img.status_code == 200:
        img.raw.decode_content = True
        with open(filename, 'wb') as f:
            shutil.copyfileobj(img.raw, f)
        if pbak == 'true': 
            if backup == True: 
                print('Backup File Exists, Skipping...')
            else:        
                print('Creating a backup file')
                dest = shutil.copyfile(filename, newdir+'poster_bak.png')
    else:
        print(Fore.RED+films.title+"cannot find the poster for this film")
        print(Fore.RESET)

def poster_4k_dv():
    print(i.title + ' 4k DV')     
    get_poster()
    add_banner_4k_dv()
    i.addLabel("Overlay")    
    os.remove('poster.png') 

def poster_4k_hdr():
    print(i.title + ' 4k HDR')     
    get_poster()
    add_banner_4k_hdr()    
    i.addLabel("Overlay")     
    os.remove('poster.png')              

def poster_4k():   
    print(i.title + " 4K Poster")
    get_poster()
    add_banner4k()        
    i.addLabel("Overlay")     
    os.remove('poster.png')   

for i in televisiondv.search(**{"label!": "Overlay"}):
    try:
        poster_4k_dv()
    except FileNotFoundError:
        print(Fore.RED+films.title+" Error, the 4k HDR poster for this film could not be created.")
        print(Fore.RESET)
        continue         
#for i in films.search(**{"hdr": True, "label!": "Overlay"}):
    try:
        poster_4k_hdr()
    except FileNotFoundError:
        print(Fore.RED+films.title+" Error, the 4k HDR poster for this film could not be created.")
        print(Fore.RESET)
        continue            
#for i in films.search(**{"hdr": False, "label!": "Overlay"}):
    try:
        poster_4k()
    except FileNotFoundError:
        print(Fore.RED+films.title+" Error, the 4k poster for this film could not be created.")
        print(Fore.RESET)
        continue    