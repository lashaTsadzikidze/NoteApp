from django.shortcuts import render, redirect
from .models import Note
import datetime

# Create your views here.
def index(request):

    if request.method == 'POST':
        note_id = request.POST.get('note_id')
        note = Note.objects.get(id=note_id)
        note.delete()
        return redirect('main')
    
    notes = Note.objects.all()
    return render(request, 'index.html', {'notes': notes})

def note_details(request, title):
    note = Note.objects.get(title=title)
    return render(request, 'note_details.html', {'note': note})

def add_note(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        now = datetime.datetime.now()

        obj = Note.objects.create(title=title, content=content, date_created=now)

        obj.save()

        return redirect('main')
    
    return render(request, 'add_note.html')

def edit_note(request, id):
    note = Note.objects.get(id=id)
    if request.method == 'POST':
        note.title = request.POST.get('title')
        note.content = request.POST.get('content')
        note.save()
        return redirect('main')

    return render(request, 'edit_note.html', {'note': note})