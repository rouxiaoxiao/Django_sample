from django.shortcuts import render

# Create your views here.


def index(request):
    context ={
        'title':'Just a title',
        'des':'Just a description',
        'score':'1.0'

    }
    return render(request,'index.html',context)


