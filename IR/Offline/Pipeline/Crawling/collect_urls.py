import os
import sys

from Offline.Helper.ORM import fetch_records
from Offline.Pipeline.preprocessor.find_url import find_url, find_full_urls


def collect_urls():
    f = open('collected_urls', 'w')
    records = fetch_records(model=os.getenv('model'), ds='../../' + os.getenv('dataset'))
    for record in records:
        urls= find_full_urls(record.text)
        for url in urls:
            f.write(str(url)+ '\n')

    f.close()

if __name__ == '__main__':
    collect_urls()
