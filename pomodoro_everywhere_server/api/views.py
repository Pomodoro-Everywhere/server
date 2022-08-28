from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world. You're at the api index.html. " \
                        + "We're not yet developed web application. Only API for native apps. " \
                        + "They're also not ready yet.")
