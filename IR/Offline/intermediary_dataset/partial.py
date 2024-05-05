import multiprocessing
from atpbar import find_reporter, flush
from Helper.ORM import fetch_new_records
from Helper.timing import Timing
from intermediary_dataset.insert import create_table, split_arr
from intermediary_dataset.multiprocess import start_processes, add_to_queue, join_queue

if __name__ == '__main__':
    create_table()

    # get records from dataset 4252114_7
    records1 = fetch_new_records('dataset1.db', 'intermediary_dataset/partially_processed_dataset1.db', 100)

    # number of processes to be run (12 because my pc has 6 physical cores and 12 logical cores)
    n = 12
    nprocesses = 12
    ntasks = 12

    # split the fetched records in to 12 lists in order to be processed
    records1 = split_arr(records1, n)

    # in order to time the execution of the script
    timing = Timing('Full Operation Timing')
    with timing as t:
        # all registered reporters are found here (for the progress bar)
        reporter = find_reporter()
        # create queue where all args of processes will be added
        queue = multiprocessing.JoinableQueue()
        # start the processes
        start_processes(reporter, nprocesses, queue)
        add_to_queue(records1, queue)
        join_queue(nprocesses, queue)
        flush()
