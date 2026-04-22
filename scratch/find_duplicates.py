import re
from collections import Counter

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

ids = re.findall(r'id=["\'](.*?)["\']', content)
duplicates = [id for id, count in Counter(ids).items() if count > 1]

if duplicates:
    print(f"Duplicate IDs found: {duplicates}")
    for id in duplicates:
        count = ids.count(id)
        print(f"ID '{id}' occurs {count} times.")
else:
    print("No duplicate IDs found.")
