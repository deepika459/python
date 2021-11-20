from django.shortcuts import render
from django.http import HttpResponse

projectsList = [
           {
           'id':'1',
           'title':'Ecommerce Website',
           'description': 'Fully functional ecommerce website'
           },
           {
           'id':'2',
           'title': "Portfolio Website",
           'description': 'this was a project where i built out my portfol'

           },
           {
           'id':'3',
           'title':'Social networl',
           'description': 'Awsome open source project iam still woring'

           },

]
def projects(request):
    page = 'projects'
    number = 9
    context = {'page': page, 'number': number, 'projects': projectsList}
    return render(request, 'projects/projects.html', context)

def project(request, pk):
    projectobj = None
    for i in projectsList:
        if i['id'] == pk:
            projectobj = i
    return render(request, 'projects/single-project.html', { 'project': projectobj})

# Create your views here.
