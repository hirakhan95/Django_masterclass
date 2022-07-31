from django.urls import path
from . import views

urlpatterns = [
    path('<int:num_pg>', views.page_num_view),
    path('<str:topic>/', views.news, name='topic-page')
]
