# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.views.decorators import csrf
import os
def tagging(request):
	context = {}
	#filePath = os.path.getcwd();
	return render(request,'taggingSentences.html',context)