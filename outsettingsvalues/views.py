# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic import TemplateView
import django.conf.global_settings as global_settings_current
from django.conf import settings

class BaseView(TemplateView):
    template_name = 'outsettingsvalues/index.html'

    def get_context_data(self, **kwargs):
        context = super(BaseView, self).get_context_data(**kwargs)
        # temp = {}
        # for i in dir(global_settings_current):
        #     temp[i] = dir(i)
        # context['settings_LMS'] = settings.LMS_BASE
        # context['settings_CMS'] = settings.CMS_BASE
        # context['settings_list'] = temp

        return context
