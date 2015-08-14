import glob, re

from bs4 import BeautifulSoup

ticker_exp = re.compile("([A-Z]{4}[3,4])")

with open("data.txt", "w") as w:
    for page in glob.glob("recommendations/*.html"):
        with open(page, "r") as r:
            raw_html = r.read()
            soup = BeautifulSoup(raw_html)
            newsdate = soup.select("time[datetime]")
            if len(newsdate) > 0:
                contents = soup.select('#contentNews')
                tickers = [ticker for ticker in ticker_exp.findall(str(contents))]
                print page, newsdate[0]["datetime"]
                w.write(newsdate[0]["datetime"] + "," + ",".join([str(t) for t in tickers]))
                w.write("\n")
