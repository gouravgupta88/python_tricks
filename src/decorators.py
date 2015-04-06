from functools import partial, wraps

import time

#################################################################

def semi_partial(fn):
    """
    Decorates the wrapped decorator to call with or without arguments
    """
    @wraps(fn)
    def wrapped_fn(*args, **kwargs):
        if args:
            return fn(*args, **kwargs)
        else:
            return partial(wrapped_fn, **kwargs)
    return wrapped_fn

#################################################################

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

@semi_partial
def retry(fn, max_retries=1):
    """
    Executes wrapped function for max_retries mentioned if it is failing
    
    Usage:

    @retry(max_retries=5)
    def retry_main():
        print "Executing retry_main function"
        raise Exception("Testing retry decorator")
    """
    @wraps(fn)
    def wrapped_fn(*args, **kwargs):
        for retry in xrange(max_retries + 1):
            try:
                result = fn(*args, **kwargs)
                return result
            except Exception as e:
                print e
                print("Exception came in function: %s. Retrying it. "
                      "Retry no: %s" % (fn.__name__, retry + 1))
    return wrapped_fn

#################################################################