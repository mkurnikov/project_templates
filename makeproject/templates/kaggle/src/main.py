from __future__ import division, print_function
# noinspection PyUnresolvedReferences
from py3compatibility import *

import pandas as pd
import numpy as np
from sklearn.pipeline import Pipeline, FeatureUnion

import settings


if __name__ == '__main__':
    dataset = pd.read_csv(settings.TRAIN_FILE)