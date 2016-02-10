# -*- coding: utf-8 -*-

from django.contrib import admin
from main.models import *

####################################################################################################
## AdminCls
####################################################################################################    

class AdminCls(admin.ModelAdmin):
    class Meta:
        # dict полей для которых нужно установить соответствующий класс <input class="..."
        field_to_class = None
 
    # Добавляем класс wysiwyg для всех полей перечисленных в Meta.wysiwyg_fields
    def formfield_for_dbfield(self, db_field, **kwargs):
        field = super(AdminCls, self).formfield_for_dbfield(db_field, **kwargs)
        if self.Meta.field_to_class:
            if db_field.name in self.Meta.field_to_class:
                field.widget.attrs['class'] = self.Meta.field_to_class[db_field.name] + ' ' + field.widget.attrs.get('class', '')
        return field

####################################################################################################
## pages
####################################################################################################    

class PageAdmin(AdminCls):
    class Meta:
        field_to_class = { 'content': 'editor' }
    list_display = ('title', 'slug', 'sort_no',)
    list_editable = ('sort_no',)
    search_fields = ('title', 'slug', 'content',)
    
class ImgAdmin(admin.ModelAdmin):
    list_display = ('__unicode__',)
    search_fields = ('img',)
    
admin.site.register(Page, PageAdmin)
admin.site.register(Img, ImgAdmin)

####################################################################################################
## blog
####################################################################################################    

class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'sort_no',)
    list_editable = ('sort_no',)
    search_fields = ('title', 'slug',)
    
class PostAdmin(AdminCls):
    class Meta:
        field_to_class = { 'content': 'editor', 'logo_ids': 'logo-ids' }
    list_display = ('title', 'blog', 'user', 'created', 'is_all', 'is_draft', )
    list_editable = ('is_all', 'is_draft', )
    search_fields = ('title', 'content',)
    list_filter = ('blog', 'user', 'created', 'is_all', 'is_draft', )
    
class LogoAdmin(AdminCls):
    class Meta:
        field_to_class = { 'studio': 'autocomplete-studio', 'client': 'autocomplete-client', 'tags': 'tags' }
    list_display = ('__unicode__', 'img', 'tags', 'is_clon')
    search_fields = ('studio', 'client', 'tags',)
    list_filter = ('is_clon', )
    
admin.site.register(Blog, BlogAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Logo, LogoAdmin)
    
####################################################################################################
## incoming
####################################################################################################    

class IncomingAdmin(admin.ModelAdmin):
    list_display = ('title', 'created')
    list_filter = ('created', )    
    
admin.site.register(Incoming, IncomingAdmin)
