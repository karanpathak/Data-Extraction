from bs4 import BeautifulSoup
import requests
import re

import pandas as pd


def get_data(html,result,len_result):
    
    #parsing the wepage via lxml parser
    soup=BeautifulSoup(html.text,"lxml")
    
    #finding Hoarding container division
    divs=soup.findAll('div',{'class':'fll media_result as_country_container'})
    
    for div in divs:
        idx = div['id']
        print "HOARDING ID: "+idx    
        
        div1 = div.find('div',{'class':'fll'})
        div2 = div1.next_sibling.next_sibling
        
        geo_tag_url=''
        media_id=''
        Media_vehicle=''
        
        Media_vehicle = div2.find('table',{'class':'media_result_left'}).find('tr').find('td').next_sibling.next_sibling.p.string
        
        #Extracting from DIV1
        
        #Geo Tag Link    
        geo_tag_url='http://www.allaboutoutdoor.com/'+div1.find('div',{'class':'map_media gallery'}).find('a')['href']
        
        #Media ID    
        media_id=re.search(r'media_id=(\d*)&',geo_tag_url).group(1)
        
        print 'Media Id: '+media_id
        print 'Media_vehicle: '+Media_vehicle
        print
        
        
        '''
        #Download Images and save it 
        image=requests.get(image_url)
        Image_File="1_O"+media_id+"_thumb_front.jpg"
        with open(folder+"/"+Image_File,"w+") as f:
            f.write(image.content)
            f.close()
        ''' 
        
        
    
        
        result.loc[len_result]=[media_id,Media_vehicle]
        len_result+=1
        
        
    return result
           
        



if __name__=="__main__":
    
    folder='/home/kp/chikoop/'
    #Preparing Pandas DataFrame    
    column = ['media_id','Media_vehicle']
    len_result=0
    
    result = pd.DataFrame(columns=column)
    
    '''
    #BASE PAGE
    
    url='http://www.allaboutoutdoor.com/inner.php'

    #fetching the webpage
    html=requests.get(url)
    
    result=get_data(html,result,len_result)
    
    with open(folder+'Update.csv','w+') as fp:
        result.to_csv(fp,index=False)
    fp.close()
    
    '''
    
    #AJAX PAGINATION
    head={'Host': 'www.allaboutoutdoor.com',
      'User-Agent':'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:48.0) Gecko/20100101 Firefox/48.0',
      'Accept': '*/*',
      'Accept-Language': 'en-US,en;q=0.5',
      'Accept-Encoding': 'gzip, deflate',
      'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
      'X-Requested-With': 'XMLHttpRequest',
      'Referer': 'http://www.allaboutoutdoor.com/inner.php',
      'Content-Length': '125',
      'Cookie':'_ga=GA1.2.1104886124.1471677211; PHPSESSID=d5c47ed86d288ff638a59126855e37d7',
      'Connection': 'keep-alive'
      }

    
    
    LastId=11010
    max_page=11060
    
    while LastId<=max_page:
        s='con=&ord_type=DESC&ord_by=state_city%2C+city_zone%2C+is_premium+DESC%2C+is_landmark+DESC%2C+is_valuedeal+&LastId='+str(LastId)+'&city_ad=1'
    
        html=requests.post(url='http://www.allaboutoutdoor.com/get_inner_list_pagination.php',data=s,headers=head)
                
        len_result=0
        result = pd.DataFrame(columns=column)
        
        result=get_data(html,result,len_result)    
        
        with open(folder+'Update.csv','a') as fp:
            result.to_csv(fp,header=False,encoding='utf-8',index=False)
        fp.close()
        LastId+=10        
        
    