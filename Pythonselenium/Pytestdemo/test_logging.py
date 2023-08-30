import logging


def test_loggingDemo():
    logger = logging.getLogger(__name__)
    filehandler = logging.FileHandler("logfile.log")
    formatter = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s :(message)s")
    filehandler.setFormatter(formatter)
    logger.addHandler(filehandler)
    # setting levels   debug>>info>>warning>>error>>critical
    logger.setLevel(logging.DEBUG)

    logger.debug("debugging statement is printed")
    logger.info("info is printed")
    logger.warning("warning message is printed")
    logger.error("error statement is printed")
    logger.critical("critical statement is printed")
