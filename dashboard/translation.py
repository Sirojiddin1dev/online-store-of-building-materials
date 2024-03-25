from modeltranslation.translator import register, TranslationOptions, translator
from .models import *


@register(Products)
class ProductsTranslationOptions(TranslationOptions):
    fields = ('title', 'product_info', 'banner_title', 'banner_text', 'advert_text', )











