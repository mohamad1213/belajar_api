from django.http import HttpResponse, JsonResponse
from .models import Crud


# untuk HttpResponse 

# def index (req):
#     html = "apa aja bileh"
#     return HttpResponse(html)


# untuk JsonResponse

def index(req):
    data = Crud.objects.all() #query set

    simpan = [] #ibarat kaleng kosong untuk menyimpan data
    for e in data: #query list
        simpan.append({
            'nama':e.nama, # append untuk menambahkan data
            'motto':e.motto
        })
    return JsonResponse({
        'data': simpan #
    }, safe=False)
