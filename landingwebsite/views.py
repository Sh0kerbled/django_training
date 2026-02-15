from django.http import HttpResponse
from django.shortcuts import render

def first_page(request):
    text = '<h1>Hello World</h1>'
    a = "textextextext"
    return render(request, "./index.html", {
        "a": a,
        "text": text
    })

def second_page(request):
    return render(request, "./link.html", {
        "<h1>nigga</h1>"
    })