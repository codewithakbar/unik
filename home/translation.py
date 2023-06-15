from .models import Category, Content, Malumotlar
from news.models import NewsCartegory, Yangiliklar
from modeltranslation.translator import TranslationOptions,register


@register(Category)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('name', 'slug')


@register(Content)
class ContentTranslationOptions(TranslationOptions):
    fields = ('title', 'desc', 'nomi')


@register(Malumotlar)
class MalumotlarTranslationOptions(TranslationOptions):
    fields = ('title', 'desc')


@register(NewsCartegory)
class NewsCartegoryTranslationOptions(TranslationOptions):
    fields = ('name', 'slug')


@register(Yangiliklar)
class YangiliklarTranslationOptions(TranslationOptions):
    fields = ('title', 'desc')

    

    

