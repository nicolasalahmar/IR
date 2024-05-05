import multiprocessing

from atpbar import register_reporter

from intermediary_dataset.insert import insert_records


def start_processes(reporter, nprocesses, queue):
    for i in range(nprocesses):
        p = multiprocessing.Process(target=worker, args=(reporter, insert_records, queue))
        p.start()


def add_to_queue(records1, queue):
    for i, rec in enumerate(records1):
        name = 'task {}'.format(i)
        queue.put((name, rec))


def join_queue(nprocesses, queue):
    for i in range(nprocesses):
        queue.put(None)
        queue.join()


def worker(reporter, task, queue):
    register_reporter(reporter)
    while True:
        args = queue.get()
        if args is None:
            queue.task_done()
            break
        task(*args)
        queue.task_done()
