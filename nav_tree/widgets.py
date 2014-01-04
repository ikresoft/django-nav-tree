from django.forms import forms
from django.core.urlresolvers import reverse
from django.contrib.admin.templatetags.admin_static import static
from django.utils.translation import ugettext as _
from django.utils.safestring import mark_safe

class UrlWidget(forms.TextInput):

    def __init__(self, attrs=None):
        super(UrlWidget, self).__init__(attrs)

    def render(self, name, value, attrs=None):
        if attrs is None:
            attrs = {}
        extra = []
    
        related_url = reverse('form_view')

        params = {'url': value}
        if params:
            url = '?' + '&amp;'.join('%s=%s' % (k, v) for k, v in params.items())
        else:
            url = ''
        if "class" not in attrs:
            attrs['class'] = 'vForeignKeyRawIdAdminField'  # The JavaScript code looks for this hook.
        # TODO: "lookup_id_" is hard-coded here. This should instead use
        # the correct API to determine the ID dynamically.
        extra.append('<a href="%s%s" class="related-lookup" id="lookup_id_%s" onclick="return showRelatedObjectLookupPopup(this);"> ' %
            (related_url, url, name))
        extra.append('<img src="%s" width="16" height="16" alt="%s" /></a>' %
            (static('admin/img/selector-search.gif'), _('Lookup')))
        output = [super(UrlWidget, self).render(name, value, attrs)] + extra
        return mark_safe(''.join(output))

