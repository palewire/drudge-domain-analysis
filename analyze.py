import os
import csv
from pprint import pprint
from urllib2 import urlparse


if __name__ == '__main__':
    this_dir = os.path.dirname(os.path.realpath(__file__))
    csv_dir = os.path.join(this_dir, 'hyperlinks')
    href_list = []
    for csv_name in os.listdir(csv_dir):
        csv_path = os.path.join(csv_dir, csv_name)
        data_list = csv.DictReader(open(csv_path, 'rb'))
        story_list = [r['url_href'] for r in data_list
            if r['url_is_story'] == 'True']
        for href in story_list:
            if href not in href_list:
                href_list.append(href)
    domain_dict = {}
    for href in href_list:
        domain = urlparse.urlparse(href).netloc
        try:
            domain_dict[domain] += 1
        except KeyError:
            domain_dict[domain] = 1
    domain_ranking = sorted(
        domain_dict.items(),
        key=lambda x:x[1],
        reverse=True
    )
    pprint(domain_ranking[:10])
