from collections import deque
import time
import threading
import requests

oplock = threading.Lock()

def read_urls():
    f = open("recommendation-pages.txt","r")
    d = f.read()
    ls = d.split("\n")
    return ls

def fetch(url, output_file, oplock):
    oplock.acquire()
    print url
    oplock.release()
    r = requests.get(url)
    if r.status_code == 200:
        with open(output_file, "w") as f:
            f.write(r.text.encode("utf-8"))

i = 1
pages = filter(lambda x: len(x) > 0, deque(read_urls()))
threads = []
while len(pages) > 0:
    while threading.active_count() < 100:
        page = pages.pop()
        url = "http://infomoney.com.br" + page
        i += 1
        t = threading.Thread(target=fetch, args=(url, "recommendations/{:08}.html".format(i), oplock))
        threads.append(t)
        t.start()
    time.sleep(0.055555)

for t in threads:
    t.join()
