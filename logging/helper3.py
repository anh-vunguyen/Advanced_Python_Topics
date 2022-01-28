import logging

logger = logging.getLogger(__name__)

# Create Handler
stream_h = logging.StreamHandler()
file_h = logging.FileHandler('file.log')

# Set level and the format
stream_h.setLevel(logging.WARNING)
file_h.setLevel(logging.ERROR)

formatter = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
file_h.setFormatter(formatter)
stream_h.setFormatter(formatter)

logger.addHandler(stream_h)
logger.addHandler(file_h)

logger.warning('This is an warning')
logger.error('This is an error')
