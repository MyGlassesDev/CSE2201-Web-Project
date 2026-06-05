from datetime import datetime
from django.shortcuts import render
from django.http import HttpRequest

# Login page
def login(request):
    assert isinstance(request, HttpRequest)

    return render(request, 'app/login.html', {
        'title': 'Login',
        'year': datetime.now().year,
    })

def home(request):
    assert isinstance(request, HttpRequest)
    return render(request, 'app/index.html', {
        'title': 'Home',
        'year': datetime.now().year,
    })


def dashboard(request):
    assert isinstance(request, HttpRequest)
    return render(request, 'app/dashboard.html', {
        'title': 'Dashboard',
        'year': datetime.now().year,
    })


def notes(request):
    assert isinstance(request, HttpRequest)
    return render(request, 'app/notes.html', {
        'title': 'Notes',
        'year': datetime.now().year,
    })


def calendar(request):
    assert isinstance(request, HttpRequest)
    return render(request, 'app/calendar.html', {
        'title': 'Calendar',
        'year': datetime.now().year,
    })


def reminders(request):
    assert isinstance(request, HttpRequest)
    return render(request, 'app/reminders.html', {
        'title': 'Reminders',
        'year': datetime.now().year,
    })


def register(request):
    assert isinstance(request, HttpRequest)
    return render(request, 'app/register.html', {
        'title': 'Register',
        'year': datetime.now().year,
    })


def contact(request):
    assert isinstance(request, HttpRequest)
    return render(request, 'app/contact.html', {
        'title': 'Contact',
        'message': 'Your contact page.',
        'year': datetime.now().year,
    })


def about(request):
    assert isinstance(request, HttpRequest)
    return render(request, 'app/about.html', {
        'title': 'About',
        'message': 'Your application description page.',
        'year': datetime.now().year,
    })