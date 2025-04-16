def analyze_text(text):
    filler_words = ['um', 'uh', 'like', 'you know']
    words = text.lower().split()
    filler_count = {fw: words.count(fw) for fw in filler_words}
    return {
        "filler_words": filler_count,
        "word_count": len(words),
    }