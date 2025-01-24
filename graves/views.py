from django.shortcuts import render, redirect
from .models import Graves, News, Page, Memorials
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

ALF = ['А', 'Б', 'В', 'Г', 'Д', 'Ж', 'З', 'Е', 'Ё', 'И', 'Й', 'К', 'Л', 'М', 'Н', 'О', 'П',
       'Р', 'С', 'Т', 'У', 'Ф', 'Х', 'Ц', 'Ч', 'Ш', 'Щ', 'Э', 'Ю', 'Я']


# Pages
def index(request):
    args = dict()
    args['news'] = News.objects.all()[::-1][:3]
    args['page'] = Page.objects.get(name='Главная')
    return render(request=request, template_name='page.html', context=args)


def contacts(request):
    return render(request=request, template_name='contacts.html')


def about(request):
    return render(request=request, template_name='about.html')


def donate(request):
    return render(request=request, template_name='donate.html')


def partners(request):
    return render(request=request, template_name='partners.html')


def gallery(request):
    return render(request=request, template_name='gallery.html')


# Graves
def graves_list(request, cem_id, letter=None):
    args = dict()
    args['cid'] = cem_id
    args['alf'] = ALF

    if letter is None:
        args['graves'] = []
    else:
        graves = Graves.objects.filter(cemetery=cem_id, name__istartswith=letter).order_by('name')
        paginator = Paginator(object_list=graves, per_page=20)

        try:
            page = request.GET['page']
        except:
            page = 1

        # page = request.GET['page']

        try:
            args['graves'] = paginator.page(page)
        except PageNotAnInteger:
            args['graves'] = paginator.page(1)
        except EmptyPage:
            args['graves'] = paginator.page(paginator.num_pages)

        args['page'] = int(page)
        args['num'] = [x for x in range(1, paginator.num_pages + 1)]
    return render(request=request, template_name='graves_list.html', context=args)


def graves_detail(request, grave_id):
    args = dict()
    args['alf'] = ALF
    args['grave'] = Graves.objects.get(id=grave_id)
    args['have_photo'] = True
    try:
        line = Graves.objects.get(id=grave_id).big_photo.readline()
    except:
        args['have_photo'] = False
    return render(request=request, template_name='graves_detail.html', context=args)


def graves_search(request):
    if request.method == 'POST':
        search = request.POST['search']
        args = dict()
        args['results'] = Graves.objects.filter(name__icontains=search)
        args['search'] = search
        return render(request=request, template_name='search.html', context=args)
    else:
        return redirect('/')


# News
def news_list(request):
    args = dict()
    news = News.objects.all().order_by('-date')

    paginator = Paginator(object_list=news, per_page=5)

    try:
        page = request.GET['page']
    except:
        page = 1

    try:
        args['news'] = paginator.page(page)
    except PageNotAnInteger:
        args['news'] = paginator.page(1)
    except EmptyPage:
        args['news'] = paginator.page(paginator.num_pages)
    return render(request=request, template_name='news.html', context=args)


def news_detail(request, news_id):
    args = dict()
    args['news'] = News.objects.get(id=news_id)
    return render(request=request, template_name='news_detail.html', context=args)


def display_page(request, title):
    args = dict()
    try:
        args['page'] = Page.objects.get(name=title)
    except:
        args['page'] = None
    return render(request=request, template_name='page.html', context=args)


def memorials_list(request, start, end):
    args = dict()
    if int(end) == 0:
        end = Memorials.objects.count()
    args['memorials'] = Memorials.objects.all().order_by('number')[int(start):int(end)]
    return render(request=request, template_name='memorial_list.html', context=args)
