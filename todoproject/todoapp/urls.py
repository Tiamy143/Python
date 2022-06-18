from django.urls import path
from . import views
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
#app_name='todoapp'
urlpatterns = [

    path('', views.add, name='add'),
    path('deletetask/<int:tid>/', views.deletetask, name='deletetask'),
    path('update/<int:id>/',views.update,name='update'),
    path('cbvhome/', views.Tasklistview.as_view(), name='cbvhome'),
    path('cbvdetails/<int:pk>/', views.Taskdetailview.as_view(), name='cbvdetails'),
    path('cbvedit/<int:pk>/', views.Taskupdateview.as_view(), name='cbvedit'),
    path('cbvdelete/<int:pk>/', views.Taskdeleteview.as_view(), name='cbvdelete'),
]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)