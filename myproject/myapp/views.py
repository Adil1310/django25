from django.shortcuts import render, redirect
from .forms import IceCreamForm

# Create your views here.

def add_icecream(request):
    if request.method == 'POST':
        form = IceCreamForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = IceCreamForm()

    return render(request, 'ice.html', {'form': form})

def success(request):
    return render(request, 'success.html')