import json

import happybase
from django.core.paginator import Paginator
from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from sys_main.models import Recruit


def page_list(request):
    return render(request,'main.html')
def introduce_page(request):
    return render(request,'introduce.html')
def meue_page(request):
    request.session['login']='login'
    page_num = request.GET.get('page_num')
    city = request.GET.get('city')
    job = request.GET.get('job')
    page_chooise=request.GET.get('page_chooise')
    page_val=request.GET.get('page_val')
    rec = Recruit.objects.filter().values()
    if city:
        rec = rec.filter(work_addr__contains=city)
    if job:
        rec = rec.filter(position__contains=job)
    rec = list(rec)
    print(Recruit.objects.filter().query)

    login = request.session.get('login')

    if login:
        conn = happybase.Connection(host='192.168.0.99',port=9090)
        table=conn.table('spiderteam:t_recruit')
        query_str=None
        if city and job:
            query_str = "RowFilter (=,'regexstring:"+city+".*:.*"+job+".*')"
        elif job:
            query_str = "RowFilter (=,'substring:"+job+"')"
        elif city:
            query_str = "RowFilter (=,'substring:" + city + "')"
        datas = table.scan(filter=query_str)
        result_dict={}
        for k,v in datas:
            for x ,y in v.items():
                key = str(x,'utf-8')
                result_dict[key[7:]] = str(y,'utf-8')
            rec.append(result_dict)
    pagtor = Paginator(rec, per_page=10)
    if not page_num:
        page_num = 1
    page = pagtor.page(page_num)
    return render(request,'menu.html',{'page':page,'page_chooise':page_chooise,'page_val':page_val})
#发布招聘信息页面
def add_page(request):
    return render(request,'add.html')
#存储招聘信息
def add_logic(request):
    position = request.POST.get('position')
    salary = request.POST.get('price')
    if salary =='0':
        salary='面议'
    elif salary == '1':
        salary = '1000元以下'
    elif salary == '2':
        salary = '1000-2000元'
    elif salary == '3':
        salary = '2000-3000元'
    elif salary == '4':
        salary = '3000-5000元'
    elif salary == '5':
        salary = '5000-8000元'
    elif salary == '6':
        salary = '8000-12000元'
    elif salary == '7':
        salary = '12000-20000元'
    elif salary == '8':
        salary = '20000元以上'

    company = request.POST.get('company')
    experience = request.POST.get('work_years')
    if experience =='0':
        experience='不限'
    elif experience == '1':
        experience = '1年以内'
    elif experience == '2':
        experience = '1-3年'
    elif experience == '3':
        experience = '3-5年'
    elif experience == '4':
        experience = '5-10年'
    elif experience == '5':
        experience = '10年以上'
    education = request.POST.get('degree')
    if education == '0':
        education = '不限'
    elif education == '1':
        education = '初中'
    elif education == '2':
        education = '高中'
    elif education == '3':
        education = '中专/技校'
    elif education == '4':
        education = '大专'
    elif education == '5':
        education = '本科'
    elif education == '6':
        education = '硕士及以上'
    work_addr = request.POST.get('work_addr')
    company_size = request.POST.get('company_size')
    job_info = request.POST.get('description')
    main_business = request.POST.get('main_business')
    com_net = request.POST.get('com_net')
    department = request.POST.get('department')
    print(position,salary,company,experience,education,work_addr,company_size,job_info,main_business,com_net,department)
    conn = happybase.Connection(host='192.168.0.99', port=9090)
    table = conn.table('spiderteam:t_recruit')
    # rowkey 地区 职位 网站 公司 薪资
    rowkey = work_addr + ':' + position + ':' + com_net + ':' + company + ':' + salary
    table.put(rowkey, {"common:position": position, "common:company": company, "common:salary": salary,
                       "common:job_info": job_info, "common:experience": experience,
                       "common:education": education, "common:work_addr": work_addr, "common:department": department,
                       "common:company_size": company_size, "common:main_business": main_business, "common:com_net": com_net})

    return render(request,'add.html')

#ip地址分布报表页面
def map_page(request):
    return render(request,'ip_map.html')
#获取ip_map数据
def get_map_datas(request):
    ip_dict={}
    conn = happybase.Connection(host='192.168.0.99',port=9090)
    table = conn.table('spiderteam:t_logs')
    for k,v in table.scan(columns=["info:request_city"]):
        for x,y in v.items():
            print(x,str(y,'utf-8'))
            city = str(y,'utf-8')

            if city in ip_dict:
                count = ip_dict.get(city)
                ip_dict[city]=count+1
            else:
                ip_dict[city]=1
    result_list=[]

    for k,v in ip_dict.items():
        result_dict = {}
        result_dict['value'] = v
        result_dict['name']=k
        result_list.append(result_dict)
    result={'datas':result_list}
    print(result)
    return JsonResponse(result)



