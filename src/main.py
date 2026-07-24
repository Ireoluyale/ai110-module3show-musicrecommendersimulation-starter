"""
Command line runner for the Music Recommender Simulation.

This file helps you quickly run and test your recommender.

You will implement the functions in recommender.py:
- load_songs
- score_song
- recommend_songs
"""

try:
    # Works with: python -m src.main   (run from the project root)
    from src.recommender import load_songs, recommend_songs
except ModuleNotFoundError:
    # Works with: python src/main.py   (run with src/ on the path)
    from recommender import load_songs, recommend_songs


# A diverse set of listener profiles to exercise the recommender.
# Each has real matches in data/songs.csv so the rankings are meaningful.
PROFILES = [
    ("High-Energy Pop", {"genre": "pop", "mood": "happy", "energy": 0.9}),
    ("Chill Lofi", {"genre": "lofi", "mood": "chill", "energy": 0.4}),
    ("Deep Intense Rock", {"genre": "rock", "mood": "intense", "energy": 0.9}),
    # --- Adversarial / edge-case profiles: designed to probe the scoring logic ---
    ("Conflicting: sad but hyped", {"genre": "pop", "mood": "melancholy", "energy": 0.95}),
    ("Out-of-range energy", {"genre": "lofi", "mood": "chill", "energy": 5.0}),
    ("Nonexistent genre/mood", {"genre": "polka", "mood": "ecstatic", "energy": 0.5}),
    ("Case mismatch", {"genre": "Pop", "mood": "Happy", "energy": 0.82}),
    ("Genre steamroll", {"genre": "lofi", "mood": "intense", "energy": 0.91}),
]


def print_recommendations(name: str, user_prefs: dict, songs: list, k: int = 5) -> None:
    recommendations = recommend_songs(user_prefs, songs, k=k)

    # Header describing the profile we recommended for.
    profile = f"genre={user_prefs['genre']}, mood={user_prefs['mood']}, energy={user_prefs['energy']}"
    print()
    print("=" * 52)
    print(f"  {name}: top {len(recommendations)} for {profile}")
    print("=" * 52)

    for rank, (song, score, explanation) in enumerate(recommendations, start=1):
        print(f"\n  {rank}. {song['title']:<22} by {song['artist']}")
        print(f"     Score: {score:.2f}")
        print(f"     Why:")
        # explanation is the reasons joined with ", " -> show one per line.
        for reason in explanation.split(", "):
            print(f"       - {reason}")

    print("\n" + "=" * 52)


def main() -> None:
    songs = load_songs("data/songs.csv")
    print(f"Loaded songs: {len(songs)}")

    for name, user_prefs in PROFILES:
        print_recommendations(name, user_prefs, songs)


if __name__ == "__main__":
    main()
