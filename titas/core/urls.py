from django.urls import path
from . import views
from .views import ProductListView, ProductVisitView, ProductListView2, ProductVisitView2


#importamos nuestras vistas a cada una de nuestra apps

urlpatterns = [
    path('', views.home, name="home"),
    path('productos/mas-vendidos/mas-recientes', ProductListView.as_view(), name="producto"), 
    path('productos/mas-vendidos/mas-antiguos', ProductListView2.as_view(), name="producto2"),
    path('productos/mas-vistos/mas-recientes', ProductVisitView.as_view(), name="producto_vistos"),
    path('productos/mas-vistos/mas-antiguos', ProductVisitView2.as_view(), name="producto_vistos2"),
    #path('/productos/<int:pk>/<slug:slug>', SubCategoriaDetailView.as_view(), name="subcategory"), 
    
    path('productos/<int:subcategory_id>/', views.subccategory, name="subccategory"),

    path('producto/<int:product_id>/', views.infoproduct, name="infoproduct"),
          
]


"""
,

urlpatterns = [
    path('', views.home, name="home"), 
    
    #path('<int:pk>/<slug:slug>', SubCategoriaDetailView.as_view(), name="subcategory"),
    #path('productos/mas-vendidos', ProductListView.as_view(), name="producto"),
    #path('productos/mas-vistos', ProductVisitView.as_view(), name="producto_vistos"),
     
]
"""