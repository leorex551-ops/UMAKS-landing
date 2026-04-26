import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

icons_map = {
    'Для легковых автомобилей': 'directions_car',
    'Для минивэнов и паркетников': 'airport_shuttle',
    'Для внедорожников': 'suv',
    'Для прочих автосредств (Газелей и мотоциклов)': 'local_shipping',
    'Ремонтные и шиномонтажные работы': 'build',
    'Съем установка + подкачка колес': 'tire_repair',
    'Мойка колес': 'local_car_wash',
    'Прокатка дисков': 'album',
    'Дополнительные услуги': 'add_circle',
    'Сезонное хранение шин': 'inventory_2',
    'Примечания к прейскуранту': 'info'
}

def fix_card(match):
    attrs = match.group(1)
    h3_text = match.group(2)
    
    icon_span = ''
    for key, icon in icons_map.items():
        if key in h3_text:
            icon_span = f'<span class="material-symbols-outlined">{icon}</span>\n                    '
            break
            
    return f'<div class="service-card reveal"{attrs}>\n                    {icon_span}<h3>{h3_text}</h3>\n                    <div class="btn-more">Подробнее <span class="material-symbols-outlined" style="font-size: 1.2rem; color: inherit; margin: 0;">arrow_forward</span></div>\n                </div>'

# Regex to match each service card and extract its title and onclick attribute
pattern = r'<div class="service-card reveal"([^>]+)>\s*(?:<span class="material-symbols-outlined">.*?</span>\s*)?<h3>(.*?)</h3>\s*<div class="btn-more">.*?</div>\s*</div>'

new_content = re.sub(pattern, fix_card, content, flags=re.DOTALL)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(new_content)
