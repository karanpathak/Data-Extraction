from bs4 import BeautifulSoup
import re
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pandas as pd
from sys import argv



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
    
    column = ['media_id','Illumination']

    len_result=0
    
    
    driver = login()    
    print "logged in"
    
    len_result=0
    inp = pd.read_csv(argv[1])
    min_id = int(argv[2])
    max_id = int(argv[3])

    result = pd.DataFrame(columns=column)
    fp = open('update_illumination.csv','a')
    
    for idx in xrange(min_id,max_id+1):
        media_id = inp.loc[idx,'media_id']    
        print media_id
        url='http://www.allaboutoutdoor.com/traditional-media-detail.php?mid='+str(media_id)

        result = pd.DataFrame(columns=column)
    
        driver.get(url)
        soup_sub = BeautifulSoup(driver.page_source,"lxml")
   
        #Finding Media Details
        Media_row_main = soup_sub.find('table',{'class' : 'media_detail_result_left2'}).find('tr') 
        
        Media_row_main = Media_row_main.next_sibling.next_sibling
    
        Media_row_main = Media_row_main.next_sibling.next_sibling
            
        Media_row_main = Media_row_main.next_sibling.next_sibling
        
        Media_row_main = Media_row_main.next_sibling.next_sibling
        
        Media_row_main = Media_row_main.next_sibling.next_sibling
        
        Media_row_main = Media_row_main.next_sibling.next_sibling
        
        Media_row_main = Media_row_main.next_sibling.next_sibling
        
        Media_row_main = Media_row_main.next_sibling.next_sibling
        
        
        Media_row_main = Media_row_main.next_sibling.next_sibling
        
        try:
            if re.match(r'Illumination',Media_row_main.td.p.strong.string):
                Illumination =  Media_row_main.td.next_sibling.next_sibling.p.string
                Illumination = " ".join((Illumination).split())
        
            else:
                Media_row_main = Media_row_main.next_sibling.next_sibling
                Illumination =  Media_row_main.td.next_sibling.next_sibling.p.string
                Illumination = " ".join((Illumination).split())
            
        except:
            pass      
       
        print Illumination
        
        
        
        result.loc[0]=[media_id,Illumination]
        
        result.to_csv(fp,header=False,encoding='utf-8')
               
    
        
    fp.close()
       
    driver.close()