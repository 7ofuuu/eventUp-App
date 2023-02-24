from django.contrib.auth.decorators import login_required
from django.urls import path

from .views import superuser, del_user, edit_user
from .views import logout, Login, Signup, ForgetPassword, Activate, ConsolidatedView

urlpatterns = [
    path('login', Login.as_view(), name='login'),
    path('signup', Signup.as_view(), name='signup'),
    path('logout', login_required(logout), name='logout'),
    path('activate/<uidb64>/<token>/', Activate.as_view(), name='activate'),
    path('forget-password/<uidb64>/<token>', ForgetPassword.as_view(), name='forget_password'),

    path('superuser/', login_required(superuser), name='superuser'),
    path('edit_user/<username>', login_required(edit_user), name='edit_user'),
    path('delete-user/<username>', login_required(del_user), name='delete_user'),

    path('consolidated-view-all', login_required(ConsolidatedView.as_view()), name='consolidated_view_all'),
    path('consolidated-view-tema_event/<tema_event>', login_required(ConsolidatedView.as_view()), name='consolidated_tema_event'),
    path('consolidated-view-username/<username>', login_required(ConsolidatedView.as_view()), name='consolidated_username'),
]
