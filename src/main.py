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


def main() -> None:
    songs = load_songs("data/songs.csv")
    print(f"Loaded songs: {len(songs)}")

    # Starter example profile
    user_prefs = {"genre": "pop", "mood": "happy", "energy": 0.8}

    recommendations = recommend_songs(user_prefs, songs, k=5)

    # Header describing the profile we recommended for.
    profile = f"genre={user_prefs['genre']}, mood={user_prefs['mood']}, energy={user_prefs['energy']}"
    print()
    print("=" * 52)
    print(f"  Top {len(recommendations)} recommendations for: {profile}")
    print("=" * 52)

    for rank, (song, score, explanation) in enumerate(recommendations, start=1):
        print(f"\n  {rank}. {song['title']:<22} by {song['artist']}")
        print(f"     Score: {score:.2f}")
        print(f"     Why:")
        # explanation is the reasons joined with ", " -> show one per line.
        for reason in explanation.split(", "):
            print(f"       - {reason}")

    print("\n" + "=" * 52)


if __name__ == "__main__":
    main()
