#coding=utf-8
from django.views.generic import TemplateView
from django.shortcuts import redirect
from django.shortcuts import render

class Login(TemplateView):

    def get(self, request):
        return render(request, "index.html")

    def post(self, request):
        return render(request, "index.html")