from django.shortcuts import render
import requests
from django.contrib import messages
from django.views.generic import View, TemplateView
from .forms import ProviderForm
import json
from app.utils  import get_provider, get_developer,get_api,get_json_api_1,weekly,get_json_api_2,task_join


def Index(request):
    if request.method=='POST':
        url= 'http://127.0.0.1:8000/api/provider'
        url_1,url_2 =get_provider(url,'Provider 1','Provider 2')
        developer_name =str(request.POST['p_name'])
        power,message =get_developer(developer_name)
        data =get_api(url_1)
        data1 = get_json_api_1(data,power,developer_name)
        messages.info(request,message)
        data2=get_json_api_2(url_2,power,developer_name)
        datas = task_join(data1,data2)
        
        h1, h2, h3, h4,h5,h6  = weekly(datas)
        context = {
            'developer_name':developer_name,
            'h1':h1,
            'h2':h2,
            'h3':h3,
            'h4':h4,
            'h5':h5,
            'h6':h6
        }
        return render(request,'detail.html',context=context)
    else:
        return render(request,'index.html')

