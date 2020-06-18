from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django.contrib import admin
from .models import *
from django.utils.safestring import mark_safe
from django import forms
class ArticleAdminForm(forms.ModelForm):
    text = forms.CharField(label="текст", widget=CKEditorUploadingWidget())


    class Meta:
        model = Article
        fields = '__all__'

class NewsAdminForm(forms.ModelForm):
    text = forms.CharField(label="текст", widget=CKEditorUploadingWidget())


    class Meta:
        model = News
        fields = '__all__'
@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('name','time','get_image')
    readonly_fields = ('get_image',)
    list_filter = ('time',)
    form = ArticleAdminForm
    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="100" ')

    get_image.short_description = "Изображение"

@admin.register(News)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('name','time','get_image')
    readonly_fields = ('get_image',)
    list_filter = ('time',)
    form = NewsAdminForm
    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="100" ')

    get_image.short_description = "Изображение"