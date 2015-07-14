from __future__ import division, print_function
# noinspection PyUnresolvedReferences
from py3compatibility import *

import pandas as pd
import numpy as np

import settings

if __name__ == '__main__':
    original_dataset = pd.read_csv(settings.TRAIN_FILE)