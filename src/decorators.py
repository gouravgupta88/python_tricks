from functools import partial, wraps

import time

#################################################################

@partial
def log_execution_time(fn):
    """
    Measure execution time of wrapped function

    Usage:

    User wants to measure execution time of func() method defined below
    @log_execution_time
    def func():
        time.sleep(10)

    func()
    Output: Time taken in executing 'func' function: 10.0005829334 secs
    """
    @wraps(fn)
    def wrapped_fn(*args, **kwargs):
        start = time.time()
        result = fn(*args, **kwargs)
        end = time.time()
        print("Time taken in executing '%s' function: %s secs" % (fn.__name__,
                                                                  end-start))
        return result
    return wrapped_fn

#################################################################
