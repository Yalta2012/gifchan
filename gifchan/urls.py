from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from gifchan import views
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
	path('', views.homepage, name='homepage'),
	path('accounts/', include('accounts.urls')),
	path('<slug:slug>/', include('threads.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
handler404 = 'gifchan.views.handling404'	