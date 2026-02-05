import fitz

doc = fitz.open(r'c:\Users\Thefr\Dropbox\Komputer\Downloads\Baza pytań _ Dyskretna-Machen.pdf')
text = ''
for page in doc:
    text += page.get_text()
print(text)
