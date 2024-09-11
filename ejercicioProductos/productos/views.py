from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def productos(request):
    # Definir productos en el contexto
    categorias = {
        'Categoria 1': ['Producto A1', 'Producto A2', 'Producto A3'],
        'Categoria 2': ['Producto B1', 'Producto B2', 'Producto B3'],
        'Categoria 3': ['Producto C1', 'Producto C2', 'Producto C3'],
    }
    return render(request, 'productos.html', {'categorias': categorias})
