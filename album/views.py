from django.shortcuts import render, redirect
from . import forms
from . import models
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required   
def add_album(request):
    if request.method == 'POST':
        album_form = forms.AlbumForm(request.POST)
        if album_form.is_valid():
            album_form.save()
            return redirect('home')
    else:
        album_form = forms.AlbumForm()
    return render(request, 'add_album.html', {'form': album_form})

#  edit table record
@login_required   
def edit_album(request, id):
    data = models.Album.objects.get(pk=id)
    album_form = forms.AlbumForm(instance=data)
    if request.method == 'POST':
        album_form = forms.AlbumForm(request.POST, instance=data)
        if album_form.is_valid():
            album_form.save()
            return redirect('home')
    return render(request, 'add_album.html', {'form':album_form})


# delete table record
@login_required   
def delete_album(request, id):
    record = models.Album.objects.get(pk=id)
    record.delete()
    return redirect('home')