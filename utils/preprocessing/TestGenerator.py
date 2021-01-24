import numpy as np
import json
import os
import sys

from utils.preprocessing.DataGenerator import DataGenerator
from utils.Other import attentionLabelBaseMap
from utils.preprocessing.TestLoader import TestLoader

class TestGenerator(DataGenerator):
    def __init__(self, directory, batch_size, stride, pe_encoder_max_length, pe_decoder_max_length):
        
        self._pe_decoder_max_length = pe_decoder_max_length
        self._batch_count = 0
        self._loader = TestLoader(directory, pe_encoder_max_length, stride)

    def get_window_batch(self, label_as_bases=False):
        while True:
            self._batch_count += 1
               
            x_windows, read_id = self._loader.get_read()
            x_windows = np.array(x_windows)
            x_windows = np.reshape(x_windows, (x_windows.shape[0], x_windows.shape[1], 1))
            yield x_windows, read_id