#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: set fileencoding=utf8 :
'''

'''

import urllib2
import bs4


class Client(object):


	def __init__(self):
		super(Client, self).__init__()

	def get_web_page(self, url):
		"""
		Retrieves an HTML URL returns, HTML
		"""
		f = urllib2.urlopen(url)
		html = f.read()
		f.close()
		return html

	def parse_web_page(self, html):
		"""
		Parses an html page searching for the agenda
		"""
		soup = bs4.BeautifulSoup(html,"lxml")
		novetats = soup.find("h2")
		novetats_llista = novetats.text.strip()
		return novetats_llista

	def print_data(self, data):
		"""
		Prints data retrieved
		"""
		print data

	def run(self):
		html = self.get_web_page("https://www.packtpub.com/packt/offers/free-learning/")
		novetats = self.parse_web_page(html)
		self.print_data(novetats)


if __name__ == "__main__":
	client = Client()
	client.run() 

