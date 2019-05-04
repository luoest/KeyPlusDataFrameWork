import logging
import logging.config
from utilities.getFilePath import loggerFile

try:
    logging.config.fileConfig(loggerFile)
except:
    FileNotFoundError
logger = logging.getLogger('caseKeyAndData')

def info(message):
    logger.info(message)

def debug(message):
    logger.debug(message)

def warning(message):
    logger.warning(message)