from django.shortcuts import render

# Create your views here.
def skill(request):
    context={'skill':'active'}
    return render(request,'edu/skill.html',context)
def projects(request):
    context={'projects':'active'}
    return render(request,'edu/projects.html',context)