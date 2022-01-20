# Author: Zhi Kai
# Time:  14:55
from django.shortcuts import render

# def runoob(request):
#     context  ={}
#     context['hello'] = 'hello world'
#     return render(request,'runoob.html',context)
#filesizeformat 以更易读 的方式显示文件的大小
# data 根据给定格式对一个日期变量进行格式化 {{ time|date:"Y-m-d" }}





def runoob(request):
    views_list=["菜鸟教程1","菜鸟教程2","菜鸟教程3","李心怡"]
    return  render(request,"runoob.html",{"views_list":views_list})