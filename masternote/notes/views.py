from django.shortcuts import render, redirect
from .forms import NewNoteForm
from .models import NotesModel
from django.contrib.auth import get_user_model
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from markdown_it import MarkdownIt
from mdit_py_plugins import tasklists, anchors, container, texmath, deflist, admon , dollarmath

# from mdit_py_plugins import deflist

from pygments import highlight
from pygments.lexers import get_lexer_by_name, guess_lexer
from pygments.formatters import HtmlFormatter


def _code_highlighter(code, name, attrs):

    if name:
        lexer = get_lexer_by_name(name, stripall=True)
    else:
        lexer = guess_lexer(code)

    formatter = HtmlFormatter(style='dracula', linenos=True)

    if attrs:
        print(attrs)

    return highlight(code, lexer, formatter)


# Create your views here.
def viewpost(request, post_id):
    template = 'notes/view_note.html'
    context = dict()

    try:
        # {"breaks": True, "typographer": True, 'html': False,'xhtmlOut': False, }
        md = MarkdownIt("js-default", {'linkify': True, 'typographer': True, 'breaks': False,
                        'highlight': _code_highlighter}).use(anchors.index.anchors_plugin).use(tasklists.tasklists_plugin).use(tasklists.tasklists_plugin).use(texmath.index.texmath_plugin).use(deflist.index.deflist_plugin).use(admon.admon_plugin)

        post_body = NotesModel.objects.filter(id=post_id, is_private=False).values(
            'body', 'title', 'last_edit', 'author__username',)
        # print(post_body[0]['body'])
        htm = md.render(post_body[0]['body'])
        context['htm_body'] = htm
        context['post_meta'] = post_body

    except Exception as e:
        context['htm_body'] = "Something went wrong"
        context['post_meta'] = "wait dev work on this problem"

        print(e)

    return render(request, template, context)


def home(request):
    template = 'index.html'
    context = dict()
    notes = NotesModel.objects.filter(is_private=False).values(
        'id', 'title', 'summary', 'author__username',).order_by('-created')
    context['notes'] = notes
    return render(request, template, context)

@login_required(login_url='login')
def addnote(request):
    templete = 'notes/createnote.html'
    next_url = None
    context = dict()

    if request.method == 'POST':
        form = NewNoteForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            User = get_user_model()
            instance.author = User.objects.get(id=request.user.id)
            instance.save()
            if instance.is_private:
                messages.info(request, 'Blog saved succesfully!')
            else:
                messages.info(request, 'Blog Published succesfully!')

            return redirect('home')
    else:
        context['form'] = NewNoteForm()
    return render(request, template_name=templete, context=context)
