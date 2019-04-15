# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.views.generic import TemplateView

from .forms import SettingForm

import types

class BaseView(TemplateView):
    template_name = 'outsettingsvalues/index.html'


    def get_context_data(self, **kwargs):
        context = super(BaseView, self).get_context_data(**kwargs)
        settings_list = {}
        for i in dir(settings):
            if callable(i) or isinstance(i, types.FunctionType) or i.startswith('__'):
                continue
            settings_list[i] = getattr(settings, i)
        context['form'] = SettingForm(data=self.request.GET or None)
        if context['form'].is_valid():
            temp_list = {}
            for key in settings_list.keys():
                if context['form'].cleaned_data['setting_name'] in key:
                    temp_list[key] = settings_list[key]
            context['settings_list'] = temp_list
        else:
            context['settings_list'] = settings_list
        return context
