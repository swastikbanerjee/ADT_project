from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .forms import UploadDoc
import subprocess
# from .hello import printHello

# Create your views here.
def uploadform(response):
    template = loader.get_template('upload.html')
    return HttpResponse(template.render())

def studentlogin(response):
    template = loader.get_template('studentlogin.html')
    return HttpResponse(template.render())

def teacherlogin(response):
    template = loader.get_template('teacherlogin.html')
    return HttpResponse(template.render())

def about(response):
    template = loader.get_template('about.html')
    return HttpResponse(template.render())

def response(request):
    template = loader.get_template('response.html')
    return HttpResponse(template.render())

def evaluate(request):
    template = loader.get_template('website.html')
    return HttpResponse(template.render())

# def CheckRep(request):
#     if request.method == 'POST':
#         form =TeacherReport(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return HttpResponse('report is being generated...')

def UploadFile(request):
    if request.method == 'POST':
        form = UploadDoc(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse('The file is saved')
    else:
        form = UploadDoc()
    context = {'form':form, }
    return render(request, 'upload.html', context)

# views.py
def ml(request):
    script_path = 'C:\StrangerCodes\ADT\Cherry\evaluate\hello.py'
    result = subprocess.run(['python', script_path], capture_output=True, text=True)
    # return HttpResponse(result.stdout)
    return HttpResponse(result.stdout)