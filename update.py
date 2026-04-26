import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

new_content = content

# 1. Update Footer Addresses Order
new_addresses = """                <div class="footer-col" style="font-size: 0.85rem;">
                    <h4>Адреса точек</h4>
                    <p>пр. Победы, 67</p>
                    <p>ул. Калинина, 158</p>
                    <p>пр. Победы, 96а</p>
                    <p>ул. Гагарина, 3а</p>
                    <p>Гагарина, 7а</p>
                    <p>Аустрина, 139</p>
                    <p>ул. Саранская, 76</p>
                </div>"""
new_content = re.sub(
    r'<div class="footer-col"[^>]*>\s*<h4>Адреса точек</h4>.*?</div>',
    new_addresses,
    new_content,
    flags=re.DOTALL
)

# 2. Update Footer Bottom links
new_footer_bottom = """<div class="footer-bottom">
                © 2026 ЮМАКС — Сеть шиномонтажей, г. Пенза | <a href="#" onclick="openPrivacyModal()">Политика конфиденциальности</a> | <a href="https://neuro-mark.ru/" target="_blank" class="dev-link">Разработано: https://neuro-mark.ru/</a> | Права защищены 2026.
            </div>"""
new_content = re.sub(
    r'<div class="footer-bottom">.*?</div>',
    new_footer_bottom,
    new_content,
    flags=re.DOTALL
)

# 3. Replace SUV Icon
new_content = re.sub(
    r'<img[^>]*icons8-внедорожник-96\.png[^>]*>',
    r'<span class="material-symbols-outlined">suv</span>',
    new_content
)

# 4. Standardize Pricing Tables Headers
def process_table(match):
    table_content = match.group(0)
    thead_match = re.search(r'(<thead[^>]*>.*?</thead>)', table_content, flags=re.DOTALL)
    if thead_match:
        thead_full = thead_match.group(1)
        # Remove all th styles - carefully matching only th tag, not thead
        new_thead = re.sub(r'<th\b[^>]*>', '<th>', thead_full)
        ths = re.findall(r'<th>(.*?)</th>', new_thead, flags=re.DOTALL)
        if ths:
            new_ths = []
            for i, th_text in enumerate(ths):
                align = 'left' if i == 0 else ('right' if i == len(ths)-1 else 'center')
                new_ths.append(f'<th style="padding: 15px; text-align: {align};">{th_text.strip()}</th>')
            
            tr_content = ''
            for th in new_ths:
                tr_content += f'\n                                {th}'
            
            final_thead = f'<thead>\n                            <tr style="background: rgba(255, 215, 0, 0.1); color: var(--brand-amber);">{tr_content}\n                            </tr>\n                        </thead>'
            
            table_content = table_content.replace(thead_full, final_thead)
    return table_content

new_content = re.sub(r'<table class="premium-table"[^>]*>.*?</table>', process_table, new_content, flags=re.DOTALL)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(new_content)
