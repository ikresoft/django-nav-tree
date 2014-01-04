from sitetree.admin import TreeItemAdmin, override_item_admin
from django.forms import forms, models

from widgets import UrlWidget
from sitetree.forms import TreeItemForm

class TreeItemForm(models.ModelForm):
	class Meta:
		widgets = {
			'url': UrlWidget(attrs={'style': 'width:205px'}),
		}

# And our custom tree item admin model.
class CustomTreeItemAdmin(TreeItemAdmin):
	form = TreeItemForm
    

override_item_admin(CustomTreeItemAdmin)