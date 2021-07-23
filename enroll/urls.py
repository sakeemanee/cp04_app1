from django.urls import path
from . import views
from enroll import views

app_name='enroll'
urlpatterns = [
   
    path('', views.base1, name="base1"),
    path('addandshow', views.add_show, name="addandshow"),
    #path('base1/', views.add_show2, name="addandshow2"),
    path('delete/<int:id>/', views.delete_data, name="deletedata"),
    path('<int:id>/', views.update_data, name="updatedata"),
    
    
    
]
