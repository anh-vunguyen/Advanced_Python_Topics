import time
import logging
from logging.handlers import TimedRotatingFileHandler

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# s, m, h, d, midnight, w0 (Monday), w1 (Tuesday)
handler = TimedRotatingFileHandler('timed_test.log', when='s', interval=5, backupCount=5)
logger.addHandler(handler)

for i in range(6):
    logger.info(f'Hello, world #{i}')
    time.sleep(5)
