# -*- coding: utf-8 -*- 

from django import forms
from django.forms.extras import widgets
# from django.forms.extras.widgets import Textarea

class Frm(forms.Form):
    def as_p_br(self):
        s = self.as_p()
        return s.replace('</label> ', '</label><br/>')
        
class FaqForm(Frm):
    name = forms.CharField(label=u'Ваше имя')
    email = forms.EmailField(label=u'Ваш e-mail')
    question = forms.CharField(label=u'Вопрос', widget=forms.Textarea())

class CommentForm(forms.Form):
    comment = forms.CharField(label=u'Коментарий', widget=forms.Textarea())
