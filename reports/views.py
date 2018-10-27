import happybase
from django.shortcuts import render

# Create your views here.
from sys_main.models import Recruit


def reports(request):
    '''
    报表展示
    :param request:
    :return:
    '''
    # conn = happybase.Connection(host='192.168.0.99', port=9090)
    # conn.open()
    # table = conn.table('spiderteam:t_recruit')
    # scanner = table.scan(columns=('other', 'common'), limit=10, reverse=True)
    # #search = table.scan(filter=("RowFilter(=,Substring=" + '北京' +':'+'web'+ ")"))
    # print(1111111,type(scanner))
    # for k,v in scanner:
    #     print('search:',k,len(v))
    bj_web = Recruit.objects.filter(work_addr__contains='北京',position__contains='web').count()
    bj_spider = Recruit.objects.filter(work_addr__contains='北京',position__contains='爬虫').count()
    bj_ai = Recruit.objects.filter(work_addr__contains='北京',position__contains='AI').count()
    bj_bigdata = Recruit.objects.filter(work_addr__contains='北京',position__contains='大数据').count()

    sh_web = Recruit.objects.filter(work_addr__contains='上海', position__contains='web').count()
    sh_spider = Recruit.objects.filter(work_addr__contains='上海', position__contains='爬虫').count()
    sh_ai = Recruit.objects.filter(work_addr__contains='上海', position__contains='AI').count()
    sh_bigdata = Recruit.objects.filter(work_addr__contains='上海', position__contains='大数据').count()

    gz_web = Recruit.objects.filter(work_addr__contains='广州', position__contains='web').count()
    gz_spider = Recruit.objects.filter(work_addr__contains='广州', position__contains='爬虫').count()
    gz_ai = Recruit.objects.filter(work_addr__contains='广州', position__contains='AI').count()
    gz_bigdata = Recruit.objects.filter(work_addr__contains='广州', position__contains='大数据').count()

    sz_web = Recruit.objects.filter(work_addr__contains='深圳', position__contains='web').count()
    sz_spider = Recruit.objects.filter(work_addr__contains='深圳', position__contains='爬虫').count()
    sz_ai = Recruit.objects.filter(work_addr__contains='深圳', position__contains='AI').count()
    sz_bigdata = Recruit.objects.filter(work_addr__contains='深圳', position__contains='大数据').count()


    return render(request,'report_pie.html',{'bj_web':bj_web,'bj_spider':bj_spider,'bj_ai':bj_ai,'bj_bigdata':bj_bigdata,
                                             'sh_web': sh_web, 'sh_spider': sh_spider, 'sh_ai': sh_ai,'sh_bigdata': sh_bigdata,})