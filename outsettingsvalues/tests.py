"""
Test outsettingsvalues view.
"""
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.shortcuts import reverse
from django.test import Client, RequestFactory, TestCase

from outsettingsvalues.views import BaseView


class TestBaseView(TestCase):
    """
    BaseView test class.
    """

    def setUp(self):
        """
        Create mane instances for all test.

        :return: None
        """
        self.client = Client()
        self.baseview = BaseView()

    def test_status_code(self):
        """
        Test status code about get request of BaseView url without param setting_name.

        :return: True or False
        """
        request = self.client.get(reverse('base'))
        self.assertEquals(request.status_code, 200)

    def test_status_code_params(self):
        """
        Test status code about get request of BaseView url with param setting_name.

        :return: True or False
        """
        request = self.client.get(reverse('base'), {'setting_name': 'INSTALLED_APPS'})
        self.assertEquals(request.status_code, 200)

    def test_load_settings(self):
        """
        Test load_settings static method with and without setting_name param.

        :return: True or False
        """
        load_with_arg = self.baseview.load_settings('INSTALLED')
        self.assertEquals(settings.INSTALLED_APPS, load_with_arg['INSTALLED_APPS'])
        load_without_arg = self.baseview.load_settings()
        self.assertEquals(settings.TEMPLATES, load_without_arg['TEMPLATES'])
        self.assertTrue((load_without_arg['INSTALLED_APPS']))

    def test_get_context_data_without_param(self):
        """
        Test get_context_data method with empty request param value.

        :return: True or False
        """
        request = RequestFactory().get(reverse('base'))
        view = self.baseview
        view.request = request
        context = view.get_context_data()

        self.assertTrue(context['settings_list']['INSTALLED_APPS'])

    def test_get_context_data_with_param(self):
        """
        Test get_context_data method with request param value.

        :return: True or False
        """
        request = RequestFactory().get(reverse('base'), {'setting_name': 'INSTALLED'})
        view = BaseView()
        view.request = request
        context = view.get_context_data()

        self.assertEquals(context['settings_list']['INSTALLED_APPS'], settings.INSTALLED_APPS)
