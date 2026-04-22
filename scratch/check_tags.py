import re

def check_html_balance(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Remove scripts and styles to avoid false positives
    content = re.sub(r'<script.*?>.*?</script>', '', content, flags=re.DOTALL)
    content = re.sub(r'<style.*?>.*?</style>', '', content, flags=re.DOTALL)
    # Remove self-closing tags and comments
    content = re.sub(r'<!--.*?-->', '', content, flags=re.DOTALL)
    content = re.sub(r'<[^>]+/>', '', content)
    
    tags = re.findall(r'<(/?)([a-zA-Z0-9]+)', content)
    stack = []
    void_tags = {'area', 'base', 'br', 'col', 'embed', 'hr', 'img', 'input', 'link', 'meta', 'param', 'source', 'track', 'wbr'}
    
    for is_closing, tag_name in tags:
        tag_name = tag_name.lower()
        if tag_name in void_tags:
            continue
        
        if is_closing:
            if not stack:
                print(f"Extra closing tag: </{tag_name}>")
            else:
                top = stack.pop()
                if top != tag_name:
                    print(f"Tag mismatch: expected </{top}>, found </{tag_name}>")
                    stack.append(top) # Put it back to continue
        else:
            stack.append(tag_name)
            
    if stack:
        print(f"Unclosed tags: {stack}")
    else:
        print("All tags balanced (excluding void tags).")

check_html_balance('index.html')
