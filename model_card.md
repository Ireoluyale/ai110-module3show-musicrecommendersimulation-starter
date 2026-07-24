# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name  

**VibeFinder 1.0**

It matches you to songs that fit your vibe.

---

## 2. Intended Use  

VibeFinder suggests songs from a small catalog. You tell it your favorite genre, favorite mood, and how much energy you want. It gives you back the top few songs that fit.

It assumes you can describe your taste in those simple terms. It also assumes your taste is in the catalog.

**Intended use:** classroom learning. It is a demo to explore how recommender scoring works.

**Not intended use:** real music apps or real users. It is too small and too simple for that. Do not use it to make choices that matter, like what a business should promote. It has known biases (see Section 6).

---

## 3. How the Model Works  

The model gives every song a score and then picks the highest ones.

It looks at three things. First, does the song's genre match your favorite genre? That is worth the most points. Second, does the mood match your favorite mood? That is worth some points. Third, how close is the song's energy to the energy you want? The closer it is, the more points it gets.

It adds those points up for each song. Then it sorts all the songs from highest score to lowest. You get the top five.

Think of it like a judge giving each song a grade, then ranking them. Genre is the biggest part of the grade. Energy is the tiebreaker when two songs are close.

This uses the starter scoring rules. No scoring changes were made yet.

---

## 4. Data  

The catalog has 20 songs. Each song has a title, artist, genre, mood, energy, tempo, valence, danceability, and acousticness.

There are many genres: pop, lofi, rock, ambient, jazz, synthwave, indie pop, hip hop, classical, reggae, edm, country, r&b, metal, folk, blues, and funk. There are many moods too, like happy, chill, intense, and relaxed.

I did not add or remove any songs. This is the starter dataset.

The data has gaps. Most genres have only one song. That makes it hard to give someone a full list in their favorite genre. Some moods also show up only once. So real, varied music taste is not fully covered.

---

## 5. Strengths  

The system works well when your taste is clear and in the catalog.

The top pick is almost always right. If your genre and mood exist, that song lands at #1 with a near-perfect score. This matched my intuition every time I tested it.

It is strong for users with extreme energy tastes. Someone who wants very high energy gets loud songs. Someone who wants very low energy gets calm songs. The energy rule sorts those cases nicely.

It also does well when a genre has more than one song, like lofi. Then it can fill several slots with real matches, not filler.

---

## 6. Limitations and Bias 

Where the system struggles or behaves unfairly. 

One clear weakness I discovered is that the way the model scores "energy" quietly under-serves users with moderate energy tastes. The energy score is calculated as `1 - |target_energy - song_energy|`, which is a symmetric distance, so a listener who wants middle-of-the-road energy (around 0.5) is never more than 0.5 away from any song in the catalog. In my experiments, that user's energy scores were squeezed into a narrow 0.53–1.0 band, while a listener who wanted very high energy (0.95) got the full 0.07–0.98 range. In practice this means the energy signal — which is supposed to act as the tiebreaker — has roughly half the resolving power for balanced listeners, so their rankings come out mushier and less personalized than those of users with extreme energy preferences. In other words, the scoring unintentionally favors people with strong high- or low-energy tastes and treats the "just wants something in the middle" listener as a lower-priority case.

---

## 7. Evaluation  

How you checked whether the recommender behaved as expected. 

I evaluated the model by running four contrasting user profiles through `recommend_songs` and inspecting the top-5 results and their scores:

- **EDM high-energy** — genre `edm`, mood `energetic`, target energy `0.95`
- **Lofi chill** — genre `lofi`, mood `chill`, target energy `0.40`
- **Pop happy** — genre `pop`, mood `happy`, target energy `0.80`
- **Moderate/balanced** — genre `indie pop`, mood `happy`, target energy `0.50`

For each profile I looked at whether the top pick was an exact genre + mood match, and how much the remaining slots reflected the user's taste versus filler chosen only by energy distance.

**What surprised me:** how sharp the drop-off is after the genre match. Every profile's #1 result scored a near-perfect ~3.98–4.00 (genre +2, mood +1, energy ~1), but the #2 result often plunged to ~1–2 because almost every genre appears only once in the catalog. The Moderate/balanced profile surprised me most: its top score was only **3.74** (not ~4.0) and its energy scores were visibly compressed — even its filler picks (Dust Road Home, Velvet Hours) clustered around 0.95–0.98 — which confirmed the energy-gap weakness described in Section 6.

### Pairwise comparisons

- **EDM vs. Lofi chill:** EDM's list is dominated by high-energy tracks (Voltage Drop 0.95, Gym Hero 0.93, Iron Verdict 0.97) even across different genres, while Lofi chill pulls low-energy tracks (Midnight Coding 0.42, Library Rain 0.35). This makes sense — the energy term rewards proximity to the target, so a 0.95 target pulls loud songs up and a 0.40 target pulls quiet ones up.
- **EDM vs. Pop happy:** EDM fills its lower slots with any loud song regardless of genre (metal, rock), whereas Pop happy keeps surfacing pop-adjacent, upbeat tracks (Sunrise City, Gym Hero, Rooftop Lights). Pop sits at a moderate-high energy (0.80), so its list stays musically closer to the top pick, while EDM's extreme 0.95 target lets energy override genre for the filler.
- **EDM vs. Moderate/balanced:** EDM's scores span a wide range (4.00 down to 0.87) but Moderate/balanced's collapse quickly (3.74 down to 0.95) with tightly bunched fillers. This is the compression effect: a 0.50 target is never far from any song, so energy stops acting as a meaningful tiebreaker for the balanced listener.
- **Lofi chill vs. Pop happy:** These are near mirror images — Lofi chill favors calm, acoustic-leaning tracks (Spacewalk Thoughts, Paper Boats) while Pop happy favors bright, danceable ones. That is exactly what the low vs. high energy targets should do, and both keep their exact-genre matches on top.
- **Lofi chill vs. Moderate/balanced:** Lofi chill has multiple in-genre matches (three lofi songs), giving it a clean high-scoring block, while Moderate/balanced has only one indie pop match and then drops off. This shows the system rewards users whose taste is well-represented in the catalog and under-serves those whose genre appears once.
- **Pop happy vs. Moderate/balanced:** Both share the `happy` mood and overlap on Sunrise City and Rooftop Lights, but Pop happy scores them higher because its 0.80 energy is closer to those upbeat songs than the balanced 0.50 target. Same songs, different ordering — a direct demonstration that the energy value, not just genre/mood, is steering the ranking.

No numeric evaluation metrics were created; this was a qualitative inspection of ranked outputs.

---

## 8. Future Work  

Here are three things I would change next.

1. **Fix the energy rule.** Right now it under-serves people who want middle energy (see Section 6). I would use a scoring shape that gives them a fair spread too.

2. **Use more song features.** The songs have danceability, valence, and acousticness, but the model ignores them. The user profile even has a "likes acoustic" flag that is never used. I would wire those in.

3. **Group similar genres.** Right now "pop" and "indie pop" are treated as strangers. I would give partial credit for close genres. This would open up the results and reduce the filter bubble.

---

## 9. Personal Reflection  

I learned that a recommender is really just a scoring rule. The rule decides who gets good results and who does not.

The surprising part was the energy math. A tiny formula ended up treating "middle" users worse than "extreme" users. I did not expect a fairness problem to hide in one line.

Now I look at music apps differently. When they suggest the same kinds of songs over and over, I think about the scoring behind it. Small choices in the rules shape what everyone hears.
