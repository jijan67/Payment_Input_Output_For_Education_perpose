from django.shortcuts import render, HttpResponse
from .models import Course, Batch, Department


# Create your views here.
def index(request):
    return render(request, 'index.html')


def all_emp(request):
    emps = Course.objects.all()
    context = {
        'emps': emps
    }
    print(context)
    return render(request, 'All_Course.html', context)


def filter_emp(request):
    if request.method == 'POST':
        dept = request.POST['dept']
        Batch = request.POST['Batch']
        emps = Course.objects.all()
        if dept:
            emps = emps.filter(dept__name__icontains = dept)
        if Batch:
            emps = emps.filter(Batch__name__icontains = Batch)

        context = {
            'emps': emps
        }
        return render(request, 'All_Course.html', context)

    elif request.method == 'GET':
        return render(request, 'Payment.html')
    else:
        return HttpResponse('An Exception Occurred')
