from django.shortcuts import render, get_object_or_404, redirect
from .models import News, CategoryForm

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
