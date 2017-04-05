import json, requests

from ombudsman.settings import ROOT_API_ENDPOINT

def get_all_analytics_pages(endpoint, params, headers):
    '''
    Processes the initial endpoint request, and any @nextLinks it returns.

    Returns one big list of all data points (the ['Value'] key in each response dictionary).
    '''
    pages = []
    print "Getting data for {}".format(endpoint)
    response = requests.get(endpoint, params=params, headers=headers)
    page = json.loads(response.text)

    pages.append(page)

    next_link = page.get('@nextLink')

    while next_link:
        print "...processing @nextLink..."
        next_link = ROOT_API_ENDPOINT + next_link
        next_link = next_link.replace(" ", "+")

        # We don't use `params` in this request, because the @nextLink contains them
        response = requests.get(next_link, headers=headers)
        page = json.loads(response.text)
        pages.append(page)
        next_link = page.get('@nextLink')

    results = []
    for page in pages:
        try:
            results += page['Value']
        except KeyError:
            continue

    return results
