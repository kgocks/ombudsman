from django.core.mail import send_mail
from django.core.exceptions import ObjectDoesNotExist
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render

from datetime import datetime, date, timedelta
import json
import requests

from ombudsman.decorators import verify_user_camp_authorization, prepare_microsoft_authorization_header, \
                                prepare_store_api_aggregate_parameters
from ombudsman.forms import ApiKeyGrantForm
from ombudsman.helpers import get_all_analytics_pages
from ombudsman.models import ApiKeyGrant
from ombudsman.settings import API_ENDPOINTS

def home(request):
    if request.method == "POST":
        form = ApiKeyGrantForm(request.POST)

        if form.is_valid():
            api_key_grant = form.save()
            send_mail(
                'Your Ombudsman API Key',
                '''
Hello, {}!

Here is your Ombudsman API key: {}

If you need help using it, just reply to this email.

-- Your friends at User Camp
                '''.format(api_key_grant.name, api_key_grant.api_key),
                'User Camp <hello@user.camp>',
                 [api_key_grant.email],
                 fail_silently=False
            )

            return HttpResponseRedirect(reverse('home') + "?registered=True")

    else:
        form = ApiKeyGrantForm()

    registered = True if request.GET.get('registered') else False

    return render(request, 'home.html', {
        'form': form,
        'registered': registered
    })

@verify_user_camp_authorization
def validate_auth(request):
    return HttpResponse("200 Authorization succeeded")

@verify_user_camp_authorization
@prepare_microsoft_authorization_header
def reviews(request, microsoft_authorization_header, app_store_id):
    # Set up the request to the reviews endpoint.
    # This endpoint doesn't provide aggregated data, so it's a special case.

    # ...get a reasonable start date
    today = date.today()
    start_date = today - timedelta(days=3)

    # ...set filter and order params
    params = {
        "applicationId": app_store_id,
        "startDate": str(start_date),
        "orderby": "date desc"
    }

    # Only add the filter parameter to the eventual API request if it's present and has a non-default value
    result_filter = request.GET.get('filter')
    if result_filter and result_filter != "none":
        params['filter'] = result_filter

    # ...get all pages
    results = get_all_analytics_pages(API_ENDPOINTS['reviews'], params, microsoft_authorization_header)

    # ... filter results that don't have reviewTitle or reviewText
    reviews = []
    for review in results:
        if bool(review['reviewTitle']) or bool(review['reviewText']):
            reviews.append(review)

    # Return the properly-formatted biz
    return JsonResponse(reviews, safe=False)

@verify_user_camp_authorization
@prepare_store_api_aggregate_parameters
@prepare_microsoft_authorization_header
def acquisitions(request, microsoft_authorization_header, store_api_aggregate_parameters, app_store_id):

    results = get_all_analytics_pages(API_ENDPOINTS['acquisitions'],
                                        store_api_aggregate_parameters,
                                        microsoft_authorization_header)

    return JsonResponse(results, safe=False)

@verify_user_camp_authorization
@prepare_store_api_aggregate_parameters
@prepare_microsoft_authorization_header
def add_on_acquisitions(request, microsoft_authorization_header, store_api_aggregate_parameters, app_store_id):

    results = get_all_analytics_pages(API_ENDPOINTS['add_on_acquisitions'],
                                        store_api_aggregate_parameters,
                                        microsoft_authorization_header)

    return JsonResponse(results, safe=False)

@verify_user_camp_authorization
@prepare_store_api_aggregate_parameters
@prepare_microsoft_authorization_header
def installs(request, microsoft_authorization_header, store_api_aggregate_parameters, app_store_id):

    results = get_all_analytics_pages(API_ENDPOINTS['installs'],
                                        store_api_aggregate_parameters,
                                        microsoft_authorization_header)

    return JsonResponse(results, safe=False)

@verify_user_camp_authorization
@prepare_store_api_aggregate_parameters
@prepare_microsoft_authorization_header
def ratings(request, microsoft_authorization_header, store_api_aggregate_parameters, app_store_id):

    results = get_all_analytics_pages(API_ENDPOINTS['ratings'],
                                        store_api_aggregate_parameters,
                                        microsoft_authorization_header)

    return JsonResponse(results, safe=False)

@verify_user_camp_authorization
@prepare_store_api_aggregate_parameters
@prepare_microsoft_authorization_header
def ads_performance(request, microsoft_authorization_header, store_api_aggregate_parameters, app_store_id):

    results = get_all_analytics_pages(API_ENDPOINTS['ads_performance'],
                                        store_api_aggregate_parameters,
                                        microsoft_authorization_header)

    return JsonResponse(results, safe=False)

@verify_user_camp_authorization
@prepare_store_api_aggregate_parameters
@prepare_microsoft_authorization_header
def ad_campaign_performance(request, microsoft_authorization_header, store_api_aggregate_parameters, app_store_id):

    results = get_all_analytics_pages(API_ENDPOINTS['ad_campaign_performance'],
                                        store_api_aggregate_parameters,
                                        microsoft_authorization_header)

    return JsonResponse(results, safe=False)

@verify_user_camp_authorization
@prepare_store_api_aggregate_parameters
@prepare_microsoft_authorization_header
def errors(request, microsoft_authorization_header, store_api_aggregate_parameters, app_store_id):

    results = get_all_analytics_pages(API_ENDPOINTS['errors'],
                                        store_api_aggregate_parameters,
                                        microsoft_authorization_header)

    return JsonResponse(results, safe=False)






