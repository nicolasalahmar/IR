import multiprocessing
from atpbar import register_reporter


def start_processes(reporter, nprocesses, queue, task):
    for i in range(nprocesses):
        p = multiprocessing.Process(target=worker, args=(reporter, task, queue))
        p.start()


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
