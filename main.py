#!/usr/bin/env python3

"""
Implement Single Layer Perceptron Algorithm for OR gate
"""

from single_layer_perceptron import PerceptronAlgorithm


training_data = [
    ([1,1], True),
    ([0,0], False),
]

test_data = [
    ([0,1]),
    ([1,0]),
]


ml_model = PerceptronAlgorithm(training_data, test_data)
# ml_model.train()