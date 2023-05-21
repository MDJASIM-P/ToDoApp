from django.urls import path
from .views import *
urlpatterns =[
    path('signup/', SignUp.as_view(), name='signup'),
    path('home/', Home.as_view(), name='home'),
    path('logout/', LogOut.as_view(), name='logout'),
    path('update/<int:id>', Update.as_view(), name='update'),
    path('delete/<int:id>', Delete.as_view(), name='delete')

]