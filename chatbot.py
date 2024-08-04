import random
import json
import pickle
import numpy as np

import nltk
from nltk.stem import WordNetLemmatizer

from tensorflow.keras.models import Sequential
from tenserflow.keras.layers import Dense, Activation, Dropout
from tenserflow.keras.optimisers import SGD

lemmatizer = WordNetLemmatizer

intents = json.loads(open('intents.jason').read())
