import time


class Timing:
    def __init__(self, name):
        self.name = name

    def __enter__(self):
        self.start_time = time.time()
        return self

    def __exit__(self, exception_type, exception_value, exception_traceback):
        self.elapsed_time = time.time() - self.start_time
        print(f'{self.name} elapsed time:', self.elapsed_time)
