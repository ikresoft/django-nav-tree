from modeltranslation.translator import translator, TranslationOptions
from sitetree.utils import get_tree_model, get_tree_item_model

class TreeItemTranslationOptions(TranslationOptions):
    fields = ('title', 'description')

translator.register(get_tree_item_model(), TreeItemTranslationOptions)
