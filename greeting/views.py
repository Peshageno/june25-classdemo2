"""Views for the main pages of the site."""
from django.shortcuts import render

def index(request):
    """Render the homepage with a greeting."""
    return render(request, 'index.html', {'greeting': 'Hello'})
