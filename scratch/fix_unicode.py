import re

def fix_ambiguous_chars(file_path):
    # Mapping of Cyrillic look-alikes to Latin counterparts
    replacements = {
        '\u0430': 'a', # Cyrillic a
        '\u0410': 'A', # Cyrillic A
        '\u0435': 'e', # Cyrillic e
        '\u0415': 'E', # Cyrillic E
        '\u043e': 'o', # Cyrillic o
        '\u041e': 'O', # Cyrillic O
        '\u0440': 'p', # Cyrillic p
        '\u0420': 'P', # Cyrillic P
        '\u0441': 'c', # Cyrillic c
        '\u0421': 'C', # Cyrillic C
        '\u0443': 'y', # Cyrillic u (looks like y)
        '\u0445': 'x', # Cyrillic x
        '\u0425': 'X', # Cyrillic X
        '\u0456': 'i', # Cyrillic i
        '\u00a0': ' ', # Non-breaking space
    }
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Rule: Replace only if NOT between > and < (not in text content)
    # This is a bit tricky with regex but we can do it line by line 
    # and focus on tags and styles.
    
    # 1. Styles and Scripts blocks are easy targets
    def replace_in_code_block(match):
        text = match.group(0)
        for cyr, lat in replacements.items():
            text = text.replace(cyr, lat)
        return text

    # Replace in <style>
    content = re.sub(r'(?si)<style>.*?</style>', replace_in_code_block, content)
    # Replace in <script>
    content = re.sub(r'(?si)<script>.*?</script>', replace_in_code_block, content)
    
    # 2. Replace in HTML tags (attributes like class, etc.)
    def replace_in_tags(match):
        tag = match.group(0)
        # We only want to replace in attributes, not in the tag name itself (though tag names shouldn't have them either)
        for cyr, lat in replacements.items():
            tag = tag.replace(cyr, lat)
        return tag

    content = re.sub(r'<[^>]+>', replace_in_tags, content)

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print("Optimization finished. Look-alike characters replaced in code blocks and tags.")

if __name__ == "__main__":
    fix_ambiguous_chars('index.html')
