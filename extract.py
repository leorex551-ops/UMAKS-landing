import docx
import json

def main():
    d = docx.Document('Прайс.docx')
    tables = [[[c.text.strip() for c in row.cells] for row in t.rows] for t in d.tables]
    with open('prices.json', 'w', encoding='utf-8') as f:
        json.dump(tables, f, ensure_ascii=False, indent=2)

if __name__ == '__main__':
    main()
