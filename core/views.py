from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Note


# ======================
# 🌐 PUBLIC PAGES
# ======================

# Home page (public library preview)
def home(request):
    notes = Note.objects.all().order_by('-uploaded_at')
    return render(request, 'home.html', {'notes': notes})


# Full library page
def library(request):
    notes = Note.objects.all().order_by('-uploaded_at')
    return render(request, 'library.html', {'notes': notes})


# ======================
# 🔐 AUTHENTICATION
# ======================

# Admin login
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user and user.is_staff:
            auth_login(request, user)
            return redirect('adminpage')
        else:
            return render(request, 'login.html', {
                'error': 'Invalid credentials or not an admin.'
            })

    return render(request, 'login.html')


# Admin logout
@login_required
def logout(request):
    auth_logout(request)
    return redirect('login')


# ======================
# 📊 ADMIN DASHBOARD
# ======================

@login_required
def adminpage(request):
    notes = Note.objects.all().order_by('-uploaded_at')
    return render(request, 'adminpage.html', {
        'user': request.user,
        'notes': notes
    })


# ======================
# ➕ CREATE (UPLOAD)
# ======================

@login_required
def upload_note(request):
    if request.method == "POST":
        title = request.POST.get('title')
        year = request.POST.get('year')
        category = request.POST.get('category')
        note_type = request.POST.get('type')
        file = request.FILES.get('file')
        video_url = request.POST.get('video_url')

        Note.objects.create(
            title=title,
            year=year,
            category=category,
            type=note_type,
            file=file if file else None,
            video_url=video_url if video_url else None
        )

        messages.success(request, "Note uploaded successfully!")
        return redirect('adminpage')

    return redirect('adminpage')


# ======================
# ✏ UPDATE
# ======================

@login_required
def edit_note(request, id):
    note = get_object_or_404(Note, id=id)

    if request.method == 'POST':
        note.title = request.POST.get('title')
        note.year = request.POST.get('year')
        note.category = request.POST.get('category')
        note.type = request.POST.get('type')
        note.video_url = request.POST.get('video_url')

        if request.FILES.get('file'):
            note.file = request.FILES.get('file')

        note.save()
        messages.success(request, "Note updated successfully!")
        return redirect('adminpage')

    return render(request, 'edit_note.html', {'note': note})


# ======================
# 🗑 DELETE
# ======================

@login_required
def delete_note(request, id):
    note = get_object_or_404(Note, id=id)
    note.delete()
    messages.success(request, "Note deleted successfully!")
    return redirect('adminpage')