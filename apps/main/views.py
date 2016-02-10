# -*- coding: utf-8 -*- 

from django.shortcuts import get_object_or_404, render_to_response
from django.http import HttpResponseRedirect
from django.template import Context
from django.core.mail import send_mail
from django.template.loader import get_template

from main.models import *
from main.forms import *

####################################################################################################
## stuff
####################################################################################################

def toInt(*args):
    result = []
    for x in args:
        if x:
            result.append(int(x))
        else:
            result.append(0)
    return result

def splitPhone(phone):
    if ')' in phone:
        code, phone = phone.split(')', 1)
        code += ')'
    else:
        code = ''
    return code.strip(), phone.strip()
    
def renderToResponse(request, template, vars=None, mimetype=None):
    if not vars:
        vars = {}
    # for k, v in getVars().items():
        # vars[k] = v
        
    # vars['mainMenu'] = Page.objects.filter(is_menu=True)
    # vars['phoneCode'], vars['phone'] = splitPhone(vars['phone'])
    
    vars['blogList'] = Blog.objects.all()

    if mimetype:
        return render_to_response(template, vars, mimetype=mimetype)
    else:
        return render_to_response(template, vars)


def emailTemplate(emailFrom, emailTo, tmplFile, vars):
    emailFrom = 'aaa@gmail.com'
    t = get_template(tmplFile)
    s = t.render(Context(vars))
    subject, body = s.split('\n', 1)
    subject = subject.strip()
    body = body.strip()
    # send_mail(subject, body, emailFrom, [emailTo], fail_silently=False)
    i = Incoming(title=subject, content=body)
    i.save()
    return 'mail "%s" => "%s"\n%s\n%s\n%s' % (emailFrom, emailTo, subject, '-'*30, body)
    
####################################################################################################
## pages
####################################################################################################

def page(request, slug):
    page = get_object_or_404(Page, slug=slug)
    return renderToResponse(request, 'page.html', locals())

####################################################################################################
## blog
####################################################################################################

def index(request):
    postList = Post.objects.filter(is_all=True, is_draft=False)
    return renderToResponse(request, 'index.html', locals())
    
def blog(request, slug, page=1):
    page = int(page)
    blog = get_object_or_404(Blog, slug=slug)
    postList = Post.objects.filter(blog=blog, is_draft=False)
    return renderToResponse(request, 'blog.html', locals())


def post(request, id):
    id = int(id)
    post = get_object_or_404(Post, id=id)
    
    if request.method == 'POST':
        if not request.user.is_authenticated():
            return HttpResponseRedirect('/login/')
        form = CommentForm(request.POST)
        if form.is_valid():
            vars = form.cleaned_data
            newComment(post, request, vars['comment'])
            form = CommentForm()
            success = True
    else:
        form = CommentForm()

    return renderToResponse(request, 'post.html', locals())

def contact(request):
    page = getPage('contact')
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            vars = form.cleaned_data
            # newComment(request, vars['comment'])
            emailDump = emailTemplate(var('emailContact'), var('emailContact'), 'contact.txt', vars)
            form = ContactForm()
    else:
        form = ContactForm()
        
    return renderToResponse(request, 'contact.html', locals())
    
def _404(request):
    return render_to_response('404.html', locals())
    
####################################################################################################
## blog
####################################################################################################

def tagListJS(request):
    items = [t.name for t in Tag.objects.all()]
    return renderToResponse(request, 'tag-list.js', locals(), mimetype='text/javascript; charset=UTF-8')
    
def autocompleteListJS(request):
    studioList = set()
    clientList = set()
    for l in Logo.objects.all():
        studioList.add(l.studio)
        clientList.add(l.client)
    return renderToResponse(request, 'autocomplete-list.js', locals(), mimetype='text/javascript; charset=UTF-8')
    
def ajaxLogo(request):
    items = Logo.objects.all()
    return renderToResponse(request, 'ajax-logo.html', locals())
    
def ajaxLogoByIdList(request, idList):
    items = [Logo.objects.get(id=int(id)) for id in idList.strip(',').split(',')]
    return renderToResponse(request, 'ajax-logo.html', locals())
    
def dragtest(request):
    items = Logo.objects.all()
    return renderToResponse(request, 'dragtest.html', locals())