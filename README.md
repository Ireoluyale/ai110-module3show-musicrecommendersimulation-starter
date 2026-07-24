# 🎵 Music Recommender Simulation

## Project Summary

In this project you will build and explain a small music recommender system.

Your goal is to:

- Represent songs and a user "taste profile" as data
- Design a scoring rule that turns that data into recommendations
- Evaluate what your system gets right and wrong
- Reflect on how this mirrors real world AI recommenders

Replace this paragraph with your own summary of what your version does.

---

## How The System Works

Explain your design in plain language.

Some prompts to answer:

Real-world recommendation systems like Spotify and YouTube predict what a listener will enjoy next by combining two big ideas: collaborative filtering, which looks at the behavior of millions of other users to find people with similar taste ("listeners like you also loved this"), and content-based filtering, which compares the measurable attributes of songs themselves—tempo, energy, mood, genre—to what a user already likes. They feed on enormous streams of data, especially implicit signals like plays, skips, and completion rates, and run them through a two-stage pipeline that first scores each candidate track and then ranks the results into an ordered, diverse playlist. My version prioritizes a simple, transparent content-based approach: it represents each song as a vector of normalized numerical features (energy, valence, danceability, acousticness, tempo) plus categorical tags (genre and mood), scores every song by how closely it matches the user's preferences rather than by raw magnitude, and then ranks those scores to return the top matches. We deliberately favor explainability and control—weighting genre above mood and closeness above popularity—over the scale and complexity of a full collaborative-filtering system, so we can clearly see why each song was recommended.



- What features does each `Song` use in your system
  - For example: genre, mood, energy, tempo
- What information does your `UserProfile` store
- How does your `Recommender` compute a score for each song
- How do you choose which songs to recommend

You can include a simple diagram or bullet list if helpful.

---

## Getting Started

### Setup

1. Create a virtual environment (optional but recommended):

   ```bash
   python -m venv .venv
   source .venv/bin/activate      # Mac or Linux
   .venv\Scripts\activate         # Windows

2. Install dependencies

```bash
pip install -r requirements.txt
```

3. Run the app:

```bash
python -m src.main
```

### Running Tests

Run the starter tests with:

```bash
pytest
```

You can add more tests in `tests/test_recommender.py`.

---

## Sample Recommendation Output

Paste a sample of your recommender's output here as a text block so a reader can see what it produces:

```
# e.g.:
# User profile: genre=indie, mood=chill, energy=low
# Recommendations:
#   1. ...
#   2. ...
#   3. ...
```
====================================================
  Top 5 recommendations for: genre=pop, mood=happy, energy=0.8
====================================================

  1. Sunrise City           by Neon Echo
     Score: 3.98
     Why:
       - genre match (pop) +2.0
       - mood match (happy) +1.0
       - energy close to 0.8 (+0.98)

  2. Gym Hero               by Max Pulse
     Score: 2.87
     Why:
       - genre match (pop) +2.0
       - energy close to 0.8 (+0.87)

  3. Rooftop Lights         by Indigo Parade
     Score: 1.96
     Why:
       - mood match (happy) +1.0
       - energy close to 0.8 (+0.96)

  4. Concrete Kings         by Blockwise
     Score: 1.00
     Why:
       - energy close to 0.8 (+1.00)

  5. Grease & Groove        by The Funktion
     Score: 0.98
     Why:
       - energy close to 0.8 (+0.98)







====================================================
  High-Energy Pop: top 5 for genre=pop, mood=happy, energy=0.9
====================================================

  1. Sunrise City           by Neon Echo
     Score: 3.92
     Why:
       - genre match (pop) +2.0
       - mood match (happy) +1.0
       - energy close to 0.9 (+0.92)

  2. Gym Hero               by Max Pulse
     Score: 2.97
     Why:
       - genre match (pop) +2.0
       - energy close to 0.9 (+0.97)

  3. Rooftop Lights         by Indigo Parade
     Score: 1.86
     Why:
       - mood match (happy) +1.0
       - energy close to 0.9 (+0.86)

  4. Storm Runner           by Voltline
     Score: 0.99
     Why:
       - energy close to 0.9 (+0.99)

  5. Voltage Drop           by Circuit Saints
     Score: 0.95
     Why:
       - energy close to 0.9 (+0.95)

====================================================
====================================================

====================================================
  Chill Lofi: top 5 for genre=lofi, mood=chill, energy=0.4
====================================================

  1. Midnight Coding        by LoRoom
     Score: 3.98
     Why:
       - genre match (lofi) +2.0
       - mood match (chill) +1.0
       - energy close to 0.4 (+0.98)

  2. Library Rain           by Paper Lanterns
     Score: 3.95
     Why:
       - genre match (lofi) +2.0
       - mood match (chill) +1.0
       - energy close to 0.4 (+0.95)

  3. Focus Flow             by LoRoom
     Score: 3.00
     Why:
       - genre match (lofi) +2.0
       - energy close to 0.4 (+1.00)

  4. Spacewalk Thoughts     by Orbit Bloom
     Score: 1.88
     Why:
       - mood match (chill) +1.0
       - energy close to 0.4 (+0.88)

  5. Paper Boats            by Hollow Pines
     Score: 0.98
     Why:
       - energy close to 0.4 (+0.98)

====================================================

====================================================
  Deep Intense Rock: top 5 for genre=rock, mood=intense, energy=0.9
====================================================

  1. Storm Runner           by Voltline
     Score: 3.99
     Why:
       - genre match (rock) +2.0
       - mood match (intense) +1.0
       - energy close to 0.9 (+0.99)

  2. Gym Hero               by Max Pulse
     Score: 1.97
     Why:
       - mood match (intense) +1.0
       - energy close to 0.9 (+0.97)

  3. Voltage Drop           by Circuit Saints
     Score: 0.95
     Why:
       - energy close to 0.9 (+0.95)

  4. Iron Verdict           by Ashen Crown
     Score: 0.93
     Why:
       - energy close to 0.9 (+0.93)

  5. Sunrise City           by Neon Echo
     Score: 0.92
     Why:
       - energy close to 0.9 (+0.92)

====================================================

====================================================
  Conflicting: sad but hyped: top 5 for genre=pop, mood=melancholy, energy=0.95
====================================================

  1. Gym Hero               by Max Pulse
     Score: 2.98
     Why:
       - genre match (pop) +2.0
       - energy close to 0.95 (+0.98)

  2. Sunrise City           by Neon Echo
     Score: 2.87
     Why:
       - genre match (pop) +2.0
       - energy close to 0.95 (+0.87)

  3. Moonlit Sonata Redux   by Camille Rossi
     Score: 1.35
     Why:
       - mood match (melancholy) +1.0
       - energy close to 0.95 (+0.35)

  4. Voltage Drop           by Circuit Saints
     Score: 1.00
     Why:
       - energy close to 0.95 (+1.00)

  5. Iron Verdict           by Ashen Crown
     Score: 0.98
     Why:
       - energy close to 0.95 (+0.98)

====================================================

====================================================
  Out-of-range energy: top 5 for genre=lofi, mood=chill, energy=5.0
====================================================

  1. Midnight Coding        by LoRoom
     Score: -0.58
     Why:
       - genre match (lofi) +2.0
       - mood match (chill) +1.0
       - energy close to 5.0 (+-3.58)

  2. Library Rain           by Paper Lanterns
     Score: -0.65
     Why:
       - genre match (lofi) +2.0
       - mood match (chill) +1.0
       - energy close to 5.0 (+-3.65)

  3. Focus Flow             by LoRoom
     Score: -1.60
     Why:
       - genre match (lofi) +2.0
       - energy close to 5.0 (+-3.60)

  4. Spacewalk Thoughts     by Orbit Bloom
     Score: -2.72
     Why:
       - mood match (chill) +1.0
       - energy close to 5.0 (+-3.72)

  5. Iron Verdict           by Ashen Crown
     Score: -3.03
     Why:
       - energy close to 5.0 (+-3.03)

====================================================

====================================================
  Nonexistent genre/mood: top 5 for genre=polka, mood=ecstatic, energy=0.5
====================================================

  1. Dust Road Home         by Wren Callahan
     Score: 0.98
     Why:
       - energy close to 0.5 (+0.98)

  2. Velvet Hours           by Sable Moon
     Score: 0.98
     Why:
       - energy close to 0.5 (+0.98)

  3. Island Time            by Palm Riddim
     Score: 0.95
     Why:
       - energy close to 0.5 (+0.95)

  4. Blue Alley Blues       by Miles Fontaine
     Score: 0.94
     Why:
       - energy close to 0.5 (+0.94)

  5. Midnight Coding        by LoRoom
     Score: 0.92
     Why:
       - energy close to 0.5 (+0.92)

====================================================

====================================================
  Case mismatch: top 5 for genre=Pop, mood=Happy, energy=0.82
====================================================

  1. Sunrise City           by Neon Echo
     Score: 1.00
     Why:
       - energy close to 0.82 (+1.00)

  2. Concrete Kings         by Blockwise
     Score: 0.98
     Why:
       - energy close to 0.82 (+0.98)

  3. Grease & Groove        by The Funktion
     Score: 0.96
     Why:
       - energy close to 0.82 (+0.96)

  4. Rooftop Lights         by Indigo Parade
     Score: 0.94
     Why:
       - energy close to 0.82 (+0.94)

  5. Night Drive Loop       by Neon Echo
     Score: 0.93
     Why:
       - energy close to 0.82 (+0.93)

====================================================

====================================================
  Genre steamroll: top 5 for genre=lofi, mood=intense, energy=0.91
====================================================

  1. Midnight Coding        by LoRoom
     Score: 2.51
     Why:
       - genre match (lofi) +2.0
       - energy close to 0.91 (+0.51)

  2. Focus Flow             by LoRoom
     Score: 2.49
     Why:
       - genre match (lofi) +2.0
       - energy close to 0.91 (+0.49)

  3. Library Rain           by Paper Lanterns
     Score: 2.44
     Why:
       - genre match (lofi) +2.0
       - energy close to 0.91 (+0.44)

  4. Storm Runner           by Voltline
     Score: 2.00
     Why:
       - mood match (intense) +1.0
       - energy close to 0.91 (+1.00)

  5. Gym Hero               by Max Pulse
     Score: 1.98
     Why:
       - mood match (intense) +1.0
       - energy close to 0.91 (+0.98)

====================================================










**Screenshot or video** *(optional)*: <!-- Insert a screenshot or demo video link here -->

---

## Experiments You Tried

Use this section to document the experiments you ran. For example:

- What happened when you changed the weight on genre from 2.0 to 0.5
- What happened when you added tempo or valence to the score
- How did your system behave for different types of users

---

## Limitations and Risks

Summarize some limitations of your recommender.

Examples:

- It only works on a tiny catalog
- It does not understand lyrics or language
- It might over favor one genre or mood

You will go deeper on this in your model card.

---

## Reflection

Read and complete `model_card.md`:

[**Model Card**](model_card.md)

Write 1 to 2 paragraphs here about what you learned:

- about how recommenders turn data into predictions
- about where bias or unfairness could show up in systems like this



