from django.core.paginator import Paginator
from django.shortcuts import render
import happybase
# Create your views here.
from sys_main.models import Recruit


def page_list(request):
    '''内容主页页面'''
    return render(request,'main.html')
def page_introduce(request):
    return render(request,'introduce.html')

def page_menu(request):
    '''主页数据展示'''
    user_login = request.session.get('login')
    num = request.GET.get('num')
    city = request.GET.get('city')
    position = request.GET.get('position')
    print('row Key:',city,position )
    if not num:
        num = 1
    if not user_login:
        rows = Recruit.objects.filter(position__contains=position,work_addr__contains=city)
        pagtor = Paginator(rows,per_page=10)

        page = pagtor.page(num)
    else:
        rows = Recruit.objects.filter(position__contains=position, work_addr__contains=city)
        pagtor = Paginator(rows, per_page=10)
        page = pagtor.page(num)

        conn = happybase.Connection(host='192.168.0.99', port=9090)
        conn.open()
        table = conn.table('spiderteam:t_recruit')
        scanner = table.scan(columns=('other', 'common'), limit=10, reverse=True)
        if city and not position:
            search = table.scan(filter=("RowFilter(=,Substring=" + city + ")"))
        if position and not city:
            search = table.scan(filter=("RowFilter(=,Substring=" + position + ")"))
        if city and position:
            search = table.scan(filter=("RowFilter(=,Substring=" + city +':'+position +")"))
        print(scanner)
        for k, v in scanner:
            print(k.decode(), v[b'common:salary'].decode())


    return render(request,'menu.html',{'page':page,'num':num,'position':position,'city':city})

