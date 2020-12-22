#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.urls import path
from . import views
urlpatterns = [
    path('', views.main, name="home_page"),
    path('pr', views.cob, name="prof_page"),
    path('pr/edit', views.edit_profile, name="prof_page_edit"),

    # path('', views.main, name="home_page"),
]