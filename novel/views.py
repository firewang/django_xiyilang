from django.shortcuts import render

# Create your views here.
from django.shortcuts import HttpResponse,render
from django.template import loader
from . import models


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
    v1 = models.Host.objects.filter(nid__gt=0)
    # v1 = models.Host.objects.filter(nid__gt=0).values('ip','port','bi__caption')
    # print(v1)
    for row in v1:
        print(row.nid,row.hostname,row.ip,row.port,row.bi_id,row.bi.caption)
        # print(row['ip'],row['port'],row['bi__caption'])
    v2 = models.ChapterCopy.objects.using('dbnovel').filter(novelid__lt=2)
    return render(request,'novel/host.html',{"v1":v1,"v2":v2})
