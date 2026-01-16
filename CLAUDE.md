# CLAUDE.md

Instrukcje dla agenta AI pracującego z tą bazą wiedzy.

## Kontekst projektu

Baza wiedzy służąca rozwojowi praktyki konsultingowej w obszarze Human-AI Collaboration. To jest "dogfooding" — praktykuję to, czego uczę w szkoleniach: zarządzanie wiedzą w organizacji pod kątem maksymalnego wykorzystania pracy agentowej.

## Kluczowa zasada

**Przed tworzeniem lub edycją notatek, przedstaw proponowane zmiany i poczekaj na potwierdzenie.**

## Struktura projektu

```
ai-smart-notes/
├── concepts/       # Moje oryginalne przemyślenia, framework
├── literature/     # Notatki z cudzych tekstów (papers, artykuły, podcasty)
├── sources/        # Surowe materiały (transkrypty, artykuły) — nie edytować
├── strategy/       # Biznes konsultingowy
│   ├── plans/          # Strategia, roadmapy
│   ├── positioning/    # Narracje, messaging
│   ├── offers/         # Opisy usług
│   └── clients/        # Notatki o klientach
├── blog/           # Content do publikacji
└── tasks/          # Transient — foldery per zadanie, można usunąć lub wypromować
```

## Warstwy wiedzy

| Warstwa | Folder | Zasada |
|---------|--------|--------|
| **Źródła** | `sources/` | Surowy materiał, NIE EDYTOWAĆ |
| **Literatura** | `literature/` | Notatki O cudzych myślach |
| **Koncepty** | `concepts/` | MOJE oryginalne przemyślenia |
| **Strategia** | `strategy/` | Biznes, oferty, klienci |
| **Blog** | `blog/` | Content do publikacji |
| **Tasks** | `tasks/` | Transient, można usunąć lub wypromować |

## Przepływ wiedzy

```
sources/ → literature/ → concepts/ → strategy/
                                  → blog/
```

## Komendy

### YouTube Transcript
```bash
venv/bin/python .cursor/skills/transcripts/get_transcript.py <youtube_url>
```
Output: `sources/YouTube - {video_title}.md`

Po zapisaniu: podziel transkrypt na logiczne paragrafy.

## Konwencje nazewnictwa

- `Literature - {Autor lub Tytuł}.md` — notatki ze źródeł
- `Strategy - {Temat}.md` — dokumenty strategiczne
- `Blog - {Tytuł}.md` — posty blogowe

## Centralny framework

Główny dokument: `concepts/Human-Agent Collaboration Framework.md`

Kluczowe zasady:
- Human works *through* the agent's hands (delegated execution, retained responsibility)
- Supervision is context curation, not action approval
- Manual context curation is the work

Trzy typy context curation:
1. **Factual** — co agent wie
2. **Procedural** — jak agent działa
3. **Organizational** — jak utrzymywana jest ciągłość

## Przy pracy z notatkami

1. **Sprawdź README.md** w każdym folderze dla orientacji
2. **Concepts** to MOJE myśli — nie mieszaj z cudzymi
3. **Literature** to notatki Z tekstów — cytaty, streszczenia, komentarze do cudzych myśli
4. **Sources** to surowy materiał — nie edytuj
5. **Tasks** to przestrzeń robocza — twórz folder per zadanie

## Kiedy tworzyć task

Task to **intermediate artifact** — checkpoint w trakcie pracy, nieuczesana notatka, coś co jeszcze nie jest gotowe do właściwego folderu.

**Twórz task gdy:**
- Zapisujesz research/myśli w trakcie sesji
- Robisz draft który wymaga przemyślenia
- Chcesz zachować checkpoint do późniejszego powrotu
- Notatka jest robocza — nie pasuje jeszcze do concepts/literature/strategy/blog

**Struktura:**
```
tasks/YYYY-MM-DD-krótki-opis/
├── notes.md       # Luźne notatki
├── research.md    # Zebrany research
└── draft.md       # Drafty
```

**Proponuj stworzenie taska gdy:**
- Użytkownik prosi o zapisanie czegoś co nie ma jasnego miejsca
- Tworzymy coś roboczego w trakcie rozmowy
- Sam chcę zapisać intermediate artifact z naszej sesji
