from contextlib import contextmanager
import time


@contextmanager
def cm_timer2():
    try:
        start_time = time.perf_counter()
        yield start_time

    finally:
        elapsed_time = time.perf_counter() - start_time
        print(f'Elapsed time: {elapsed_time} seconds')
