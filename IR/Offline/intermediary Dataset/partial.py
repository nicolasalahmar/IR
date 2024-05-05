import time
from Helper.ORM import fetch_new_records
from multiprocessing import Pool
from insert import insert_records, create_table

if __name__ == '__main__':
    create_table()

    # get records from dataset
    records1 = fetch_new_records('../dataset1.db', 'partially_processed_dataset1.db')

    # number of processes to be run (12 because my pc has 6 physical cores and 12 logical cores)
    n = 12

    # split the fetched records in to 12 lists in order to be processed
    chunk_size = int(len(records1) / n)
    records1 = [records1[i:i + chunk_size] for i in range(0, len(records1), chunk_size)]

    start_time = time.time()
    with Pool(n) as p:
        p.map(insert_records, records1)
    elapsed_time = time.time() - start_time
    print('Elapsed Time: ', elapsed_time)
