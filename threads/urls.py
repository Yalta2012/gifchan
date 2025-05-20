from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from threads import views
from django.conf import settings

app_name = 'threads'

urlpatterns = [
    path('', views.board,name='board'),
	path('create_thread/',views.create_thread,name='create_thread'),
	path('<int:id>', views.thread, name = 'thread'),
	path('<int:id>/answer/',views.create_message,name='create_message'),
	path('<int:id>/answer/<int:message_id>',views.create_message,name='create_message')
]