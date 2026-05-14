# Промпт для вайбкодинга: SEO-оптимизация лендинга ЮМАКС (index.html)

## Контекст проекта

Ты — senior frontend-разработчик с экспертизой в техническом SEO. Тебе нужно отредактировать файл `index.html` лендинга шиномонтажа ЮМАКС (Пенза) перед деплоем на хостинг с доменом `юмакс-шиномонтаж.рф`.

**Информация о бизнесе:**
- Название: ЮМАКС
- Деятельность: Сеть шиномонтажей в Пензе
- Количество точек: 7
- Режим работы: 24/7 (круглосуточно, без выходных)
- Основной телефон: +7 (8412) 99-99-01
- Основной домен (после деплоя): `https://юмакс-шиномонтаж.рф/`
- Целевой регион: Пенза, Пензенская область
- Основной поисковик: Яндекс (приоритет №1), Google (приоритет №2)
- Главные услуги: шиномонтаж, хранение шин, выездной шиномонтаж, покраска дисков, заправка кондиционеров, ремонт дисков

**Адреса точек:**
1. пр. Победы, 67 — режим: 8:00–22:00
2. ул. Калинина, 158 — режим: 8:00–20:00
3. пр. Победы, 96а — режим: круглосуточно
4. ул. Гагарина, 3а — режим: 8:00–22:00
5. ул. Гагарина, 7а — режим: 8:00–21:00
6. ул. Аустрина, 139 — режим: 8:00–21:00
7. ул. Саранская, 76 (территория базы) — режим: 8:00–20:00

**Файлы в корне проекта (используй существующие):**
- `index.html` — редактируем
- `logo.png` — логотип
- `favicon.png` — иконка для вкладки браузера (уже подготовлена)
- `OG.jpg` — картинка для соцсетей (Open Graph, 1200×630)
- `hero.mp4` — видео на главной
- `pokraska-diskov2.jpg`, `pokraska-diskov3.jpg`, `pokraska-diskov4.jpg` — фото покраски
- `air.png` — фото кондиционера
- `Roof.png` — фото выездного шиномонтажа
- `storage.jpg` — фото хранения шин

---

## Задача

Отредактируй `index.html` строго по списку ниже. Не добавляй ничего лишнего, не меняй существующую структуру блоков и контент, не трогай CSS и JS-логику. Работай только с HTML-разметкой и атрибутами.

---

## Раздел 1. Тег `<html>`

Убедись, что в открывающем теге прописан атрибут языка:

```html
<html lang="ru">
```

---

## Раздел 2. Блок `<head>` — мета-теги

Полностью замени или дополни блок `<head>` следующими тегами в указанном порядке. Если какой-то тег уже есть — обнови его значение, не дублируй.

### 2.1. Базовые мета-теги

```html
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<meta http-equiv="X-UA-Compatible" content="IE=edge">
```

### 2.2. SEO мета-теги для главной страницы

```html
<title>Шиномонтаж в Пензе круглосуточно — ЮМАКС | 7 точек, от 2 600 ₽</title>
<meta name="description" content="Шиномонтаж ЮМАКС в Пензе: 7 точек по городу, работаем 24/7, замена резины за 40 минут без очереди. Цены от 2 600 ₽ за комплекс. Запись онлайн ☎ (8412) 99-99-01">
<meta name="keywords" content="шиномонтаж Пенза, шиномонтаж круглосуточно, шиномонтаж 24 часа, замена резины Пенза, переобуть авто Пенза, балансировка колёс Пенза, хранение шин Пенза, выездной шиномонтаж Пенза, покраска дисков Пенза, ЮМАКС шиномонтаж">
<meta name="author" content="ЮМАКС">
<meta name="robots" content="index, follow">
<meta name="googlebot" content="index, follow">
<meta name="yandex" content="index, follow">
<link rel="canonical" href="https://юмакс-шиномонтаж.рф/">
```

### 2.3. Геолокация (важно для локального бизнеса)

```html
<meta name="geo.region" content="RU-PNZ">
<meta name="geo.placename" content="Пенза">
<meta name="geo.position" content="53.195063;45.018316">
<meta name="ICBM" content="53.195063, 45.018316">
```

### 2.4. Подтверждение прав в поисковиках (плейсхолдеры — клиент вставит свои коды)

```html
<meta name="yandex-verification" content="ВСТАВИТЬ_КОД_ИЗ_ЯНДЕКС_ВЕБМАСТЕРА">
<meta name="google-site-verification" content="ВСТАВИТЬ_КОД_ИЗ_GOOGLE_SEARCH_CONSOLE">
```

### 2.5. Open Graph (для Telegram, ВКонтакте, WhatsApp, Facebook)

```html
<meta property="og:type" content="website">
<meta property="og:site_name" content="ЮМАКС — Шиномонтаж в Пензе">
<meta property="og:title" content="ЮМАКС — Шиномонтаж в Пензе круглосуточно">
<meta property="og:description" content="7 точек по городу, работаем 24/7, замена за 40 минут без очереди. Цены от 2 600 ₽. Запись онлайн ☎ (8412) 99-99-01">
<meta property="og:url" content="https://юмакс-шиномонтаж.рф/">
<meta property="og:image" content="https://юмакс-шиномонтаж.рф/OG.jpg">
<meta property="og:image:secure_url" content="https://юмакс-шиномонтаж.рф/OG.jpg">
<meta property="og:image:type" content="image/jpeg">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:image:alt" content="ЮМАКС — Шиномонтаж в Пензе, 7 точек, работаем 24/7">
<meta property="og:locale" content="ru_RU">
```

### 2.6. Twitter Cards

```html
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="ЮМАКС — Шиномонтаж в Пензе круглосуточно">
<meta name="twitter:description" content="7 точек, 24/7, замена за 40 минут. От 2 600 ₽">
<meta name="twitter:image" content="https://юмакс-шиномонтаж.рф/OG.jpg">
<meta name="twitter:image:alt" content="ЮМАКС — Шиномонтаж в Пензе">
```

### 2.7. Favicon (используй существующий файл `favicon.png` в корне проекта)

```html
<link rel="icon" type="image/png" href="/favicon.png">
<link rel="shortcut icon" type="image/png" href="/favicon.png">
<link rel="apple-touch-icon" href="/favicon.png">
<meta name="theme-color" content="#af101a">
```

### 2.8. Preconnect для ускорения (если используются внешние шрифты/иконки)

Если в проекте подключаются Google Fonts или Material Symbols через CDN — добавь в начало `<head>`:

```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
```

---

## Раздел 3. Структурированные данные JSON-LD

Перед закрывающим тегом `</head>` добавь два блока JSON-LD.

### 3.1. Основная организация (AutoRepair + LocalBusiness)

```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "AutoRepair",
  "@id": "https://юмакс-шиномонтаж.рф/#organization",
  "name": "ЮМАКС",
  "alternateName": "Шиномонтаж ЮМАКС",
  "description": "Сеть шиномонтажей в Пензе. 7 точек по городу, работаем 24/7, замена резины за 40 минут без очереди.",
  "image": "https://юмакс-шиномонтаж.рф/logo.png",
  "logo": "https://юмакс-шиномонтаж.рф/logo.png",
  "url": "https://юмакс-шиномонтаж.рф/",
  "telephone": "+78412999901",
  "priceRange": "₽₽",
  "currenciesAccepted": "RUB",
  "paymentAccepted": "Cash, Credit Card",
  "address": {
    "@type": "PostalAddress",
    "streetAddress": "пр. Победы, 96а",
    "addressLocality": "Пенза",
    "addressRegion": "Пензенская область",
    "postalCode": "440000",
    "addressCountry": "RU"
  },
  "geo": {
    "@type": "GeoCoordinates",
    "latitude": 53.195063,
    "longitude": 45.018316
  },
  "openingHoursSpecification": [
    {
      "@type": "OpeningHoursSpecification",
      "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"],
      "opens": "00:00",
      "closes": "23:59"
    }
  ],
  "sameAs": [
    "https://2gis.ru/penza/search/ЮМАКС шиномонтаж"
  ],
  "aggregateRating": {
    "@type": "AggregateRating",
    "ratingValue": "4.9",
    "reviewCount": "120",
    "bestRating": "5",
    "worstRating": "1"
  },
  "areaServed": {
    "@type": "City",
    "name": "Пенза"
  }
}
</script>
```

### 3.2. Список филиалов (отдельные LocalBusiness для каждой точки)

```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "ItemList",
  "name": "Адреса шиномонтажей ЮМАКС в Пензе",
  "itemListElement": [
    {
      "@type": "LocalBusiness",
      "name": "ЮМАКС — Пр. Победы, 67",
      "image": "https://юмакс-шиномонтаж.рф/logo.png",
      "telephone": "+78412444818",
      "address": {
        "@type": "PostalAddress",
        "streetAddress": "пр. Победы, 67",
        "addressLocality": "Пенза",
        "addressCountry": "RU"
      },
      "openingHours": "Mo-Su 08:00-22:00"
    },
    {
      "@type": "LocalBusiness",
      "name": "ЮМАКС — Ул. Калинина, 158",
      "image": "https://юмакс-шиномонтаж.рф/logo.png",
      "telephone": "+78412301855",
      "address": {
        "@type": "PostalAddress",
        "streetAddress": "ул. Калинина, 158",
        "addressLocality": "Пенза",
        "addressCountry": "RU"
      },
      "openingHours": "Mo-Su 08:00-20:00"
    },
    {
      "@type": "LocalBusiness",
      "name": "ЮМАКС — Пр. Победы, 96а",
      "image": "https://юмакс-шиномонтаж.рф/logo.png",
      "telephone": "+78412207401",
      "address": {
        "@type": "PostalAddress",
        "streetAddress": "пр. Победы, 96а",
        "addressLocality": "Пенза",
        "addressCountry": "RU"
      },
      "openingHours": "Mo-Su 00:00-23:59"
    },
    {
      "@type": "LocalBusiness",
      "name": "ЮМАКС — Ул. Гагарина, 3а",
      "image": "https://юмакс-шиномонтаж.рф/logo.png",
      "telephone": "+79273816452",
      "address": {
        "@type": "PostalAddress",
        "streetAddress": "ул. Гагарина, 3а",
        "addressLocality": "Пенза",
        "addressCountry": "RU"
      },
      "openingHours": "Mo-Su 08:00-22:00"
    },
    {
      "@type": "LocalBusiness",
      "name": "ЮМАКС — Гагарина, 7а",
      "image": "https://юмакс-шиномонтаж.рф/logo.png",
      "telephone": "+78412308803",
      "address": {
        "@type": "PostalAddress",
        "streetAddress": "ул. Гагарина, 7а",
        "addressLocality": "Пенза",
        "addressCountry": "RU"
      },
      "openingHours": "Mo-Su 08:00-21:00"
    },
    {
      "@type": "LocalBusiness",
      "name": "ЮМАКС — Аустрина, 139",
      "image": "https://юмакс-шиномонтаж.рф/logo.png",
      "telephone": "+78412728844",
      "address": {
        "@type": "PostalAddress",
        "streetAddress": "ул. Аустрина, 139",
        "addressLocality": "Пенза",
        "addressCountry": "RU"
      },
      "openingHours": "Mo-Su 08:00-21:00"
    },
    {
      "@type": "LocalBusiness",
      "name": "ЮМАКС — Ул. Саранская, 76",
      "image": "https://юмакс-шиномонтаж.рф/logo.png",
      "telephone": "+78412290290",
      "address": {
        "@type": "PostalAddress",
        "streetAddress": "ул. Саранская, 76 (территория базы)",
        "addressLocality": "Пенза",
        "addressCountry": "RU"
      },
      "openingHours": "Mo-Su 08:00-20:00"
    }
  ]
}
</script>
```

---

## Раздел 4. Семантическая разметка контента

### 4.1. Один `<h1>` на странице

Убедись, что в HTML только **один** тег `<h1>` — это главный заголовок «Шиномонтаж в Пензе — быстро, честно, качественно». Если в модалках или скрытых блоках есть ещё `<h1>` — поменяй их на `<h2>` или `<h3>` в зависимости от иерархии.

### 4.2. Иерархия заголовков

Проверь и приведи к корректной иерархии:
- `<h1>` — главный заголовок страницы (1 шт.)
- `<h2>` — заголовки крупных секций («Почему выбирают ЮМАКС», «Цены на услуги шиномонтажа», «Записаться», «Выберите ближайшую точку», «Что говорят клиенты»)
- `<h3>` — подзаголовки внутри секций (карточки услуг, заголовки точек на карте)
- `<h4>` — заголовки блоков в футере («Телефон шиномонтажа», «Адреса точек»)

Не пропускай уровни (нельзя сразу с `<h2>` на `<h4>`).

### 4.3. Семантические теги

Замени общие `<div>` на семантические HTML5-теги там, где это уместно:
- Шапка сайта → `<header>`
- Главная навигация → `<nav>` внутри header
- Основной контент → `<main>`
- Каждая большая секция → `<section>` с атрибутом `aria-labelledby` или `aria-label`
- Подвал → `<footer>`
- Карточки отзывов → `<article>`

**Не переписывай всю верстку**, только обозначь самые крупные блоки. Если сейчас уже используются эти теги — оставь как есть.

---

## Раздел 5. Атрибуты `alt` для изображений

Пройдись по всем тегам `<img>` и пропиши осмысленные `alt`-атрибуты. Уникальные для каждой картинки, с упоминанием бренда и города где уместно.

| Файл изображения | Рекомендуемый alt |
|---|---|
| `logo.png` (в шапке) | `ЮМАКС — шиномонтаж в Пензе, логотип` |
| `logo.png` (в модалках) | `Логотип ЮМАКС` |
| `logo.png` (в футере) | `ЮМАКС — сеть шиномонтажей в Пензе` |
| `pokraska-diskov2.jpg` | `Порошковая покраска литых дисков в ЮМАКС, Пенза` |
| `pokraska-diskov3.jpg` | `Восстановление дисков методом алмазной проточки на станке ЧПУ` |
| `pokraska-diskov4.jpg` | `Готовый автомобильный диск после премиальной покраски с лаком` |
| `air.png` | `Заправка автомобильного кондиционера фреоном R134a в ЮМАКС` |
| `Roof.png` | `Выездной шиномонтаж ЮМАКС — фургон с оборудованием` |
| `storage.jpg` | `Сезонное хранение шин в отапливаемом помещении ЮМАКС, Пенза` |

Для **декоративных иконок** (Material Symbols Outlined типа `bolt`, `payments`, `location_on`) — если они подаются как `<img>`, пропиши `alt=""` (пустой), чтобы скринридеры их пропускали. Если они подаются через `<span class="material-symbols-outlined">` — никаких изменений не нужно, добавь только `aria-hidden="true"`.

---

## Раздел 6. Оптимизация ссылок и кнопок

### 6.1. Замена `javascript:void(0)` на семантические кнопки

В навигации сейчас ссылки вида:
```html
<a href="javascript:void(0)">Кондиционеры</a>
```

Замени их на `<button>` с правильным типом и aria-атрибутами:
```html
<button type="button" class="nav-link" aria-haspopup="dialog" data-modal="conditioning">Кондиционеры</button>
```

Либо, если это якоря на секции — используй реальные `href="#section-id"`. Поисковики не следуют по `javascript:void(0)` ссылкам, и теряется ссылочный вес.

### 6.2. Атрибуты для телефонных ссылок

У всех ссылок на телефоны (`tel:`) добавь атрибут для микроразметки:
```html
<a href="tel:+78412999901" rel="nofollow" aria-label="Позвонить в ЮМАКС: 8 (8412) 99-99-01">8 (8412) 99-99-01</a>
```

### 6.3. Внешние ссылки

Для внешних ссылок (на 2ГИС, Яндекс.Карты) добавь:
```html
<a href="https://2gis.ru/..." target="_blank" rel="noopener noreferrer">Все отзывы на 2ГИС</a>
```

### 6.4. Ссылки на маршруты в Яндекс.Картах

Сейчас ссылки имеют вид `https://yandex.ru/maps/?text=Пенза, пр. Победы, 67`. Это работает, но лучше использовать координатные ссылки или закодировать кириллицу. Оставь как есть, **только добавь** `target="_blank" rel="noopener nofollow"`.

---

## Раздел 7. Производительность и Core Web Vitals

### 7.1. Lazy loading для изображений

Всем `<img>`, **кроме первого экрана** (логотип в шапке, hero-видео-постер), добавь:
```html
<img src="..." alt="..." loading="lazy" decoding="async">
```

Для изображений первого экрана:
```html
<img src="..." alt="..." loading="eager" decoding="async" fetchpriority="high">
```

### 7.2. Оптимизация видео hero.mp4

Добавь к тегу `<video>`:
```html
<video src="hero.mp4" autoplay muted loop playsinline preload="metadata" poster="/hero-poster.jpg" aria-label="Видео работы шиномонтажа ЮМАКС"></video>
```

Атрибут `preload="metadata"` загружает только метаданные, а не всё видео. Атрибут `poster` нужно подготовить отдельно (статичный кадр из видео в формате JPG/WebP).

### 7.3. Width и height у изображений

Всем `<img>` пропиши явные размеры `width` и `height` (в пикселях, без `px`) — это предотвращает Layout Shift (CLS):
```html
<img src="logo.png" alt="ЮМАКС" width="180" height="60">
```

Если точные размеры неизвестны — оставь это для ручной правки и пометь `<!-- TODO: проставить width/height -->`.

---

## Раздел 8. Доступность (a11y) — попутно с SEO

### 8.1. Skip-link для навигации с клавиатуры

В самом начале `<body>` добавь:
```html
<a href="#main" class="skip-link">Перейти к основному содержимому</a>
```

И стили в `<style>` (или скажи, что нужно добавить в CSS):
```css
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
```

### 8.2. ARIA-атрибуты для модалок

У всех модалок (`<div class="modal">`) пропиши:
```html
<div class="modal" role="dialog" aria-modal="true" aria-labelledby="modal-title-id" aria-hidden="true">
  <h2 id="modal-title-id">Заголовок модалки</h2>
</div>
```

### 8.3. Подписи к формам

Каждое поле формы должно иметь связанный `<label>`:
```html
<label for="name">Ваше имя*</label>
<input type="text" id="name" name="name" required autocomplete="name">

<label for="phone">Телефон*</label>
<input type="tel" id="phone" name="phone" required autocomplete="tel">
```

Атрибуты `autocomplete` помогают браузеру подставлять данные.

---

## Раздел 9. Что НЕ делать

Чтобы не сломать существующий лендинг:

1. **Не меняй CSS-классы** существующих элементов
2. **Не трогай JavaScript-логику** (открытие модалок, валидация форм, переключение слайдеров)
3. **Не удаляй существующие блоки контента** — только добавляй атрибуты и оборачивай в семантические теги
4. **Не меняй цены, адреса, телефоны** — это бизнес-данные
5. **Не добавляй встроенный CSS/JS**, кроме того, что прямо указано в этом промпте (skip-link)
6. **Не подключай новые внешние библиотеки** (jQuery, шрифты, аналитику) — это будет сделано отдельно

---

## Раздел 10. Дополнительные файлы (создай рядом с index.html)

Помимо редактирования `index.html`, создай в корне проекта два файла:

### 10.1. `robots.txt`

```
User-agent: *
Allow: /
Disallow: /admin/
Disallow: /*?utm_*
Disallow: /*?from=*

Sitemap: https://юмакс-шиномонтаж.рф/sitemap.xml
Host: юмакс-шиномонтаж.рф
```

### 10.2. `sitemap.xml`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
  <url>
    <loc>https://юмакс-шиномонтаж.рф/</loc>
    <lastmod>2026-04-29</lastmod>
    <changefreq>weekly</changefreq>
    <priority>1.0</priority>
  </url>
</urlset>
```

---

## Раздел 11. Финальная проверка

После всех правок самостоятельно проверь:

1. ✅ Один `<h1>` на странице
2. ✅ Корректная иерархия заголовков (нет пропусков уровней)
3. ✅ Все `<img>` имеют атрибут `alt` (уникальный или пустой для декоративных)
4. ✅ Все `<img>` имеют `loading="lazy"` (кроме первого экрана)
5. ✅ Title до 70 символов, description до 160 символов
6. ✅ Открывающий `<html lang="ru">`
7. ✅ Все JSON-LD валидны (можно проверить на validator.schema.org)
8. ✅ `og:image` указывает на абсолютный URL `https://юмакс-шиномонтаж.рф/OG.jpg`
9. ✅ Канонический URL прописан
10. ✅ Все `javascript:void(0)` заменены или преобразованы в кнопки

---

## Формат ответа

В ответе выдай:
1. **Полностью отредактированный файл `index.html`** — целиком, готовый к деплою
2. **Файл `robots.txt`**
3. **Файл `sitemap.xml`**
4. **Краткий отчёт** в конце: что было изменено по разделам (1–11), сколько `<img>` получили alt, сколько `javascript:void(0)` заменено, какие файлы дополнительно нужно создать клиенту (hero-poster.jpg для видео).

Работай педантично. Каждое изменение должно соответствовать одному из пунктов промпта. Если в каком-то месте `index.html` есть конфликт между текущей разметкой и инструкциями — приоритет у инструкций промпта.
