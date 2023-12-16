from django.shortcuts import render, redirect
from . import forms
from . import models
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView

from django.urls import reverse_lazy
from django.utils.decorators import method_decorator


@method_decorator(login_required, name='dispatch')
class add_album_view(CreateView):
    model = models.Album
    form_class = forms.AlbumForm
    template_name = 'add_album.html'
    success_url = reverse_lazy('add_album')
    
    def form_valid(self, form):
        form.instance.users = self.request.user
        return super().form_valid(form)



# class based edit post
@method_decorator(login_required, name='dispatch')
class edit_album_view(UpdateView):
    model = models.Album
    form_class = forms.AlbumForm
    template_name = 'add_album.html'
    # select primary key id
    pk_url_kwarg ='id'
    #  reverse_lazy work like redirect
    success_url = reverse_lazy('home')



# delete table record
@login_required   
def delete_album(request, id):
    record = models.Album.objects.get(pk=id)
    record.delete()
    return redirect('home')

# @method_decorator(login_required, name='dispatch')

# class delete_album(DeleteView):
#     model = models.Album
#     template_name = 'delete_album.html'
#     success_url = reverse_lazy("home")
#     pk_url_kwarg = 'id'