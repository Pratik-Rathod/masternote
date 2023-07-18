from django.shortcuts import render, redirect
from .forms import NewNoteForm
from django.contrib.auth import get_user_model
from django.contrib import messages
# Create your views here.


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
            messages.info(request, 'Blog Published succesfully!')
            return redirect('home')
    else:
        context['form'] = NewNoteForm()
    return render(request, template_name=templete, context=context)
