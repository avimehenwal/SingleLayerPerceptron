#!/usr/bin/env python3

"""
Implement Single Layer Perceptron Algorithm for OR gate
"""

import coloredlogs, logging
from pandas import *


# Create a logger object
logger = logging.getLogger(__name__)
coloredlogs.install(level='DEBUG', logger=logger)

# Some examples.
# logger.debug("this is a debugging message")
# logger.info("this is an informational message")
# logger.warning("this is a warning message")
# logger.error("this is an error message")
# logger.critical("this is a critical message")

training_data = [
    ([1,1], True),
    ([0,0], False),
]

test_data = [
    ([0,1]),
    ([1,0]),
]

training_dataframe = DataFrame(training_data)
test_dataframe     = DataFrame(test_data)

logger.info("Training Dataset Size : {}".format(len(training_data)))
logger.debug("Given Dataset\n{}".format(training_dataframe))