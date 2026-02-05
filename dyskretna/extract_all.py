import fitz
import re
import json

doc = fitz.open(
    r"c:\Users\Thefr\Dropbox\Komputer\Downloads\Baza pytań _ Dyskretna-Machen.pdf"
)
full_text = ""
for page in doc:
    full_text += page.get_text()

# Zapisz do pliku
with open("full_text.txt", "w", encoding="utf-8") as f:
    f.write(full_text)

print("Tekst zapisany do full_text.txt")
print(f"Długość: {len(full_text)} znaków")
