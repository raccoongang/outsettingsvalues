"""
Out settings values view.
"""
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import types

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

        :param setting_name: None or request.GET.get("setting_name")
        :return: settings_list
        """
        settings_list = {}
        for i in dir(settings):
            if callable(i) or isinstance(i, types.FunctionType) or i.startswith('__'):
                continue
            if setting_name is None:
                settings_list[i] = getattr(settings, i)
            elif setting_name.upper() in i:
                settings_list[i] = getattr(settings, i)
        return settings_list

    def get_context_data(self, **kwargs):
        """
        Display settings.

        :param kwargs: None
        :return: context
        """
        context = super(BaseView, self).get_context_data(**kwargs)
        settings_list = self.load_settings(self.request.GET.get("setting_name"))
        context['settings_list'] = settings_list
        return context
