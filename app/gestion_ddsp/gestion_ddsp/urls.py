"""gestion_ddsp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
import carte.views as carte_views
import gestionnaire.views as gestionnaire_views

urlpatterns = [
    path('', carte_views.Index.as_view(), name='carte'),
    path('admin/', admin.site.urls),
    path('generate_all/', carte_views.GenerateDirections.as_view()),
    path('gestion/', gestionnaire_views.Gestionnaire.as_view(), name='gestionnaire_empty'),
    path('gestion/<str:direction>/', gestionnaire_views.Gestionnaire.as_view(), name='gestionnaire'),
    path('search_engine/', gestionnaire_views.SearchEngine.as_view(), name='search_engine'),
    path('change_site_state/', gestionnaire_views.ChangeSiteState.as_view(), name='change_site_state'),
    path('change_hebergement/', gestionnaire_views.ChangeHebergement.as_view(), name='change_hebergement'),
    path('create_or_modify_hebergeur/', gestionnaire_views.createOrModifyHebergeur.as_view(), name='create_or_modify_hebergeur'),

]
