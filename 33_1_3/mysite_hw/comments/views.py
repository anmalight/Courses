from django.shortcuts import render
from django.http import HttpResponse


def static_comments_new(request):
    return HttpResponse("It's comments creation")


def static_comments_edit(request):
    return HttpResponse("It's comments editing")


def static_comments_etc(request):
    return HttpResponse("It's comments additional actions")


def dynamic_number_id(request, number):
    return HttpResponse("It's comment number {}".format(number))


def dynamic_del_ed(request, number, act):
    if act == 'add':
        return HttpResponse("It's comment number {} editing".format(number))
    elif act == 'delete':
        return HttpResponse("It's comment number {} deleting".format(number))
    else:
        return HttpResponse('Sorry. Page does not exists')


def checking_smth1(request):
    return HttpResponse('2 numbers and 3 letters')


def checking_smth2(request):
    return HttpResponse('number-letter-number')


def checking_smth3(request, phone_number):
    return HttpResponse('Number in format xxx-xxx-xx-xx: {}'.format(phone_number))

