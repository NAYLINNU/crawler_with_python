#!/usr/bin/env python

import requests

def request(url):
	try:
		return requests.get("http://" + url)
		
	except requests.exceptions.ConnectionError:
		pass

target_url = "192.168.220.6/mutillidae/"

with open("/home/anonymous/Downloads/subdomains-wordlist.list", "r") as wordlist_file:
	for line in wordlist_file:
		word = line.strip()
		test_url = target_url + "/" + word
		response = request(test_url)
		if response:
			print("[+] Discovered URl -->" + test_url)