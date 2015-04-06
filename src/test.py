from src.decorators import log_execution_time, retry

import time

@log_execution_time
def func():
    time.sleep(10)

func()

@retry(max_retries=5)
def retry_main():
    print "Executing retry_main function"
    raise Exception("Testing retry decorator")

retry_main()