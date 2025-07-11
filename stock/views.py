from django.shortcuts import render, redirect, get_object_or_404
from .models import Artigo
from .forms import ArtigoForm

def lista_artigos(request):
    artigos = Artigo.objects.all()
    return render(request, 'stock/lista.html', {'artigos': artigos})

def criar_artigo(request):
    if request.method == 'POST':
        form = ArtigoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_artigos')
    else:
        form = ArtigoForm()
    
    artigos = Artigo.objects.all()
    return render(request, 'stock/criar.html', {
        'form': form,
        'artigos': artigos,
    })

def editar_artigo(request, artigo_id):
    artigo = get_object_or_404(Artigo, pk=artigo_id)
    if request.method == 'POST':
        form = ArtigoForm(request.POST, instance=artigo)
        if form.is_valid():
            form.save()
            return redirect('lista_artigos')
    else:
        form = ArtigoForm(instance=artigo)
    return render(request, 'stock/editar.html', {'form': form})

def eliminar_artigo(request, artigo_id):
    artigo = get_object_or_404(Artigo, pk=artigo_id)
    if request.method == 'POST':
        artigo.delete()
        return redirect('lista_artigos')
    return render(request, 'stock/eliminar.html', {'artigo': artigo})
