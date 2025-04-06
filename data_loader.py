import pandas as pd
from config import DATA_DIR, SONGS_FILE, NFEATURE, S

def load_songs():
    """Load songs data and initialize last_t column"""
    songs = pd.read_csv(DATA_DIR + SONGS_FILE, index_col=0)
    songs.insert(0, 'last_t', -S)  # Initialize last_t column
    return songs