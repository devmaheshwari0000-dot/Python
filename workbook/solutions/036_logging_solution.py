# Hints:
# - Configure logging.basicConfig and FileHandler; use logging.handlers.TimedRotatingFileHandler for rotation.

# Solution:
import logging
from logging.handlers import TimedRotatingFileHandler

logger = logging.getLogger('example')
logger.setLevel(logging.INFO)
handler = TimedRotatingFileHandler('app.log', when='D')
formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)

logger.info('Test log')
