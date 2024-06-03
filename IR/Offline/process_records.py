import multiprocessing
import os

from atpbar import find_reporter, flush
from dotenv import load_dotenv

from Offline.Helper.ORM import fetch_records, create_table
from Offline.Helper.timing import Timing
from Offline.Manual.intermediary_dataset.insert import split_arr, insert_records, add_to_queue
from Offline.Manual.intermediary_dataset.multiprocess import start_processes, join_queue

load_dotenv()


if __name__ == '__main__':
    create_table(os.getenv('model'))
    create_table(os.getenv('new_model'))

    # get records from dataset
    with Timing('Fetching New Records Timing'):
        records1 = fetch_records()

    # number of processes to be run (12 because my pc has 6 physical cores and 12 logical cores)
    n = int(os.getenv('ncores'))
    nprocesses = int(os.getenv('nprocesses'))
    ntasks = int(os.getenv('ntasks'))

    # split the fetched records in to 12 lists in order to be processed
    records1 = split_arr(records1, n)

    # in order to time the execution of the script
    with Timing('Full Operation Timing'):
        # all registered reporters are found here (for the progress bar)
        reporter = find_reporter()
        # create queue where all args of processes will be added
        queue = multiprocessing.JoinableQueue()
        # start the processes
        start_processes(reporter, nprocesses, queue, insert_records)
        add_to_queue(records1, queue)
        join_queue(nprocesses, queue)
        flush()
