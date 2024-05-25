from django.urls import path
from . import views

urlpatterns = [

    path('',views.LoginPageView.as_view(),name='login_page'),
    path('dashboard/',views.dashboard, name='dashboard'),
    path('generate_id/',views.generate_id, name="generate_id"),
    path('edit_Person/', views.edit_Person,name="edit_Person"),
    path('search/',views.search, name="search"),
    # path('filter_expired_persons/',views.filter_expired_persons,name="filter_expired_persons"),
    path('delete_person/<int:pk>/', views.delete_person, name= "delete_person"),
    path('logout/',views.logout, name='logout'),

]