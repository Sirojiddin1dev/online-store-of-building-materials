from modeltranslation.translator import register, TranslationOptions, translator
from .models import *


@register(Banner)
class BannerTranslationOptions(TranslationOptions):
    fields = ('title',)


@register(Blog)
class BlogTranslationOptions(TranslationOptions):
    fields = ('title', 'description',)

