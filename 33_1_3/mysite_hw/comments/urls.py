from django.urls import path
from django.urls import re_path
from comments.views import static_comments_new, static_comments_edit, static_comments_etc, dynamic_number_id, dynamic_del_ed, \
                           checking_smth1, checking_smth2, checking_smth3

urlpatterns = [
    path('new', static_comments_new),
    path('edit', static_comments_edit),
    path('etc', static_comments_etc),
    path('<int:number>/', dynamic_number_id),
    path('<int:number>/<str:act>', dynamic_del_ed),
    #  -------
    re_path(r'^\d{2}\w{3}$', checking_smth1),
    re_path(r'^\d{1}-\w{1}-\d{1}$', checking_smth2),
    re_path(r'(?P<phone_number>0(67|68|96|97|98|50|66|95|99|63|73|93|91)-\d{3}-\d{2}-\d{2})/$', checking_smth3)
]