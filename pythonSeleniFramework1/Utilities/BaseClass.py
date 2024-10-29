import inspect
import logging

import pytest


@pytest.mark.usefixtures("setup")
class BaseClass():
    pass                        # 'pass' is use when we want the class to do absolutely nothing

    def test_logsMethod(self):
        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)
        fileHandler = logging.FileHandler('Logfile.log')
        formatter = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(message)s")
        fileHandler.setFormatter(formatter)
        logger.addHandler(fileHandler)
        logger.setLevel(logging.INFO)

        return logger