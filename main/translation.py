from modeltranslation.translator import register, TranslationOptions, translator
from .models import *

@register(Tag)
class TagTranslationOptions(TranslationOptions):
    fields = ('name',)


@register(Banner)
class BannerTranslationOptions(TranslationOptions):
    fields = ('title',)


@register(Category)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('name',)


@register(Blog)
class BlogTranslationOptions(TranslationOptions):
    fields = ('title', 'description',)

