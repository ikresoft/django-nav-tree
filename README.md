django-nav-tree
===============

Django Navigation App (helper for django-sitetree)

Small app for better selection url names in tree item admin. App support autodiscover to load forms for constructing url names.

Installation

Put nav_tree before sitetree in INSTALLED_APPS, in urls.py put 

from nav_tree import utils as nav_utils
nav_utils.autodiscover()

urlpatterns = patterns('',
	url(r'^nav-tree/', include('nav_tree.urls')),
)

Sample form:
```
from categories.models import Category
from nav_tree import form_registry
from nav_tree.forms import BaseUrlForm


class ArticleCategoryIndexForm(BaseUrlForm):
    category = models.ModelChoiceField(queryset=Category.objects.all())

    def path(self):
        ancestors = list(self.cleaned_data['category'].get_ancestors()) + [self.cleaned_data['category'], ]
        return '/'.join([force_unicode(i.slug) for i in ancestors]) + '/'

    def submit(self):
        url = "%s %s" % (self.Meta.url_name, self.path())
        return url

    class Meta:
        verbose_name = 'List by category'
        url_name = 'article_archive_index'

form_registry.register('article_archive_index', ArticleCategoryIndexForm)
```
