from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponseForbidden, HttpResponseBadRequest, HttpResponseNotAllowed

from datetime import datetime, date, timedelta
import requests, json

from ombudsman.models import ApiKeyGrant
from ombudsman.settings import AZURE_AD_ENDPOINT

def verify_user_camp_authorization(view_func):
    '''
    Checks that the `uc_api_key` query string parameter is present, and that its value is a valid
    User Camp API key.

    Also checks that the request method is GET.
    '''
    def decorator(request, *args, **kwargs):
        if request.method != "GET":
            return HttpResponseNotAllowed()

        try:
            api_key = request.GET['uc_api_key']
        except KeyError:
            return HttpResponseForbidden("403 Forbidden uc_api_key was missing")

        try:
            grant = ApiKeyGrant.objects.get(api_key=api_key)
        except (ObjectDoesNotExist, ValueError):
            return HttpResponseForbidden("403 Forbidden. The API key provided is invalid.")

        return view_func(request, *args, **kwargs)
    return decorator


def prepare_microsoft_authorization_header(view_func):
    '''
    Views with this decorator need to accept `microsoft_authorization_header`, a dictionary that contains the
    access token necessary to query the Microsoft Store Analytics API.
    '''
    def decorator(request, *args, **kwargs):
        # Make sure the query string contains the four required Azure AD parameters
        azure_ad = {}
        try:
            azure_ad['tenant_id'] = request.GET['azure_ad_tenant_id']
            azure_ad['client_id'] = request.GET['azure_ad_client_id']
            azure_ad['application_key'] = request.GET['azure_ad_application_key']
            azure_ad['app_id_uri'] = request.GET['azure_ad_app_id_uri']

        except KeyError:
            return HttpResponseBadRequest("400 Bad Request. Make sure all Azure AD parameters are present.")

        auth_data = {
            'resource': 'https://manage.devcenter.microsoft.com',
            'response_type': 'client_credentials',
            'client_id': azure_ad['client_id'],
            'client_secret': azure_ad['application_key'],
            'grant_type': 'client_credentials',
            'app_id_uri': azure_ad['app_id_uri'],
        }

        auth = requests.post(AZURE_AD_ENDPOINT.format(azure_ad['tenant_id']), data=auth_data)
        auth_response = json.loads(auth.text)

        token = auth_response['access_token']
        microsoft_authorization_header = {"Authorization": "Bearer {}".format(token)}

        return view_func(request, microsoft_authorization_header, *args, **kwargs)
    return decorator

def prepare_store_api_aggregate_parameters(view_func):
    '''
    Prepares a common set of parameters for all Store API requests
    '''
    def decorator(request, *args, **kwargs):
        # Since this data is often quite delayed, use a bigger time delta.
        today = date.today()
        start_date = today - timedelta(days=6)

        store_api_aggregate_parameters = {
            "applicationId": kwargs['app_store_id'],
            "orderby": "date desc",
            "startDate": str(start_date)
        }

        # Optional filter. If the request has ?filter=all, do not add the filter key to the eventual request
        # to the API.
        result_filter = request.GET.get('filter')
        if result_filter and result_filter != "none":
            store_api_aggregate_parameters['filter'] = result_filter

        # Optional groupby. Defaults to `date` for aggregate requests.
        groupby = request.GET.get('groupby')
        if groupby and groupby != "none":
            store_api_aggregate_parameters['groupby'] = groupby

        return view_func(request, store_api_aggregate_parameters, *args, **kwargs)
    return decorator

