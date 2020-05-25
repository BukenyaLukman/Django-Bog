from django.urls import path
from blog.api.views import PostAPIView

app_name = 'blog'

urlpatterns = [
	path('',PostAPIView.as_view(),name='detail'),

]