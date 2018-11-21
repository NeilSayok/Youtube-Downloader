import pafy
import requests
import os



def playlist_download(url):
    from bs4 import BeautifulSoup as bs
    try:
        r = requests.get(url)
        print("Here")
        page = r.text
        soup = bs(page, 'html.parser')
        res = soup.find_all('a', {'class': 'pl-video-title-link'})
        res = ['https://www.youtube.com' + l.get("href") for l in res]
        return res
    except Exception as e:
        print(e)


c = 1

uri = input('Input URL::')
path = input('Enter Path ::')
path =  path + '\\'

try:
    os.makedirs(path)    
    print("Directory " , path ,  " Created ")
except FileExistsError:
    print("Directory " , path ,  " already exists")  


arr = []
if 'playlist' in uri:
    arr = playlist_download(uri)
else:
    arr.append(uri)

err = []

for i in arr:
    try:
        fh1 = open(path + "done.txt","a") 
        fh = open(path +"err.txt", "a")
        video = pafy.new(i)
        name = str(c) + '. ' + video.title
        try:
            for p in ('|', '?', '\\', '/', ':', '*', '<', '>', '\"'):
                 name = name.replace(p, '_')

            best = video.getbest(preftype="mp4")
            print("Downloading "+name+"...")
            best.download(quiet=True, filepath= path + name + '.' + best.extension)
            print("Done Downloading "+name)
            fh1.write("Done : " +name+ '\n')
            fh1.close()
            c += 1

        except Exception as e:
            print(e)
            err.append((i,c))
            fh.write('Failed : '+ name +'\n')
            print("Error Downloading "+name)
            fh.close()    
            c += 1
    except Exception as f:
        print(f)


fh1 = open(path + "done.txt","a") 
fh = open(path +"err.txt", "a")

fh.write('=======================================================================================')
fh1.write('=======================================================================================')
fh.close()
fh1.close()

for _ in range(0,3):
    if len(err) == 0:
        break
    else:
        for i in err:
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
                    err.remove(i)
                    fh1.write("Done : " +name+ '\n')
                    fh1.close()
                    c += 1

                except Exception as e:
                    print(e)
                    fh.write('Failed : '+ name +'\n')
                    print("Error Downloading "+name)
                    fh.close()    
                    c += 1
            except Exception as f:
                print(f)
else:
    for k in err:
        print(k + " "+pafy.new(k[0]).title)

        
