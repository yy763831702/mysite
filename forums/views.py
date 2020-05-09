from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Forum, Category, SubCategory
from django.http import Http404
# Create your views here.

def index(request):
    latest_forum_list = Forum.objects.order_by('created_at')[:5]
    template = loader.get_template('forums/index.html')

    return render(request, 'forums/index.html', {"categories": Category.objects.all})

def single_slug(request, single_slug):
    categories = [c.slug for c in Category.objects.all()]

    if single_slug in categories:
        matching_sub = SubCategory.objects.filter(category__slug=single_slug)
        return render(request, 'forums/category.html', context = {"subcategories": matching_sub})

    return HttpResponse("'{single_slug}' does not correspond to anything we know of!")

def detail(request, forum_id):
    try:
        forum = Forum.objects.get(pk = forum_id)

    except Forum.DoesNotExist:
        raise Http404("Forum does not exist")

    return render(request, 'forums/detail.html', {'forum': forum})

def results(request, forum_id):
    return HttpResponse("you are looking at response s%" % forum_id)
