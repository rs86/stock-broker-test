import sys
import glob
from bs4 import BeautifulSoup

with open("recommendation-pages.txt", "w") as w:
    ls = []
    for page in glob.glob("index-pages/*.html"):
        print page
        with open(page, "r") as f:
            html = f.read()
            soup = BeautifulSoup(html)
            for a in soup.select("a[href*=onde-investir/acoes/]"):
                ls.append(a["href"])
    ls = set(ls)
    for l in ls:
        w.write(l+"\n")
