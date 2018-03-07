from django.shortcuts import render

# Create your views here.
from django.shortcuts import HttpResponse,render,redirect
from django.template import loader
from . import models
import json
from utils import pagination


def index(request):
    template = loader.get_template('novel/pyecharts.html')
    context = {
        "myechart": line3d(),
        "myechart1": line3d(),
    }
    return HttpResponse(template.render(context, request))



def line3d():
    from pyecharts import Line3D
    import math
    _data = []
    for t in range(0, 25000):
        _t = t / 1000
        x = (1 + 0.25 * math.cos(75 * _t)) * math.cos(_t)
        y = (1 + 0.25 * math.cos(75 * _t)) * math.sin(_t)
        z = _t + 2.0 * math.sin(75 * _t)
        _data.append([x, y, z])
    range_color = ['#313695', '#4575b4', '#74add1', '#abd9e9', '#e0f3f8', '#ffffbf',
                   '#fee090', '#fdae61', '#f46d43', '#d73027', '#a50026']
    line3d = Line3D("3D line plot demo", width=1200, height=600)
    line3d.add("", _data, is_visualmap=True, visual_range_color=range_color, visual_range=[0, 30],
               is_grid3D_rotate=True, grid3D_rotate_speed=180)
    return line3d.render_embed()

def host(request):
    if request.method =="GET":
        current_page = int(request.GET.get('p',1))
        val = int(request.COOKIES.get('per_page_count',10))
        v4 = models.Host.objects.filter(nid__gt=0)
        page_obj = pagination.Page(current_page,len(v4),val)
        data = v4[page_obj.start:page_obj.end]
        page_str = page_obj.page_str("/novel/host/")
        # v1 = models.Host.objects.filter(nid__gt=0).values('ip','port','bi__caption')
        # print(v1)
        # for row in v1:
        #     print(row.nid,row.hostname,row.ip,row.port,row.bi_id,row.bi.caption)
            # print(row['ip'],row['port'],row['bi__caption'])
        v2 = models.ChapterCopy.objects.using('dbnovel').filter(novelid__lt=2)
        v3 = models.Bussiness.objects.all()
        return render(request,'novel/host.html',{"v1":data,"v2":v2,"v3":v3,'page_str': page_str})

    elif request.method=="POST":
        hostname = request.POST.get("hostname")
        ipname = request.POST.get("ipname")
        portname = request.POST.get("portname")
        bu_id = request.POST.get("bu_id")
        models.Host.objects.create(hostname=hostname , ip = ipname , port=portname, bi_id = bu_id)
        return redirect('/novel/host')

def ajax_test(request):
    ret_dic = {"status":True ,"error_msg":None, "data_return":None}
    try:
        hostname = request.POST.get("hostname")
        ipname = request.POST.get("ipname")
        portname = request.POST.get("portname")
        bu_id = request.POST.get("bu_id")
        if hostname and ipname and portname:
            models.Host.objects.create(hostname=hostname, ip=ipname, port=portname, bi_id=bu_id)
            return  HttpResponse("OK")
        else:
            ret_dic['status'] = False
            ret_dic['error_msg'] = '未知错误'
    except Exception as e:
        ret_dic['status'] = False
        ret_dic['error_msg'] = "请求错误"
    # 利用json将字典转化为字符串
    finally:
        return HttpResponse(json.dumps(ret_dic))

