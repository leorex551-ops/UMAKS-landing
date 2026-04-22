import unicodedata

def check_mixed_scripts(text):
    for char in text:
        try:
            print(f"'{char}': {unicodedata.name(char)}")
        except:
            print(f"'{char}': Unknown")

text = "Зaявкa oтпpaвлeнa"
check_mixed_scripts(text)
