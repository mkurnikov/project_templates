from __future__ import division, print_function
# noinspection PyUnresolvedReferences
from py3compatibility import *

import os
### project root directory, for support to relative paths
PROJECT_ROOT = os.path.dirname(__file__)
DATA_DIRECTORY = os.path.join(PROJECT_ROOT, 'data')

### submittion files
SUBMIT_FILE_TEMPLATE = os.path.join(DATA_DIRECTORY, 'submit_{name}.csv')
SUBMIT_FILE = SUBMIT_FILE_TEMPLATE.format(name='')


### mongo stuff
from pymongo import MongoClient
_client = MongoClient()

# TODO: fill project name
_db = _client['{project_name}']
MONGO_DATABASE = _db

MONGO_GRIDSEARCH_COLLECTION = _db['grid_search']
MONGO_SUBMISSIONS_COLLECTION = _db['submissions']


### for pickled models
PICKLED_MODELS_DIR = os.path.join(PROJECT_ROOT, 'pickled_models')


### TODO: fill train.csv path, fill test.csv path
TRAIN_FILE = os.path.join(PROJECT_ROOT, '{train.csv path}')
TEST_FILE = os.path.join(PROJECT_ROOT, '{test.csv path}')

### TODO: fill target
TARGET = '{target}'


### logging stuff
LOG_ROOT = os.path.join(PROJECT_ROOT, 'log')










