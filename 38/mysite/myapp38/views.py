from datetime import timedelta

from django.shortcuts import render, redirect
from myapp38.models import Animal, Visit
from django.utils import timezone

from .forms import AddAnimalForm
from django.views.generic import FormView

# Create your views here.


def first_page(request):
    return render(request, 'first.html')


def second_page(request):
    return render(request, 'second.html')


def third_page(request):
    return render(request, 'third.html')


def fourth_page(request):
    return render(request, 'fourth.html')


def animal_list(request):
    animals = Animal.objects.filter(added_at__lte=timezone.now()).order_by('added_at')
    return render(request, 'animal_list.html', {'animals': animals})


def animal_id(request, animal_id):
    end_time = timezone.now()
    start_time = timezone.now() - timedelta(minutes=20)
    # Entry.objects.filter(pub_date__range=(start_date, end_date))

    one_animal = Animal.objects.get(id=animal_id)
    view_animal = Visit.objects.filter(animal__id=animal_id).order_by('-time').filter(time__range=(start_time, end_time )).count()
    return render(request, 'one_animal.html', {'one_animal': one_animal, 'view_animal': view_animal})


def animal_new(request):
    if request.method == "POST":
        form = AddAnimalForm(request.POST)
        if form.is_valid():
            animal = form.save()
            animal.save()
            return redirect('myapp38/animal/', pk=animal.pk)
    else:
        form = AddAnimalForm()
    return render(request, 'add_animal.html', {'form': form})