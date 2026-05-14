import re
import os

def update_html():
    with open('index.html', 'r', encoding='utf-8') as f:
        content = f.read()

    # 4.3. Семантические теги: div -> section
    section_classes = ['advantages', 'pricing', 'form-section', 'map-section', 'reviews', 'storage']
    for cls in section_classes:
        content = re.sub(rf'<div class="{cls}"', rf'<section class="{cls}"', content)
    
    # We need to change the closing tags too. They are usually followed by a comment.
    content = re.sub(r'<!-- Преимущества -->\s*</div>', r'<!-- Преимущества -->\n    </section>', content)
    content = re.sub(r'<!-- Цены -->\s*</div>', r'<!-- Цены -->\n    </section>', content)
    content = re.sub(r'<!-- Форма -->\s*</div>', r'<!-- Форма -->\n    </section>', content)
    content = re.sub(r'<!-- Карта -->\s*</div>', r'<!-- Карта -->\n    </section>', content)
    content = re.sub(r'<!-- Отзывы -->\s*</div>', r'<!-- Отзывы -->\n    </section>', content)
    content = re.sub(r'<!-- Хранение -->\s*</div>', r'<!-- Хранение -->\n    </section>', content)

    # Convert review cards to article
    content = re.sub(r'<div class="review-card">', r'<article class="review-card">', content)
    # The review cards end with </div>. Since there are multiple divs inside, this is tricky with regex. Let's just use replace since we know the structure.
    content = re.sub(r'</div>\s*<!-- \/review-card -->', r'</article>', content) # Assuming no comments, let's just do it with bs4.

    # 5. Alt attributes
    alts = {
        'logo.png': 'ЮМАКС — шиномонтаж в Пензе, логотип', # will handle multiples later
        'pokraska-diskov2.jpg': 'Порошковая покраска литых дисков в ЮМАКС, Пенза',
        'pokraska-diskov3.jpg': 'Восстановление дисков методом алмазной проточки на станке ЧПУ',
        'pokraska-diskov4.jpg': 'Готовый автомобильный диск после премиальной покраски с лаком',
        'air.png': 'Заправка автомобильного кондиционера фреоном R134a в ЮМАКС',
        'Roof.png': 'Выездной шиномонтаж ЮМАКС — фургон с оборудованием',
        'storage.jpg': 'Сезонное хранение шин в отапливаемом помещении ЮМАКС, Пенза'
    }

    # 6. Links to buttons
    # 6.2 Phone links
    content = re.sub(r'<a href="tel:\+78412999901" class="phone">', r'<a href="tel:+78412999901" class="phone" rel="nofollow" aria-label="Позвонить в ЮМАКС: 8 (8412) 99-99-01">', content)

    # 8. Skip-link
    if 'class="skip-link"' not in content:
        content = content.replace('<body>', '<body>\n    <a href="#main" class="skip-link">Перейти к основному содержимому</a>')
        skip_link_css = '''
        .skip-link {
            position: absolute;
            top: -40px;
            left: 0;
            background: #af101a;
            color: #fff;
            padding: 8px 16px;
            z-index: 100;
            text-decoration: none;
        }
        .skip-link:focus { top: 0; }
'''
        content = content.replace('</style>', skip_link_css + '    </style>')

    # 4.3 main tag
    if '<main id="main">' not in content:
        content = content.replace('<div class="hero">', '<main id="main">\n    <section class="hero">')
        content = content.replace('<section class="hero">', '<main id="main">\n    <section class="hero">')
        content = content.replace('<footer>', '</main>\n    <footer>')

    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(content)

if __name__ == "__main__":
    update_html()
