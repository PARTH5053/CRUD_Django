from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name = ''),
    path('register/',views.register, name='register'),
    path('login/',views.login, name='login'),
    path('logout/',views.logout, name='logout'),
    path('dashboard/',views.dashboard, name='dashboard'),

    path('add-record',views.create_record,name = 'add-record'),
    path('update-record/<int:pk>',views.update_record, name='update-record'),
    path('view-record/<int:pk>',views.view_record, name='view-record'),
    path('delete-record/<int:pk>',views.delete_record, name='delete-record'),

]