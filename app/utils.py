import urllib.request
import json
import numpy as np
from operator import itemgetter
import requests


def get_provider(url,p_name1,p_name2):
    r = requests.get(url)  
    datas = r.json()
    for i in datas:
        name =i['name']
        if name==p_name1:
            url_1 =i['endpoint']
        elif name==p_name2:
            url_2 =i['endpoint']
        else:
            url_1 =None
            url_2 =None
    return  url_1,url_2

def get_developer(developer_name):
    r = requests.get('http://localhost:8000/api/developer/')  # http://www.mocky.io/v2/5d47f24c330000623fa3ebfa
    datas = r.json()
    power=0
    for i in datas:
        name=i['name']
        level = i['level']
        duration=i['duration']
        #burada developer'ın çalışma gücü hesaplanır
        if developer_name==name:
            message ="İşleminiz Başarılı."
            power=int(level)*int(duration)
        elif developer_name=='Developer Seçiniz':
            message='Developer Seçimi Yapmadınız:!'
    return  power,message


def get_api(url_1):
    res = requests.get(url_1)
    try:
        data = res.json()
    except KeyError:
        data = None
    return data

def get_json_api_1(data,power,developer_name):
    #Oncelik zorluk derecesinde büyükten küçüüğe sıralama
    api_1 = sorted(data, key=itemgetter('zorluk'), reverse=True)
    value_1 = []
    for i in api_1:
        name= i['id']
        difficulty = i['zorluk']
        time = i['sure']
        if difficulty == power:
            value_1.append([difficulty,time,name,developer_name,power])
    return value_1

def get_json_api_2(url_2,power,developer_name):
    r = requests.get(url_2)
    value_2=[]
    for i in range(67):
        data = r.json()[i]
        for key, value in data.items():
            name= key
            difficulty= value['level']
            time = value['estimated_duration']
            if difficulty==power:
                value_2.append([difficulty,time,name,developer_name,power])
    return value_2

def task_join(data1,data2):
    data = data1 + data2
    return data

def weekly(datas):
    task_h1 = []
    task_h2 = []
    task_h3 = []
    task_h4 = []
    task_h5 = []
    task_h6 = []
    work = 0
    time =0
    difficulty =0
    # print('datas',datas)
    for i in datas:
        difficulty = i[0]
        time = i[1]
        name = i[2]
        person = i[3]
        value = i[4]
        work += int(time)
        if work<=45 :
            task_h1.append({'zorluk':difficulty,'sure':time,'ad':name,'kisi':person})
        elif work > 45 and work <= 90 :
            task_h2.append({'zorluk':difficulty,'sure':time,'ad':name,'kisi':person})
        elif work > 90 and work <= 135:
            task_h3.append({'zorluk':difficulty,'sure':time,'ad':name,'kisi':person})
        elif work > 135 and work <= 180:
            task_h4.append({'zorluk':difficulty,'sure':time,'ad':name,'kisi':person})
        elif work > 180 and work <= 225:
            task_h5.append({'zorluk':difficulty,'sure':time,'ad':name,'kisi':person})
        elif work > 225 and work <= 275:
            task_h6.append({'zorluk':difficulty,'sure':time,'ad':name,'kisi':person})
    return task_h1,task_h2,task_h3,task_h4,task_h5,task_h6


