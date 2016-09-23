from bs4 import BeautifulSoup
import requests
import re
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pandas as pd
from sys import argv

def login(user,passwd):
    
    #LOGIN  
    driver = webdriver.PhantomJS(executable_path='/usr/local/bin/phantomjs')
    
    #driver = webdriver.Firefox()
    driver.get('http://www.allaboutoutdoor.com/login.php')
        
    username = driver.find_element_by_id('email')
    password = driver.find_element_by_id('password')
        
    username.send_keys(user)
    password.send_keys(passwd)
        
    driver.find_element_by_id('formID').find_element_by_name("submit").click()
    
    return driver


folder='/home/kp/chikoop/'
#Preparing Pandas DataFrame    
column=['comp_id','description','turnover_per_annum','name','designation','email','mobile','address']

len_result=0

result = pd.DataFrame(columns=column)

username = "lovishcool1@gmail.com"
password = "abc98765"

driver = login(username,password)
print "logged In"

inp=pd.read_csv(argv[1])
print "File Read"

sub_link=''
comp_id = ''
description = ''
turnover_per_annum = ''
name = ''
email=''
mobile=''
address=''
designation=''

n=len(inp)
for i in xrange(n):
    comp_id = inp.loc[i,'comp_id']      
    print 'comp_id: '+str(comp_id)
    sub_link="http://www.allaboutoutdoor.com/profile.php?comp="+str(comp_id)

    driver.get(sub_link)    
    soup_sub = BeautifulSoup(driver.page_source,"lxml")
    main = soup_sub.find('div',{'id':'company_profile'})
    
    description = main.find('div',{'class':'company_description'}).div.next_sibling.next_sibling.next_sibling.next_sibling.p.string
    print 'description: '+description
    
    
    turnover_per_annum = main.find('div',{'id':'touchpoint_share999'}).find('div',{'class':'flr'}).h6.string
    turnover_per_annum = re.search(r'INR (.*)$',turnover_per_annum).group(1)
    
    
    print 'turnover_per_annum: '+turnover_per_annum
    
    
    details = main.find('div',{'class':'company_contact'})
    name = details.find('div',{'class':'fll'}).h3.string
    designation = details.find('p').strong.string

    print 'name: '+name
    print 'designation: '+designation
    
    row = details.find('table').find('tr')
    
    if re.match(r'Email',row.td.strong.string):
        email = row.td.next_sibling.next_sibling.a.string
        row = row.next_sibling.next_sibling
    
    if re.match(r'Mobile',row.td.strong.string):
        mobile = row.td.next_sibling.next_sibling.string
        row = row.next_sibling.next_sibling
    
    if re.match(r'Address',row.td.strong.string):
        address = row.td.next_sibling.next_sibling.string
        row = row.next_sibling.next_sibling
    
    print 'email: '+email
    print 'mobile: '+ mobile
    print 'address: '+address   
    
    result.loc[len_result]=[comp_id,description,turnover_per_annum,name,designation,email,mobile,address]
    len_result+=1
    
with open(folder+'update1.csv','a') as fp:
    result.to_csv(fp,header=True,encoding='utf-8')
fp.close()
    
print 'written to file'
print
print
    