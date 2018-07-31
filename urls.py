from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^POST/$', views.CommentRequest.as_view(), name = 'CommentRequest'),
    #url(r'^GET/$', views.StudentRequest.as_view(), name = 'StudentRequest'),
    url(r'^GET/(?P<student_id>[a-zA-Z0-9_.-]+)/(?P<course_id>[a-zA-Z0-9_.-]+)$', views.StudentRequest.as_view(), name = 'StudentRequest'),
]
