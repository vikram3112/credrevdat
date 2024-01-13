import inspect
import logging


class Logging_class:
    @staticmethod
    def log_generator():
        name = inspect.stack()[1][3]
        logger =logging.getLogger(name)
        logfile =logging.FileHandler("C:\\Users\\Dreamer\\Documents\\pythonProject1\\pythonProject\\credkartjanproject\\Logs\\Runfile.log")
        format = logging.Formatter("%(asctime)s - %(levelname)s - %(name)s - %(funcName)s - %(message)s")
        logfile.setFormatter(format)
        logger.addHandler(logfile)
        logger.setLevel(logging.INFO)
        return logger


