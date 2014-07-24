import sys, random, time
import urllib2
import smtplib, os
from email.MIMEMultipart import MIMEMultipart
from email.MIMEBase import MIMEBase
from email.MIMEText import MIMEText
from email.MIMEImage import MIMEImage
from email.Utils import COMMASPACE, formatdate
from email import Encoders
from bs4 import BeautifulSoup

def textExtraction():
	website = urllib2.urlopen("Insert website here")
	websiteHtml = website.read()
	website.close()

	soup = BeautifulSoup(websiteHtml)
	for script in soup(["script", "style"]):
        	script.extract()
	text = soup.get_text()
	textFile = open ("ExtractedText.txt", "w+")
	textFile.write(text.encode('utf8'))
	textFile.close()

def Email():
	gmail_user = "user@gmail.com"
        gmail_pwd = "user_password"
        FROM = 'user@gmail.com'
        TO = ['recepient@email provider.com'] #must be a list
        SUBJECT = "Insert subject here"
        TEXT = "insert message here"
        
	# Preparing for the actual message
        message = """\From: %s\nTo: %s\nSubject: %s\n\n%s
        """ % (FROM, ", ".join(TO), SUBJECT, TEXT)
        try:
        	#server = smtplib.SMTP(SERVER) 
                server = smtplib.SMTP("smtp.gmail.com", 587) #port 465 is also another option
                server.ehlo()
                server.starttls()
                server.login(gmail_user, gmail_pwd)
                server.sendmail(FROM, TO, message)
                #server.quit()
                server.close()
                print 'successfully sent the mail'
	except:
                print "failed to send mail"

def LinkFinder():
	links = [] #Creates a list of links 
	website = urllib2.urlopen("Insert website address here")
	websiteHtml = website.read()
	website.close()
	soup = BeautifulSoup(websiteHtml)	
	AllLinks = soup.find_all("a")
	for link in soup.find_all('a'):
        	links.append(link.get('href'))

	return links #Returns the links associated with a website
