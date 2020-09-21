from django.shortcuts import render, HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.core.paginator import Paginator
from .models import Product, Subcategory
from header.models import Slider
from django.db.models import Q



# Create your views here.
#Vista para la pagina Home y ordenar productos en la portada
def home(request):    
    sliders = Slider.objects.all()    
    productos_mas_vendidos = Product.objects.filter(fisico = True).order_by('-ventas_terramar')[:4]  
    productos_mas_vistos = Product.objects.filter(fisico = True).order_by('-vistas_terramar')[:4] 
    queryset = request.GET.get('buscar') 
    if queryset:
        productos_mas_vendidos = Product.objects.filter(
            Q(titulo__icontains = queryset) |
            Q(titular__icontains = queryset) |
            Q(descripcion__icontains = queryset) |
            Q(subcategory__name__icontains = queryset)
        ).distinct()
        productos_mas_vistos  = Product.objects.filter(
            Q(titulo__icontains = queryset) |
            Q(titular__icontains = queryset) |
            Q(descripcion__icontains = queryset) |
            Q(subcategory__name__icontains = queryset) 
        ).distinct()
    return render(request, "core/home.html",{'productos_mas_vendidos':productos_mas_vendidos,  'productos_mas_vistos': productos_mas_vistos, 'sliders': sliders})

# Muestra los productos mas vendidos
class ProductListView(ListView):
    model = Product
    template_name = "core/producto_list.html"
    paginate_by = 12
    ordering =  ["-ventas_terramar"]
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)        
        return context
    def get_queryset(self):
        queryset = self.request.GET.get('buscar')
        if queryset:
            object_list  = Product.objects.filter(
            Q(titulo__icontains = queryset) |
            Q(titular__icontains = queryset) |
            Q(descripcion__icontains = queryset) |
            Q(subcategory__name__icontains = queryset),
            fisico = True, 
        ).distinct()
        else:      
            return Product.objects.filter(fisico = True).order_by('-created') 
        return object_list


class ProductListView2(ListView):
    model = Product
    template_name = "core/producto_list.html"
    paginate_by = 12
    ordering =  ["-ventas_terramar"]
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)        
        return context

    def get_queryset(self):
        queryset = self.request.GET.get('buscar')
        if queryset:
            object_list  = Product.objects.filter(
            Q(titulo__icontains = queryset) |
            Q(titular__icontains = queryset) |
            Q(descripcion__icontains = queryset) |
            Q(subcategory__name__icontains = queryset),
            fisico = True, 
        ).distinct()
        else:
            return Product.objects.filter(fisico = True).order_by('created')
        return object_list

# Muestr los productos mas vistos 
class ProductVisitView(ListView):
    model = Product
    template_name = "core/producto_list_2.html"
    paginate_by = 12
    ordering =  ["-vistas_terramar"]
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)         
        return context

    def get_queryset(self):
        queryset = self.request.GET.get('buscar')  
       
        if queryset:
            object_list  = Product.objects.filter(
            Q(titulo__icontains = queryset) |
            Q(titular__icontains = queryset) |
            Q(descripcion__icontains = queryset) |
            Q(subcategory__name__icontains = queryset),
            fisico = True, 
        ).distinct()
        else:
            return Product.objects.filter(fisico = True).order_by('-created')
        return object_list
        


class ProductVisitView2(ListView):
    model = Product
    template_name = "core/producto_list_2.html"
    paginate_by = 12
    ordering =  ["-vistas_terramar"]
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)         
        return context

    def get_queryset(self):   
        queryset = self.request.GET.get('buscar')       
        if queryset:
            object_list  = Product.objects.filter(
            Q(titulo__icontains = queryset) |
            Q(titular__icontains = queryset) |
            Q(descripcion__icontains = queryset) |
            Q(subcategory__name__icontains = queryset),
            fisico = True, 
        ).distinct()
        else:  
            return Product.objects.filter(fisico = True).order_by('created')   
        return object_list
        

# Muestra los productos de la subcategoria.


def subccategory(request, subcategory_id):
    subcategory = get_object_or_404(Subcategory, id=subcategory_id)    
    product = Product.objects.filter(subcategory=subcategory)
    queryset = request.GET.get('buscar')     
   
    if queryset:
        product = Product.objects.filter(        
        Q(titulo__icontains = queryset) | 
        Q(titular__icontains = queryset) |
        Q(descripcion__icontains = queryset)       
        )
    paginator = Paginator(product,12)
    page = request.GET.get('page')
    product = paginator.get_page(page)
    return render(request, "core/subcategoria_detail.html", {'subcategory':subcategory, 'product':product, 'paginator':paginator})


# Muestra el info producto

def infoproduct(request, product_id):
    product = get_object_or_404(Product, pk =product_id)    
    return render(request, "core/infoproducto_detail.html", {'product':product})
