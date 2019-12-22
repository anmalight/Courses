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


class MyClass:
    string = ''

    def __init__(self, s):
        self.string = s


def index(request):
    my_num = 33
    month_list = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October',
                  'November', 'December']
    my_str = 'some string'
    my_dict = {"some_key": "some_value"}
    my_list = ['list_first_item', 'list_second_item', 'list_third_item']
    my_set = {'set_first_item', 'set_second_item', 'set_third_item'}
    my_tuple = ('tuple_first_item', 'tuple_second_item', 'tuple_third_item')
    my_class = MyClass('class string')
    return render(request, 'index.html', {
        'my_num': my_num,
        'my_str': my_str,
        'my_dict': my_dict,
        'my_list': my_list,
        'month_list': month_list,
        'my_set': my_set,
        'my_tuple': my_tuple,
        'my_class': my_class,
        'display_num': True,
    })

def index1(request):
    str_str = "kdsjfh"
    num_list = [2, 43, 55, 67]
    return render(request, 'index1.html', {
        "str_str": str_str,
        'num_list': num_list
    })

    return render(request, 'index1.html')
# def slug_name_product(request, number, sl):
#     return HttpResponse("It's product slug-name for {} product".format(number))

