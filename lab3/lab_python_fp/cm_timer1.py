import time


class cm_timer1:
    def __enter__(self):
        self.start_time = time.perf_counter()
        return self.start_time

    def __exit__(self, type, value, traceback):
        elapsed_time = time.perf_counter() - self.start_time
        self.start_time = None

        print(f'elapsed time: {elapsed_time} seconds')
