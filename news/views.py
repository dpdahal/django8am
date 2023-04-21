from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.http import JsonResponse

from .models import *
from django.http import HttpResponse
from django.core.mail import send_mail
from django.contrib import messages
from rest_framework import viewsets
from .serializers import NewsSerializer
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
import requests


class NewsViewSet(viewsets.ModelViewSet):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = News.objects.all()
    serializer_class = NewsSerializer


# Create your views here.

def news_api(request):
    url = "https://newsapi.org/v2/everything?q=tesla&from=2023-03-21&sortBy=publishedAt&apiKey=ca3206dc1298409fb3560250bcce05d1"
    response = requests.get(url)
    data = response.json()
    data = data['articles']
    send_data={
        'newsData':data
    }
    return render(request, 'pages/news/api.html', send_data)


def index(request):
    data = {

        'categoryData': Category.objects.all(),
    }
    return render(request, 'pages/home/index.html', data)


def news(request):
    if request.method == 'POST':
        search = request.POST['search']
        find_data = News.objects.filter(title__icontains=search) | News.objects.filter(
            category__name__icontains=search)
        paginator = Paginator(find_data, 3)
        page = request.GET.get('page')
        find_data = paginator.get_page(page)
        data = {
            'newsData': find_data,
            'title': 'Search Result'
        }
        return render(request, 'pages/news/news.html', data)
    else:
        news_data = News.objects.all()
        paginator = Paginator(news_data, 3)
        page = request.GET.get('page')
        news_data = paginator.get_page(page)
        data = {
            'newsData': news_data,
            'title': 'All News'
        }
        return render(request, 'pages/news/news.html', data)


def contact(request):
    if request.method == 'POST':
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']
        send_mail("Subject: " + subject, message,
                  email, ['online2020programming@gmail.com'],
                  fail_silently=False)
        messages.success(request, 'Your message has been sent successfully')
        back = request.META.get('HTTP_REFERER')
        return redirect(back)
    else:
        return render(request, 'pages/contact/contact.html')


def news_details(request, slug):
    newsData = News.objects.get(slug=slug)
    category = newsData.category.id
    related_news = News.objects.filter(category=category).exclude(id=newsData.id)
    data = {
        'newsData': News.objects.get(slug=slug),
        'related_news': related_news,
    }
    return render(request, 'pages/news/news-details.html', data)


def category_news(request, slug):
    data = {
        'catData': Category.objects.get(slug=slug),
    }
    return render(request, 'pages/news/category-news.html', data)


def page(request, slug):
    data = {
        'pageContent': Page.objects.get(slug=slug),
    }
    return render(request, 'pages/page/page.html', data)
