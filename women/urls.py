from django.contrib import admin
from django.urls import path, include, re_path

from women.views import pageNotFound, WomenHome, about, AddPage, ShowPost, WomenCategory, RegisterUser, \
    LoginUser, logout_user, ContactFormView
from  django.views.decorators.cache import cache_page

urlpatterns = [
    # path('', index, name='home'),
    # path('about/', about, name='about'),
    # path('addpage/', addpage, name='add_page'),
    # path('contact/', contact, name='contact'),
    # path('login/', login, name='login'),
    # path('post/<slug:post_slug>/', show_post, name='post'),
    # path('category/<int:cat_id>/', show_category, name='category'),

    path('', WomenHome.as_view(), name='home'),
    path('about/', about, name='about'),
    path('addpage/', AddPage.as_view(), name='add_page'),
    path('contact/', ContactFormView.as_view(), name='contact'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('post/<slug:post_slug>/', ShowPost.as_view(), name='post'),
    path('category/<slug:cat_slug>/', WomenCategory.as_view(), name='category'),
]

handler404 = pageNotFound