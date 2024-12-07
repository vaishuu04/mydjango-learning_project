from django.shortcuts import render

# Create your views here.
def index(request):
    context_dict= {'text':'Hello world', 'number':'100'}
    return render(request, 'tempapp/index.html', context_dict)

def others(request):
    return render(request, 'tempapp/others.html')

def relative(request):
    return render(request, 'tempapp/relative_url.html')