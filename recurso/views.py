from django.http import HttpResponse

from .models import Teacher

def teacher_index(request):
    response = HttpResponse()
    query  = Teacher.objects.all()
    

    if query.exists():
        response = HttpResponse(
            status=200
        )
    else:
        response = HttpResponse(
            status=404
        )

    return response