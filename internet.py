#! /usr/bin/python

import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import * 
from PyQt4.QtWebKit import * 

app = QApplication(sys.argv)
web = QWebView()
web.load(QUrl("http://en.wikipedia.org/wiki/Main_Page"))
printer = QPrinter()
printer.setPageSize(QPrinter.A4)
printer.setOutputFormat(QPrinter.PdfFormat)
printer.setOutputFileName("News.pdf")

def convertIt():
    web.print_(printer)
    print "Pdf generated"
    QApplication.exit()

QObject.connect(web, SIGNAL("loadFinished(bool)"), convertIt)

sys.exit(app.exec_())
