from django.core.urlresolvers import reverse
from django.test import TestCase, Client

import urllib

from ombudsman.models import ApiKeyGrant

class ApiValidationTestCase(TestCase):
    def setUp(self):
        self.client = Client(HTTP_HOST='ombudsman.user.camp')

    def test_api_validation(self):
        api_key_grant = ApiKeyGrant.objects.create(
            name = 'Tester McTesterson',
            email = 'tester@example.com',
            app_url = 'https://www.microsoft.com/en-ca/store/p/candy-crush-saga/9nblggh18846',
            )

        test_params = {
            # 'azure_ad_tenant_id': 'e2b1a758-a783-4095-8502-faf582f8b494',
            # 'azure_ad_client_id': 'c73741ae-30b7-4e60-bdab-620d95526fe3',
            # 'azure_ad_application_key': 'hunter2',
            # 'azure_ad_app_id_uri': 'http://example.com'
        }

        request_url_base = reverse('validate_auth') + "?"

        # 'validate_auth' is decorated by @verify_user_camp_api_key
        request_url = request_url_base + urllib.urlencode(test_params)
        response = self.client.get(request_url)

        # Returns 403 due to the absent uc_api_key field
        self.assertEqual(response.status_code, 403)

        # Try again, with a present but invalid uc_api_key
        test_params['uc_api_key'] = 'swordfish'

        request_url = request_url_base + urllib.urlencode(test_params)
        response = self.client.get(request_url)

        # Returns 403 due to the present but invalid uc_api_key
        self.assertEqual(response.status_code, 403)

        # Try again, with a present and valid uc_api_key
        test_params['uc_api_key'] = api_key_grant.api_key

        request_url = request_url_base + urllib.urlencode(test_params)
        response = self.client.get(request_url)

        # Works
        self.assertEqual(response.status_code, 200)
