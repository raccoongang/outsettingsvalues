"""
Test outsettingsvalues view.
"""
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.shortcuts import reverse
from django.test import Client, RequestFactory, TestCase
from mock import patch

from outsettingsvalues.views import BaseView


class TestBaseView(TestCase):
    """
    BaseView test class.
    """

    class _MockSetting:
        SCALAR_FIELD = 'scalar_field'
        DICT_FIELD = {'a': 1, 'b': 2}
        LIST_FIELD = ['ITEM1', 'ITEM2']

        def callable_item(self):
            return None

    def setUp(self):
        """
        Create mane instances for all test.

        """
        self.client = Client()
        self.baseview = BaseView()

    def test_status_code(self):
        """
        Test status code about get request of BaseView url without param setting_name.

        """
        request = self.client.get(reverse('base'))
        self.assertEquals(request.status_code, 200)

    def test_status_code_params(self):
        """
        Test status code about get request of BaseView url with param setting_name.

        """
        request = self.client.get(reverse('base'), {'setting_name': 'INSTALLED_APPS'})
        self.assertEquals(request.status_code, 200)

    @patch('outsettingsvalues.views.settings', _MockSetting())
    def test_load_settings(self):
        """
        Test load_settings static method with and without setting_name param.

        """
        load_with_arg = self.baseview.load_settings('LIST')
        self.assertEquals(self._MockSetting().LIST_FIELD, load_with_arg['LIST_FIELD'])
        load_without_arg = BaseView().load_settings()
        self.assertEquals(self._MockSetting().LIST_FIELD, load_without_arg['LIST_FIELD'])
        self.assertFalse(load_without_arg.get('callable_item'))

    def test_get_context_data_without_param(self):
        """
        Test get_context_data method with empty request param value.

        """
        request = RequestFactory().get(reverse('base'))
        view = self.baseview
        view.request = request
        context = view.get_context_data()

        self.assertTrue(context['settings_list']['INSTALLED_APPS'])

    def test_get_context_data_with_param(self):
        """
        Test get_context_data method with request param value.

        """
        request = RequestFactory().get(reverse('base'), {'setting_name': 'INSTALLED'})
        view = BaseView()
        view.request = request
        context = view.get_context_data()

        self.assertEquals(context['settings_list']['INSTALLED_APPS'], settings.INSTALLED_APPS)
