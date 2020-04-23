
from pathlib import Path
import os
from loguru import logger
import sys
from Py import SCRIPT

ROOTER = SCRIPT.ROOTER


class Worker:

    _logger = None

    @staticmethod
    def set_logger(logger_):
        Worker._logger = logger_

    def work(self, x=ROOTER):
        self._logger.info("convert FROM pdf folder TO csv {}", x())
        return x()
