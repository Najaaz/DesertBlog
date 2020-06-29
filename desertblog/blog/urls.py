from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('<int:post_id>/comments/', views.comments, name="comments"),
    path('<int:post_id>/add_comment/', views.add_comment, name="add_comment"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

