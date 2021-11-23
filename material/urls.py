from django.urls import path

from .views import MaterialCreate, MaterialDelete, MaterialList, MaterialUpdate

urlpatterns = [
    path('cadastrar/material/', MaterialCreate.as_view(),
         name='cadastrar-material'),
    path('atualizar/material/<int:pk>/',
         MaterialUpdate.as_view(), name='atualizar-material'),
    path('deletar/material/<int:pk>/',
         MaterialDelete.as_view(), name='deletar-material'),
    path('listar/material/', MaterialList.as_view(), name='listar-material')

]
