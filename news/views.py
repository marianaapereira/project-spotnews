from django.shortcuts import render, get_object_or_404, redirect
from .models import News, CategoryForm, NewsForm, Category, User
from rest_framework import viewsets
from .serializers import CategorySerializer


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


def categories_form_page(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('home-page')

    else:
        form = CategoryForm()

    return render(request, 'categories_form.html', {
        'form': form
    })


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


def news_form_page(request):
    categories_list = Category.objects.all()
    users_list = User.objects.all()

    if request.method == 'POST':
        form = NewsForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()

            return redirect('home-page')

    else:
        form = NewsForm()

    return render(request, 'news_form.html', {
        'form': form,
        'categories': categories_list,
        'authors': users_list
    })
