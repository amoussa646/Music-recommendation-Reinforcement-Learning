# Music Recommendation System

A Python-based music recommendation system that uses a combination of exploration and exploitation strategies to provide personalized song recommendations based on user preferences and ratings.

## Features

- Interactive command-line interface for user preferences and ratings
- Personalized song recommendations based on:
  - User's initial feature preferences (genres, decades, etc.)
  - User's song ratings
  - Temporal exploration-exploitation balance
- Support for 21 different musical features including:
  - Decades (1980s-2020s)
  - Genres (Pop, Rock, Country, Folk, Dance, etc.)
  - Musical characteristics (Electric, Acoustic, etc.)

## Requirements

- Python 3.x
- Required packages (see requirements.txt):
  - numpy==2.2.4
  - pandas==1.4.1

## Installation

1. Clone the repository:

```bash
git clone <repository-url>
cd music_recommender
```

2. Install the required packages:

```bash
pip install -r requirements.txt
```

3. Ensure you have the songs data file (`songs.csv`) in the `data/` directory.

## Usage

1. Run the main script:

```bash
python main.py
```

2. Follow the interactive prompts:
   - Select your preferred music features from the provided list
   - Rate initial songs to help the system understand your preferences
   - Receive and rate recommendations
   - Continue getting new recommendations as desired

## How It Works

The recommendation system uses a hybrid approach:

1. **Initial Setup**:

   - Users select preferred musical features
   - System provides initial songs for rating

2. **Recommendation Algorithm**:

   - Uses a greedy approach with epsilon-greedy exploration
   - Balances exploration of new songs with exploitation of known preferences
   - Considers temporal aspects of recommendations
   - Updates user preferences based on ratings

3. **Feature Updates**:
   - System continuously learns from user ratings
   - Adjusts recommendations based on evolving preferences

## Project Structure

- `main.py`: Entry point of the application
- `config.py`: Configuration settings and constants
- `data_loader.py`: Handles loading of song data
- `recommender.py`: Core recommendation algorithms
- `ui.py`: User interface and interaction handling
- `utils.py`: Utility functions for calculations and data processing
- `data/`: Directory containing song data
