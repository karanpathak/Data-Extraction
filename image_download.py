from sys import argv
import pandas as pd
import requests

folder_name=argv[4]
folder = '/home/hoarding/karan/lovish/'+folder_name+'/images/'

df1=pd.read_csv(argv[1])
#df1 = df1.set_index('Hoarding Id')
min_index=int(argv[2])
max_index=int(argv[3])
for i in range(min_index,max_index+1):
    print (i)
    image_url = df1.loc[i,'link']
    image=requests.get(image_url)
    Image_File=df1.loc[i,'name']
    with open(folder+Image_File,"w+b") as f:
        f.write(image.content)
    f.close()
    print (str(i)+":written to file\n")
