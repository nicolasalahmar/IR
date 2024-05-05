from Helper.ORM import fetch_new_records
from multiprocessing import Pool

from Helper.timing import Timing
from intermediary_dataset.insert import insert_records, create_table

if __name__ == '__main__':
    create_table()

    # get records from dataset 4252114_7
    records1 = fetch_new_records('dataset1.db', 'intermediary_dataset/partially_processed_dataset1.db', 100)

    # number of processes to be run (12 because my pc has 6 physical cores and 12 logical cores)
    n = 12

    # split the fetched records in to 12 lists in order to be processed
    chunk_size = int(len(records1) / n)
    records1 = [records1[i:i + chunk_size] for i in range(0, len(records1), chunk_size)]

    timing = Timing('Full Operation Timing')
    with timing as t:
        with Pool(n) as p:
            p.map(insert_records, records1)
