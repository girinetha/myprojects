from django.shortcuts import render
from modelformsapp.forms import projectform
from modelformsapp.models import project
# Create your views here.

def index(request):
    return render(request,'index.html')

def listprojects(request):
    listprojects=project.objects.all()
    return render(request,'listprojects.html',{'listprojects':listprojects})

def addproject(request):
    form=projectform()
    if request.method=='POST':
        form=projectform(request.POST)
        if form.is_valid():
            form.save()
        return index(request)
    return render(request,'addproject.html',{'form':form})