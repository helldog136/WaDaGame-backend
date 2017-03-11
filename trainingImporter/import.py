from bs4 import BeautifulSoup
import requests
import re
import urllib2
import os
import cookielib
import json

def get_soup(url,header):
    return BeautifulSoup(urllib2.urlopen(urllib2.Request(url,headers=header)),'html.parser')

query_file = open("query_file.txt","r")

for query in query_file:
    image_type="ActiOn"
    query= query.split()
    query='+'.join(query)
    url="https://www.google.co.in/search?q="+query+"+gameplay"+"&source=lnms&tbm=isch"
    print url
    #add the directory for your image here
    header={'User-Agent':"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.134 Safari/537.36"
    }
    soup = get_soup(url,header)


    ActualImages=[]# contains the link for Large original images, type of  image
    for a in soup.find_all("div",{"class":"rg_meta"}):
        link , Type =json.loads(a.text)["ou"]  ,json.loads(a.text)["ity"]
        ActualImages.append((link,Type))

    print  "there are total" , len(ActualImages),"images"

    DIR = "training"

    if not os.path.exists(DIR):
                os.mkdir(DIR)
    DIR = os.path.join(DIR, query.replace("+","_"))

    if not os.path.exists(DIR):
                os.mkdir(DIR)
    ###print images
    cntr = 0
    for i , (img , Type) in enumerate( ActualImages):
        try:
            req = urllib2.Request(img, headers={'User-Agent' : header})
            raw_img = urllib2.urlopen(req).read()
            print cntr
            if len(Type)==0:
                f = open(os.path.join(DIR , query.replace("+","_") + "_"+ str(cntr)+".jpg"), 'wb')
            else :
                f = open(os.path.join(DIR , query.replace("+","_") + "_"+ str(cntr)+"."+Type), 'wb')
            f.write(raw_img)
            f.close()
            cntr += 1
        except Exception as e:
            print "could not load : "+img
            print e
