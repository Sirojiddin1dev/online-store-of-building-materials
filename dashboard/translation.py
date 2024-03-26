from modeltranslation.translator import register, TranslationOptions, translator
from .models import *


@register(Products)
class ProductsTranslationOptions(TranslationOptions):
    fields = ('title', 'product_info', 'advert_text', )











