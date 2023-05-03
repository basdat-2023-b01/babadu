from django.urls import path, include

urlpatterns = [
    path('', include('base.urls')),
    path('authentication/', include('authentication.urls')),
    path('pertandingan/', include('pertandingan.urls')),
    path('event/', include('event.urls')),
]
