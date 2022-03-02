from django.shortcuts import render
from matplotlib.style import context

# Create your views here.

def about(request):
    context = {'about':'active'}
    return render(request, 'core/about.html', context)
def contact(request):
    context = {'contact':'active'}
    return render(request, 'core/contact.html', context)
