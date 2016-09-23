from bs4 import BeautifulSoup
import requests
import re
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pandas as pd


def login(username,password):
    
    #LOGIN  
    driver = webdriver.PhantomJS(executable_path='/usr/local/bin/phantomjs')
    
    #driver = webdriver.Firefox()
    driver.get('http://www.allaboutoutdoor.com/login.php')
        
    username = driver.find_element_by_id('email')
    password = driver.find_element_by_id('password')
        
    username.send_keys(username)
    password.send_keys(password)
        
    driver.find_element_by_id('formID').find_element_by_name("submit").click()
    
    return driver


folder='/home/kp/chikoop/'
#Preparing Pandas DataFrame    
#column=['comp_id','company_name','image_url','sub_link','description','turnover_per_annum','name','email','mobile','address','designation']

column=['comp_id','company_name','image_url','sub_link',]
len_result=0

result = pd.DataFrame(columns=column)

username = "lovishcool1@gmail.com"
password = "abc98765"

#driver = login(username,password)

#AJAX 
head={
'Host':'www.allaboutoutdoor.com',
'User-Agent':'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:48.0) Gecko/20100101 Firefox/48.0',
'Accept': '*/*',
'Accept-Language':'en-US,en;q=0.5',
'Accept-Encoding':'gzip, deflate',
'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
'X-Requested-With': 'XMLHttpRequest',
'Referer': 'http://www.allaboutoutdoor.com/our-community.php',
'Content-Length': '31',
'Cookie':'_ga=GA1.2.1104886124.1471677211; PHPSESSID=7fdbeccc6821e26562ff28d865d819f1; _gat=1',
'Connection': 'keep-alive',
'Cache-Control': 'max-age=0'
}

s='section=99&keywords=&category=1'
html=requests.post(url='http://www.allaboutoutdoor.com/our-comm-ajax.php',data=s,headers=head)
soup=BeautifulSoup(html.text,"lxml")
divs = soup.findAll('div',{'class':'fll profile_pic tac'})


company_name = ''
image_url = ''
base_link = ''
sub_link = ''
comp_id = ''
description = ''
turnover_per_annum = ''
name = ''
email=''
mobile=''
address=''
designation=''


for div in divs:
    
    
    base_link = 'http://www.allaboutoutdoor.com/'    
    sub_link = base_link + div.a['href']
    image_url = base_link + div.a.img['src']
    company_name = div.find('p').a.string
    comp_id = re.search(r'comp=(\d*)$',sub_link).group(1)
   
    print 'comp_id: '+comp_id
    print 'company name: '+company_name
    print 'sub_link: '+sub_link    
    
with open(folder+'new.csv','a') as fp:
            result.to_csv(fp,header=False,encoding='utf-8')
    fp.close()
    
    '''
    #Download Images and save it 
    image=requests.get(image_url)
   
    Image_File= '_'.join(company_name.split())
    with open(folder+Image_File,"w+") as f:
        f.write(image.content)
    f.close()    
    '''
    
    '''
    driver.get(sub_link)    
    soup_sub = BeautifulSoup(driver.page_source,"lxml")
    main = soup_sub.find('div',{'id':'company_profile'})
    
    description = main.find('div',{'class':'company_description'}).div.next_sibling.next_sibling.next_sibling.next_sibling.p.string
      
    turnover_per_annum = main.find('div',{'id':'touchpoint_share999'}).find('div',{'class':'flr'}).h6.string
    turnover_per_annum = re.search(r'INR (.*)$',turnover_per_annum).group(1)
    
    print 'description: '+description
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
    
    result.loc[len_result]=[comp_id,company_name,image_url,sub_link,description,turnover_per_annum,name,designation,email,mobile,address]
    len_result+=1
    
    with open(folder+'new.csv','a') as fp:
            result.to_csv(fp,header=False,encoding='utf-8')
    fp.close()
    
    print 'written to file'
    print
    print
    break
    '''