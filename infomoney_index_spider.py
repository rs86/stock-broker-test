from collections import deque
import time
import threading
import requests
from bs4 import BeautifulSoup

def read_urls():
    with open("pages.txt", "r") as f:
        pages = [line.replace("\n", "") for line in f.readlines()]
    return pages

def run(url, output_file, oplock):
    oplock.acquire()
    print url
    oplock.release()
    r = requests.get(url)
    if r.status_code == 200:
        with open(output_file, "w") as f:
            f.write(r.text.encode("utf-8"))

oplock = threading.Lock()

threads = deque([(url, "index-pages/{}.html".format(idx)) \
                    for idx, url \
                    in enumerate(read_urls())])

running_threads = []

while len(threads) > 0:

    print threading.active_count(), \
            len(threads), \
            len(running_threads)

    while threading.active_count() < 20:
        url, output_file = threads.pop()
        t = threading.Thread(target=run, args=(url, output_file, oplock))
        running_threads.append(t)
        t.start()
    time.sleep(0.100)


for t in running_threads:
    t.join()
