# coding=utf8

from django.http import HttpResponse
from django.shortcuts import render


def home_page(request):
	return render(request, 'home.html', dict(new_item_text=request.POST.get('item_text', '')))
