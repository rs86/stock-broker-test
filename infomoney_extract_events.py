import glob, re

from bs4 import BeautifulSoup

ticker_exp = re.compile("([A-Z]{4}[3,4])")

rows = []

with open("data.txt", "w") as w:
    for page in sorted(glob.glob("recommendations/*.html")):
        with open(page, "r") as r:
            print "Parsing page {}...".format(page)
            raw_html = r.read()
            soup = BeautifulSoup(raw_html)
            timestamp = soup.select("time")[0]["datetime"]
            contents = soup.select("#contentNews")[0].text
            tickers = ticker_exp.findall(contents)
            rows += [(page, timestamp, ticker) for ticker in tickers]

    w.write("file,timestamp,ticker\n")
    for row in rows:
        w.write(",".join(row) + "\n")

