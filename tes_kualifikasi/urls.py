from django.urls import path
from tes_kualifikasi.views import *

app_name = 'tes-kualifikasi'

urlpatterns = [
    path('data/kualifikasi', data_kualifikasi_view, name='data-kualifikasi'),
    path('pertanyaan/kualifikasi', pertanyaan_kualifikasi_view, name='pertanyaan-kualifikasi'),
]
