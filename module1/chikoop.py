from bs4 import BeautifulSoup
import requests
import re
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pandas as pd



def get_data(html,driver,result,len_result,folder):
    
    #parsing the wepage via lxml parser
    soup=BeautifulSoup(html.text,"lxml")
    
    #finding Hoarding container division
    divs=soup.findAll('div',{'class':'fll media_result as_country_container'})
    
    for div in divs:
        idx = div['id']
        print "HOARDING ID: "+idx    
        
        div1 = div.find('div',{'class':'fll'})
       
        
        geo_tag_url=''
        media_id=''
        Illumination=''
        
        
        #Extracting from DIV1
        
        #Geo Tag Link    
        geo_tag_url='http://www.allaboutoutdoor.com/'+div1.find('div',{'class':'map_media gallery'}).find('a')['href']
        
        #Media ID    
        media_id=re.search(r'media_id=(\d*)&',geo_tag_url).group(1)
        
        #image_url='http://www.allaboutoutdoor.com/'+div1.find('div',{"class": "zoom_media gallery"}).find('a')['href']
       
        
        '''
        #Download Images and save it 
        image=requests.get(image_url)
        Image_File="1_O"+media_id+"_thumb_front.jpg"
        with open(folder+"/"+Image_File,"w+") as f:
            f.write(image.content)
            f.close()
        ''' 
        
        
    
        view_details_url='http://www.allaboutoutdoor.com/'+div.find('div',{'class':'mr5'}).find('a')['href']
        driver.get(view_details_url)
        
        soup_sub = BeautifulSoup(driver.page_source,"lxml")
        
        #Finding Media Details
        Media_row_main = soup_sub.find('table',{'class' : 'media_detail_result_left2'}).find('tr') 
        #Media_Owner = Media_row_main.td.next_sibling.next_sibling.p.a.string 
        #Media_Owner = " ".join((Media_Owner).split())
    
        Media_row_main = Media_row_main.next_sibling.next_sibling
        #Address = Media_row_main.td.next_sibling.next_sibling.p.string
        #Address = " ".join((Address).split())
    
        Media_row_main = Media_row_main.next_sibling.next_sibling
        #FTF = Media_row_main.td.next_sibling.next_sibling.p.string
        #FTF = " ".join((FTF).split())
            
        Media_row_main = Media_row_main.next_sibling.next_sibling
        #row_temp = Media_row_main.td.next_sibling.next_sibling.find('a')
        #Location = row_temp.previousSibling+row_temp.string+row_temp.nextSibling
        #Location = " ".join((Location).split())
        
        Media_row_main = Media_row_main.next_sibling.next_sibling
        #Area_Description = Media_row_main.td.next_sibling.next_sibling.p.string
        #Area_Description = " ".join((Area_Description).split())
        
        Media_row_main = Media_row_main.next_sibling.next_sibling
        #Price = Media_row_main.td.next_sibling.next_sibling.p.string
        #Price = " ".join((Price).split())
        
        Media_row_main = Media_row_main.next_sibling.next_sibling
        #Actual_size =  Media_row_main.td.next_sibling.next_sibling.p.string
        #Actual_size = " ".join((Actual_size).split())
        
        Media_row_main = Media_row_main.next_sibling.next_sibling
        #Wrap_type =  Media_row_main.td.next_sibling.next_sibling.p.string
        #Wrap_type = " ".join((Wrap_type).split())
        
        Media_row_main = Media_row_main.next_sibling.next_sibling
        #Total_area =  Media_row_main.td.next_sibling.next_sibling.p.string
        #Total_area = " ".join((Total_area).split())
        
        print media_id
        Media_row_main = Media_row_main.next_sibling.next_sibling
        

        if re.match(r'Illumination',Media_row_main.td.p.strong.string):
            Illumination =  Media_row_main.td.next_sibling.next_sibling.p.string
            Illumination = " ".join((Illumination).split())
        
        else:
            Media_row_main = Media_row_main.next_sibling.next_sibling
            Illumination =  Media_row_main.td.next_sibling.next_sibling.p.string
            Illumination = " ".join((Illumination).split())
            
       
        '''
        #Finding Owner Details
        Owner_row_main = soup_sub.find('div',{'class' : 'fll media_company_contact '}).find('tr')
        row = Owner_row_main.find('tr')
        Name = row.td.h3.string
        Name = " ".join((Name).split())
        
        
        row = row.next_sibling.next_sibling
        
        row_temp = row.td.p.strong.a
        
        Designation = row_temp.previousSibling
        Designation = " ".join((Designation).split())
        
        row = row.next_sibling.next_sibling
        Email = row.td.next_sibling.next_sibling.find('p').a.string    
        Email = " ".join((Email).split())
        
        try:
            row = row.next_sibling
            Phone = row.td.next_sibling.next_sibling.p.string        
            Phone = " ".join((Phone).split())
        
        except AttributeError:
            print "No phone number"
        
        

        
        print image_url
        print geo_tag_url
        print "Name: "+Name
        print "Designation: " +Designation
        print "Email: "+Email
        print "Phone: "+Phone
        print "Media_Owner: "+Media_Owner  
        print "Address: "+Address
        print "Location: "+Location
        print "FTF: "+FTF
        print "Area_Description: "+Area_Description 
        print "Price: "+Price
        print "Actual_size: "+Actual_size
        print "Wrap_type: "+Wrap_type
        print "Total_area: "+Total_area
        '''
        
       
        print Illumination
        result.loc[len_result]=[media_id,Illumination]
        len_result+=1
        
        
    return result
           
        



if __name__=="__main__":
    
    folder='/home/kp/chikoop/'
    #Preparing Pandas DataFrame    
    column = ['media_id','Illumination']

    len_result=0
    
    result = pd.DataFrame(columns=column)
    
    #LOGIN
    driver = webdriver.PhantomJS(executable_path='/usr/local/bin/phantomjs')
    #driver = webdriver.Firefox()
    driver.get('http://www.allaboutoutdoor.com/login.php')
    
    username = driver.find_element_by_id('email')
    password = driver.find_element_by_id('password')
    
    username.send_keys("lovishcool1@gmail.com")
    password.send_keys("abc98765")
    
    driver.find_element_by_id('formID').find_element_by_name("submit").click()
        
    '''
    
    #BASE PAGE
    
    url='http://www.allaboutoutdoor.com/inner.php'

    #fetching the webpage
    html=requests.get(url)
    
    result=get_data(html,driver,result,len_result,folder)
    
    with open(folder+'Main.csv','w+') as fp:
        result.to_csv(fp)
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

    
    LastId=10
    max_page=10
    
    while LastId<=max_page:
        s='con=&ord_type=DESC&ord_by=state_city%2C+city_zone%2C+is_premium+DESC%2C+is_landmark+DESC%2C+is_valuedeal+&LastId='+str(LastId)+'&city_ad=1'
    
        html=requests.post(url='http://www.allaboutoutdoor.com/get_inner_list_pagination.php',data=s,headers=head)
                
        len_result=0
        result = pd.DataFrame(columns=column)
        
        result=get_data(html,driver,result,len_result,folder)    
        
        with open(folder+'update_illumination.csv','a') as fp:
            result.to_csv(fp,header=False,encoding='utf-8')
        fp.close()
        LastId+=10        
        
    driver.close()