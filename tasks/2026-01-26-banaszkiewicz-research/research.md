# Research: Anna Banaszkiewicz (Instytut Nenckiego)

## Profil

**Stanowisko**: Postdoc w Laboratorium Neurobiologii Języka (Laboratory of Language Neurobiology)
**Instytucja**: Instytut Biologii Doświadczalnej im. M. Nenckiego PAN, Warszawa
**Kierownik laboratorium**: prof. Katarzyna Jednoróg
**Email**: a.banaszkiewicz@nencki.edu.pl

### Wykształcenie i kariera
- PhD w Laboratorium Obrazowania Mózgu (Nencki) - temat: neuroplastyczność i język migowy
- Promotor: prof. Artur Marchewka
- Mgr psychologii (UW, 2014)
- Staż postdoc: Vanderbilt University (Brain Development Laboratory)
- Staż badawczy: Basque Center of Cognition, Brain and Language (2021-2022)

### Granty jako PI
- NCN ETIUDA (2019/32/T/HS6/00529)
- NCN PRELUDIUM (2017/27/N/HS6/02722)

---

## Co robi w pracy

### Główne obszary badawcze

1. **Neuroplastyczność indukowana nauką języka**
   - Jak mózg reorganizuje się podczas nauki nowego języka
   - Dynamika zmian w czasie (badania longitudinalne)
   - Multimodalne podejście MRI (fMRI + DTI)

2. **Język migowy i bimodalny bilingwizm**
   - Nauka języka migowego przez osoby słyszące
   - Przetwarzanie języka migowego u głuchych i słyszących
   - Wpływ wieku na akwizycję języka

3. **Rozwój językowy u dzieci neuroróżnorodnych**
   - Związek między umiejętnościami językowymi, uwagą i poznaniem społecznym
   - Różnice indywidualne w rozwoju językowym
   - Dysleksja i ryzyko rodzinne dysleksji

### Metodologia (ogólnie)
- fMRI (funkcjonalne obrazowanie rezonansem magnetycznym)
- DTI (obrazowanie tensora dyfuzji) - mikrostruktura istoty białej
- TMS (przezczaszkowa stymulacja magnetyczna)
- Badania longitudinalne (wielokrotne pomiary w czasie)
- Metody behawioralne

---

## Szczegóły metodologiczne (z publikacji)

### Oprogramowanie i narzędzia

| Narzędzie | Zastosowanie | Źródło |
|-----------|--------------|--------|
| **SPM8/SPM12** | Preprocessing fMRI, GLM analysis | Badania dysleksji, język migowy |
| **FSL (eddy, FNIRT)** | Korekcja artefaktów DTI, rejestracja | Badania Braille, DTI |
| **ANTs** | Tworzenie szablonów grupowych, rejestracja nieliniowa | DTI template building |
| **ART toolbox** | Odrzucanie wolumenów z ruchem | Badania dzieci |
| **R (rmcorr package)** | Korelacje repeated-measures, statystyki | Wszystkie badania |
| **MATLAB** | Skrypty analityczne, preprocessing | Całe laboratorium |
| **dcm2bids, heudiconv** | Konwersja DICOM → BIDS | GitHub nencki-lobi |

### Pipeline preprocessingu fMRI (SPM-based)

1. **Motion correction** - korekcja ruchu głowy
2. **Slice timing correction** - korekcja czasu akwizycji
3. **Normalization** - do przestrzeni MNI
4. **Smoothing** - wygładzanie przestrzenne
5. **ART toolbox** - identyfikacja artefaktów:
   - Threshold ruchu: 3 mm translacja
   - Threshold rotacji: 0.05 rad
   - Kryterium włączenia: min. 80% wolumenów bez artefaktów

### Pipeline preprocessingu DTI (FSL + ANTs)

1. **Denoising** - filtr Marchenko-Pastur PCA
2. **Gibbs ringing correction**
3. **Eddy current & motion correction** (FSL eddy)
4. **B0 field inhomogeneity correction**
5. **Tensor fitting** - weighted linear least squares
6. **Template creation** (ANTs buildtemplateparallel)
7. **Metryki**: FA (Fractional Anisotropy), AD, RD

### Analizy statystyczne

| Metoda | Kontekst użycia |
|--------|-----------------|
| **GLM (General Linear Model)** | Modelowanie aktywacji fMRI |
| **Repeated-measures ANOVA** | Porównania między time pointami |
| **ROI analysis** | Analiza w zdefiniowanych regionach |
| **Whole-brain analysis** | Eksploracyjna, FWE/FDR corrected |
| **rmcorr (R)** | Korelacje dla danych longitudinalnych |
| **Bootstrap** | Przedziały ufności (100 resamples) |

### Korekty wielokrotnych porównań
- **FWE (Family-Wise Error)** - p < 0.05
- **Bonferroni correction** - dla ROI
- Progi: *p ≤ .05; **p ≤ .005; ***p ≤ .001

### Typowy design eksperymentu (badania longitudinalne)

```
TP0 (baseline) → TP1 (2.5 mies) → TP2 (5 mies) → TP3 (8 mies) → TP4 (follow-up)
     ↓                ↓               ↓              ↓              ↓
   fMRI            fMRI           fMRI          fMRI           fMRI
   DTI             DTI            DTI           DTI            DTI
   Behavioral      Behavioral     Behavioral    Behavioral     Behavioral
```

5 sesji neuroobrazowania × ~30 uczestników = **~150 skanów** na projekt

---

## Codzienna praca (z rozmowy)

### Profil pracy
- **Naukowiec, nie programista** - zna R, ale nie jest ekspertem
- **Dużo data wrangling** - czyszczenie, przetwarzanie, QC
- **Pipeline'y danych** - często problematyczne, wymagają dostosowania

### Aktualny problem (anegdota)
- Nowy pipeline neuroobrazowania → **zaszumione dane**
- Inni badacze (dorośli) olewają → u nich szum mniej wpływa
- **Ona bada dzieci** → dzieci się ruszają, mniejsze mózgi, więcej artefaktów
- Musi sama odszumiać dane
- Algorytm semi-supervised do QC: ona oznacza "dobre/złe", model się uczy
- **Output: CSV z 30 kolumnami** - metryki jakości, trudne do interpretacji

### Implikacje dla oferty
To nie jest klient na abstrakcyjne "AI Workspace" - to klient który potrzebuje:
- Pomocy z kodem R/Python
- Interpretacji outputów z narzędzi
- Debugowania skryptów
- "Rubber duck" dla problemów analitycznych

---

### Kluczowe publikacje
- "Multimodal imaging of brain reorganization in hearing late learners of sign language" (2020, Human Brain Mapping)
- "The role of the superior parietal lobule in lexical processing of sign language" (2021, Cortex)
- "Temporal Dynamics of Brain White Matter Plasticity in Sighted Subjects during Tactile Braille Learning" (2021, J Neuroscience)
- "Children with dyslexia and familial risk for dyslexia present atypical development of the neuronal phonological network" (2019)

---

## Kontekst laboratorium

Laboratorium Neurobiologii Języka (prof. Jednoróg) zajmuje się:
- Neurobiologicznymi podstawami umiejętności językowych
- Typowym i atypowym rozwojem czytania u dzieci
- Predyktorami zaburzeń rozwojowych (dysleksja)
- Interwencjami opartymi na dowodach

Metody laboratorium: fMRI, sMRI, EEG, ERP, VBM, SBM, DTI, spektroskopia MR (MEGA-PRESS)

---

## Co możemy zaproponować

### 🎯 Najlepsze dopasowanie: Claude jako "starszy kolega który umie kodować"

**Jej sytuacja**: Naukowiec, nie programista. Zna trochę R, musi robić rzeczy programistyczne.

**Propozycja**: Pokazać jak Claude może być asystentem do:
- **Debugging kodu R** - "co ten błąd znaczy?", "dlaczego to nie działa?"
- **Pisanie funkcji** - "napisz mi funkcję która przekształci ten CSV"
- **Interpretacja outputów** - "mam 30 kolumn z pipeline'u, co to znaczy?"
- **Dokumentacja** - "skomentuj ten skrypt żeby inni zrozumieli"

**Entry point**: "Pokaż mi swój najbardziej frustrujący skrypt R - rozwiążemy go w 15 minut"

---

### Inne możliwości (mniej pilne)

#### 1. Wsparcie przy Quality Control danych

**Problem**: Zaszumione dane z nowego pipeline'u, algorytm semi-supervised, CSV z 30 kolumnami.

**Claude może**:
- Wyjaśnić co poszczególne metryki QC znaczą
- Pomóc napisać skrypt do automatycznej klasyfikacji
- Wizualizacja rozkładów metryk (ggplot2)

#### 2. Grant Writing Support

**Problem**: Pisanie grantów NCN/ERC pochłania tygodnie.

**Propozycja**: Workflow wspierający:
- Research background i state-of-the-art
- Spójność narracji między sekcjami
- Iteracyjne poprawki z feedbackiem

**Relevance**: Jako postdoc prawdopodobnie aplikuje o SONATA, OPUS, ERC Starting.

#### 3. Systematic Literature Review

**Problem**: Śledzenie literatury o neuroplastyczności, rozwoju językowym, dysleksji.

**Claude może**:
- Podsumowywać artykuły
- Ekstrahować metodologie z papers
- Budować tabele porównawcze badań

#### 4. Knowledge Management dla laboratorium

**Problem**: Wiedza metodologiczna rozproszona, onboarding nowych osób.

**Propozycja** (długoterminowo):
- Dokumentacja protokołów SPM/FSL
- FAQ dla typowych problemów
- Onboarding guide dla nowych PhD students

---

## Jak podejść do rozmowy

### Kluczowy insight
Ona nie potrzebuje "systemu" ani "workspace'u" - potrzebuje **pomocy z codziennymi frustracjami**:
- Kod który nie działa
- Output którego nie rozumie
- Zadanie które zajmuje za dużo czasu

### Pytania otwierające (konkretne, nie abstrakcyjne)
- "Ile czasu spędzasz na debugowaniu kodu R?"
- "Co robisz gdy skrypt nie działa a nie wiesz dlaczego?"
- "Jak radzisz sobie z tym CSV z 30 kolumnami z pipeline'u?"
- "Kto Ci pomaga gdy utkniesz na problemie technicznym?"

### Demo zamiast sprzedaży
**Propozycja**: "Pokaż mi jeden konkretny problem - rozwiążemy go razem w 15 minut"

Przykłady problemów które można rozwiązać na żywo:
- Błąd w skrypcie R
- Interpretacja dziwnych wyników
- Wizualizacja danych
- Zrozumienie dokumentacji narzędzia

### Potencjalne obiekcje
- "Nie mam czasu" → To właśnie oszczędza czas, demo na żywo
- "AI nie zna mojej dziedziny" → Pokazać że rozumie SPM, FSL, rmcorr
- "To brzmi skomplikowane" → Niski próg: wystarczy mówić do chatbota

---

## Źródła

### Profile
- [ResearchGate - Anna Banaszkiewicz](https://www.researchgate.net/profile/Anna-Banaszkiewicz)
- [Google Scholar](https://scholar.google.pl/citations?user=ocUfYqIAAAAJ&hl=pl)
- [Laboratory of Language Neurobiology - Nencki](https://nencki.edu.pl/laboratories/laboratory-of-language-neurobiology/)
- [Vanderbilt Brain Development Lab - Alumni](https://lab.vanderbilt.edu/boothlab/people/alumni/)
- [GitHub nencki-lobi](https://github.com/nencki-lobi) - repozytoria laboratorium

### Kluczowe publikacje (pełne teksty/abstrakty)
- [Multimodal imaging of brain reorganization in sign language learners (2021, Human Brain Mapping)](https://pubmed.ncbi.nlm.nih.gov/33098616/)
- [Brain plasticity during tactile Braille learning (2021, NeuroImage)](https://pubmed.ncbi.nlm.nih.gov/33307223/)
- [Superior parietal lobule in sign language processing (2021, Cortex)](https://pubmed.ncbi.nlm.nih.gov/33401098/)
- [White matter plasticity in Braille learning (2021, J Neuroscience)](https://pmc.ncbi.nlm.nih.gov/articles/PMC8372016/)
- [Children with dyslexia - phonological network (2019, Frontiers)](https://www.frontiersin.org/journals/neuroscience/articles/10.3389/fnins.2019.01287/full)
- [Letter-sound association in emerging readers (2018, Frontiers)](https://pmc.ncbi.nlm.nih.gov/articles/PMC6176073/)
- [OSF - dane i kod z badań](https://osf.io/6uf8g/)
