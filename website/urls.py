#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.urls import path
from . import views
from .views import SignUpView, ApplicationView
from .views import ApplicationDeleteView
from django.contrib.auth import views as authViews

urlpatterns = [
    path('', views.main, name="home_page"),
    path('<pk>/delete/', views.delit_application),
    path('pr', views.cob, name="prof_page"),
    path('<pk>/show/', views.show_all_inf),
    path('<pk>/responding/', views.responding),
    path('pr/edit', views.edit_profile, name="prof_page_edit"),
    path('signup/', SignUpView.as_view(), name=''),
    #path('signup/', SignUpView.as_view(), name=''),
    #path('edit/application/<int:pk>/', views.edit_application, name='post-detail'),
    path('pr/exit/', authViews.LogoutView.as_view(next_page='/'), name='exit'),
    path("activate", views.activate)
    # path('', views.main, name="home_page"),
]
# ApplicationView.as_view(),