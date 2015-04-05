from src.decorators import log_execution_time

import time

@log_execution_time
def func():
    time.sleep(10)

func()
