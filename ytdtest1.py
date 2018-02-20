import pafy
import requests

def playlist_download(url):
    from bs4 import BeautifulSoup as bs
    try:
        r = requests.get(url)
        page = r.text
        soup = bs(page, 'html.parser')
        res = soup.find_all('a', {'class': 'pl-video-title-link'})
        res = ['https://www.youtube.com' + l.get("href") for l in res]
        return res
    except requests.ConnectionError as e:
        print(e)


c = 1

uri = input('Input URL::')
uri = uri[1:-1]
arr = []
if 'playlist' in uri:
    arr = playlist_download(uri)
else:
    arr.append(uri)

for i in arr:
    try:
        video = pafy.new(i)
        name = str(c) + '. ' + video.title
        best = video.getbest(preftype="mp4")
        best.download(quiet=False, filepath='E:\\Tutorials\\College\\Automata Theory\\' + name + '.' + best.extension)
        c += 1

    except:
        pass

