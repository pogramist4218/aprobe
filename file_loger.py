import logging
from logging import handlers

configs = {
    "info": {
        "name": "info_logger",
        "level": logging.INFO,
        "filename": "./logs/messages.log",
        "mode": "a",
        "format": '%(asctime)s - %(message)s'
    },
    "error": {
        "name": "errors_logger",
        "level": logging.ERROR,
        "filename": "./logs/errors.log",
        "mode": "a",
        "format": '%(asctime)s - %(message)s'
    }
}

def logInfo(message):
    logger = getLogger("info")
    logger.info(message)

def logError(error):
    logger = getLogger("error")
    logger.error(error)

def getLogger(level):
    logger = logging.getLogger(configs[level]["name"])
    logger.setLevel(configs[level]["level"])
    logger.addHandler(get_file_handler(level))
    return logger

def get_file_handler(level):
   file_handler = logging.FileHandler(configs[level]["filename"], configs[level]["mode"])
   formatter = logging.Formatter(configs[level]["format"])
   file_handler.setFormatter(formatter)
   return file_handler
