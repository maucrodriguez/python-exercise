from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
from .forms import SevenPairsForm

def find_pairs(number_list, total):
    result = []
    partials = {}

    for n in number_list:
        element = total - n
        if element in partials:
            result.append((n, element))
        partials[n] = n
    return result

def seven_pairs(request):
    pairs = None
    if request.method == 'POST':
        form = SevenPairsForm(request.POST)
        if form.is_valid():
            values = form.cleaned_data['values']
            pairs = find_pairs(values, 7)
    else:
        form = SevenPairsForm()

    return render(request, 'seven/seven.html', {'form': form, 'pairs': pairs})