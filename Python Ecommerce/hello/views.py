from django.http import HttpResponse

# Create Views

def home(request):
    return HttpResponse ("Eymard Julian S. Jimeno")

def individual_post(request):
    return HttpResponse('Hi')


