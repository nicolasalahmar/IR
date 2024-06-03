import os

from dotenv import load_dotenv

load_dotenv()


n = int(os.getenv('ncores'))
nprocesses = int(os.getenv('nprocesses'))
ntasks = int(os.getenv('ntasks'))
