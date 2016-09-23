from bs4 import BeautifulSoup
import re
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pandas as pd
from sys import argv
import json
a=[]
inp = pd.read_csv('lat_long.csv')
for idx in xrange(0,11069):
        s=inp.loc[idx,'Lat']
        if s==' ':
            a.append(idx)
print a