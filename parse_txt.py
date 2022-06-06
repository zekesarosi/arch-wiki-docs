#!/usr/bin/env python

from urllib.request import urlopen
from bs4 import BeautifulSoup
import os
from glob import glob


path_to_docs = "/usr/share/doc/arch-wiki/html/en/"

doc_list = [y for x in os.walk(path_to_docs) for y in glob(os.path.join(x[0], '*.html'))]

for doc in doc_list:
    n = 0
    file = doc
    html = open(doc)
    soup = BeautifulSoup(html, features="html.parser")

    # kill all script and style elements
    for script in soup(["script", "style"]):
        script.extract()    # rip it out

    # get text
    text = soup.get_text()

    # break into lines and remove leading and trailing space on each
    lines = (line.strip() for line in text.splitlines())
    # break multi-headlines into a line each
    chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
    # drop blank lines
    text = '\n'.join(chunk for chunk in chunks if chunk)
    file = file.split('/')
    file = file[7]
    writable = open(f'/usr/share/doc/arch-wiki/txt/en/{file[:-5]}.txt', mode='w+')
    writable.write(text)
    writable.close()
    n += 1
    print("Processed Files: ", n)

