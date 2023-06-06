from .models import Category, Content, Malumotlar
from modeltranslation.translator import TranslationOptions,register


@register(Category)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('name', 'slug')


@register(Content)
class ContentTranslationOptions(TranslationOptions):
    fields = ('title', 'desc')


@register(Malumotlar)
class MalumotlarTranslationOptions(TranslationOptions):
    fields = ('title', 'desc')




