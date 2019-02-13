from django.test import TestCase

# Create your tests here.


from django.db import models
import datetime
from django.urls import reverse

from django.db import models


from ckeditor.fields import RichTextField



# Create your models here.

class Post(models.Model):
    text = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.text


class Letter(models.Model):
    alpha = models.CharField(max_length=200, default='')
    alpha.alphabetic_filter = True

    def __str__(self):
        return self.alpha



class Word(models.Model):
    letter = models.ForeignKey(Letter, on_delete=models.CASCADE, default='', related_name='connect')
    word = models.CharField(max_length=200, default='')
    word_exp = models.TextField()

    def __str__(self):
        return self.word

class About(models.Model):
    title_a = models.CharField(max_length=100)
    content_a = models.TextField()
    title_a = RichTextField()
    content_a  =RichTextField()

    def __str__(self):
        return self.title_a

class Services(models.Model):
    title_s = models.CharField(max_length=100)
    content_s = models.TextField()

    def __str__(self):
        return self.title_s


class Learn(models.Model):
    title_l = models.CharField(max_length=100)
    content_l = models.TextField()
    content_l = RichTextField()

    def __str__(self):
        return self.title_l


class Model(models.Model):
    title = models.CharField(max_length=200)
    def __str__(self):
        return self.title

class Yuklemeler(models.Model):
    upload = models.FileField(verbose_name="PDF yuklemeler", upload_to='uploads/%Y/%m/%d/', blank=True)
    namefile = models.CharField(max_length=400, blank=True, verbose_name="Yuklenen file adi.")

    def __str__(self):
        return self.namefile

class Statistics(models.Model):
    upload = models.ForeignKey(Yuklemeler, on_delete=models.CASCADE, verbose_name="PDF yuklemeler", blank=True)
    title = models.CharField(max_length=200)
    content = models.TextField()
    content = RichTextField()
    slug = models.SlugField()



    def __str__(self):
        return self.title







___
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



def statistics_view(request):
    title = Statistics.objects.all()
    title_l = Model.objects.values()
    context = {'title': title, 'title_l': title_l}
    return render(request, 'polls/statistics.html', context)



def research(request):
    statistics = Statistics.objects.all()
    upload = Yuklemeler.objects.all()
    context = {
        'statistics': statistics,
        'upload': upload,
    }
    return render(request, 'polls/researches.html', context)



def contact(request):
    title = 'Məktub göndər'
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
        title = 'Təşəkkür edirik'
        confirm_message = 'Bizimlə əlaqə saxladığınız üçün təşəkkür edirik.'
        form = None

    context = {'title': title, 'form': form, 'confirm_message': confirm_message}
    return render(request, 'polls/contact.html', context)

