from bs4 import BeautifulSoup
import requests
import pandas as pd

max_id=547
folder='/home/ubuntu/chikoop/'
column = ['Hoarding Id','','']
len_result=0
result = pd.DataFrame(columns=column)
url='http://marquisads.com/admin1/showallboardmail.asp'
html = requests.get(url)
soup = BeautifulSoup(html.text,"lxml")
    
row = soup.find('form').find('center').find('tr').find('tr').next_sibling.next_sibling.next_sibling.next_sibling

    
for idx in xrange(1,max_id):
    
    
    childrens = row.findChildren()
    print childrens
    print 
    break
    '''temp=[]
    for children in childrens:
        if children.b!=None:
            temp.append(children.b.next_sibling)
        
    
    print 'Id: '+temp[2]
    
    
    result.loc[len_result]=[temp[2],temp[0],temp[1],temp2[0],temp2[1],temp2[2],temp2[3],temp3[0],temp3[1],Contact,Email,img_link]
    len_result+=1
    '''

'''
with open(folder+'marquisads.csv','a') as fp:
    result.to_csv(fp,encoding='utf-8',index=False,header=False)
fp.close()
print "written to file"
'''
