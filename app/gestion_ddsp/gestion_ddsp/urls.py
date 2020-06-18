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
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('', carte_views.Index.as_view(), name='index'),
    path('generate_all/', carte_views.GenerateDirections.as_view()),
    path('get_ddsp_name/', carte_views.GetDdspName.as_view(), name='get_ddsp_name'),
    path('gestion/', gestionnaire_views.Gestionnaire.as_view(), name='gestionnaire_empty'),
    path('gestion/<str:direction>/', gestionnaire_views.Gestionnaire.as_view(), name='gestionnaire'),
    path('deplacements/', gestionnaire_views.Deplacements.as_view(), name='deplacements'),
    path('search_engine/', gestionnaire_views.SearchEngine.as_view(), name='search_engine'),
    path('change_site_state/', gestionnaire_views.ChangeSiteState.as_view(), name='change_site_state'),
    path('change_hebergement/', gestionnaire_views.ChangeHebergement.as_view(), name='change_hebergement'),
    path('create_or_modify_hebergeur/', gestionnaire_views.createOrModifyHebergeur.as_view(), name='create_or_modify_hebergeur'),
    path('delete_hebergeur/', gestionnaire_views.DeleteHebergeur.as_view(), name='delete_hebergeur'),
    path('create_or_modify_contact/', gestionnaire_views.createOrModifyContact.as_view(), name='create_or_modify_hebergeur'),
    path('delete_contact/', gestionnaire_views.DeleteContact.as_view(), name='delete_hebergeur'),
    path('create_or_modify_deplacement/', gestionnaire_views.createOrModifyDeplacement.as_view(), name='create_or_modify_deplacement'),
    path('delete_deplacement/', gestionnaire_views.DeleteDeplacement.as_view(), name='delete_deplacement'),
    path('save_stagiaire/', gestionnaire_views.SaveStagiaire.as_view(), name='save_stagiaire'),
    path('save_url/', gestionnaire_views.SaveUrl.as_view(), name='save_url'),
    path('save_version/', gestionnaire_views.SaveVersion.as_view(), name='save_version'),
    path("create_ddsp/", gestionnaire_views.CreateDdsp.as_view(), name="create_ddsp"),
    path("remove_ddsp/", gestionnaire_views.RemoveDdsp.as_view(), name="remove_ddsp"),
    path("insert_csv/", carte_views.insert_csv, name="insert_csv"),
    path('admin/', admin.site.urls),
    path("logout/", LogoutView.as_view(), name="logout"),

]
