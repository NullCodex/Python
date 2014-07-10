#! /usr/bin/jameson

import sys, random, time
import urllib2
import smtplib, os
from email.MIMEMultipart import MIMEMultipart
from email.MIMEBase import MIMEBase
from email.MIMEText import MIMEText
from email.Utils import COMMASPACE, formatdate
from email import Encoders
from bs4 import BeautifulSoup

#unicodeData.endcode('ascii', 'ignore')
links = []

wikiFile = urllib2.urlopen("http://en.wikipedia.org/wiki/Zeus")
wikiHtml = wikiFile.read()
wikiFile.close()

soup = BeautifulSoup(wikiHtml)
for script in soup(["script", "style"]):
	script.extract()
text = soup.get_text()
#lines = (line.strip() for line in text.splitlines())
#chunks = (phrase.strip() for line in lines for phrase in line.split(" "))
#text = '\n'.join(chunk for chunk in chunks if chunk)
#text.encode('ascii', 'ignore')
fo = open ("foo.txt", "w+")
fo.write(text.encode('utf8'))
fo.close()
#wikiAll = soup.find_all("a")
#for link in soup.find_all('a'):
	#links.append(link.get('href'))

#for x in range (len(links)):
	#print links[x]
def Email():
	fromAddress = 'yu1256365@hotmail.com'
	toAddress = 'jamesonyu95@gmail.com'
	msg = MIMEMultipart()
	msg.attach(MIMEText(foo.txt))
	server = smtplib.SMTP('smtp.gmail.com:587')
	server.ehlo()
	server.starttls()
	server.login("jamesonyu95@gmail.com", "#Netprohfx1%")
	server.sendmail(fromAddress, toAddress, msg.as_string())
	server.close()
