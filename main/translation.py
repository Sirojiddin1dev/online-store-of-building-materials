from modeltranslation.translator import register, TranslationOptions, translator
from .models import *

@register(Tag)
class TagTranslationOptions(TranslationOptions):
    fields = ('name',)

