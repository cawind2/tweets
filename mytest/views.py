from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View


class Index(View):
    def get(self, request):
        return HttpResponse('I am called from a get Request')

    def post(self,):
        return HttpResponse('I am called from a post request')


# Create your views here.
