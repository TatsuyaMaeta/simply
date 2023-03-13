from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name=""),
    path("register", views.register, name="register"),
    path("my-login", views.my_login, name="my-login"),
    path("dashboard", views.dashboard, name="dashboard"),
    path("profile-management", views.profile_management, name="profile-management"),
    path("user-logout", views.user_logout, name="user-logout"),
    path("delete-account", views.delete_account, name="delete-account"),
]
# ここにpathw書いた時点でviews.pyに続く名前のdefをちゃんと書くこと！
