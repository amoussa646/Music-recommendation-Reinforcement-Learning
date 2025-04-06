import numpy as np
from data_loader import load_songs
from recommender import Recommender
from ui import get_user_preferences, get_user_ratings, main_ui_loop
from config import NFEATURE

def main():
    # Initialize data and recommender
    songs_df = load_songs()
    recommender = Recommender(songs_df)
    
    # Get user preferences and initial ratings
    user_features = get_user_preferences()
    user_features = get_user_ratings(recommender, user_features)
    
    # Main recommendation loop
    main_ui_loop(recommender, user_features)

if __name__ == "__main__":
    main()