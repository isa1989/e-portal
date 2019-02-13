from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from django.http import HttpResponseRedirect, HttpResponse
from django.core.mail import send_mail
from .models import Post, Letter, Word, About, Services, Learn, Statistics, Model, Statistics, Yuklemeler
from django.core.mail import send_mail
from django.conf import settings
from django.utils.html import strip_tags
from .forms import ContactForm
# Create your views here.


def index(request):
    return render(request, 'polls/index.html')


def header(request):
    return render(request, 'polls/header.html')

def about(request):
    about_list = About.objects.all()
    return render(request, 'polls/about.html', context={'about_list': about_list})

def xidmet(request):
    #xidmet_list = Services.objects.all()
    xidmet_list = Services.objects.values()
    context = {'xidmet_list': xidmet_list}
    return render(request, 'polls/xidmet.html', context)

def contact(request):
    return render(request, 'polls/contact.html')

def dictionary(request):
    dict1 = Letter.objects.all()
    dict2 = Word.objects.all()
    word_l = Letter.objects.all()
    word_e = Word.objects.all()
    context = {'word_l': word_l, 'word_e': word_e}
    return render(request, 'polls/luget.html', context)

def learn(request):
    title = Learn.objects.values()
    #title_c = Learn.objects.values('content_l')
    context = {'title': title}
    return render(request, 'polls/oyren.html', context)

def index2(request):
    return render(request, 'polls/index2.html')





def index3(request):
    stat = Statistics.objects.all()
    upload = Yuklemeler.objects.all()
    context = {
        'stat': stat,
        'upload': upload,
        'home_page': "active",
        }
    return render(request, 'polls/researches.html', context)

def statistics_view(request, statistics_id):
    statistics = Statistics.objects.get(slug=statistics_id)
    uploads = Yuklemeler.objects.filter(statistics=statistics)
    context = {
      'statistics': statistics,
      'uploads': uploads,
      'stat_page': "active",
      }
    return render(request, 'polls/researches.html', context)



def contact(request):
    title = 'Send us'
    form = ContactForm(request.POST or None)
    confirm_message = None

    if form.is_valid():
        name = form.cleaned_data['name']
        comment = form.cleaned_data['comment']
        subject = 'Message'
        message = '%s %s' % (comment, name)
        emailFrom = form.cleaned_data['email']
        emailTo = [settings.EMAIL_HOST_USER]
        send_mail(subject, message, emailFrom, emailTo, fail_silently=True)
        title = 'Thank you'
        confirm_message = 'Thank you for contact us.'
        form = None

    context = {'title': title, 'form': form, 'confirm_message': confirm_message}
    return render(request, 'polls/contact.html', context)

