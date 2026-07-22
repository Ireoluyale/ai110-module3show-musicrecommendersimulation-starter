from typing import List, Dict, Tuple, Optional
from dataclasses import dataclass

@dataclass
class Song:
    """
    Represents a song and its attributes.
    Required by tests/test_recommender.py
    """
    id: int
    title: str
    artist: str
    genre: str
    mood: str
    energy: float
    tempo_bpm: float
    valence: float
    danceability: float
    acousticness: float

@dataclass
class UserProfile:
    """
    Represents a user's taste preferences.
    Required by tests/test_recommender.py
    """
    favorite_genre: str
    favorite_mood: str
    target_energy: float
    likes_acoustic: bool

class Recommender:
    """
    OOP implementation of the recommendation logic.
    Required by tests/test_recommender.py
    """
    def __init__(self, songs: List[Song]):
        self.songs = songs

    def recommend(self, user: UserProfile, k: int = 5) -> List[Song]:
        # TODO: Implement recommendation logic
        return self.songs[:k]

    def explain_recommendation(self, user: UserProfile, song: Song) -> str:
        # TODO: Implement explanation logic
        return "Explanation placeholder"

def load_songs(csv_path: str) -> List[Dict]:
    """Read the CSV at csv_path into a list of song dicts, converting numeric fields to int/float."""
    import csv

    int_fields = {"id", "tempo_bpm"}
    float_fields = {"energy", "valence", "danceability", "acousticness"}

    songs: List[Dict] = []
    with open(csv_path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            song: Dict = {}
            for key, value in row.items():
                if key in int_fields:
                    song[key] = int(value)
                elif key in float_fields:
                    song[key] = float(value)
                else:
                    song[key] = value
            songs.append(song)
    return songs

def score_song(user_prefs: Dict, song: Dict) -> Tuple[float, List[str]]:
    """Score one song against user_prefs, returning (score, reasons) per the Phase 2 recipe."""
    # Algorithm Recipe (Phase 2):
    #   Start at 0 and add:
    #     Genre match       +2.0  (song.genre == user's favorite genre)
    #     Mood match        +1.0  (song.mood  == user's favorite mood)
    #     Energy similarity +0.0..+1.0  = 1.0 * (1 - |target_energy - song.energy|)
    #   Genre is the heaviest (coarse identity signal); mood refines it;
    #   energy is graded so it acts as the natural tiebreaker.
    score = 0.0
    reasons: List[str] = []

    if user_prefs.get("genre") == song.get("genre"):
        score += 2.0
        reasons.append(f"genre match ({song['genre']}) +2.0")

    if user_prefs.get("mood") == song.get("mood"):
        score += 1.0
        reasons.append(f"mood match ({song['mood']}) +1.0")

    target_energy = user_prefs.get("energy")
    if target_energy is not None:
        energy_points = 1.0 * (1 - abs(target_energy - song["energy"]))
        score += energy_points
        reasons.append(f"energy close to {target_energy} (+{energy_points:.2f})")

    return (score, reasons)

def recommend_songs(user_prefs: Dict, songs: List[Dict], k: int = 5) -> List[Tuple[Dict, float, str]]:
    """Score every song and return the top k as (song, score, explanation), highest first."""
    # Score every song in the catalog, then rank highest-first.
    # score_song is the "judge": it returns (score, reasons) for each song.
    scored = [
        (song, *score_song(user_prefs, song))  # -> (song, score, reasons)
        for song in songs
    ]

    # Sort by score, highest first.
    scored.sort(key=lambda item: item[1], reverse=True)

    # Return the top k, turning each song's reasons into a readable explanation.
    return [
        (song, score, ", ".join(reasons) if reasons else "no matching features")
        for song, score, reasons in scored[:k]
    ]
