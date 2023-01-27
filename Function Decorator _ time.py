import time

def execution_time(fn):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = fn(*args, **kwargs)
        end = time.time()
        print(f'Executed in {end - start} seconds.')
        return result
    return wrapper

@execution_time
def my_function():
    time.sleep(5)

my_function()