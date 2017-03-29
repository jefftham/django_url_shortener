from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect, HttpRequest
from .models import Url_table
from .forms import *
from urllib.parse import urlparse


def get_domain(url):
    parsed_uri = urlparse(url)
    domain = '{uri.scheme}://{uri.netloc}/'.format(uri=parsed_uri)
    return domain


# Create your views here.


def index(request):
    template = 'url_app/index.html'
    prefix_server = request.scheme+"://"+request.get_host()+"/"
    context = {'prefix_server': prefix_server}
    form = UrlForm(request.POST or None, initial={'full': '', 'short': ''})

    if request.method == 'POST':
        if form.is_valid():
            cd = form.cleaned_data
            if form.has_changed():
                # print("The following fields changed: %s" % ", ".join(form.changed_data))
                if 'short' in form.changed_data:
                    qs = Url_table.objects.filter(full__iexact=cd['full'])
                    if not qs.exists():
                        # if both full url and short url changed
                        print("create both short and full")
                        data, status = Url_table.objects.get_or_create(full=cd['full'], short=cd['short'])
                    else:
                        # update the short url
                        print("update short only")
                        data = get_object_or_404(Url_table, full=cd['full'])
                        data.short = cd['short']
                        data.save()
                else:
                    print("edit exiting url")
                    data, status = Url_table.objects.get_or_create(full=cd['full'])

            short = prefix_server + data.short
            context['short'] = short
            context["data"] = data
            form = UrlForm(initial={'full': cd['full'], 'short': data.short})
            context["form"] = form
        else:
            print("form is not valid")
            context["data"] = {'error': True}
            cd = form.cleaned_data
            context["form"] = form
    else:
        context["form"] = form
    # pull all shorten url
    urls = Url_table.objects.all()
    for url in urls:
        url.domain = get_domain(url.full)
    context['urls'] = urls
    return render(request, template, context)


def redirect(request, short=''):
    print(short)
    url = get_object_or_404(Url_table, short=short)
    url.count += 1
    url.save()
    return HttpResponseRedirect(url.full)


def display_meta(request):
    '''
        display all the html meta data that receive from http request
        (http headers)
    '''
    print(request)
    values = request.META.items()
    # values.sort()
    html = []
    for k, v in values:
        html.append('<tr><td>request.META.%s</td><td>%s</td></tr>' % (k, v))
    return HttpResponse('<table>%s</table>' % '\n'.join(html))