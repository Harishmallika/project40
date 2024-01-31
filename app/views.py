from django.shortcuts import render

# Create your views here.

from app.models import *

q1
def equijoints(request):
    EMPOBJECTS=emp.objects.select_related('deptno').all()
    EMPOBJECTS=emp.objects.select_related('deptno').filter(hiredate__year=2023)
    EMPOBJECTS=emp.objects.select_related('deptno').filter(deptno__dname='ACCOUNTING')
    EMPOBJECTS=emp.objects.select_related('deptno').filter(deptno__dloc='DALLAS')
    EMPOBJECTS=emp.objects.select_related('deptno').filter(ename='SMITH') 
    EMPOBJECTS=emp.objects.select_related('deptno').filter(job='CLERK',deptno__deptno=20,sal__lt=1800) 

    

    d={'EMPOBJECTS':EMPOBJECTS}
    return render(request,'equijoints.html',d)