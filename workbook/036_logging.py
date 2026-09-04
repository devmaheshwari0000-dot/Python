# Example 36: Logging basics
# Topics: logging module
import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
logger.info('This is an info message')

# Task: configure logging to write to a file and rotate daily
