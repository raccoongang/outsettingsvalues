"""
Out settings values view.
"""
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.views.generic import TemplateView


class BaseView(TemplateView):
    """
    View output settings values, make search on them.
    """

    template_name = 'outsettingsvalues/index.html'

    @staticmethod
    def load_settings(setting_name=None):
        """
        Forms settings dict from django.conf settings.
        """
        settings_list = {}
        setting_name = setting_name or ''
        for settings_field in dir(settings):
            field_value = getattr(settings, settings_field)
            if callable(field_value):
                continue
            if setting_name == '':
                settings_list[settings_field] = field_value
            elif setting_name.upper() in settings_field.upper():
                settings_list[settings_field] = field_value
        return settings_list

    def get_context_data(self, **kwargs):
        """
        Display settings.
        """
        context = super(BaseView, self).get_context_data(**kwargs)
        settings_list = self.load_settings(self.request.GET.get("setting_name"))
        context['settings_list'] = settings_list
        return context
