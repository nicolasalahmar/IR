from ir_measures import MAP, P, R, MRR
import os
from dotenv import load_dotenv

load_dotenv()

qrels_path = os.getenv("qrels_path")
queries_path = os.getenv("queries_path")
run_path = os.getenv("run_path")

measures = [MAP(), P@10, R@10, MRR]

n = int(os.getenv('ncores'))
nprocesses = int(os.getenv('nprocesses'))
ntasks = int(os.getenv('ntasks'))
