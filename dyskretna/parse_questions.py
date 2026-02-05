import fitz
import re
import json
import html
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")

BASE_DIR = Path(__file__).resolve().parent
PDF_PATH = r"c:\Users\Thefr\Dropbox\Komputer\Downloads\Baza pytań _ Dyskretna-Machen.pdf"
OUTPUT_QUESTIONS = BASE_DIR / "questions.json"
OUTPUT_NEW_QUESTIONS = BASE_DIR / "new_questions.json"
OPTION_MARKER = r"[○✓●]"

def extract_text(doc: fitz.Document) -> str:
    chunks = []
    for page in doc:
        blocks = page.get_text("blocks")
        # Sort by vertical position, then horizontal to keep column order
        blocks_sorted = sorted(blocks, key=lambda b: (round(b[1], 1), round(b[0], 1)))
        page_text = "\n".join(b[4] for b in blocks_sorted if b[4].strip())
        chunks.append(page_text)
    return "\n".join(chunks)

def clean_text(text: str) -> str:
    text = re.sub(r"\d{1,2}\.\d{2}\.\d{4}.*?Baza pytań.*?baza\.php.*?\d+/\d+", "", text, flags=re.DOTALL)
    text = re.sub(r"https?://\S+", "", text)
    text = re.sub(r"\b\d+/\d+\b", "", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()

doc = fitz.open(PDF_PATH)
full_text = extract_text(doc)

# Parsowanie pytań
questions = []
# Znajdź wszystkie pytania
pattern = r'Pytanie (\d+): (.+?)(?=Pytanie \d+:|$)'
matches = re.findall(pattern, full_text, re.DOTALL)

for match in matches:
    q_num = int(match[0])
    content = match[1].strip()
    
    # Podziel na pytanie i odpowiedzi
    # Szukamy pierwszego ○ lub ✓
    first_option = re.search(OPTION_MARKER, content)
    if first_option:
        question_text = clean_text(content[:first_option.start()])
        options_text = content[first_option.start():]
        
        # Parsuj opcje
        options = []
        # Split by option markers
        option_parts = re.split(rf'(?={OPTION_MARKER})', options_text)
        for part in option_parts:
            part = part.strip()
            if not part:
                continue
            is_correct = part.startswith('✓')
            option_text = clean_text(part[1:])
            if option_text:
                options.append({
                    'text': option_text,
                    'correct': is_correct
                })
        
        if options:
            questions.append({
                'id': q_num,
                'question': question_text,
                'options': options,
                'multiple': sum(1 for o in options if o['correct']) > 1
            })

print(f"Znaleziono {len(questions)} pytań")

# Zapisz do JSON
with open(OUTPUT_QUESTIONS, 'w', encoding='utf-8') as f:
    json.dump(questions, f, ensure_ascii=False, indent=2)

with open(OUTPUT_NEW_QUESTIONS, 'w', encoding='utf-8') as f:
    json.dump(questions, f, ensure_ascii=False, indent=2)

print("Pytania zapisane do questions.json")

# Pokaż kilka pierwszych pytań
for q in questions[:3]:
    print(f"\n=== Pytanie {q['id']} ===")
    print(f"Treść: {q['question'][:100]}...")
    print(f"Liczba opcji: {len(q['options'])}")
    print(f"Wielokrotny wybór: {q['multiple']}")
