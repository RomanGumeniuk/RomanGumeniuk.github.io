import html
import json
import re
import sys
import urllib.request
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")

BASE_DIR = Path(__file__).resolve().parent
URL = "https://dyskretna.xn--drog-eta.pl/baza.php"
OUTPUT_QUESTIONS = BASE_DIR / "questions.json"
OUTPUT_NEW_QUESTIONS = BASE_DIR / "new_questions.json"
OPTION_MARKERS = {"○", "✓", "●"}


def extract_text(raw_html: str) -> str:
    img_tags = {}

    def stash_img(match: re.Match) -> str:
        token = f"__IMG_{len(img_tags)}__"
        img_tags[token] = match.group(0)
        return token

    raw_html = re.sub(r"(?i)<img\b[^>]*>", stash_img, raw_html)
    raw_html = re.sub(r"(?i)<br\s*/?>", "\n", raw_html)
    raw_html = re.sub(r"(?i)</p>", "\n", raw_html)
    raw_html = re.sub(r"(?i)</div>", "\n", raw_html)
    raw_html = re.sub(r"(?is)<script.*?</script>", "", raw_html)
    raw_html = re.sub(r"(?is)<style.*?</style>", "", raw_html)
    raw_html = re.sub(r"<[^>]+>", "", raw_html)
    raw_html = html.unescape(raw_html)

    raw_html = raw_html.replace("Powrót do strony głównej", " ")
    raw_html = raw_html.replace("Baza pytań", " ")
    raw_html = raw_html.replace("Drukuj", " ")
    raw_html = raw_html.replace("\r", "")

    for token, tag in img_tags.items():
        raw_html = raw_html.replace(token, tag)

    return raw_html


def parse_questions(text: str) -> list[dict]:
    questions = []
    pattern = re.compile(r"Pytanie\s+(\d+):")
    matches = list(pattern.finditer(text))

    for i, match in enumerate(matches):
        q_num = int(match.group(1))
        start = match.end()
        end = matches[i + 1].start() if i + 1 < len(matches) else len(text)
        section = text[start:end]
        lines = [line.strip() for line in section.splitlines() if line.strip()]

        question_lines = []
        options = []
        in_options = False
        pending_marker = None

        for line in lines:
            if line in OPTION_MARKERS:
                pending_marker = line
                continue

            marker_match = re.match(r"^([○✓●])\s*(.*)$", line)
            if marker_match:
                in_options = True
                marker = marker_match.group(1)
                option_text = marker_match.group(2).strip()
                options.append({
                    "text": option_text,
                    "correct": marker == "✓",
                })
                continue

            if pending_marker:
                in_options = True
                options.append({
                    "text": line,
                    "correct": pending_marker == "✓",
                })
                pending_marker = None
                continue

            if in_options and options:
                options[-1]["text"] = f"{options[-1]['text']} {line}".strip()
            else:
                question_lines.append(line)

        question_text = " ".join(question_lines).strip()
        if not options:
            continue

        questions.append({
            "id": q_num,
            "question": question_text,
            "options": options,
            "multiple": sum(1 for o in options if o["correct"]) > 1,
        })

    return questions


def main() -> None:
    raw_html = urllib.request.urlopen(URL).read().decode("utf-8", errors="replace")
    text = extract_text(raw_html)
    questions = parse_questions(text)

    print(f"Znaleziono {len(questions)} pytań")

    OUTPUT_QUESTIONS.write_text(json.dumps(questions, ensure_ascii=False, indent=2), encoding="utf-8")
    OUTPUT_NEW_QUESTIONS.write_text(json.dumps(questions, ensure_ascii=False, indent=2), encoding="utf-8")

    print("Pytania zapisane do questions.json i new_questions.json")


if __name__ == "__main__":
    main()
