from django.shortcuts import render
from . import models
from django.core import serializers
from .serializers import ItemsSerializer
from  django.http import JsonResponse
from rest_framework import viewsets
from rest_framework.decorators import api_view


def Homepage(request):
    return render(request,'index.html',{})

# Convert to JSON
def convert_to_dict(item):
    d = {}
    d['name'] = item.name
    d['category'] = item.category
    d['sub_category'] = item.sub_category
    d['amount'] = item.amount
    return d

# return all items
@api_view(['GET','POST','PUT'])
def Get_All(request):
    # For all get request

    if request.method == 'GET':
        category = request.GET.get('category')
        sub_cat = request.GET.get('sub_category')
        name = request.GET.get('name')
        q = models.Item.objects.all()

        # Filter the search according to number parameters
        if name:
            q = q.filter(name=name)
        if category:
            q = q.filter(category = category)
        if sub_cat:
            q = q.filter(sub_category = sub_cat)

        # Convert the django queryset to JSON
        queryset = []
        for i in q:
            queryset.append(convert_to_dict(i))
        return JsonResponse(queryset,safe=False)

    # For all Post requests

    elif request.method == 'POST':
        try:
            new_item = models.Item(
                name = request.POST['name'],
                category = request.POST['category'],
                sub_category = request.POST['sub_category'],
                amount = request.POST['amount']
            )
            new_item.save()
            return JsonResponse({'Status':'Success',
                                 'Body':{'name':new_item.name,
                                         'category':new_item.category,
                                         'sub_category':new_item.sub_category,
                                         'amount':new_item.amount}},safe=False)
        except Exception as e:
            return JsonResponse({'Status':'Error',
                                 'Body':str(e)},safe=False)

    # For all update requests
    elif request.method == 'PUT':
        try:
            item = models.Item.objects.get(name = request.POST['name'])
            if request.POST.get('new_name'):
                item.name = request.POST['new_name']
            if request.POST.get('new_category'):
                item.category = request.POST['new_category']
            if request.POST.get('new_sub_category'):
                item.sub_category = request.POST['new_sub_category']
            if request.POST.get('new_amount'):
                item.amount = request.POST['new_amount']
            item.save()
            return JsonResponse({'Status':'Success',
                                 'Body':{'name':item.name,
                                         'category':item.category,
                                         'sub_category':item.sub_category,
                                         'amount':item.amount}},safe=False)
        except Exception as e:
            return JsonResponse({'Status':'Error',
                                 'Body':str(e)},safe=False)








