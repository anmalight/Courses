from django.urls import path
from django.urls import re_path
from news.views import static_news_new, static_news_edit, static_news_etc, dynamic_number_id, dynamic_del_ed, \
                           checking_smth1, checking_smth2, checking_smth3

urlpatterns = [
    path('new', static_news_new),
    path('edit', static_news_edit),
    path('etc', static_news_etc),
    path('<int:number>/', dynamic_number_id),
    path('<int:number>/<str:act>', dynamic_del_ed),
    #  -------
    re_path(r'^\d{2}\w{3}$', checking_smth1),
    re_path(r'^\d{1}-\w{1}-\d{1}$', checking_smth2),
    re_path(r'(?P<phone_number>0(67|68|96|97|98|50|66|95|99|63|73|93|91)-\d{3}-\d{2}-\d{2})/$', checking_smth3)
]