from dataclasses import fields
from django.shortcuts import render
from django.views.generic import (View, TemplateView, ListView, DetailView,
                                    CreateView, UpdateView, DeleteView)
from django.http import HttpResponse
from . import models

# Create your views here.

# def index(request):
#     return render(request, '../templates/basic_app/index.html')

# class CBView(TemplateView):
    # def get(self, request):
    #     return HttpResponse("Class Based Views ARE COOL")
# class IndexView(TemplateView):
#     template_name = 'index.html'

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['inject_me'] = "A basic display of how to return a context in CBV using TemplateView."
#         return context

class IndexView(TemplateView):
    '''Connects a template to this Class-Base-View'''
    template_name = 'index.html'
    
    def get_context_data(self, **kwargs):
        '''Creates and return a context in a Class-Based-View'''
        context = super().get_context_data(**kwargs)
        context['school_list'] = ''
        return context


class SchoolListView(ListView):
    '''Renders the list of schools created in the School Model'''
    context_object_name = 'schools'
    model = models.School
    template_name = 'basic_app/school_list.html'

class SchoolDetailView(DetailView):
    '''Renders the details of each school created in the School Model'''
    context_object_name = 'school_detail'
    model = models.School
    template_name = 'basic_app/school_details.html'

class SchoolCreateView(CreateView):
    '''Create an new instance of school from the School Model in models.py'''
    fields = ('name', 'principal', 'location')
    model = models.School

class SchoolUpdateView(UpdateView):
    '''Updates the specified fields'''
    fields = ('name', 'principal')
    model = models.School