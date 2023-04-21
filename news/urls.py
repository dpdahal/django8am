from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('api', views.NewsViewSet)

urlpatterns = [
    path('', views.index, name='index'),
    path('contact', views.contact, name='contact'),
    path('news', views.news, name='news'),
    path('category/<slug>', views.category_news, name='category'),
    path('news-details/<slug>', views.news_details, name='news_details'),
    path('page/<slug>', views.page, name='page'),
    path('news-api', views.news_api, name='news-api'),
    path('api/', include(router.urls)),

]
