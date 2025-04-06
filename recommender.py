import random
import math
import pandas as pd
from utils import compute_utility, get_song_features
from config import NFEATURE, S, START_CONSTANT
import numpy as np
class Recommender:
    def __init__(self, songs_df):
        self.songs = songs_df.copy()
        self.rated_songs = set()
        self.tot_reco = 0
        
    def best_recommendation(self, user_features, epoch, s):
        """Song with highest utility"""
        utilities = np.zeros(self.songs.shape[0])
        
        for i, (title, song) in enumerate(self.songs.iterrows()):
            song_features = get_song_features(song, NFEATURE)
            utilities[i] = compute_utility(user_features, song_features, epoch - song.last_t, s)
        return self.songs[self.songs.index == self.songs.index[utilities.argmax()]]
    
    def random_choice(self):
        """Random songs which aren't been rated yet"""
        song = self.songs.sample()
        while song.index[0] in self.rated_songs:
            song = self.songs.sample()
        return song
    
    def greedy_choice(self, user_features, epoch, s):
        """Greedy approach to the problem"""
        self.tot_reco += 1
        epsilon = 1 / math.sqrt(epoch+1)
        if random.random() > epsilon:  # choose the best
            return self.best_recommendation(user_features, epoch, s)
        else:
            return self.random_choice()
    
    def greedy_choice_no_t(self, user_features, epoch, s, epsilon=0.3):
        """Greedy approach with constant epsilon"""
        self.tot_reco += 1
        if random.random() > epsilon:  # choose the best
            return self.best_recommendation(user_features, epoch, s)
        else:
            return self.random_choice()
    
    def all_recommendation(self, user_features):
        """Top 10 songs using exploration and exploitation"""
        reco_songs = []
        for _ in range(10):
            song = self.greedy_choice_no_t(user_features, self.tot_reco, S)
            reco_songs.append(song)
            self.songs.loc[self.songs.index.isin(song.index), 'last_t'] = self.tot_reco
        return reco_songs