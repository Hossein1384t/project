from django.shortcuts import render
from django.template.context_processors import request



# Create your views here.
def cart_summary(request):
    return render(request, "cart_summary.html", {})

def cart_add(request):
    pass

def cart_delete(request):
    pass

def cart_update(request):
    pass
