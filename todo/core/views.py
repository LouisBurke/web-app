from django.shortcuts import render_to_response

from .models import todo

# Create your views here.
def index(request):
    items = todo.objects.all()
    return render_to_response('core/index.html', {'items': items})
