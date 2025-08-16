def get_num_words(text):
    return len(text.split())

def get_char_counts(text):
    char_counts = {}
    for char in text:
        char = char.lower()
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1
    return char_counts

def formatted_dicts(get_char_counts):
    dicts = []
    for char, count in get_char_counts.items():
        dicts.append({"char": char, "num": count})
    dicts.sort(key = lambda x: x["num"], reverse = True)
    return dicts