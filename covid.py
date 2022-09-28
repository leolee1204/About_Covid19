#!/usr/bin/python3
import bar_chart_race as bcr #pip bar_chart_race
import pandas as pd
from datetime import datetime
import requests
from bs4 import BeautifulSoup
import os
import matplotlib.pyplot as plt


def show_bar_chart_race():
   plt.rcParams['font.sans-serif'] = ['simhei']
   plt.rcParams['axes.unicode_minus'] = False
   df =pd.read_csv('covid19.csv')
   bcr.bar_chart_race(df.set_index('date'),'covid19.gif', orientation='v')

def res_open_data():
   now = datetime.now().strftime("%Y-%m-%d")
   res = requests.get('https://covid-19.nchc.org.tw/')
   soup = BeautifulSoup(res.text,'lxml')
   datas = soup.find_all('span',style='font-size: 1em;')
   datalist = []
   datalist.append(['date',now])
   for data in datas:
       city,number = data.text.strip().split('+')
       datalist.append([city,number])
   return datalist

def save_df():
   #只篩選到日
   # now = pd.to_datetime(datetime.now(),format="%Y-%m-%d").date()
   datalist = res_open_data()
   df = pd.DataFrame(datalist).T
   if 'covid19.csv' not in os.listdir(os.getcwd()):
       df.to_csv('covid19.csv',mode='a',header=False,index=False)
   else:
       df = df[1:]
       df.to_csv('covid19.csv', mode='a',header=False,index=False)

if __name__ == '__main__':
    save_df()
    show_bar_chart_race()

