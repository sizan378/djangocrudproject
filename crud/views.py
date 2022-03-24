from django.shortcuts import render, HttpResponseRedirect
from .models import Contact
from .forms import stockmarketForm


def show_data(request):
    data = Contact.objects.all()
    return render(request,'index.html',{'data':data})

def update_data(request, id):
    if request.method == 'POST':
        pi = Contact.objects.get(pk=id)
        fm = stockmarketForm(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
        return HttpResponseRedirect('/')
    else:
        pi = Contact.objects.get(pk=id)
        fm = stockmarketForm(instance=pi)
    return render(request, 'update.html', {'forms':fm})

def delete_data(request,id):
    if request.method == 'POST':
        data = Contact.objects.get(pk=id)
        data.delete()
        return HttpResponseRedirect('/')