from modeltranslation.translator import register, TranslationOptions, translator
from .models import *


@register(About)
class AboutTranslationOptions(TranslationOptions):
    fields = ('text', 'title',)






