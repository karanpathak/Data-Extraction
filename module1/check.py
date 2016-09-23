from os import path
from sys import argv
import pandas as pd

folder = '/home/hoarding/karan/module1/images/'
df1=pd.read_csv(argv[1])
min_index=int(argv[2])
max_index=int(argv[3])
for i in range(min_index,max_index+1):
    media_id = df1.loc[i,'media_id']
    Image_File="1_Z"+str((2*int(media_id))+3)+"_thumb_front.jpg"
    if path.isfile(folder+Image_File)==False:
        print (str(media_id))