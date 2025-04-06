import math
import random
import numpy as np
import pandas as pd
def compute_utility(user_features, song_features, epoch, s):
    """Compute utility U based on user preferences and song preferences"""
    dot = user_features.dot(song_features)
    ee = (1.0 - 1.0 * math.exp(-1.0 * epoch / s))
    return dot * ee

def iterative_mean(old, new, t, start_constant):
    """Compute the new mean, Added startConstant for low penalty in starting phase"""
    t += start_constant
    return ((t-1) / t) * old + (1/t) * new

def update_features(user_features, song_features, rating, t, start_constant):
    return iterative_mean(user_features, song_features * rating, float(t)+1.0, start_constant)

def get_song_features(song, n_feature):
    """Feature of particular song"""
    if isinstance(song, pd.Series):
        return song[-n_feature:]
    elif isinstance(song, pd.DataFrame):
        return get_song_features(pd.Series(song.loc[song.index[0]]), n_feature)
    else:
        raise TypeError("{} should be a Series or DataFrame".format(song))