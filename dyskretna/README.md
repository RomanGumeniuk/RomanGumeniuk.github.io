# 📚 Quiz - Matematyka Dyskretna

Interaktywna strona z pytaniami do nauki matematyki dyskretnej. Idealna do przygotowania się do egzaminu!

## 🌐 Jak uruchomić na GitHub Pages

1. **Utwórz repozytorium na GitHub:**
   - Zaloguj się na [github.com](https://github.com)
   - Kliknij "New repository"
   - Nazwij repozytorium np. `dyskretna-quiz`
   - Zaznacz "Public" (publiczne)
   - Kliknij "Create repository"

2. **Prześlij pliki:**
   - Skopiuj pliki `index.html` i `questions.json` do repozytorium
   - Możesz to zrobić przez interfejs GitHub (przeciągnij pliki) lub przez Git

3. **Włącz GitHub Pages:**
   - Wejdź w "Settings" repozytorium
   - Przewiń do sekcji "Pages"
   - W "Source" wybierz "main" branch
   - Kliknij "Save"
   - Po chwili strona będzie dostępna pod adresem: `https://twoja-nazwa.github.io/dyskretna-quiz/`

## ✨ Funkcje

- **114 pytań** z matematyki dyskretnej
- **Automatyczne zapisywanie** postępu w przeglądarce
- **Filtrowanie** - pokaż tylko pytania nieodpowiedziane, poprawne lub błędne
- **Wyszukiwanie** - szukaj w treści pytań
- **Losowanie kolejności** - ucz się w różnej kolejności
- **Responsywny design** - działa na telefonach i komputerach
- **Ciemny motyw** - przyjazny dla oczu

## 📁 Pliki

- `index.html` - główna strona z quizem (wszystko w jednym pliku)
- `questions.json` - pytania w formacie JSON (opcjonalnie, pytania są też wbudowane w HTML)

## 🎯 Jak używać

1. Wybierz odpowiedź (lub kilka przy pytaniach wielokrotnego wyboru)
2. Kliknij "Sprawdź" przy pytaniu lub "Sprawdź wszystkie"
3. ✓ Zielony = poprawna odpowiedź
4. ✗ Czerwony = błędna odpowiedź
5. ⚠ Żółty = poprawna odpowiedź, której nie zaznaczono

## 🔧 Lokalne uruchomienie

Możesz też uruchomić stronę lokalnie:

```bash
# W folderze z plikami
python -m http.server 8080
# Otwórz http://localhost:8080 w przeglądarce
```

Lub po prostu otwórz plik `index.html` w przeglądarce.

## 📖 Źródło pytań

Pytania pochodzą z bazy pytań "Dyskretna-Machen".

---

Powodzenia na egzaminie! 🍀
