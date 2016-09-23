from bs4 import BeautifulSoup
import re
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pandas as pd
from sys import argv
import json

def login():

    driver = webdriver.PhantomJS(executable_path='/usr/local/bin/phantomjs')
    
    driver.get('http://www.allaboutoutdoor.com/login.php')
    
    username = driver.find_element_by_id('email')
    password = driver.find_element_by_id('password')
    
    username.send_keys("lovishcool1@gmail.com")
    password.send_keys("abc98765")
    driver.find_element_by_id('formID').find_element_by_name("submit").click()
    return driver
    
    
if __name__=="__main__":
    
    column = ['media_id','lat','long']

    driver = login()    
    print "logged in"
    
    inp = pd.read_csv(argv[1])
    min_id = int(argv[2])
    max_id = int(argv[3])
    
    fp = open('lat_long.csv','a')
    
    for idx in xrange(min_id,max_id+1):
        result = pd.DataFrame(columns=column)
        media_id = inp.loc[idx,'media_id']  
        
        url = 'http://www.allaboutoutdoor.com/show_media_map.php?category_id=1&media_id='+str(media_id)+'&iframe=true&width=100%&height=100%'
        print idx        
        print media_id
        driver.get(url)
        soup= BeautifulSoup(driver.page_source,"lxml")
        
        data  = soup.find_all("script")[7].string 
        data = data.replace('\n','')
        data = data.replace('\t','')
        
        p = re.compile(r'var media = \[\[(.*?)\],\];')
        m = p.search(data)

        lat=''
        longi=''
        
        try:
            
            if m:
                s= str(m.group(1)).replace(',','').split()
                lat=s[1]
                longi=s[2]
            
            else:
                lat='not found'
                longi='not found'
            
        except:
            pass
        
        result.loc[0]=[media_id,lat,longi]
        
        result.to_csv(fp,header=False,encoding='utf-8')
        print 'written to file. LAT=%s LONG=%s\n'%(lat,longi) 
               
    
        
    fp.close()
       
    driver.close()