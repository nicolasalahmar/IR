import os
import sys

from Offline.Helper.ORM import fetch_records


def collect_urls():
    records = fetch_records(model=os.getenv('model'), ds='../../' + os.getenv('dataset'))
    for record in records:
        print(record.text)
        sys.exit()


if __name__ == '__main__':
    collect_urls()
