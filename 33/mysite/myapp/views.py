from django.shortcuts import render
from django.http import HttpResponse


# def first(request, number):
#     return HttpResponse("It's {}".format(number))

def main_page(request):
    return HttpResponse('Main page')

def number_id(request, number):
    return HttpResponse("It's product {}".format(number))

def create_product(request, number, act):
    if act=='create':
        return HttpResponse("It's product creation for {} product".format(number))
    elif act=='delete':
        return HttpResponse("It's product deleting for {} product".format(number))
    elif act=='info':
        return HttpResponse("It's product information for {} product".format(number))
    else:
        return HttpResponse("It's product slug {}".format(number))

# def slug_name_product(request, number, sl):
#     return HttpResponse("It's product slug-name for {} product".format(number))

