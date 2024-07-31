from django.urls import path, include
from Goods import views


urlpatterns = [
    path('', views.main, name='index'),
    path('authentication/', include('Goods.authentication.urls')),
    path('back-office/', include('Goods.back-office.urls')),
    path('user/', include('Goods.user.urls')),  
    path('userss/', views.category, name='category'),
    # path('det<int:id>/', views.detail_post_view, name='detailled'),
    # path('post<int:postid>/preference/<int:userpreference>/', views.postpreference, name='postpreference'),
    # path('supsubtract/<int:id>/', views.substruct, name='subtract'), 
]