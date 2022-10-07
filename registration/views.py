from django.shortcuts import render, redirect

from .forms import *


def index(request):
    if request.method == 'POST':
        form = RegistForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = RegistForm()

    return render(request, 'registration/index.html', {'form': form, 'title': 'Регистрация на сайте'})
