from django.shortcuts import redirect, render
from django.http import HttpResponse
from livros.models import Item
from django.template import loader
from django import forms
from .forms import ItemForm
from django.views.generic.list import ListView
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
import pandas as pd




# Create your views here.
def index(request):
    #return HttpResponse('Hello, World')
    return render(request, 'livros/index.html')

def lista(request):
    try:
        item_lista=Item.objects.all()
        template = loader.get_template('livros/lista.html')
        context={'item_lista':item_lista,
        }
        return HttpResponse(template.render(context,request))
    except:
        return HttpResponse('<h1>Erro ao Listar Lista!</h1>')

def detail(request, item_id):
    item= Item.objects.get(pk=item_id)
    context={'item':item,}
    return render(request,'livros/detail.html',context)

def cadastro(request):
    form = ItemForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('livros:index')
    return render(request, 'livros/form.html', {'form':form})

class ListaC(ListView):
    model = Item
    context_object_name = 'item_lista'
    template_name = 'livros/lista.html'
    paginate_by = 3
    
    #http://127.0.0.1:8000/loja/lista/?page=1

def relatorio(request):
    item = Item.objects.all().values()
    df = pd.DataFrame(item)
    mydict = {
        'df': df.to_html()
    }
    return render(request, 'livros/relatorio.html', context= mydict)

def html(request):
    return render(request, 'livros/html.html')



#def my_image(request):
  #   template = loader.get_template('livros/index.html')
 #    context = {}
 #    return HttpResponse(template.render(context, request))