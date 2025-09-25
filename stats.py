def words(text):
    return len(text.split())

def characters(text):
    letters = {}
    for ch in text.lower():
        if ch in letters:
            letters[ch] = letters[ch] + 1
        else:
            letters[ch] = 1
    return letters