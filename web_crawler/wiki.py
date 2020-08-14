import requests
from bs4 import BeautifulSoup
import pandas as pd
import json
from urllib import request, parse
import os
import time
import lxml.html
import datetime
import csv
def save(title):
    df = pd.DataFrame(
        data=[{
            'title': title,
        }],
        columns=['title'])
    return df
# with open('E:/csv/ds.txt', "r") as f:    #開啟檔案
#     data = f.read()
# print(data)
# dic=data.split(' ')
# print(dic)
joblist=pd.DataFrame()
break_true=False
t=False
# for i in range(len(dic)):
#     df=save(dic[i])
#     jslist=jslist.append(df,ignore_index=True)
# jslist.to_csv('E:/csv/dict.csv',encoding="utf-8-sig")
count=0
with open('E:/dict/dict4.csv','r',encoding="utf-8-sig") as f:
    reader=csv.reader(f) #讀檔案內容
    df=save('tttt')
    joblist=joblist.append(df,ignore_index=True)
    for row in reader:
        try:
            break_true = False
            url='https://zh.wikipedia.org/wiki/%s'%(row[0])
            res=requests.get(url)
            soup=BeautifulSoup(res.text,'html.parser')
            list=soup.select('div[class="mw-parser-output"]')
            for dicts in list: #抓詞
                repeat = False
                dicts=dicts('p')
                for s in dicts:
                    s=s('a')
                    for i in range(len(s)):#每一個詞
                        t = False
                        count+=1
                        if '尋找「' in s[i].text:
                            break_true = True#紀錄是否為空
                            print('這個頁面是空的')
                            break
                        if '[' in s[i].text: #數字略過
                            pass
                        else:
                            print(count,s[i].text)
                            df=save(s[i].text)
                            for title_repeat in joblist['title']:  # 跟前面存的所有標題比對一次
                                if (s[i].text == title_repeat or len(s[i].text)>15): #抓過就跳出不抓這個詞
                                    print("這個詞存過了")
                                    count-=1
                                    t=True
                                    break
                            if (t==False):
                                joblist=joblist.append(df,ignore_index=True)
                                break
                if break_true == True:#若空找下一個詞
                    break
        except:
            pass
joblist.to_csv('E:/dict/dictss.csv',encoding="utf-8-sig")