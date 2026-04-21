import re

def find_ambiguous_chars(file_path):
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
        '\u043d': 'n', # Not really lookalike but sometimes issues
        '\u00a0': ' ', # Non-breaking space
    }
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # We want to find these characters ONLY inside HTML tags attributes, CSS, or JS
    # Re-writing the file is safer with a controlled replacement
    
    # Pattern to match potential lookalikes
    lookalike_pattern = '[' + ''.join(replacements.keys()) + ']'
    
    stats = {}
    
    # Simple approach: find problematic characters in what looks like code
    # We'll check each line.
    lines = content.splitlines()
    new_lines = []
    
    for i, line in enumerate(lines):
        # We try to identify if the line contains code or visible text.
        # This is a heuristic. A better way is to avoid replacing them 
        # if they are between > and < (outside tags).
        
        # But wait, usually these characters are in class names or styles.
        # Let's find all occurrences and report.
        
        new_line = ""
        last_idx = 0
        
        # More robust: use regex to find where these might be hidden in code-like structures
        # For simplicity in this task, I will replace them if they are in typical code blocks:
        # 1. Inside <style> tags
        # 2. Inside <script> tags
        # 3. Inside HTML attributes like class="", id="", onclick=""
        
        # Actually, the quickest way to fix the warning for the USER who says 
        # "This document contains MANY ambiguous chars" is to 
        # check specifically for Cyrillic inside English-only contexts.
        
        # I'll just find them and print them first.
        for match in re.finditer(lookalike_pattern, line):
            char = match.group()
            pos = match.start()
            stats[char] = stats.get(char, 0) + 1
            
        new_lines.append(line) # Currently not changing anything
        
    print(f"Found ambiguous characters: {stats}")

if __name__ == "__main__":
    find_ambiguous_chars('index.html')
