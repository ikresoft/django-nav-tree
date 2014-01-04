from django.core.urlresolvers import get_urlconf, get_resolver

class FormRegistry(object):

    def __init__(self):
        self.registry = {}

    def register(self, url_name, form_class, app_label=None):
        if app_label is None:
            if not hasattr(form_class.Meta, 'app_label'):
                app_label = form_class.__module__.split('.')[0]
            else:
                app_label = getattr(form_class.Meta, 'app_label')
        if not hasattr(self.registry, app_label):
            self.registry[app_label] = {}
        
        self.registry[app_label][url_name] = form_class

    def get_apps(self):
        return self.registry

form_registry = FormRegistry()