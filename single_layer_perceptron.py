"""
Module File to implement
Single Later Perceptron Algorithm
"""

import coloredlogs, logging
from pandas import *
import numpy as np

# Create a logger object
logger = logging.getLogger(__name__)
coloredlogs.install(level='DEBUG', logger=logger)


# Some examples.
# logger.debug("this is a debugging message")
# logger.info("this is an informational message")
# logger.warning("this is a warning message")
# logger.error("this is an error message")
# logger.critical("this is a critical message")



class PerceptronAlgorithm:
    """Perceptron Learning Algorithm implementation"""

    # class objects placeholder

    def __init__(self, training_data, test_data):
        """
        Constructor method
        Initalize initial Algorithm unknown values
        """
        # Fitting Data
        self.training_set = DataFrame(training_data)
        self.training_set.columns = ["Feature Vector", "Label"]
        # get dtypes, index, columns, and values
        # logger.debug("Data Types\n{}".format(self.training_set.dtypes))
        # logger.debug("columns\n{}".format(self.training_set.columns))
        # logger.debug("index\n{}".format(self.training_set.index))
        # logger.debug("values\n{}".format(self.training_set.values))
        # pandas.describe()
        
        self.training_set_dimentionality = len(self.training_set.iloc[0,0])
        self.test_dataset = DataFrame(test_data)
        # initial_weight = np.zeros(self.training_set.shape, dtype=int)
        initial_weight = [0, 0]
        self.training_set["Weight Vector"] = initial_weight
        # self.learning_rate = 
        # self.bias = 
        
        logger.info("Training Dataset Size : {}".format(self.training_set.shape))
        logger.debug("Given Dataset\n{}".format(self.training_set))
        logger.info("Dimentionality of Feature vector : {}".format(self.training_set_dimentionality))
        # logger.debug("Zero Weight vector initialized\n{}".format(self.weight_vector))

    def predict_label(self):
        pass

    def update_weight(self):
        pass

    def train():
        pass
