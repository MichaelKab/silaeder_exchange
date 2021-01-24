#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.urls import path
from . import views
from .views import SignUpView, ApplicationView
urlpatterns = [
    path('', views.main, name="home_page"),

    path('pr', views.cob, name="prof_page"),
    path('pr/edit', views.edit_profile, name="prof_page_edit"),
    path('signup/', SignUpView.as_view(), name=''),
    path('signup/', SignUpView.as_view(), name=''),
    path('edit/application/<int:pk>/', views.edit_application, name='post-detail'),
    # path('', views.main, name="home_page"),
]
# ApplicationView.as_view(),