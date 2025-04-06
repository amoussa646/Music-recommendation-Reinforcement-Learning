DATA_DIR = "data/"
SONGS_FILE = "songs.csv"
NFEATURE = 21  # Number of Features
S = 50  # Hyper Parameter
START_CONSTANT = 5  # for low penalty in starting phase
FEATURES = [
    "1980s", "1990s", "2000s", "2010s", "2020s", 
    "Pop", "Rock", "Country", "Folk", "Dance", 
    "Grunge", "Love", "Metal", "Classic", "Funk", 
    "Electric", "Acoustic", "Indie", "Jazz", "SoundTrack", "Rap"
]