from django.http import HttpResponse

def index(request):
    return HttpResponse("Youre at the polls index.")

