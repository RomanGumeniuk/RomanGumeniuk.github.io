# ⛏ ATM10 — Przewodnik Ekipy

Statyczna strona internetowa dla ekipy graczy All The Mods 10 na Minecrafcie.

## 🚀 Jak wdrożyć na GitHub Pages

### Krok 1: Utwórz repozytorium

1. Zaloguj się na [github.com](https://github.com)
2. Kliknij **New repository** (zielony przycisk)
3. Nazwij repozytorium np. `atm10-guide`
4. Ustaw na **Public**
5. Kliknij **Create repository**

### Krok 2: Wrzuć pliki

Skopiuj wszystkie pliki projektu do repozytorium:

```
index.html
css/style.css
js/main.js
README.md
```

Możesz to zrobić przez:

- **Drag & drop** plików na stronie repozytorium
- Lub przez Git:

```bash
git init
git add .
git commit -m "ATM10 Team Guide"
git branch -M main
git remote add origin https://github.com/TWOJ-USER/atm10-guide.git
git push -u origin main
```

### Krok 3: Włącz GitHub Pages

1. Wejdź w **Settings** repozytorium
2. W bocznym menu kliknij **Pages**
3. W sekcji **Source** wybierz: **Deploy from a branch**
4. Branch: **main**, folder: **/ (root)**
5. Kliknij **Save**

### Krok 4: Gotowe!

Po kilku minutach strona będzie dostępna pod adresem:

```
https://TWOJ-USER.github.io/atm10-guide/
```

## 📁 Struktura plików

```
/
├── index.html          ← Główna strona z całą treścią
├── css/
│   └── style.css       ← Style: dark theme, animacje, responsywność
├── js/
│   └── main.js         ← Logika: karty ról, zakładki, smooth scroll
└── README.md           ← Ten plik
```

## 🎮 Funkcje

- **6 kart ról** z interaktywnym rozwijaniem (Technik, Kombatant, Farmer, Mag, Budowniczy, Odkrywca)
- **Pro Tipy** z 4 zakładkami (Skróty, Ekwipunek, Priorytety, Ogólne)
- **Mapa Progresji** z 3 etapami (Early / Mid / Endgame)
- Dark gaming theme z animacjami
- W pełni responsywna (desktop + tablet + mobile)
- Zero zewnętrznych zależności (oprócz Google Fonts i Font Awesome CDN)
