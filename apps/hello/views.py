from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound, JsonResponse

def index_view(request):
    return HttpResponse("hello world")