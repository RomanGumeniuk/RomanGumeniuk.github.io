import json

# Wczytaj pytania
with open("questions.json", "r", encoding="utf-8") as f:
    questions = json.load(f)

# Wczytaj szablon HTML
with open("index_template.html", "r", encoding="utf-8") as f:
    template = f.read()

# Wstaw pytania do szablonu
questions_json = json.dumps(questions, ensure_ascii=False, indent=2)
final_html = template.replace("EMBEDDED_QUESTIONS_PLACEHOLDER", questions_json)

# Zapisz finalny plik
with open("index.html", "w", encoding="utf-8") as f:
    f.write(final_html)

print(f"Wygenerowano index.html z {len(questions)} pytaniami")
print("Strona jest gotowa do użycia!")
