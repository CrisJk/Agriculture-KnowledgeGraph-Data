# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.views.decorators import csrf
import os
def tagging(request):
	context = {}
	#从测试集中选取一个句子和标签
	filePath = os.path.abspath(os.path.join(os.getcwd(),"../TrainDataBaseOnWiki"))
	#如果标签是对的，则将这个样本写到训练集文件中(已标注)
	#如果标签是错的，则填写一个正确的标签
	#如果不知道该如何标注，换一个
	return render(request,'taggingSentences.html',context)