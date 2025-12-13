import logging

def start_logging():
    logging.basicConfig(level=logging.ERROR, format='%(message)s')
    logformat = logging.Formatter('[%(levelname)s] %(message)s')
    logfile = logging.FileHandler(filename='output.log', mode='w' , encoding='UTF-8')
    logfile.setFormatter(logformat)
    logger = logging.getLogger(__name__)
    logger.addHandler(logfile)
    logger.setLevel(logging.INFO)
    logger.propagate = True

    return logger
