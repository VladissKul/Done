from django.http import HttpResponseForbidden
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import NoteForm
from .models import Note


@login_required
def create_note(request):
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            note = form.save(commit=False)
            note.user = request.user
            note.save()
            return redirect('notes_list')
    else:
        form = NoteForm(initial={'user': request.user})
    return render(request, 'notes/create_note.html', {'form': form})


@login_required()
def notes_list(request):
    # Получаем все заметки текущего пользователя
    notes = Note.objects.filter(user=request.user)

    # Передаем заметки в контекст для отображения в шаблоне
    context = {'notes': notes}

    return render(request, 'notes/notes_list.html', context)


@login_required()
def note_detail(request, note_id):
    note = get_object_or_404(Note, pk=note_id, user=request.user)
    if request.method == 'GET':
        form = NoteForm(instance=note)
        return render(request, 'notes/note_detail.html', {'note': note, 'form': form})
    else:
        try:
            form = NoteForm(request.POST, instance=note)
            form.save()
            return redirect('notes_list')
        except ValueError:
            return render(request, 'notes/note_detail.html', {'note': note, 'form': form, 'error': 'Bad info'})


@login_required
def delete_note(request, note_id):
    note = get_object_or_404(Note, pk=note_id, user=request.user)
    if request.method == 'POST':
        note.delete()
        return redirect('notes_list')