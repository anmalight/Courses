from django.http import HttpResponseRedirect
from django.shortcuts import render

from .forms import NameForm, LoginForm
from django.views.generic import FormView

from django.contrib.auth import authenticate, login
from django.contrib.auth import logout

from django.contrib.auth.decorators import login_required


# def index(request):
#     return render(request, 'index.html')

class MyFormView(FormView):
    template_name = 'index.html'
    http_method_names = ['get', 'post']
    form_class = NameForm
    success_url = '/'

    def form_valid(self, form):
        sex = form.cleaned_data['your_sex']
        age = form.cleaned_data['your_age']
        lvl = form.cleaned_data['your_eng_lvl']
        eng_m = ['B2', 'B1', 'C2', 'C1']
        eng_f = ['B1', 'C2', 'C1']
        if (sex == 'M' and int(age) >= 20 and lvl in eng_m) or (
                sex == 'F' and int(age) > 22 and lvl in eng_f):
            return HttpResponseRedirect('plus/')
        else:
            return HttpResponseRedirect('minus/')


def get_name(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:

            sex = form.cleaned_data['your_sex']
            age = form.cleaned_data['your_age']
            lvl = form.cleaned_data['your_eng_lvl']
            if (sex == 'M' and int(age) >= 20 and (lvl=='B2' or lvl=='C2' or lvl=='C1')) or (sex == 'F' and int(age) > 22and (lvl=='B2' or lvl=='C2' or lvl=='C1')):
                return HttpResponseRedirect('plus/')
            else:
                return HttpResponseRedirect('minus/')


    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()

    return render(request, 'index.html', {'form': form})


# @login_required
def my_view(request):

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
            # Redirect to a success page.
            # ...
        # else:
            # Return an 'invalid login' error message.
            # ...
            # print("The username and password were incorrect.")
    form = LoginForm()
    return render(request, 'login_test.html', {"form": form})


def logout_view(request):
    logout(request)
    # Redirect to a success page.

def good_name(request):
    return render(request, 'good_name.html')


def plus(request):
    return render(request, 'plus.html')

def minus(request):
    return render(request, 'minus.html')

def index(request):
    return render(request, 'home.html')

