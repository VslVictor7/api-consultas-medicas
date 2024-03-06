from django.contrib import admin
from django.urls import path, include
from api import views
from rest_framework.routers import DefaultRouter
from api.views import ConsultDetail, ProfDetail

router = DefaultRouter()

router.register("Profissionais", views.ProfissionalApi)
router.register("Consultas", views.clinicaApi)

urlpatterns = [

    path('admin/', admin.site.urls),
    path('', include(router.urls), name='home'),
    path('Consulta/<int:pk>', ConsultDetail.as_view()),
    path('Profissional/<int:pk>', ProfDetail.as_view()),

]