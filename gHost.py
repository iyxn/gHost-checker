#!/usr/bin/python
# gHost HTTP Request Checker by HardGhost
# Tools untuk mengecek http header dan host checker, cocok digunakan untuk mengecek header
# bug operator secara massal.
#
# Tools ini membutuhkan: 
# - module requests
#
# *Panduan Instalasi* 
# 
# Komputer(linux)/termux:
# ketik command : python2
#               : pip2 install requests
#               : python2 gHost.py
#
# Note:
#   kalian harus paham kode HTTP status seperti 200,300,400,400,500 dll. 
#
# Credit: Hardian 'HardGhost' Alkori
# Web: HardGhost Security | http://hardghost-sec.blogspot.com
# Github: http://github.com/hardghost07 


# mengimport module
from datetime import datetime
import requests 
import os
import time
import sys
import fileinput

clear = os.system('clear') 
clear

# opening
print ' gHost HTTP Header Requests Checker' 
print 'Bug Report hardghostalkori@gmail.com' 
print ' |        ScarletDev Studio        |\n' 
print 'Web: hardghost-sec.blogspot.com |'
print 'Git: http://github.com/hardghost07'
print
print 'Note: Belum Support SSL, Tapi Coba Aja.\n'

try:
   filename = raw_input("Path File Bug Host(txt): ")
   if os.path.exists(filename) == False:
             print "File Not Found!" 
             exit()
   print
   print 'Contoh Proxy:' 
   print '-squid.jagoanssh.com:80'
   print '-proxy.configinternet.host:80\n'
   print "Enter/Lewati Untuk Mode Direct"
   proxy_http = raw_input("HTTP Proxy Host:Port : ")
   proxydict = {
   	             "http" : proxy_http
   	            }          
   output = raw_input('Simpan File Hasil Dengan Nama? (*.txt): ')
   print

except KeyboardInterrupt:
    print "Aborted"

os.system('clear')
wk = str(datetime.now())
print 'Checker Started At'
print wk
print

def exe():
 with open(filename) as fp: 
    for line in fp:        
        line = line.rstrip()
        try:
            if proxy_http == '':
                print 'Host:', line,'- Direct'
            else:
                print 'Host:', line,'-',proxy_http
            r = requests.get("http://"+line,proxies = proxydict,allow_redirects=True,timeout = 5)              
        except requests.exceptions.ReadTimeout:           
            if proxy_http == '':
                print 'Status: timeout'
                print
            else:
                print "Status: Invalid Proxy or Proxy Timeout\n"
        except requests.exceptions.TooManyRedirects:
            print "Status: 302 Found"
            print
        except requests.exceptions.InvalidURL:
            print "Invalid URL"
            print
        except requests.exceptions.ConnectTimeout:
            if proxy_http == '':
                print 'Status: timeout'
                print
            else:
                print "Status: Invalid Proxy or Proxy Timeout\n"
                print
            print
        except requests.exceptions.ConnectionError:
            if proxy_http == '':
                print 'Status: timeout'
                print
            else:
                print "Status: Invalid Proxy or Proxy Timeout\n"
                print
            print
        except requests.exceptions.ProxyError:
            print 'Status: timeout'
            print
        else:
            print "Status: ",r.status_code            
            stat = r.status_code            	                    	                 	
            if stat > 199:
                f = open(output,"a")
                if proxy_http == '':
                 f.write(str(line+' : '))
                else:
                 f.write(str(line+'-'+proxy_http+' : '))
                f.write('%s'%(stat)+'\n')
            try:  
             con = r.headers['Connection']
            except KeyError:
             print "Connection:-\n"
            else:
             print "Connection: ",con
             print           
exe()

print '-- DONE --'
print 'Checker Stopped At'
print wk,'\n'

if os.path.exists(output) == True:
    with open(output) as out:
        hitung_baris = 0
        for line in out:
            hitung_baris += 1
        print '[!] DITEMUKAN', hitung_baris, 'HOST HIDUP [!] '
        print 'Host Hidup Disimpan Dengan Nama', output, '\n'
else:
    print '[!] Maaf, Host Hidup Tidak Ditemukan gHost Checker [!]\n'