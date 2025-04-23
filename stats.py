def get_word_count(content):
    words = content.split()
    return len(words)

def get_symbol_counts(words):
    count_dict = {}
    for word in words:
        norm = word.lower()
        if norm in count_dict:
            count_dict[norm] += 1
        else:
            count_dict[norm] = 1
    return count_dict

def get_sorted_symbol_count(counts):
    #dict is symb -> count
    #return val is ORDERED by count
    sorted_results = dict(sorted(counts.items(), key=lambda symb: symb[1], reverse=True))
    
    return sorted_results