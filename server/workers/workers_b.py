from loguru import logger
from pathlib import Path
import os
import sys
from Py import convertcoma

converter_us = convertcoma.converter_us()


def set_logger(logger_):
    global logger
    logger = logger_


def work(x):
    logger.info("CSV-2 version FROM csv folder {}", x)
    return converter_us(x)
