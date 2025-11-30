from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from website.forms import   ContactForm, NewsletterForm
from django.contrib import messages


def home_view(request):
    return render(request, "website/index.html")


def contact_view(request):
    if request.method =='POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            ticket = form.save(commit=False)
            ticket.name = ticket.name.title()
            ticket.save()
            messages.success(request, "Your ticket submited Succsessfuly!")
        else:
            messages.error(request, "Your ticket didnt submit!")

    form = ContactForm()
    return render(request, "website/contact.html", {'form': form})

def newsletter_view(request):
    if request.method == 'POST':
        form = NewsletterForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        HttpResponse('not valid')


def about_view(request):
    return render(request, "website/about.html")


def test_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('done')
        else:
            return HttpResponse('not valid')

    form = ContactForm()
    return render(request, "test.html", {'form':form})
