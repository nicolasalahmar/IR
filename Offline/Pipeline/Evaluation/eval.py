import csv
import multiprocessing
import ir_measures
from atpbar import find_reporter, flush, atpbar
from Manual.intermediary_dataset.insert import split_arr
from Manual.intermediary_dataset.multiprocess import start_processes, join_queue
from Pipeline.Evaluation import measures, qrels_path, run_path, queries_path, n, nprocesses
import os
from dotenv import load_dotenv

load_dotenv()


def evaluate(index):
    qrels = ir_measures.read_trec_qrels(qrels_path)

    create_run_file(index)

    run = ir_measures.read_trec_run(run_path)

    return ir_measures.calc_aggregate(measures, qrels, run)


def create_run_file(index):
    queries = open(queries_path, 'r')
    queries = csv.reader(queries)

    next(queries)
    queries = split_arr(queries, n)

    reporter = find_reporter()
    # create queue where all args of processes will be added
    queue = multiprocessing.JoinableQueue()
    # start the processes
    start_processes(reporter, nprocesses, queue, write_to_run_file)
    add_to_queue(queries, queue, index)
    join_queue(nprocesses, queue)
    flush()


def write_to_run_file(name, queries, index):
    for i in atpbar(range(len(queries)), name=name):
        res = index.search(queries[i][1])
        for doc_no, score, rank in res:
            f = open(run_path, 'a')
            f.write(f'{queries[i][0]} 0 {doc_no} {rank} {score} IR\n')
            f.close()


def add_to_queue(records1, queue, index):
    for i, rec in enumerate(records1):
        name = 'task {}'.format(i)
        queue.put((name, rec, index))
