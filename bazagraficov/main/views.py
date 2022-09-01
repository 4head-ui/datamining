from django.shortcuts import render
from .data import connectx,connecty
from plotly.graph_objs import Bar,Layout,Line
from plotly import offline
from .models import admingrafic
import matplotlib.pyplot as plt


def index(request):
    return render(request,'main/base.html')


def faq(request):
    return render(request,'main/faq.html')


def grafic(request):
    x_value = connectx()
    y_value = connecty()
    data = [Bar(x=x_value,y=y_value)]
    x_axis_config = {'title': 'График икс','dtick':1}
    y_axis_config = {'title': 'График игрик'}
    my_l = Layout(title='График',xaxis=x_axis_config,yaxis=y_axis_config)
    info = offline.plot({'data':data,'layout':my_l},filename='graficbarbd.html')
    context={'info':info}
    return render(request,'main/grafic.html',context)


def graficline(request):
    x_value = connectx()
    y_value = connecty()
    data = [Line(x=x_value,y=y_value)]
    x_axis_config = {'title': 'График икс','dtick':1}
    y_axis_config = {'title': 'График игрик'}
    my_l = Layout(title='График',xaxis=x_axis_config,yaxis=y_axis_config)
    info = offline.plot({'data':data,'layout':my_l},filename='graficlinebd.html')
    context={'info':info}
    return render(request,'main/graficline.html',context)


def graficpltplot(request):
    x_value = connectx()
    y_value = connecty()
    fig, ax = plt.subplots()
    ax.plot(x_value, y_value, linewidth=3)
    plt.style.use('seaborn')
    # Назначение заголовка диаграммы и меток осей.
    ax.set_title("График matplotlib", fontsize=24)
    ax.set_xlabel("Ось x", fontsize=14)
    ax.set_ylabel("Ось игрик", fontsize=14)

    # Назначение размера шрифта делений на осях.
    ax.tick_params(axis='both', labelsize=14)
    info = plt.show()
    context = {'info':info}
    return render(request,'main/graficpltplot.html',context)


def graficpltscatter(request):
    x_value = connectx()
    y_value = connecty()
    fig, ax = plt.subplots()
    ax.scatter(x_value, y_value,s=50)
    plt.style.use('seaborn')
    # Назначение заголовка диаграммы и меток осей.
    ax.set_title("График matplotlib", fontsize=24)
    ax.set_xlabel("Ось x", fontsize=14)
    ax.set_ylabel("Ось игрик", fontsize=14)

    # Назначение размера шрифта делений на осях.
    ax.tick_params(axis='both', labelsize=14)
    info = plt.show()
    context = {'info': info}
    return render(request,'main/graficpltscatter.html',context)


def graficadmin(request):
    xcont=[]
    ycont=[]
    xelem=[]
    yelem=[]
    x_values = admingrafic.objects.all()
    for x in x_values:
        xcont.append((x.decimalx))
    y_values = admingrafic.objects.all()
    for y in y_values:
        ycont.append((y.decimaly))
    for elemx in xcont:
        v = elemx.split(' ')
        for d in v:
            dd = int(d)
            xelem.append(dd)
    for elemy in ycont:
        y = elemy.split(' ')
        for dd in y:
            ddd = int(dd)
            yelem.append(ddd)
    data = [Bar(x=xelem,y=yelem)]
    x_axis_config = {'title': 'График икс','dtick':1}
    y_axis_config = {'title': 'График игрик'}
    my_l = Layout(title='График',xaxis=x_axis_config,yaxis=y_axis_config)
    info = offline.plot({'data':data,'layout':my_l},filename='graficadminbar.html')
    context={'info':info}

    return render(request,'main/graficfromadmin.html',context)


def graficadminline(request):
    xcont=[]
    ycont=[]
    xelem=[]
    yelem=[]
    x_values = admingrafic.objects.all()
    for x in x_values:
        xcont.append((x.decimalx))
    y_values = admingrafic.objects.all()
    for y in y_values:
        ycont.append((y.decimaly))
    for elemx in xcont:
        v = elemx.split(' ')
        for d in v:
            dd = int(d)
            xelem.append(dd)
    for elemy in ycont:
        y = elemy.split(' ')
        for dd in y:
            ddd = int(dd)
            yelem.append(ddd)
    data = [Line(x=xelem,y=yelem)]
    x_axis_config = {'title': 'График икс','dtick':1}
    y_axis_config = {'title': 'График игрик'}
    my_l = Layout(title='График',xaxis=x_axis_config,yaxis=y_axis_config)
    info = offline.plot({'data':data,'layout':my_l},filename='graficadminline.html')
    context={'info':info}

    return render(request,'main/graficfromadminline.html',context)


def graficadminplot(request):
    xcont=[]
    ycont=[]
    xelem=[]
    yelem=[]
    x_values = admingrafic.objects.all()
    for x in x_values:
        xcont.append((x.decimalx))
    y_values = admingrafic.objects.all()
    for y in y_values:
        ycont.append((y.decimaly))
    for elemx in xcont:
        v = elemx.split(' ')
        for d in v:
            dd = int(d)
            xelem.append(dd)
    for elemy in ycont:
        y = elemy.split(' ')
        for dd in y:
            ddd = int(dd)
            yelem.append(ddd)
    fig, ax = plt.subplots()
    ax.plot(xelem,yelem, linewidth=3)
    plt.style.use('seaborn')
    # Назначение заголовка диаграммы и меток осей.
    ax.set_title("График matplotlib", fontsize=24)
    ax.set_xlabel("Ось x", fontsize=14)
    ax.set_ylabel("Ось игрик", fontsize=14)

    # Назначение размера шрифта делений на осях.
    ax.tick_params(axis='both', labelsize=14)
    info = plt.show()
    context = {'info':info}
    return render(request,'main/graficadminplot.html',context)


def graficadminscatter(request):
    xcont=[]
    ycont=[]
    xelem=[]
    yelem=[]
    x_values = admingrafic.objects.all()
    for x in x_values:
        xcont.append((x.decimalx))
    y_values = admingrafic.objects.all()
    for y in y_values:
        ycont.append((y.decimaly))
    for elemx in xcont:
        v = elemx.split(' ')
        for d in v:
            dd = int(d)
            xelem.append(dd)
    for elemy in ycont:
        y = elemy.split(' ')
        for dd in y:
            ddd = int(dd)
            yelem.append(ddd)
    fig, ax = plt.subplots()
    ax.scatter(xelem,yelem, s=50)
    plt.style.use('seaborn')
    # Назначение заголовка диаграммы и меток осей.
    ax.set_title("График matplotlib", fontsize=24)
    ax.set_xlabel("Ось x", fontsize=14)
    ax.set_ylabel("Ось игрик", fontsize=14)

    # Назначение размера шрифта делений на осях.
    ax.tick_params(axis='both', labelsize=14)
    info = plt.show()
    context = {'info':info}
    return render(request,'main/graficadminscatter.html',context)





