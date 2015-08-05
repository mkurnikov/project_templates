from __future__ import division, print_function
# noinspection PyUnresolvedReferences
from py3compatibility import *

import pandas as pd
import numpy as np
from sklearn.pipeline import Pipeline, FeatureUnion

from src.base import get_train_data_target
import src.feature_sets as feature_sets
import settings


def get_feature_union():
    pass


def get_estimation_pipeline():
    pass


def get_overall_pipeline():
    return Pipeline([
        get_feature_union(),
        get_estimation_pipeline()
    ])


if __name__ == '__main__':
    dataset, target = get_train_data_target()
