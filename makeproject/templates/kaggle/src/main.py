from __future__ import division, print_function
# noinspection PyUnresolvedReferences
from py3compatibility import *

import pandas as pd
import numpy as np
from sklearn.pipeline import Pipeline, FeatureUnion

from src.base import get_train_data_target
import settings


if __name__ == '__main__':
    dataset, target = get_train_data_target()
