from config import FEATURES, NFEATURE, S, START_CONSTANT
import numpy as np

from utils import get_song_features, update_features 
def get_user_preferences():
    """Get initial user preferences for features"""
    user_features = np.zeros(len(FEATURES))
    print("Select song features that you like")
    
    for i, feature in enumerate(FEATURES):
        print(f"{i+1}. {feature}")
    
    liked_feat = set()
    choice = "y"
    while choice.lower().strip() == "y":
        num = input("Enter number associated with feature: ")
        liked_feat.add(FEATURES[int(num)-1])
        choice = input("Do you want to add another feature? (y/n): ")
    
    for i, feature in enumerate(FEATURES):
        if feature in liked_feat:
            user_features[i] = 1.0 / len(liked_feat)
    
    return user_features

def get_user_ratings(recommender, user_features, num_songs=5):
    """Get initial user ratings for recommendations"""
    print(f"\n\nRate following {num_songs} songs. So that we can know your taste.\n")
    
    for t in range(num_songs):
        if t >= 10:
            recommendation = recommender.greedy_choice_no_t(user_features, t+1, S, 0.3)
        else:
            recommendation = recommender.greedy_choice(user_features, t+1, S)
        
        song_name = recommendation.index[0]
        
        user_rating = input(f'How much do you like "{song_name}" (1-10): ')
        user_rating = int(user_rating) / 10.0
        
        song_features = get_song_features(recommendation, NFEATURE)
        user_features = update_features(
            user_features, song_features, user_rating, t, START_CONSTANT
        )
        recommender.songs.loc[recommender.songs.index.isin(recommendation.index), 'last_t'] = t+1
        recommender.rated_songs.add(song_name)
    
    return user_features

def main_ui_loop(recommender, user_features):
    """Main user interface loop for recommendations"""
    while True:
        print("\nWait \n\n")
        recommendations = recommender.all_recommendation(user_features)
        
        for i, music in enumerate(recommendations):
            print(f"{i+1}. {music.index[0]}")
        
        print("\n\nRate songs one by one or leave it blank")
        for music in recommendations:
            song_name = music.index[0]
            if song_name in recommender.rated_songs:
                print("Song already rated")
                continue
            
            rating = input(f"Rate {song_name} (1/10): ").strip()
            if rating:
                recommender.rated_songs.add(song_name)
                song_features = get_song_features(music, NFEATURE)
                user_features = update_features(
                    user_features, song_features, int(rating), recommender.tot_reco, START_CONSTANT
                )
        
        choice = input("\nDo you want more recommendations? (y/n) ").strip().lower()
        if choice != 'y':
            break