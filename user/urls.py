from django.urls import path, include

from user import views


urlpatterns = [
    path('register/', views.register_view),
    path('login/', views.login_view),
    path('logout/', views.logout_view),
    path('profile/', views.profile_view),
    path('profile/delete/', views.delete_profile_view),
    path('auth/', views.auth, ),
    path('admin/', views.admin.site.urls),
    path('users/', include('users.urls')),

]