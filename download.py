import os
import pytz
import requests
from pprint import pprint
from urllib import urlretrieve
from datetime import datetime, timedelta


if __name__ == '__main__':
    base_url = 'http://www.pastpages.org/api/beta/screenshots'
    this_directory = os.path.dirname(os.path.realpath(__file__))
    end_time = datetime(2014, 11, 2, 0, 0, 0).replace(
        tzinfo=pytz.timezone("US/Pacific")
    )
    start_time = end_time - timedelta(days=7)
    payload = {
        'site__slug': 'drudge-report',
        'timestamp__gte': start_time.isoformat(),
        'timestamp__lte': end_time.isoformat(),
        'limit': 50,
    }
    r = requests.get(base_url, params=payload)
    # Fetch all the images
    url_list = [o['html'] for o in r.json()['objects'] if o['html']]
    # Fetch the images
    length = len(url_list)
    for i, url in enumerate(url_list):
        print "Fetching archive %s/%s" % (i+1, length)
        urlretrieve(url, os.path.join('screenshots', url.split("/")[-1]))
