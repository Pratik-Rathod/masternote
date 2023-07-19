from django.shortcuts import render, redirect
from .forms import NewNoteForm
from .models import NotesModel
from django.contrib.auth import get_user_model
from django.contrib import messages
from markdown_it import MarkdownIt

# Create your views here.


def viewpost(request, post_id):
    template = 'notes/view_note.html'
    context = dict()
    try:
        
        #{"breaks": True, "typographer": True, 'html': False,'xhtmlOut': False, }
        md = MarkdownIt("js-default")
        # print(md.options)
        post_body = NotesModel.objects.filter(id=post_id).values('body','title','last_edit','author__username',)   
        # print(post_body[0]['body'])
        htm = md.render(post_body[0]['body'])
   
    except Exception as e:
        pass

    context['htm_body'] = htm
    context['post_meta'] = post_body

    return render(request, template, context)


def home(request):
    template = 'index.html'
    context = dict()
    notes = NotesModel.objects.filter(is_private=False).values(
        'id', 'title', 'summary', 'author__username')
    context['notes'] = notes
    return render(request, template, context)


def addnote(request):
    templete = 'notes/createnote.html'
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
