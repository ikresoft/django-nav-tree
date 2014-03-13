# Suppose you have `myapp` application.
# In its `models.py` you define your customized models.
from django.db import models
from sitetree.models import TreeItemBase, TreeBase


class MenuTreeItem(TreeItemBase):
    css_class = models.CharField('Tree item CSS class', max_length=100, null=True, blank=True)
    template = models.CharField(max_length=100, null=True, blank=True)
    activity_class = models.CharField(max_length=50, null=True, blank=True)
