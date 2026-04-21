import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

with open('Полный прайс.txt', 'r', encoding='utf-8') as f:
    price_text = f.read()

# Make it look nice for white-space pre-wrap
price_html = f"""<div style="white-space: pre-wrap; font-family: 'Inter', sans-serif; font-size: 0.95rem; line-height: 1.6; color: var(--text-white); padding: 20px; background: rgba(0,0,0,0.2); border-radius: 8px; border: 1px solid var(--glass-border); margin-bottom: 30px;">
{price_text}
</div>"""

pattern = re.compile(r'(<h3 style="margin: 0; font-size: 1\.8rem;">Полный прайс-лист</h3>\s*</div>).*?(<div class="modal-footer" style="flex-wrap: wrap; flex-direction: column;">)', re.DOTALL)

new_html = pattern.sub(r'\1\n            ' + price_html + r'\n            \2', html)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(new_html)

print("Done")
