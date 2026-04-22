import re

# Mapping of Latin characters that look like Cyrillic
latin_to_cyrillic = {
    'a': 'а', 'A': 'А',
    'e': 'е', 'E': 'Е',
    'o': 'о', 'O': 'О',
    'p': 'р', 'P': 'Р',
    'c': 'с', 'C': 'С',
    'y': 'у', 'Y': 'У',
    'x': 'х', 'X': 'Х',
    'i': 'і', 'I': 'І', # Less common in Russian but possible
    'T': 'Т', # Latin T and Cyrillic Т are different but look same
    'M': 'М',
    'H': 'Н',
    'K': 'К',
    'B': 'В',
}

def fix_mixed_scripts(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # We want to find words that are mostly Cyrillic but have some Latin characters
    # Or just strings that are clearly intended to be Russian
    
    def replace_func(match):
        word = match.group(0)
        # If word contains both Cyrillic and the specific Latin characters we know
        has_cyrillic = any('\u0400' <= c <= '\u04FF' for c in word)
        has_suspicious_latin = any(c in latin_to_cyrillic for c in word)
        
        if has_cyrillic and has_suspicious_latin:
            new_word = "".join(latin_to_cyrillic.get(c, c) for c in word)
            if new_word != word:
                print(f"Fixed: {word} -> {new_word}")
            return new_word
        return word

    # Match sequences of alphanumeric characters (including Cyrillic)
    # This is a bit broad but should work
    new_content = re.sub(r'[a-zA-Z\u0400-\u04FF]+', replace_func, content)
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(new_content)

fix_mixed_scripts('index.html')
