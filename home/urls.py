from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
	path('cyclic',views.cyclic),
	path('cyclicSubmit',views.cyclicSubmit),
	path('blind',views.blind),
	path('blindSubmit',views.blindSubmit),
	path('cct',views.cct),
	path('cctSubmit',views.cctSubmit),
	path('',views.index),
    
]
