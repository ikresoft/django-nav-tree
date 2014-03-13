from django.template import Token
from tastypie import fields
from tastypie.resources import ModelResource, ALL, ALL_WITH_RELATIONS
from sitetree.utils import get_tree_model, get_tree_item_model

class MenuItemResource(ModelResource):
    items = fields.ToManyField('self', attribute='menutreeitem_parent', full=True, readonly=True)
    class Meta:
        queryset = get_tree_item_model().objects.all()
        resource_name = 'sitetree/menuitem'
        allowed_methods = ['get']

    def dehydrate(self, bundle):
        var_array = []
        if bundle.obj.urlaspattern:
            token = Token("Text", bundle.obj.url)
            var_array = token.split_contents()
        bundle.data['var_array'] = var_array[1:]
        return bundle

class MenuResource(ModelResource):
    items = fields.ToManyField(MenuItemResource, attribute='menutreeitem_tree', full=True, readonly=True)

    class Meta:
        queryset = get_tree_model().objects.all()
        resource_name = 'sitetree/menu'
        allowed_methods = ['get']
