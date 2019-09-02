import pafy
import requests
import os
import threading
import sys


def update_packages():
    packages = ["pafy","requests","beautifulsoup4","youtube_dl"]
    for package in packages:
        os.system("pip install --upgrade "+package)

ch = input("Check for Package Updates? [Y/N]") 

if ch == 'y' or ch == 'Y':
    update_packages()
c = 1

def playlist_download(url):
    from bs4 import BeautifulSoup as bs
    try:
        r = requests.get(url)
        page = r.text
        soup = bs(page, 'html.parser')
        res = soup.find_all('a', {'class': 'pl-video-title-link'})
        res = ['https://www.youtube.com' + l.get("href") for l in res]
        return res
    except Exception as e:
        print(e)

def download_err(i):
    global path
    try:
        fh1 = open(path + "done.txt","a") 
        fh = open(path +"err.txt", "a")
        video = pafy.new(i[0])
        name = str(i[1]) + '. ' + video.title
        try:
            for p in ('|', '?', '\\', '/', ':', '*', '<', '>', '\"'):
                 name = name.replace(p, '_')

            best = video.getbest(preftype="mp4")
            print("Downloading "+name+"...")
            best.download(quiet=True, filepath= path + name + '.' + best.extension)

            print("Done Downloading "+name)
            fh1.write("Done : " +name+ '\n')
            fh1.close()
            

        except Exception as e:
            print(e +"\\"+ str(i[0])+"\\"+str(i[1])+"\\"+name)
            fh.write('Failed : '+ name +'\n')
            print("Error Downloading "+name)
            fh.close()    
            
    except Exception as f:
        print(f)
        

def download(i):
    global path
    global c
    global threads
    try:
        fh1 = open(path + "done.txt","a") 
        fh = open(path +"err.txt", "a")
        video = pafy.new(i)
        name = str(c) + '. ' + video.title
        c += 1
        try:
            for p in ('|', '?', '\\', '/', ':', '*', '<', '>', '\"'):
                 name = name.replace(p, '_')

            best = video.getbest(preftype="mp4")
            print("Downloading "+name+"...")
            best.download(quiet=False, filepath= path + name + '.' + best.extension)
            print("Done Downloading "+name)
            fh1.write("Done : " +name+ '\n')
            fh1.close()
            

        except Exception as e:
            print(e +"\\"+ str(i[0])+"\\"+str(i[1])+"\\"+name)
            c += 1
            fh.write('Failed : '+ name +'\n')
            print("Error Downloading "+name)
            for _ in range(0,3):
                t=threading.Thread(target=download_err, args=((i,c),))
                threads.append(t)
                t.start()
            #err.append((i,c))
            fh.close()    
            
    except Exception as f:
        print(f)
        c += 1






## Variables and others
c = 1

uri = input('Input URL::')
path = input('Enter Path ::')

path =  path + '\\'

try:
    os.makedirs(path)    
    print("Directory " , path ,  " Created ")
except FileExistsError:
    print("Directory " , path ,  " already exists")

temp = []

if ',' in uri:
    temp = uri.split(',')
else:
    temp.append(uri)

arr = []
for url in temp:
    if 'playlist' in url:
        arr = playlist_download(url)
    else:
        arr.append(url)
        
err = []
## Variables and others

threads = []

for i in arr:
    #t=threading.Thread(target=download, args=(str(i),))
    #threads.append(t)
    #t.start()
    download(i)
    

while len(threads)>0 :
    for i in threads:
        if not i.isAlive():
            threads.remove(i)
else:
    import sort_txt_file as stf
    stf.correct_txt(path)
    sys.exit()
    





        
