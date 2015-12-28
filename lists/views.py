# coding=utf8

from django.http import HttpResponse
from django.shortcuts import render, redirect

from lists.models import Item


def home_page(request):
	if request.method == "POST":
		Item.objects.create(text=request.POST['item_text'])
		return redirect('/lists/the-only-list-in-the-world/')
	return render(request, 'home.html')


def view_list(request):
	return render(request, 'list.html', dict(items=Item.objects.all()))
