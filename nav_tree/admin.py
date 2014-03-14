from sitetree.admin import TreeItemAdmin, override_item_admin
from django.forms import forms, models
from django.utils.translation import ugettext_lazy as _

from widgets import UrlWidget
from sitetree.forms import TreeItemForm

from django.conf import settings

if 'modeltranslation' in settings.INSTALLED_APPS:
    from modeltranslation.admin import TranslationAdmin, TabbedTranslationAdmin, TranslationTabularInline
    class AdvTreeItemAdmin(TreeItemAdmin, TabbedTranslationAdmin):
        pass
else:
    class AdvTreeItemAdmin(TreeItemAdmin):
        pass

class TreeItemForm(models.ModelForm):
    class Meta:
        widgets = {
            'url': UrlWidget(attrs={'style': 'width:205px'}),
        }

# And our custom tree item admin model.
class CustomTreeItemAdmin(AdvTreeItemAdmin):
    form = TreeItemForm

    fieldsets = (
        (_('Basic settings'), {
            'fields': ('parent', 'title', 'url',)
        }),
        (_('Custom settings'), {
            'classes': ('collapse',),
            'fields': ('css_class', 'template', 'activity_class',)
        }),
        (_('Access settings'), {
            'classes': ('collapse',),
            'fields': ('access_loggedin', 'access_guest', 'access_restricted', 'access_permissions', 'access_perm_type')
        }),
        (_('Display settings'), {
            'classes': ('collapse',),
            'fields': ('hidden', 'inmenu', 'inbreadcrumbs', 'insitetree')
        }),
        (_('Additional settings'), {
            'classes': ('collapse',),
            'fields': ('hint', 'description', 'alias', 'urlaspattern')
        }),
    )

    def formfield_for_dbfield(self, db_field, **kwargs):
        field = super(CustomTreeItemAdmin, self).formfield_for_dbfield(db_field, **kwargs)
        if 'modeltranslation' in settings.INSTALLED_APPS:
            self.patch_translation_field(db_field, field, **kwargs)
        return field


override_item_admin(CustomTreeItemAdmin)
