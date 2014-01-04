from django.forms import forms, widgets, fields
from django.contrib.admin.templatetags.admin_static import static

class BaseUrlForm(forms.Form):
	url_name = fields.CharField(widget=widgets.HiddenInput())

	def __init__(self, url_name, *args, **kwargs):
		super(BaseUrlForm, self).__init__(*args, **kwargs)
		self.url_name = url_name
		self.fields["url_name"].initial = self.url_name

	def submit(self):
		pass

	def get_url_name(self):
		return self.url_name

	class Media:
		js = (static('admin/js/%s' % 'admin/RelatedObjectLookups.js'),)

	class Meta:
		verbose_name = 'BaseUrlForm'