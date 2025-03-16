def count_words(text):
    words = text.split()
    return len(words)

def count_chars(text):
    num_chars = {}
    for c in text.lower():
        num_chars[c] = num_chars.get(c, 0) + 1
    return num_chars

def sort_char_count(dict):
    list = []
    for key in dict:
        list.append({"character": key, "count": dict[key]})
    return sorted(list, reverse=True, key=lambda d: d["count"])