#!/usr/bin/python
# gHost HTTP Request Checker by HardGhost
# Tools untuk mengecek http header dan host checker, cocok digunakan untuk mengecek header
# bug operator 
#
# Tools ini membutuhkan: 
# - Python 2.7, Android: qpython (playstore) 
# - module requests
#
# *Panduan Instalasi* #
# 
# Komputer(linux)/termux:
# ketik command : python
#               : pip install python
#               : python gHost.py
#
# Android (non termux)(Rekomendasi):
# - download qpython di playstore
# - buka qpython, pilih qpypi lalu pilih pip dan jalankan
# - ketik command pip install requests lalu kembali ke menu
# - buka editor, buka file gHost.py dan jalankan. 
#
# Note:
#   kalian harus paham kode HTTP status seperti 200,301,400,403 dll. 
#
# Credit: Hardian 'HardGhost' Alkori
# Web: HardGhost Security | http://hardghost-sec.blogspot.com
# Github: http://github.com/hardghost07 


# mengimport module
import requests 
import os
import time

clear = os.system('clear') 
clear

# opening
print ' gHost HTTP Header Requests Checker' 
print 'Bug Report hardghostalkori@gmail.com' 
print '  | hardghost-sec.blogspot.com |\n'

# membuat blok statemen 
def urlcheck() :
# handling exceptions
 try:
     url = raw_input('Url (Ctrl+c Untuk Keluar):')
     rq = requests.get('https://'+url, allow_redirects=False)
 except requests.exceptions.ConnectionError:
     print
     print'Invalid Hostname\n'
     while True:
         urlcheck()
 except requests.exceptions.InvalidURL:
     print
     print 'Invalid URL\n' 
     while True:
         urlcheck()
 except KeyboardInterrupt:
     print 'Bye Bye....' 
# Menampilkan Request 
 print'Request Address: ',rq.url
 print'Encoding:', rq.encoding
 try:
     headers = rq.headers ['Content-Type'] 
 except KeyError:
     print 'Content-Type: -' 
 else:
     print 'Content-Type:', headers
 raw = rq.raw.version
 if raw == 11:
    print 'HTTP Version: HTTP/1.1'
 else:
    print 'HTTP Version: HTTP/1.0'
 stat1 = rq.status_code
 if stat1 == 200:
     print "Status: 200" 
     print "----------------" 
     print
     while True:
         urlcheck()
 else:
     print 'Status:', rq.status_code
 loc = rq.headers['Location']
 print 'Redirect To: ', loc
 print

# menampilkan url yang valid jika status url pertama terjadi redirect url(301,302)
 req2 = requests.get(loc, allow_redirects=True)
 print '---------------------------------------' 
 print 'Valid address:', req2.url
 print 'Status: ', req2.status_code
 print 'Encoding:', rq.encoding
 print '---------------------------------------\n'
urlcheck() 

while True:
    urlcheck() 