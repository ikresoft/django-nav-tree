from django.utils import six
from django.forms import forms as newforms
from django.http import HttpResponse
from django.shortcuts import render
from django.core.urlresolvers import get_urlconf, get_resolver

from nav_tree import form_registry
from django.contrib.admin.templatetags.admin_static import static
from forms import BaseUrlForm

#load all urlnames

def form_view(request):
    apps = {}
    apps['Other'] = {}
    media = newforms.Media()

    known_url_names = []
    def _stack_known_urls(reverse_dict, ns=None):
        for url_name, url_rules in reverse_dict.items():
            if isinstance(url_name, six.string_types):
                if ns is not None:
                    url_name = '%s:%s' % (ns, url_name)
                known_url_names.append(url_name)

    #urls
    resolver = get_resolver(get_urlconf())
    for ns, (url_prefix, ns_resolver) in resolver.namespace_dict.items():
        if ns != 'admin':
            _stack_known_urls(ns_resolver.reverse_dict, ns)
    _stack_known_urls(resolver.reverse_dict)

    if request.method == 'POST':
        for app, forms in form_registry.get_apps().items():
            apps[app] = {}
            for url_name, form in forms.items():
                apps[app][request.POST.get('url_name')] = form(url_name, request.POST)
                if apps[app][request.POST.get('url_name')].is_valid():
                    if request.is_ajax():
                        return HttpResponse(apps[app][request.POST.get('url_name')].submit(), content_type="text/plain")
    else:
        for app, forms in form_registry.get_apps().items():
            apps[app] = {}
            for url_name, form in forms.items():
                known_url_names.remove(url_name)
                apps[app][url_name] = form(url_name)
                media += apps[app][url_name].media
        for url in known_url_names:
            apps['Other'][url] = None
    context = {
        'apps': apps,
        'is_popup': request.GET.get('_popup', '') != '',
        'media': media,
    }
    return render(request, "nav_tree/app_list.html", context)