from django.template.response import TemplateResponse
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_protect
from .models import Person

def index(request):
    return TemplateResponse(request, 'main/index.html')

@csrf_protect
def save_index_form(request):
    if request.method == 'POST':

        if 'save' in request.POST:
            name = request.POST.get('name')
            age = request.POST.get('age')
            city = request.POST.get('city')
            data = {'name': name, 'age': age, 'city': city}
            return JsonResponse(data=data)

        if 'save in DB' in request.POST:
            name = request.POST.get('name')
            age = request.POST.get('age')
            city = request.POST.get('city')

            person = Person()
            person.name = name
            person.age = age
            person.city = city
            person.save()

            return HttpResponse('Данные отправлены')



