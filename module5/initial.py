from bs4 import BeautifulSoup
import requests
import pandas as pd
from sys import argv

min_id=int(argv[1])
max_id=int(argv[2])

for idx in xrange(min_id,max_id+1):
    url='http://www.shubhangiadvertising.in/admin1/viewhoardings1.asp?hoardingid='+str(idx)
    html = requests.get(url)
    soup = BeautifulSoup(html.text,"lxml")
    
    Contact= '9552568209'
    Email='sunil@shubhangiadvertising.in'
    img_link=''
    
    first_table = soup.find('form').table
    second_table = first_table.next_sibling.next_sibling
    
    main1_row = first_table.find('tr').next_sibling.next_sibling
    img_link = main1_row.next_sibling.next_sibling.find('img')['src']
    col1 = main1_row.find('tr')
    temp1 = []
    childrens = col1.findChildren()
    for children in childrens[:3]:
        if children.b!=None:
            temp1.append(children.b.next_sibling)
    print temp1
    
    temp_row = second_table.find('table').find('tr') 
    temp2=[]
    for i in xrange(4):
        childrens = temp_row.findChildren()    
        temp2.append(childrens[2].string )
        temp_row = temp_row.next_sibling
    
    print temp2        
    break