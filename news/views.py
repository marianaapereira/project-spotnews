from django.shortcuts import render, get_object_or_404
from .models import News

# Create your views here.


def home_page(request):
    news_list = News.objects.all()

    return render(request, 'home.html', {
        'news_list': news_list
    })


def news_details_page(request, id):
    news = get_object_or_404(News, id=id)

    return render(request, 'news_details.html', {
        'news': news
    })
