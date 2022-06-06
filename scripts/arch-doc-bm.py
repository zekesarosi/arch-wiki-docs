#!/usr/bin/env python3

from multiprocessing import Process, Manager
import webbrowser
import dmenu
import os
from glob import glob
import re
import collections
from rank_bm25 import BM25Okapi


def search(query, doc_list):
	docs = doc_list
	tokenized_corpus = list()
	corpus = list()
	for doc in docs:
		file = open(doc)
		contents = file.read()
		file.close()
		corpus.append(contents)
		tokenized_corpus.append(contents.split(" "))
	bm25 = BM25Okapi(tokenized_corpus)
	tokenized_query = query.split(" ")
	searched_docs = list()
	for top in bm25.get_top_n(tokenized_query, corpus, n=10):
		searched_docs.append(doc_list[corpus.index(top)])
	return searched_docs

		

def main():
	path_to_docs = '/usr/share/doc/arch-wiki/html/en/'
	working_directory = os.getcwd()
	os.chdir(path_to_docs)
	
	running = True
	doc_list = [y for x in os.walk(path_to_docs) for y in glob(os.path.join(x[0], '*.html'))]

	while running:
		wiki_pages = list()
		for file in doc_list:
			file = file.split('/')
			file = file[7]
			wiki_pages.append(file[:-5])	
			
		selection = dmenu.show(wiki_pages, font='-35', case_insensitive=True)


		if selection not in wiki_pages:
			doc_list = search(selection, doc_list)
			

		else:
			url_to_doc = path_to_docs + selection + ".html"
			webbrowser.open(url_to_doc)
			running = False

if __name__ == "__main__":
	main()