import logging
import traceback

try:
    a = [1, 2 , 3]
    val = a[4]
except:
    logging.error("The error is %s", traceback.format_exc())
