"""
Kai Cenat / IShowSpeed style viral moment detector.

Scores moments based on:
- Volume spikes
- Fast speech
- Excitement words
- Laughter and screaming
- Sudden topic changes
- Crowd reactions
- Short bursts of high energy
"""

EXCITEMENT_WORDS = {
    'no way', 'bro', 'crazy', 'what', 'wtf', 'insane',
    'oh my god', 'let\'s go', 'nah', 'yo', 'holy'
}


def score_segment(text: str) -> int:
    text = text.lower()
    score = 0

    for word in EXCITEMENT_WORDS:
        if word in text:
            score += 10

    if text.count('!') >= 2:
        score += 20

    if text.isupper() and len(text) > 5:
        score += 30

    return min(score, 100)
