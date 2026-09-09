# Task 4: Sentiment Analysis & Aspect-Based Opinion Mining

## Project Overview
An applied Natural Language Processing (NLP) pipeline developed for the **CodeAlpha Data Analytics Virtual Internship** (Intern ID: CA/DF1/271765)[cite: 1]. The project analyzes unstructured customer feedback, calculates emotional polarity using NLTK's VADER lexicon, generates lexical word clouds, and evaluates sentiment across hardware features to provide actionable product and marketing recommendations.

---

## 🎬 Video Demonstration
🎥 [Watch the Video Demonstration on LinkedIn](https://lnkd.in/p/dzMJj2qc)

## Technical Workflow
1. **Corpus Sanitization & Preprocessing:** 
   - Converted review strings to lowercase.
   - Removed URLs and non-alphabetic characters using Regular Expressions (`re`).
   - Filtered out English stopwords via NLTK to retain informative tokens.
2. **Lexicon-Based Sentiment Scoring:**
   - Evaluated reviews using NLTK's `SentimentIntensityAnalyzer` (VADER).
   - Classified feedback into three distinct tiers using normalized compound polarity scores:
     * **Positive:** Compound Score $\ge 0.05$
     * **Neutral:** $-0.05 <$ Compound Score $< 0.05$
     * **Negative:** Compound Score $\le -0.05$
3. **Rating Correlation & Validation:**
   - Cross-validated algorithmic compound scores against customer star ratings (1–5) to ensure statistical consistency between quantitative ratings and qualitative text.
4. **Lexical Mining (Word Clouds):**
   - Extracted high-contrast lexical clouds contrasting product satisfaction drivers against recurring friction points.
5. **Aspect-Level Opinion Mining:**
   - Segmented polarity distributions across core hardware aspects: *Audio*, *Battery*, *Comfort*, *Connectivity*, *Durability*, and *Support*.

---

## Key Business Insights & Recommendations
* **Audio Fidelity & Battery (Key Strengths):** Acoustic clarity, bass depth, and extended standby life drive the majority of positive sentiment.
  * *Action:* Anchor future product marketing campaigns on acoustic performance and long-haul travel battery reliability.
* **Durability & Materials (Critical Pain Point):** Physical headband failures and premature ear cushion wear account for over 70% of 1-star reviews.
  * *Action:* Upgrade structural joint components from brittle injection plastics to reinforced aluminum-alloy framing.
* **Bluetooth Stability (Firmware Optimization):** Frequent audio drops trigger customer frustration in 2-star reviews.
  * *Action:* Release an Over-The-Air (OTA) firmware update optimizing device polling intervals and reconnection protocols.

---

## Project Structure
```text
Task4_SentimentAnalysis/
├── sentiment_analysis_nlp.ipynb   # Complete step-by-step NLP analysis notebook
├── customer_reviews_dataset.csv     # Extracted and sanitized reviews dataset
└── README.md                        # Task documentation and report
