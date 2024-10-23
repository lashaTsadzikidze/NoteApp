from django.contrib import admin
from django.urls import path
from notes import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='main'),
    path('add/', views.add_note, name='add_note'),
    path('notes/<str:title>/', views.note_details, name='note_details'),
    path('edit/<int:id>/', views.edit_note, name='edit_note'),
]
