import logging
class Baseclass:
    def getlogger(self):
        logger = logging.getLogger(__name__)
        filehandler = logging.FileHandler("logfile.log")
        formatter = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s :(message)s")
        filehandler.setFormatter(formatter)
        logger.addHandler(filehandler)
        # setting levels   debug>>info>>warning>>error>>critical
        logger.setLevel(logging.INFO)
        return logger
