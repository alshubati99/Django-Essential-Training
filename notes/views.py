from typing import Any
from django.db.models.query import QuerySet
from django.forms.models import BaseModelForm
from django.shortcuts import render
from django.http import Http404, HttpResponse
from .models import Notes
from django.views.generic import CreateView, DetailView, ListView, UpdateView

from .forms import NotesForm
from django.views.generic.edit import DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect

# Create your views here.
class NotesListView(LoginRequiredMixin, ListView):
   model = Notes
   context_object_name = "notes"
   template_name="notes/notes_list.html"
   login_url = "/admin"

   # Override the get queryset method 
   def get_queryset(self):
      return self.request.user.notes.all()
   
      

class NotesDetialView(DetailView):
   model = Notes
   context_object_name = "notes"

# def list(request):
#     all_notes = Notes.objects.all()
#     return render(request, 'notes/notes_list.html',{'notes': all_notes})

# def detail(request, pk):
#     try:
#      note = Notes.objects.get(pk=pk)
#     except Notes.DoesNotExist:
#        raise Http404("Note doesn't exist")
       
#     return render(request, 'notes/notes_detail.html',{'note': note})

class NotesCreateView(CreateView):
   model= Notes
   form_class = NotesForm
   success_url= '/smart/notes'
   def form_valid(self, form):
      self.object = form.save(commit=False)
      self.object.user = self.request.user
      self.object.save()
      return HttpResponseRedirect(self.get_success_url())
   

class NotesUpdateView(UpdateView):
    model= Notes
    success_url= '/smart/notes'
    form_class = NotesForm

class NotesDeleteView(DeleteView):
   model = Notes
   success_url = '/smart/notes'
   template_name = 'notes/notes_delete.html'
   