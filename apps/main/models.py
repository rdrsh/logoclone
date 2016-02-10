# -*- coding: utf-8 -*- 

from types import *

from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import User
from django.contrib.sites.models import Site
from django.contrib.comments.models import Comment
from tagging.models import Tag
from tagging.fields import TagField

from django.conf import settings

####################################################################################################
## Vars
####################################################################################################

# class Var(models.Model):
    # name = models.SlugField(max_length=255, verbose_name=u'Название', unique=True)
    # value = models.CharField(max_length=255, verbose_name=u'Значение')
    # comment = models.CharField(max_length=255, verbose_name=u'Коментарий')
    
    # def __unicode__(self):
        # return u'%s = %s' % (self.comment, self.value)
        
    # class Meta:
        # verbose_name = u"Настройки"
        # verbose_name_plural = u"Настройки"
        # ordering = ('name',)

####################################################################################################
## getVars
####################################################################################################

def isInt(x):
    return type(x) is IntType

# def getVars():
    # vars = {}
    # dbVars = dict([i.name, i.value] for i in Var.objects.all())
    # for k, v in DEFAULT_VARS.items():
        # if k in dbVars:
            # if isInt(v):
                # v = int(dbVars[k])
            # else:
                # v = dbVars[k]
        # vars[k] = v
    # return vars
    
# def var(name):
    # VARS = getVars()
    # return VARS[name]

####################################################################################################
## page
####################################################################################################

class Page(models.Model):
    title = models.CharField(max_length=255, verbose_name=u'Заголовок')
    slug = models.SlugField(max_length=255, verbose_name=u'URL', unique=True)
    content = models.TextField(verbose_name=u'Содержимое', blank=True)
    sort_no = models.FloatField(verbose_name=u'Порядковый номер', blank=True, default=100)

    def __unicode__(self):
        return self.title
    
    class Meta:
        verbose_name = u"Страница"
        verbose_name_plural = u"Страницы"
        ordering = ('sort_no',)
        
class Img(models.Model):
    img = models.ImageField(upload_to='img/img/', verbose_name=u'Картинка')

    def __unicode__(self):
        return u'/%s' % self.img
    
    class Meta:
        verbose_name = u"Картинка"
        verbose_name_plural = u"Картинки"
        
####################################################################################################
## blog
####################################################################################################

CUT = '<!-- CUT -->'

class Blog(models.Model):
    title = models.CharField(max_length=255, verbose_name=u'Заголовок', unique=True)
    slug = models.SlugField(max_length=255, verbose_name=u'URL', unique=True)
    sort_no = models.FloatField(verbose_name=u'Порядковый номер', blank=True, default=100)
    is_logo = models.BooleanField(verbose_name=u'Logo?')

    def __unicode__(self):
        return self.title
    
    class Meta:
        ordering = ('sort_no',)
        verbose_name = u"Блог"
        verbose_name_plural = u"Блоги"
        
class Post(models.Model):
    user = models.ForeignKey(User, verbose_name=u'Пользователь')
    blog = models.ForeignKey(Blog, verbose_name=u'Блог')
    title = models.CharField(max_length=255, verbose_name=u'Заголовок')
    content = models.TextField(verbose_name=u'Содержимое')
    created = models.DateField(auto_now=True, verbose_name=u'Дата')
    is_all = models.BooleanField(verbose_name=u'На главную')
    is_draft = models.BooleanField(verbose_name=u'Черновик')
    logo_ids = models.CharField(max_length=255, blank=True, verbose_name=u'Логотипы')
    
    def content_cut(self):
        return self.content.split(CUT)[0]
    
    def logo_list(self):
        return [Logo.objects.get(id=int(id)) for id in self.logo_ids.split(',')]
            
    def __unicode__(self):
        return self.title
    
    class Meta:
        ordering = ('-created',)
        verbose_name = u"Пост"
        verbose_name_plural = u"Посты"

w = 100
h = 100
class Logo(models.Model):
    w = w
    h = h
    studio = models.CharField(max_length=255, verbose_name=u'Студия')
    client = models.CharField(max_length=255, verbose_name=u'Клиент')
    img = models.ImageField(upload_to='img/logo/', verbose_name=u'Логотип (%d X %d)' % (w, h))
    tags = TagField(verbose_name=u'Теги')
    is_clon = models.BooleanField(verbose_name=u'Клон')

    def __unicode__(self):
        return '%s - %s' % (self.studio, self.client)
    
    class Meta:
        verbose_name = u"Логотип"
        verbose_name_plural = u"Логотипы"
        
####################################################################################################
## incoming
####################################################################################################

class Incoming(models.Model):
    title = models.CharField(max_length=255, verbose_name=u'Заголовок')
    content = models.TextField(verbose_name=u'Содержание')
    created = models.DateTimeField(auto_now=True, verbose_name=u'Дата')
    
    def __unicode__(self):
        return self.title
        
    class Meta:
        verbose_name = u"Входящие"
        verbose_name_plural = u"Входящие"
        ordering = ('-created',)
        
        
####################################################################################################
## incoming
####################################################################################################

def newComment(model, request, comment):
    user = request.user
    c = Comment()
    
    c.user = user
    c.user_name = user.username
    c.user_email = user.email
    c.ip_address = request.META.get('REMOTE_ADDR')
    c.comment = comment
    
    # c.site = Site.objects.get(id=settings.SITE_ID)
    c.site_id = settings.SITE_ID
    
    c.content_type = ContentType.objects.get_for_model(model)
    c.object_pk = model.id
    
    c.save()