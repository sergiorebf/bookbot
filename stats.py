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

def sort_on(item):
    return item["num"]

def build_sorted_char_list(dictionary):
    result = []
    for ch, num in dictionary.items():
        result.append({"char": ch, "num": num})
    result.sort(key=sort_on, reverse = True)
    return result