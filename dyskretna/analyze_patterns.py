import json
import re
from collections import Counter, defaultdict

with open("questions.json", "r", encoding="utf-8") as f:
    questions = json.load(f)

# ========== 1. POSITION DISTRIBUTION ==========
print("=" * 60)
print("1. ROZKŁAD POZYCJI POPRAWNYCH ODPOWIEDZI (single-choice)")
print("=" * 60)

pos_counts = Counter()
pos_questions = defaultdict(list)
total_single = 0

for q in questions:
    if q["multiple"]:
        continue
    total_single += 1
    for i, opt in enumerate(q["options"]):
        if opt["correct"]:
            pos_counts[i] += 1
            pos_questions[i].append(q["id"])

for pos in sorted(pos_counts):
    labels = ["A", "B", "C", "D", "E"]
    pct = pos_counts[pos] / total_single * 100
    print(f"  Pozycja {labels[pos]} (index {pos}): {pos_counts[pos]} razy ({pct:.1f}%) — np. Q{pos_questions[pos][:5]}")

# ========== 2. LENGTH PATTERNS ==========
print("\n" + "=" * 60)
print("2. DŁUGOŚĆ POPRAWNEJ ODPOWIEDZI vs NIEPOPRAWNYCH")
print("=" * 60)

longest_correct = 0
shortest_correct = 0
middle_correct = 0
correct_is_longest_ids = []
correct_is_shortest_ids = []

for q in questions:
    if q["multiple"]:
        continue
    correct_idx = None
    lengths = []
    for i, opt in enumerate(q["options"]):
        length = len(opt["text"])
        lengths.append((length, i, opt["correct"]))
        if opt["correct"]:
            correct_idx = i
            correct_len = length
    
    lengths_sorted = sorted(lengths, key=lambda x: x[0], reverse=True)
    max_len = lengths_sorted[0][0]
    min_len = lengths_sorted[-1][0]
    
    if correct_len == max_len:
        longest_correct += 1
        correct_is_longest_ids.append(q["id"])
    elif correct_len == min_len:
        shortest_correct += 1
        correct_is_shortest_ids.append(q["id"])
    else:
        middle_correct += 1

print(f"  Poprawna = NAJDŁUŻSZA: {longest_correct}/{total_single} ({longest_correct/total_single*100:.1f}%) — np. Q{correct_is_longest_ids[:8]}")
print(f"  Poprawna = NAJKRÓTSZA: {shortest_correct}/{total_single} ({shortest_correct/total_single*100:.1f}%) — np. Q{correct_is_shortest_ids[:8]}")
print(f"  Poprawna = ŚREDNIA DŁUGOŚĆ: {middle_correct}/{total_single} ({middle_correct/total_single*100:.1f}%)")

# Rank analysis
print("\n  Ranking długości (1=najdłuższa, 5=najkrótsza):")
rank_counts = Counter()
for q in questions:
    if q["multiple"]:
        continue
    lengths = [(len(opt["text"]), i, opt["correct"]) for i, opt in enumerate(q["options"])]
    lengths_sorted = sorted(lengths, key=lambda x: x[0], reverse=True)
    for rank, (l, i, c) in enumerate(lengths_sorted):
        if c:
            rank_counts[rank + 1] += 1
for r in sorted(rank_counts):
    print(f"    Rank {r}: {rank_counts[r]} razy ({rank_counts[r]/total_single*100:.1f}%)")

# ========== 3. KEYWORD PATTERNS ==========
print("\n" + "=" * 60)
print("3. SŁOWA KLUCZOWE W POPRAWNYCH vs NIEPOPRAWNYCH")
print("=" * 60)

keywords_to_check = [
    "co najmniej", "co najwyżej", "dokładnie", "dla każdego", "dla każdej",
    "dowolny", "dowolnej", "dowolnego", "dowolnym", "każdy", "każdej", "każdego",
    "pewnej", "pewnego", "pewnym", "pewien", "pewna",
    "nie jest", "nie może", "nie można", "nie zawiera",
    "zawsze", "jedynie", "wyłącznie", "tylko",
    "wtedy i tylko wtedy", "jeżeli", "jeśli",
    "może być", "jest możliw",
    "lub", "albo",
    "nie mniejsz", "nie większ",
    "niejednorodną", "jednorodną", "nieliniow",
    "nieparzyst", "parzyst",
]

keyword_stats = {}
for kw in keywords_to_check:
    correct_count = 0
    incorrect_count = 0
    correct_total = 0
    incorrect_total = 0
    correct_qids = []
    
    for q in questions:
        for opt in q["options"]:
            text_lower = opt["text"].lower()
            if kw.lower() in text_lower:
                if opt["correct"]:
                    correct_count += 1
                    correct_qids.append(q["id"])
                else:
                    incorrect_count += 1
        
    total = correct_count + incorrect_count
    if total > 0:
        ratio = correct_count / total * 100
        keyword_stats[kw] = (correct_count, incorrect_count, total, ratio, correct_qids[:5])

# Sort by ratio
print("  Słowo kluczowe | w poprawnych | w niepoprawnych | łącznie | % w poprawnych")
for kw, (cc, ic, t, r, ids) in sorted(keyword_stats.items(), key=lambda x: -x[1][3]):
    if t >= 3:
        print(f"  '{kw}': {cc} poprawnych, {ic} niepoprawnych, ratio={r:.1f}% — Q{ids}")

# ========== 4. "co najmniej" vs "co najwyżej" vs "dokładnie" ==========
print("\n" + "=" * 60)
print("4. PATTERN: 'co najmniej' vs 'co najwyżej' vs 'dokładnie'")
print("=" * 60)

for phrase in ["co najmniej", "co najwyżej", "dokładnie"]:
    correct_ids = []
    incorrect_ids = []
    for q in questions:
        for opt in q["options"]:
            if phrase in opt["text"].lower():
                if opt["correct"]:
                    correct_ids.append(q["id"])
                else:
                    incorrect_ids.append(q["id"])
    total = len(correct_ids) + len(incorrect_ids)
    if total > 0:
        print(f"  '{phrase}': poprawna {len(correct_ids)}x, niepoprawna {len(incorrect_ids)}x — ratio {len(correct_ids)/total*100:.1f}%")
        print(f"     poprawne w Q: {correct_ids[:10]}")

# ========== 5. FORMULA PATTERNS ==========
print("\n" + "=" * 60)
print("5. WZORY/FORMUŁY W ODPOWIEDZIACH")
print("=" * 60)

formula_patterns = {
    "binom": r"\\binom",
    "frac": r"\\frac",
    "sum": r"\\sum",
    "n!": r"n!",
    "k!": r"k!",
    "geq": r"\\geq",
    "leq": r"\\leq",
    "neq": r"\\neq",
    "forall": r"\\forall",
    "Rightarrow": r"\\Rightarrow",
    "Leftrightarrow": r"\\Leftrightarrow",
    "cap": r"\\cap",
    "cup": r"\\cup",
    "overline": r"\\overline",
    "in": r"\\in",
    "land": r"\\land",
}

for name, pattern in formula_patterns.items():
    cc = 0
    ic = 0
    cids = []
    for q in questions:
        for opt in q["options"]:
            if pattern in opt["text"]:
                if opt["correct"]:
                    cc += 1
                    cids.append(q["id"])
                else:
                    ic += 1
    total = cc + ic
    if total >= 5:
        print(f"  '{name}': poprawna {cc}x, niepoprawna {ic}x — ratio {cc/total*100:.1f}% — Q{cids[:5]}")

# ========== 6. NEGATION PATTERNS ==========
print("\n" + "=" * 60)
print("6. NEGACJA W ODPOWIEDZIACH")
print("=" * 60)

neg_words = ["nie jest", "nie może", "nie można", "nie zawiera", "nie wynika",
             "nie są", "nie istnieje", "nie mają", "żadna", "żadne", "żadnego",
             "nigdy", "niemożliw"]

for nw in neg_words:
    cc = 0
    ic = 0
    cids = []
    for q in questions:
        for opt in q["options"]:
            if nw.lower() in opt["text"].lower():
                if opt["correct"]:
                    cc += 1
                    cids.append(q["id"])
                else:
                    ic += 1
    total = cc + ic
    if total >= 3:
        print(f"  '{nw}': poprawna {cc}x, niepoprawna {ic}x — ratio {cc/total*100:.1f}%")

# ========== 7. MULTIPLE vs SINGLE ==========
print("\n" + "=" * 60)
print("7. SINGLE-CHOICE vs MULTI-CHOICE")
print("=" * 60)

multi_count = sum(1 for q in questions if q["multiple"])
single_count = sum(1 for q in questions if not q["multiple"])
print(f"  Single-choice: {single_count}")
print(f"  Multi-choice: {multi_count}")

# For multi-choice: how many correct answers?
print("\n  Multi-choice: rozkład liczby poprawnych odpowiedzi:")
multi_correct_counts = Counter()
for q in questions:
    if q["multiple"]:
        nc = sum(1 for o in q["options"] if o["correct"])
        multi_correct_counts[nc] += 1
for n in sorted(multi_correct_counts):
    print(f"    {n} poprawnych: {multi_correct_counts[n]} pytań")

# ========== 8. ANSWER IS THE MOST PRECISE/QUALIFIED ==========
print("\n" + "=" * 60)
print("8. ODPOWIEDZI Z WARUNKAMI KWALIFIKUJĄCYMI")
print("=" * 60)

qualifiers = ["wtedy i tylko wtedy", "dla wszystkich", "dla każdego", "dla każdej", 
              "dla pewnego", "dla pewnej", "spełniony jest", "zachodzi",
              "istnieją", "istnieje"]

for qual in qualifiers:
    cc = 0
    ic = 0
    cids = []
    for q in questions:
        for opt in q["options"]:
            if qual.lower() in opt["text"].lower():
                if opt["correct"]:
                    cc += 1
                    cids.append(q["id"])
                else:
                    ic += 1
    total = cc + ic
    if total >= 3:
        print(f"  '{qual}': poprawna {cc}x, niepoprawna {ic}x — ratio {cc/(total)*100:.1f}% — Q{cids[:5]}")

# ========== 9. SPECIAL: wielomian szachowy starts with 1 ==========
print("\n" + "=" * 60)
print("9. WIELOMIAN SZACHOWY — pattern z '1 +' na początku")
print("=" * 60)
for q in questions:
    if "wielomian" in q["question"].lower() or "szachow" in q["question"].lower() or "funkcję tworzącą" in q["question"].lower():
        print(f"\n  Q{q['id']}: {q['question'][:80]}")
        for i, opt in enumerate(q["options"]):
            marker = "✓" if opt["correct"] else "✗"
            print(f"    [{marker}] {opt['text'][:100]}")

# =========== 10. POSITION for SINGLE-CHOICE breakdown ============
print("\n" + "=" * 60)
print("10. POZYCJA POPRAWNEJ — szczegółowy breakdown")
print("=" * 60)

# Group by question topic
topic_pos = defaultdict(lambda: Counter())
for q in questions:
    if q["multiple"]:
        continue
    topic = "other"
    qt = q["question"].lower()
    if "indukcj" in qt:
        topic = "indukcja"
    elif "rekuren" in qt:
        topic = "rekurencja"
    elif "kombinat" in qt or "wariacja" in qt or "permutac" in qt or "pudełek" in qt or "pudełk" in qt or "wrzuc" in qt:
        topic = "kombinatoryka"
    elif "szufladk" in qt:
        topic = "szufladkowa"
    elif "włączani" in qt:
        topic = "wlacznie-wylaczanie"
    elif "szachow" in qt or "wielomian" in qt:
        topic = "szachownica"
    elif "stirling" in qt or "euler" in qt or "fibonacci" in qt or "harmonic" in qt:
        topic = "ciagi-specjalne"
    elif "łaciński" in qt or "prostokąt" in qt or "kwadrat" in qt:
        topic = "kwadraty-lacinskie"
    elif "graf" in qt or "drzew" in qt or "euler" in qt or "hamilton" in qt:
        topic = "graf"
    
    for i, opt in enumerate(q["options"]):
        if opt["correct"]:
            topic_pos[topic][i] += 1

for topic in sorted(topic_pos):
    print(f"\n  Temat: {topic}")
    total_topic = sum(topic_pos[topic].values())
    for pos in range(5):
        labels = ["A", "B", "C", "D", "E"]
        cnt = topic_pos[topic].get(pos, 0)
        print(f"    {labels[pos]}: {cnt}/{total_topic} ({cnt/total_topic*100:.0f}%)")

# ========== 11. SPECIFIC NUMBER PATTERNS ==========
print("\n" + "=" * 60)
print("11. SPECYFICZNE WARTOŚCI LICZBOWE")
print("=" * 60)

# For questions about "ile sposobów", check if correct answer has certain formula patterns
for q in questions:
    if q["multiple"]:
        continue
    qt = q["question"].lower()
    if "sposobów" in qt or "na ile" in qt or "sposoby" in qt:
        for i, opt in enumerate(q["options"]):
            if opt["correct"]:
                print(f"  Q{q['id']}: Poprawna [{['A','B','C','D','E'][i]}]: {opt['text'][:80]}")

# ========== 12. UNIQUE WORD ANALYSIS ==========
print("\n" + "=" * 60)
print("12. SŁOWA UNIKALNE DLA POPRAWNYCH ODPOWIEDZI")
print("=" * 60)

correct_words = Counter()
incorrect_words = Counter()

for q in questions:
    for opt in q["options"]:
        words = re.findall(r'[a-ząćęłńóśźżA-ZĄĆĘŁŃÓŚŹŻ]+', opt["text"])
        for w in words:
            w_lower = w.lower()
            if len(w_lower) > 4:
                if opt["correct"]:
                    correct_words[w_lower] += 1
                else:
                    incorrect_words[w_lower] += 1

# Find words that appear much more in correct answers
print("  Słowa pojawiające się częściej w poprawnych (min 3 wystąpienia):")
for word, count in correct_words.most_common(200):
    ic = incorrect_words.get(word, 0)
    total = count + ic
    if total >= 5 and count / total > 0.35:
        print(f"    '{word}': {count} poprawnych, {ic} niepoprawnych — ratio {count/total*100:.1f}%")

# ========== 13. "DOWOLNY" ANALYSIS ==========
print("\n" + "=" * 60)
print("13. 'DOWOLNY/DOWOLNEJ/DOWOLNEGO' — trap word?")
print("=" * 60)

dowolny_variants = ["dowoln"]
for variant in dowolny_variants:
    cc = 0
    ic = 0
    cids = []
    iids = []
    for q in questions:
        for opt in q["options"]:
            if variant in opt["text"].lower():
                if opt["correct"]:
                    cc += 1
                    cids.append(q["id"])
                else:
                    ic += 1
                    iids.append(q["id"])
    print(f"  'dowoln*': poprawna {cc}x, niepoprawna {ic}x — ratio {cc/(cc+ic)*100:.1f}%")
    print(f"    Poprawne: Q{cids[:10]}")

# ========== 14. Questions with "Zaznacz zdanie prawdziwe" ==========
print("\n" + "=" * 60)
print("14. Pytania 'Zaznacz zdanie prawdziwe' — pozycja poprawnej")
print("=" * 60)

zaznacz_pos = Counter()
zaznacz_ids = defaultdict(list)
for q in questions:
    if q["multiple"]:
        continue
    if "zaznacz zdani" in q["question"].lower() or "zaznacz zdania prawdziwe" in q["question"].lower():
        for i, opt in enumerate(q["options"]):
            if opt["correct"]:
                zaznacz_pos[i] += 1
                zaznacz_ids[i].append(q["id"])

total_zaznacz = sum(zaznacz_pos.values())
for pos in range(5):
    labels = ["A", "B", "C", "D", "E"]
    cnt = zaznacz_pos.get(pos, 0)
    print(f"  {labels[pos]}: {cnt}/{total_zaznacz} ({cnt/total_zaznacz*100:.1f}%) — Q{zaznacz_ids[pos][:8]}")

# ========== 15. First word / structure of correct answer ==========
print("\n" + "=" * 60)
print("15. CZY POPRAWNA ZAWIERA DODATKOWE WARUNKI/OGRANICZENIA?")
print("=" * 60)

# Count options with conditions like "gdzie k < n", "k >= n"
condition_words = ["gdzie", "takich że", "taki że", "takimi że", "pod warunkiem", 
                   "o ile", "wówczas", "wtedy gdy"]
for cw in condition_words:
    cc = 0
    ic = 0
    for q in questions:
        for opt in q["options"]:
            if cw.lower() in opt["text"].lower():
                if opt["correct"]:
                    cc += 1
                else:
                    ic += 1
    total = cc + ic
    if total >= 3:
        print(f"  '{cw}': poprawna {cc}x, niepoprawna {ic}x — ratio {cc/(total)*100:.1f}%")

print("\n\n===== DONE =====")
