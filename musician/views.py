from django.shortcuts import render, redirect
from . import forms
from .import models 
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required    
def add_musician(request):
    if request.method == 'POST':
        musician_form = forms.MusicianForm(request.POST)
        if musician_form.is_valid():
            musician_form.instance.users = request.user
            musician_form.save()
            return redirect('add_musician')
    else:
        musician_form = forms.MusicianForm()
    return render(request, 'add_musician.html', {'form': musician_form})



# edit musician
@login_required    
def edit_musician(request, id):
    data = models.Musician.objects.get(pk=id)
    musician_form = forms.MusicianForm(instance=data)
    if request.method == 'POST':
        musician_form = forms.MusicianForm(request.POST, instance=data)
        if musician_form.is_valid():
            musician_form.save()
            return redirect('home')

    return render(request, 'add_musician.html', {'form':musician_form})