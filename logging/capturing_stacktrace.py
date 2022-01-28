import logging

try:
    a = [1, 2, 3]
    val = a[4]
except IndexError as e:
    logging.error(e, exc_info=True)
