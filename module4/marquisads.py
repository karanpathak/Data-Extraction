from bs4 import BeautifulSoup
import requests
import pandas as pd

max_id=547
folder='/home/ubuntu/chikoop/'
column = ['Hoarding Id','City','Location','HOARDING SIZE','NAME OF ROAD','LANDMARK','TYPE OF AREA','LIT/NONLIT','BOARD LOCATION','Contact','Email','img_link']
len_result=0
result = pd.DataFrame(columns=column)


for idx in xrange(400,max_id):
    url='http://www.marquisads.com/admin1/viewhoardings1.asp?hoardingid='+str(idx)
    html = requests.get(url)
    soup = BeautifulSoup(html.text,"lxml")
    
    Contact= '9225803751'
    Email='operations.marquis@gmail.com'
    img_link=''
    
    second_row = soup.find('form').find('tr').next_sibling.next_sibling
    temp_col = second_row.find('tr')
    
    childrens = temp_col.findChildren()
    #print childrens
    #print 
    temp=[]
    for children in childrens:
        if children.b!=None:
            temp.append(children.b.next_sibling)
        
    
    print 'Id: '+temp[2]
    
    third_row = second_row.next_sibling.next_sibling
    temp_row = third_row.find('tr').find('tr').td
    
    
    img_link = temp_row.img['src']
    temp_row = temp_row.next_sibling.next_sibling
    
    
    temp_sub_row = temp_row.find('table').find('tr')
    
    temp2=[]
    
    for i in xrange(4):
        childrens = temp_sub_row.findChildren()    
        temp2.append(childrens[2].string )
        temp_sub_row = temp_sub_row.next_sibling.next_sibling
    
    
    print temp2
    
    
    temp_sub_row = temp_row.findAll('table')[-1].find('tr')
    temp3=[]
    for i in xrange(2):
        childrens = temp_sub_row.findChildren()    
        temp3.append(childrens[2].string )
        temp_sub_row = temp_sub_row.next_sibling.next_sibling
    
    print temp3
    print img_link
    
    result.loc[len_result]=[temp[2],temp[0],temp[1],temp2[0],temp2[1],temp2[2],temp2[3],temp3[0],temp3[1],Contact,Email,img_link]
    len_result+=1
    

with open(folder+'marquisads.csv','a') as fp:
    result.to_csv(fp,encoding='utf-8',index=False,header=False)
fp.close()
print "written to file"