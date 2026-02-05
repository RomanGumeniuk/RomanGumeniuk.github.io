# Pytania z matematyki dyskretnej - dane ze strony https://dyskretna.xn--drog-eta.pl/baza.php

questions = [
    {
        "id": 1,
        "text": "Zaznacz zdania prawdziwe",
        "answers": [
            {"text": "Uporządkowany podział zbioru, to podział zbioru na podzbiory, taki że elementy w tych podzbiorach są uporządkowane rosnąco.", "correct": False},
            {"text": "Jeśli rodzina zbiorów {A₁,A₂,...,Aₖ} jest podziałem zbioru S, to S=A₁∪A₂∪...∪Aₖ.", "correct": True},
            {"text": "Liczba podziałów zbioru S może być zapisana za pomocą współczynnika wielomianowego.", "correct": False},
            {"text": "Podziałem zbioru nazywamy każdą rodzinę pewnych niepustych rozłącznych podzbiorów zbudowanych z pewnych elementów tego zbioru.", "correct": False},
            {"text": "Wszystkie podziały pewnego zbioru n-elementowego można wygenerować za pomocą generacji wszystkich liczb binarnych z zakresu od 0 do 2ⁿ−1.", "correct": False}
        ]
    },
    {
        "id": 2,
        "text": "Obiekty kombinatoryczne B,A,C i C,A,B utworzone ze zbioru {A,B,C,D} i są identyczne (nie można ich odróżnić). Podane obiekty mogą być przykładem:",
        "answers": [
            {"text": "podziału zbioru na dwa podzbiory.", "correct": False},
            {"text": "3-elementowej wariacji bez powtórzeń ze zbioru 4-elementowego.", "correct": False},
            {"text": "3-elementowej wariacji z powtórzeniami ze zbioru 4-elementowego.", "correct": False},
            {"text": "3-elementowej kombinacji z powtórzeniami ze zbioru 4-elementowego.", "correct": True},
            {"text": "3-elementowej permutacji bez powtórzeń ze zbioru 4-elementowego.", "correct": False}
        ]
    },
    {
        "id": 3,
        "text": "Zaznacz zdania prawdziwe:",
        "answers": [
            {"text": "Każde rozmieszczenie k rozróżnialnych elementów w n rozróżnialnych pudełkach odpowiada k-wyrazowej wariacji bez powtórzeń ze zbioru n-elementowego.", "correct": False},
            {"text": "k-wyrazową wariacją bez powtórzeń z n-elementowego zbioru nazywamy każdy ciąg elementów pochodzących z tego zbioru, a liczba takich wariacji wynosi nᵏ.", "correct": False},
            {"text": "Każde liniowe uporządkowanie k rozróżnialnych elementów ze zbioru n-elementowego jest k-wyrazową wariacją bez powtórzeń z tego zbioru.", "correct": True},
            {"text": "k-wyrazową wariacją bez powtórzeń ze zbioru n-elementowego nazywamy każdy k-wyrazowy ciąg elementów tego zbioru i liczba takich wariacji wynosi n!/(n−k)!, gdzie k<n lub k≥n.", "correct": False},
            {"text": "k-wyrazową wariacją bez powtórzeń z n-elementowego zbioru nazywamy każdy k-wyrazowy ciąg elementów tego zbioru.", "correct": False}
        ]
    },
    {
        "id": 4,
        "text": "Każdy sposób wrzucenia 4 identycznych elementów do 5 rozróżnialnych pudełek jest przykładem:",
        "answers": [
            {"text": "5-elementowej wariacji bez powtórzeń ze zbioru 4-elementowego.", "correct": False},
            {"text": "4-elementowej wariacji z powtórzeniami ze zbioru 5-elementowego.", "correct": False},
            {"text": "4-elementowej kombinacji z powtórzeniami ze zbioru 5-elementowego.", "correct": True},
            {"text": "5-elementowej kombinacji bez powtórzeń ze zbioru 4-elementowego.", "correct": False},
            {"text": "4-elementowej permutacji z powtórzeniami ze zbioru 5-elementowego.", "correct": False}
        ]
    },
    {
        "id": 5,
        "text": "Zaznacz zdanie prawdziwe.",
        "answers": [
            {"text": "Zasada dobrego uporządkowania stwierdza, że zbiór liczb całkowitych zawiera element najmniejszy.", "correct": False},
            {"text": "Dowód poprawności pierwszej zasady indukcji matematycznej opiera się o zasadę dobrego uporządkowania i wykorzystuje technikę sprowadzania do sprzeczności.", "correct": True},
            {"text": "Zbiorem dobrze uporządkowanym jest dowolny podzbiór zbioru liczb całkowitych oraz liczb wymiernych, ale nie liczb rzeczywistych.", "correct": False},
            {"text": "Jeśli dla każdej pary elementów a i b można odpowiedzieć na pytanie czy a≤b, to zbiór S jest dobrze uporządkowany.", "correct": False},
            {"text": "Zbiór liczb całkowitych ujemnych jest dobrze uporządkowany.", "correct": False}
        ]
    },
    {
        "id": 6,
        "text": "Zaznacz zdanie prawdziwe.",
        "answers": [
            {"text": "Dowód kroku indukcyjnego w drugiej zasadzie indukcji wymaga wykazania prawdziwości zdania S(n₀)∧S(n₀+1)∧...∧S(k) i prawdziwości zdania S(k+1) dla pewnej liczby k≥1.", "correct": False},
            {"text": "Dowód kroku indukcyjnego w drugiej zasadzie indukcji wymaga pokazania, że dla pewnej konkretnej wartości k≥n₀ zachodzi implikacja [S(n₀)∧...∧S(k)]⇒S(k+1).", "correct": False},
            {"text": "W zasadzie silnej indukcji matematycznej warunek początkowy ma postać S(n₀)∧S(n₀+1)∧...∧S(n₁), gdzie n₀,n₁∈Z⁺ i n₀≤n₁, a S(n) oznacza zdanie otwarte, w którym występuje liczba całkowita dodatnia n.", "correct": True},
            {"text": "Dowód kroku indukcyjnego w drugiej zasadzie indukcji wymaga wykazania prawdziwości zdania S(k+1) dla każdej liczby k≥n₀.", "correct": False},
            {"text": "Dowód warunku początkowego w drugiej zasadzie indukcji matematycznej wymaga pokazania prawdziwości pewnych zdań S(n) dla dowolnych elementów n, takich że n₀≤n≤n₁.", "correct": False}
        ]
    },
    {
        "id": 7,
        "text": "Zasada indukcji matematycznej jest techniką, która może być zastosowana do dowodzenia twierdzeń S(n):",
        "answers": [
            {"text": "dotyczących kolejnych liczb rzeczywistych.", "correct": False},
            {"text": "dotyczących dowolnych liczb dodatnich.", "correct": False},
            {"text": "dotyczących liczb wymiernych.", "correct": False},
            {"text": "w których n należy do zbioru liczb całkowitych dodatnich.", "correct": True},
            {"text": "w których n jest nieujemne.", "correct": False}
        ]
    },
    {
        "id": 8,
        "text": "Zaznacz zdanie prawdziwe.",
        "answers": [
            {"text": "Zależność postaci cₙaₙ+cₙ₋₁aₙ₋₁+cₙ₋₂aₙ₋₂+cₙ₋₃aₙ₋₃=0, gdzie cₙ,cₙ₋₁,cₙ₋₂,cₙ₋₃ są pewnymi stałymi, cₙ≠0 i cₙ₋₃≠0, jest liniową zależnością rekurencyjną jednorodną rzędu trzeciego i może być rozwiązana za pomocą równania charakterystycznego stopnia trzeciego.", "correct": True},
            {"text": "Rozwiązanie liniowej niejednorodnej zależności rekurencyjnej rzędu pierwszego ze stałymi współczynnikami, postaci aₙ₊₁+caₙ=f(n) jest dane wzorem: aₙ=a₀dⁿ gdzie d₀ i d oznaczają pewne stałe, n∈N.", "correct": False},
            {"text": "Rozwiązanie liniowej niejednorodnej zależności rekurencyjnej rzędu drugiego ze stałymi współczynnikami, ma postać aₙ=c₁r₁ⁿ+c₂r₂ⁿ lub aₙ=c₁r₁ⁿ+c₂nrⁿ w zależności od liczby różnych pierwiastków równania charakterystycznego.", "correct": False},
            {"text": "Rozwiązanie liniowej jednorodnej zależności rekurencyjnej rzędu drugiego ze stałymi współczynnikami o równaniu charakterystycznym o dwóch różnych pierwiastkach, ma postać aₙ=c₁x₁ⁿ+c₂x₂ⁿ gdzie x₁ i x₂ są wyznaczane w oparciu o początkowe elementy ciągu.", "correct": False},
            {"text": "Wyznaczenie wzoru jawnego jest możliwe dla ciągów liczbowych opisanych jedynie zależnościami rekurencyjnymi jednorodnymi.", "correct": False}
        ]
    },
    {
        "id": 9,
        "text": "Zależność rekurencyjna (a₀=0, a₁=3, a₂=4, a₃=6, 2aₙ₊₁+3aₙ₋₃=0 dla n≥3) jest zależnością rekurencyjną:",
        "answers": [
            {"text": "liniową ze stałymi współczynnikami rzędu czwartego jednorodną.", "correct": True},
            {"text": "liniową ze stałymi współczynnikami rzędu drugiego jednorodną.", "correct": False},
            {"text": "liniową ze stałymi współczynnikami rzędu pierwszego niejednorodną.", "correct": False},
            {"text": "liniową ze stałymi współczynnikami rzędu czwartego niejednorodną.", "correct": False},
            {"text": "liniową ze stałymi współczynnikami rzędu trzeciego jednorodną.", "correct": False}
        ]
    },
    {
        "id": 10,
        "text": "Zależność rekurencyjna (a₀=1, a₁=2, a₂=3, aₙ+5aₙ₋₁−4aₙ₋₃=0 dla n≥3) jest zależnością:",
        "answers": [
            {"text": "która nie może być rozwiązana metodą równania charakterystycznego.", "correct": False},
            {"text": "dla której równanie charakterystyczne jest równaniem kwadratowym.", "correct": False},
            {"text": "dla której równanie charakterystyczne jest równaniem stopnia trzeciego.", "correct": True},
            {"text": "nieliniową.", "correct": False},
            {"text": "niejednorodną.", "correct": False}
        ]
    },
    {
        "id": 11,
        "text": "Zaznacz zdanie prawdziwe:",
        "answers": [
            {"text": "Liczby Stirlinga drugiego rodzaju opisujące liczbę sposobów podziału zbioru n-elementowego na k-niepustych podzbiorów są nie mniejsze niż liczby Stirlinga pierwszego rodzaju opisujące liczbę sposobów rozmieszczenia n elementów w k cyklach.", "correct": False},
            {"text": "Z definicji przyjmuje się, że liczba Stirlinga drugiego rodzaju S(n,n)=1 dla n≥0, ponieważ opisywany przez nią podział jest niemożliwy.", "correct": False},
            {"text": "Liczby harmoniczne Hₙ są dyskretnym odpowiednikiem funkcji f(x)=1/x i tworzą ciąg liczbowy rosnący logarytmicznie wolno dla n→∞.", "correct": False},
            {"text": "Liczby Eulera pierwszego rzędu ⟨n⟩ oznaczają liczbę n-elementowych permutacji bez powtórzeń ze zbioru n-elementowego zawierających k wzniesień.", "correct": True},
            {"text": "Twierdzenie Zeckendorfa stwierdza, iż każda liczba całkowita dodatnia n może być jednoznacznie przedstawiona w postaci iloczynu pewnych liczb Fibonacciego i zapisana w postaci odpowiedniego ciągu zer i jedynek.", "correct": False}
        ]
    },
    {
        "id": 12,
        "text": "Zaznacz zdanie prawdziwe:",
        "answers": [
            {"text": "Liczby Fibonacciego są przykładem zależności rekurencyjnej rzędu drugiego niejednorodnej.", "correct": False},
            {"text": "Ciąg liczb harmonicznych jest zbudowany z liczb całkowitych.", "correct": False},
            {"text": "Za pomocą liczb Stirlinga pierwszego rodzaju s(n,k), k=0,1,…,n, można obliczyć wartość funkcji n!.", "correct": True},
            {"text": "Liczby Eulera związane są z liczbą k-elementowych podzbiorów zbioru n-elementowego.", "correct": False},
            {"text": "Liczby Stirlinga drugiego rodzaju związane są ze zliczaniem k-elementowych permutacji ze zbioru n-elementowego.", "correct": False}
        ]
    },
    {
        "id": 13,
        "text": "Zaznacz zdanie prawdziwe:",
        "answers": [
            {"text": "Zasada włączania i wyłączania ma postać: |⋃ᵢ₌₁ⁿAᵢ|=∑ᵢ₌₁ⁿ|Aᵢ|+∑₁≤i<j≤n|Aᵢ∩Aⱼ|+⋯+(−1)ⁿ⁻¹|A₁∩A₂∩⋯∩Aₙ|", "correct": False},
            {"text": "Zasada włączania i wyłączania, mówi, że aby wyznaczyć liczbę elementów zbioru A₁∪A₂∪⋯∪Aₙ, należy zanalizować wszystkie możliwe przecięcia (części wspólne) zbiorów z rodziny {A₁,A₂,…,Aₙ} i dodać liczność przecięć nieparzystej liczby zbiorów oraz odjąć liczność przecięć parzystej liczby zbiorów.", "correct": True},
            {"text": "Zasada włączania i wyłączania, mówi, że aby wyznaczyć liczbę elementów zbioru A₁∩A₂∩⋯∩Aₙ, należy zanalizować wszystkie możliwe przecięcia zbiorów z rodziny {A₁,A₂,…,Aₙ} i dodać liczność przecięć parzystej liczby zbiorów oraz odjąć liczność przecięć nieparzystej liczby zbiorów.", "correct": False},
            {"text": "Zasada włączania i wyłączania jest uogólnieniem prawa sumy umożliwiającym obliczenie liczności części wspólnej zbiorów, bez konieczności wyznaczania elementów należących do tej części wspólnej.", "correct": False},
            {"text": "Prawo sumy (pozwalające na wyznaczenie liczności sumy dwóch zbiorów) nie jest równoważne zasadzie włączania i wyłączania (pozwalającej na wyznaczenie liczności sumy zbiorów A₁,…,Aₙ dla n=2.", "correct": False}
        ]
    },
    {
        "id": 14,
        "text": "Pełna poprawna zasada włączania i wyłączania dla 4 zbiorów składa się z",
        "answers": [
            {"text": "4 składników, ponieważ są 4 zbiory.", "correct": False},
            {"text": "15 składników.", "correct": True},
            {"text": "16 składników, ponieważ należy sprawdzić część wspólną każdego zbioru z każdym.", "correct": False},
            {"text": "5 składników.", "correct": False},
            {"text": "nieskończonej liczby składników.", "correct": False}
        ]
    },
    {
        "id": 15,
        "text": "Zaznacz zdanie prawdziwe.",
        "answers": [
            {"text": "Zasada szufladkowa Dirichleta stwierdza, że jeśli skończony zbiór S jest podzielony na k rozłącznych niepustych podzbiorów, to dokładnie jeden z tych zbiorów zawiera ⌈|S|/k⌉ elementów lub więcej.", "correct": False},
            {"text": "Zasada szufladkowa Dirichleta stwierdza, że jeśli skończony zbiór S jest podzielony na k rozłącznych niepustych podzbiorów, to liczność tych wszystkich zbiorów wynosi co najmniej ⌊|S|/k⌋.", "correct": False},
            {"text": "Uogólniona zasada szufladkowa sprowadza się do „klasycznej" zasady szufladkowej, gdy każdy z elementów analizowanego zbioru S należy do co najmniej jednego podzbioru spośród A₁,…,Aₖ.", "correct": False},
            {"text": "Uogólniona zasada szufladkowa Dirichleta określa minimalną wartość średniej arytmetycznej liczb elementów zbiorów A₁,…,Aₖ będących podzbiorami skończonego zbioru S, takimi że każdy element zbioru S należy do co najmniej 1 spośród zbiorów Aᵢ (1≤|S|/k).", "correct": True},
            {"text": "Dowód uogólnionej zasady szufladkowej Dirichleta wymaga zastosowania zwykłej zasady szufladkowej.", "correct": False}
        ]
    },
    {
        "id": 16,
        "text": "Jeśli zbiór 12 elementowy zostanie podzielony w dowolny sposób na 3 niepuste rozłączne podzbiory, to",
        "answers": [
            {"text": "dokładnie jeden podzbiór zawiera 4 elementy lub więcej.", "correct": False},
            {"text": "dokładnie jeden podzbiór zawiera 4 elementy.", "correct": False},
            {"text": "co najwyżej jeden podzbiór zawiera 4 elementy lub więcej.", "correct": False},
            {"text": "co najmniej jeden podzbiór zawiera 4 elementy lub więcej.", "correct": True},
            {"text": "podzbiory są równoliczne.", "correct": False}
        ]
    },
    {
        "id": 17,
        "text": "Zaznacz zdanie prawdziwe.",
        "answers": [
            {"text": "Macierz o wymiarze p×p zbudowaną z elementów ze zbioru {1,…,n}, gdzie p<n, w której w żadnym wierszu i kolumnie elementy się nie powtarzają nazywamy kwadratem łacińskim.", "correct": False},
            {"text": "Rozszerzenie prostokąta łacińskiego p×q (p≤n, q<n) do kwadratu n×n nie jest możliwe, jeśli dla pewnego elementu l (1≤l≤n) liczba jego wystąpień w prostokącie l(l) jest mniejsza od p+q−n.", "correct": True},
            {"text": "Rozszerzenie dowolnego prostokąta łacińskiego o dodatkowe kolumny jest zawsze możliwe, należy jedynie w każdej nowej kolumnie umieszczać elementy występujące najrzadziej.", "correct": False},
            {"text": "Rozszerzalny prostokąt łaciński p×q rozbudowuje się do kwadratu łacińskiego n×n przez dopisanie najpierw (n−q) wierszy, a następnie (n−p) kolumn.", "correct": False},
            {"text": "Dla n będącego liczbą pierwszą istnieje dokładnie n−1 wzajemnie ortogonalnych kwadratów łacińskich o wymiarze n×n, a dla n będącego potęgą liczby pierwszej co najmniej n−1 wzajemnie ortogonalnych kwadratów łacińskich o wymiarze n×n.", "correct": False}
        ]
    },
    {
        "id": 18,
        "text": "Zaznacz zdanie prawdziwe:",
        "answers": [
            {"text": "Dla dowolnej szachownicy B, wartość współczynnika r₁ jest równa liczbie zabronionych pól obszaru B.", "correct": False},
            {"text": "Wielomian szachowy dla obszaru B o wymiarze n×n, postaci r(x)=1+r₁x+r₂x²+⋯+rₙxⁿ, nie zawiera niezerowych współczynników rₖ dla k>n, ponieważ nie można ustawić więcej niż n wzajemnie nieatakujących się wież na szachownicy o wymiarze n×n.", "correct": True},
            {"text": "Każda linia pozioma dzieli dowolną szachownicę B na dwa niezależne obszary, niemające wspólnych wierszy ani kolumn.", "correct": False},
            {"text": "Jeśli szachownica B składa się z dwóch niezależnych obszarów C,D, to wówczas r(x)=r(C)+xr(D).", "correct": False},
            {"text": "W oparciu o wielomian szachowy obszaru B można wyznaczyć wszystkie współczynniki wielomianu szachowego dla dopełnienia tego obszaru B̄.", "correct": False}
        ]
    },
    {
        "id": 19,
        "text": "Zaznacz zdanie prawdziwe.",
        "answers": [
            {"text": "k-wyrazową wariacją z powtórzeniami ze zbioru n-elementowego nazywamy każdy k-wyrazowy ciąg elementów tego zbioru, a liczba takich wariacji wynosi: n!/(n−k)!, gdzie k<n lub k≥n.", "correct": False},
            {"text": "Liczba k-wyrazowych wariacji z powtórzeniami jest równa liczbie k-wyrazowych permutacji z powtórzeniami.", "correct": False},
            {"text": "k-wyrazowa wariacja z powtórzeniami ze zbioru n-elementowego odpowiada rozmieszczeniu k rozróżnialnych elementów w n rozróżnialnych pudełkach.", "correct": True},
            {"text": "Liczba k-wyrazowych wariacji z powtórzeniami ze zbioru n-elementowego jest nie większa od liczby k-wyrazowych wariacji bez powtórzeń.", "correct": False},
            {"text": "Istnieje bᵇ różnych b-wyrazowych wariacji z powtórzeniami ze zbioru a-elementowego (a≤b lub b<a).", "correct": False}
        ]
    },
    {
        "id": 20,
        "text": "Obiekty kombinatoryczne D,C,A,B i A,D,C,B zostały utworzone ze zbioru {A,B,C,D,E} i nie są identyczne (można je odróżnić). Podane obiekty mogą być przykładem:",
        "answers": [
            {"text": "4-elementowej kombinacji z powtórzeniami ze zbioru 5-elementowego.", "correct": False},
            {"text": "5-elementowej wariacji z powtórzeniami ze zbioru 4-elementowego.", "correct": False},
            {"text": "4-elementowej wariacji bez powtórzeń ze zbioru 5-elementowego.", "correct": True},
            {"text": "Uporządkowanego podziału zbioru na dwa podzbiory.", "correct": False},
            {"text": "4-elementowej kombinacji bez powtórzeń ze zbioru 5-elementowego.", "correct": False}
        ]
    },
    {
        "id": 21,
        "text": "Zaznacz zdanie prawdziwe.",
        "answers": [
            {"text": "Kombinacja k-elementowa z powtórzeniami ze zbioru n-elementowego, to k-elementowy podzbiór elementów tego zbioru, w którym kolejność elementów nie jest istotna.", "correct": False},
            {"text": "Każda k-elementowa kombinacja z powtórzeniami ze zbioru n-elementowego może być przedstawiona jako k-elementowa permutacja z powtórzeniami ze zbioru n-elementowego.", "correct": False},
            {"text": "Każda k-elementowa kombinacja z powtórzeniami ze zbioru n-elementowego może być interpretowana jako rozmieszczenie k identycznych elementów w n rozróżnialnych pudełkach.", "correct": True},
            {"text": "Każda k-elementowa kombinacja z powtórzeniami ze zbioru n-elementowego może być przedstawiona jako permutacja z powtórzeniami dwóch różnych symboli powtarzających się odpowiednio n i k razy.", "correct": False},
            {"text": "Liczba wszystkich k-elementowych kombinacji z powtórzeniami ze zbioru n-elementowego wynosi C(k+n−1,n) gdzie k<n.", "correct": False}
        ]
    },
    {
        "id": 22,
        "text": "Do 6 rozróżnialnych pudełek wrzucane są w dowolny sposób 4 rozróżnialne elementy. Każdy sposób wrzucenia elementów do pudełek jest przykładem:",
        "answers": [
            {"text": "4-elementowej wariacji z powtórzeniami ze zbioru 6-elementowego.", "correct": True},
            {"text": "6-elementowej permutacji z powtórzeniami ze zbioru 4-elementowego.", "correct": False},
            {"text": "4-elementowej kombinacji z powtórzeniami ze zbioru 6-elementowego.", "correct": False},
            {"text": "4-elementowej wariacji bez powtórzeń ze zbioru 6-elementowego.", "correct": False},
            {"text": "6-elementowej kombinacji z powtórzeniami ze zbioru 4-elementowego.", "correct": False}
        ]
    },
    {
        "id": 23,
        "text": "Zaznacz zdanie prawdziwe.",
        "answers": [
            {"text": "Pierwsza zasada indukcji matematycznej może być sformułowana następująco [S(1)∧(∀k≥1 S(k)⇒S(k+1))]⇒∀n≥1 S(n), gdzie S(n) oznacza zdanie otwarte, w którym występuje pewna liczba całkowita dodatnia n.", "correct": True},
            {"text": "Pierwsza zasada indukcji może być podana dla dowolnego elementu n₀, od którego rozpoczyna się proces indukcyjny i przyjmuje wówczas postać [S(n₀)∧(S(k)⇒S(k+1))]⇒∀n≥n₀ S(n).", "correct": False},
            {"text": "Dowód kroku indukcyjnego w pierwszej zasadzie indukcji matematycznej wymaga wykazania prawdziwości zdania S(k) i prawdziwości zdania S(k+1) dla pewnej liczby k≥1.", "correct": False},
            {"text": "Dowód warunku początkowego w pierwszej zasadzie indukcji matematycznej wymaga pokazania prawdziwości zdania S(n) dla dowolnego elementu n≥n₀.", "correct": False},
            {"text": "Dowód kroku indukcyjnego w pierwszej zasadzie indukcji matematycznej wymaga wykazania prawdziwości zdania S(k) i prawdziwości zdania S(k+1) dla każdej liczby k≥n₀.", "correct": False}
        ]
    },
    {
        "id": 24,
        "text": "Zasada indukcji matematycznej może być zastosowana do dowodzenia twierdzeń S(n), w którym n należy do zbioru:",
        "answers": [
            {"text": "liczb rzeczywistych dodatnich.", "correct": False},
            {"text": "liczb naturalnych.", "correct": True},
            {"text": "dowolnego podzbioru zbioru liczb wymiernych.", "correct": False},
            {"text": "liczb całkowitych.", "correct": False},
            {"text": "liczb rzeczywistych.", "correct": False}
        ]
    },
    {
        "id": 25,
        "text": "Zaznacz zdanie prawdziwe.",
        "answers": [
            {"text": "Rozwiązanie zależności liniowej jednorodnej rzędu drugiego ze stałymi współczynnikami o równaniu charakterystycznym o dwóch różnych pierwiastkach x₁ i x₂ ma postać aₙ=x₁r₁ⁿ+x₂r₂ⁿ.", "correct": False},
            {"text": "Każda zależność postaci cₙaₙ+cₙ₋₁aₙ₋₁+…+cₙ₋ₖaₙ₋ₖ=0, gdzie cᵢ dla i=n−k,…,n są zupełnie dowolnymi stałymi rzeczywistymi, jest liniową zależnością rekurencyjną rzędu k-tego.", "correct": True},
            {"text": "Rozwiązanie liniowej jednorodnej zależności rekurencyjnej rzędu pierwszego ze stałymi współczynnikami postaci aₙ₊₁+caₙ=0 jest dane wzorem aₙ=a₀bⁿ, gdzie b=−c, a c oznacza pewną stałą i nie ∈N.", "correct": False},
            {"text": "Rozwiązanie zależności rekurencyjnej polega na wyznaczeniu wartości liczbowej elementu ciągu występującego po elementach początkowych.", "correct": False},
            {"text": "Zależność postaci cₙaₙ+cₙ₋₁aₙ₋₁+cₙ₋₂aₙ₋₂=1, gdzie cₙ,cₙ₋₁,cₙ₋₂ są pewnymi stałymi, cₙ≠0 i cₙ₋₂≠0, może być rozwiązana za pomocą metody równania charakterystycznego.", "correct": False}
        ]
    },
    {
        "id": 26,
        "text": "Zależność rekurencyjna (a₀=0, a₁=3, a₂=4, a₃=6, 2aₙ+3aₙ₋₄=2 dla n≥4) jest zależnością rekurencyjną:",
        "answers": [
            {"text": "liniową ze stałymi współczynnikami rzędu drugiego jednorodną.", "correct": False},
            {"text": "liniową ze stałymi współczynnikami rzędu pierwszego niejednorodną.", "correct": False},
            {"text": "liniową ze stałymi współczynnikami rzędu czwartego niejednorodną.", "correct": True},
            {"text": "liniową ze stałymi współczynnikami rzędu czwartego jednorodną.", "correct": False},
            {"text": "którą można rozwiązać za pomocą metody równania charakterystycznego.", "correct": False}
        ]
    },
    {
        "id": 27,
        "text": "Zależność rekurencyjna (a₀=1, a₁=2, a₂=3, a₃=4, aₙ₊₁+5aₙ₋₁−4aₙ₋₃=0) dla n≥3 jest zależnością:",
        "answers": [
            {"text": "która nie może być rozwiązana metodą równania charakterystycznego.", "correct": False},
            {"text": "dla której równanie charakterystyczne jest równaniem kwadratowym.", "correct": False},
            {"text": "nieliniową.", "correct": False},
            {"text": "dla której równanie charakterystyczne jest równaniem stopnia czwartego.", "correct": True},
            {"text": "niejednorodną.", "correct": False}
        ]
    },
    {
        "id": 28,
        "text": "Zaznacz zdanie prawdziwe.",
        "answers": [
            {"text": "Wyrażenia postaci x(n,n)=1, n≥0 oraz x(n,0)=0, n>0 są składnikami definicji rekurencyjnej liczb Stirlinga zarówno pierwszego (x=s), jak i drugiego rodzaju (x=S).", "correct": True},
            {"text": "Z definicji przyjmuje się, że liczba Stirlinga pierwszego rodzaju s(n,n)=1 dla n≥0, ponieważ opisywane przez nią rozmieszczenie obiektów w cyklach jest niemożliwe.", "correct": False},
            {"text": "Liczby Eulera drugiego rzędu ⟨⟨n,k⟩⟩ oznaczają liczbę dowolnych permutacji z powtórzeniami ze zbioru n-elementowego zawierających k wzniesień takich, że pomiędzy poszczególnymi wystąpieniami pewnej liczby znajdują się tylko liczby większe od niej.", "correct": False},
            {"text": "Liczby harmoniczne drugiego rzędu Hₙ⁽²⁾ są dyskretnym odpowiednikiem funkcji f(x)=1/x.", "correct": False},
            {"text": "W oparciu o twierdzenie Zeckendorfa można stworzyć system liczbowy, w którym dowolna liczba rzeczywista dodatnia może być przedstawiona jako ∑ₖ₌₀ᵐbₖFₖ, gdzie bₖ∈{0,1}, a Fₖ oznacza liczbę Fibonacciego.", "correct": False}
        ]
    },
    {
        "id": 29,
        "text": "Zaznacz zdanie prawdziwe.",
        "answers": [
            {"text": "Liczby Stirlinga drugiego rodzaju dotyczą podziału zbioru na cykle, a liczby Stirlinga pierwszego rodzaju podziału zbioru na podzbiory.", "correct": False},
            {"text": "Liczby Eulera dotyczą wariacji z powtórzeniami.", "correct": False},
            {"text": "Cykle jedno- i dwu-elementowe są równoważne zbiorom jedno- i dwu-elementowym.", "correct": True},
            {"text": "Ciąg liczb harmonicznych pierwszego rzędu jest zbieżny.", "correct": False},
            {"text": "Ciąg liczb Fibonacciego jest przykładem zależności rekurencyjnej rzędu trzeciego, ponieważ w zależności rekurencyjnej występują trzy elementy ciągu.", "correct": False}
        ]
    },
    {
        "id": 30,
        "text": "Zaznacz zdanie prawdziwe.",
        "answers": [
            {"text": "Zasada włączania i wyłączania jest uogólnieniem prawa iloczynu dla więcej niż dwóch zbiorów skończonych.", "correct": False},
            {"text": "Zasada włączania i wyłączania ma postać: |⋃ᵢ₌₁ⁿAᵢ|=∑ᵢ₌₁ⁿ|Aᵢ|−∑₁≤i<j≤n|Aᵢ∩Aⱼ|+∑₁≤i<j<k≤n|Aᵢ∩Aⱼ∩Aₖ|−⋯+(−1)ⁿ⁻¹|A₁∩A₂∩⋯∩Aₙ|", "correct": True},
            {"text": "Zasada włączania i wyłączania umożliwia obliczenie liczności części wspólnej n zbiorów A₁,A₂,...,Aₙ w oparciu o liczności sum zbiorów z rodziny {A₁,A₂,...,Aₙ}.", "correct": False},
            {"text": "Zasadę włączania i wyłączania stosuje się do obliczenia liczności sumy pewnej liczby zbiorów w sytuacji, gdy nie można wyznaczyć elementów należących do tej sumy.", "correct": False},
            {"text": "Zasadę włączania i wyłączania można zastosować wyłącznie do obliczenia liczności sumy zbiorów, których części wspólne nie są zbiorami pustymi; zasady tej nie można zastosować dla zbiorów rozłącznych.", "correct": False}
        ]
    }
]
