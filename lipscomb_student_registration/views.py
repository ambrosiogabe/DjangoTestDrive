from django.shortcuts import render
from django.views import generic
from django.views.generic.base import TemplateView
from student.models import Student
import datetime

class HomeView(TemplateView):
    template_name = 'index.html'

def form(request):
    return render(request, "form.html")

def submit(request):
    f_name = str(request.POST['first_name'])
    l_name = str(request.POST['last_name'])

    mi = str(request.POST['middle_name'])
    if len(mi) > 0:
        mi = str(mi[0])

    add = str(request.POST['address'])
    city = str(request.POST['city'])
    state = str(request.POST['state'])
    zi = str(request.POST['zip'])
    phone = str(request.POST['phone'])
    dob = request.POST['dob'].split("-")
    clas = str(request.POST['class'])
    s_pin = str(request.POST['s_pin'])

    f_id = request.POST['f_id']
    if f_id != "":
        f_id = int(request.POST['f_id'])
    else:
        f_id = None
    date_enrolled = str(request.POST['date_enrolled'])

    if len(dob) > 1:
        date = datetime.datetime(int(dob[0]), int(dob[1]), int(dob[2]), 0, 0, 0, 0)
    else:
        date = None

    if len(date_enrolled.split("-")) != 3:
        date_enrolled = None

    i = str(len(Student.objects.all()) + 1)
    s = Student(i, l_name, f_name, mi, add, city, state, zi, phone, clas, f_id, s_pin, date, date_enrolled)
    try:
        s.save()
    except Exception as e:
        print(e.args)
        context = {'error_message':'Please fill out all fields exactly as instructed.',
                    'f_name': f_name,
                    'l_name': l_name,
                    'm_name': mi,
                    'address': add,
                    'city': city,
                    'state': state,
                    'zip': zi,
                    'phone': phone,
                    'class': clas,
                    's_pin': s_pin,
                    'f_id': f_id,
                    }
        return render(request, 'form.html', context)
    else:
        context = {}
        return render(request, 'thank_you.html', context)

def thanks(request):
    return render(request, 'thank_you.html')
