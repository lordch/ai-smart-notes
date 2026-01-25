# Third-Party Library Debugging Agent

## Domena
Development / DevOps / Technical Troubleshooting

## Problem klienta
- Bug w third-party library — dokumentacja nie pomaga
- Stack Overflow answers outdated lub dla innej wersji
- Nie wiadomo co się dzieje "pod maską"
- Czytanie source code biblioteki jest czasochłonne
- "Działa na moim komputerze" — różnice między wersjami

## Kluczowy insight

> Claude Code ma dostęp do **każdego pip/npm package** który masz zainstalowany — może czytać actual source code tej wersji, którą używasz.

## Workflow agentowy

1. Opisanie problemu agentowi (co nie działa, jaki error)
2. Agent lokalizuje zainstalowaną bibliotekę:
   - `pip show library_name` → location
   - Czyta source code z installed package
3. Agent analizuje relevant code:
   - Znajduje funkcję która rzuca błąd
   - Śledzi flow danych
   - Porównuje z dokumentacją
4. Agent identyfikuje root cause:
   - Brakująca konfiguracja
   - Edge case nie obsłużony
   - Różnica między wersjami
5. Agent proponuje fix lub workaround

## Przykładowy prompt
```
I'm getting this error when using Modal with Streamlit:
[paste error traceback]

The client IP address is not being forwarded through WebSocket connections.

Debug this by:
1. Find where Modal is installed (pip show modal)
2. Read the relevant source code for request handling
3. Compare HTTP vs WebSocket request handling
4. Identify why IP forwarding works for HTTP but not WebSocket
5. Suggest a fix or workaround
```

## Real Example (Matt Stockton)

**Problem**: Modal library nie przekazuje client IP przez WebSocket.

**Analiza agenta**:
- Znalazł `_proxy_http_request` function — wywołuje `_add_forwarded_for_header`
- Znalazł `_proxy_websocket_request` function — NIE wywołuje tego samego
- Zidentyfikował exact line numbers gdzie implementacje się różnią

**Outcome**: Precyzyjna informacja do bug reportu / własnego patcha.

## Before / After
| Manual | Z agentem |
|--------|-----------|
| Googlowanie (często outdated) | Analiza actual source code |
| Guessing wersji w answers | Dokładnie ta wersja co masz |
| Godziny czytania source | Minuty na analizę |
| "Może to..." trial and error | Root cause identification |
| Frustracja | Systematic debugging |

## ROI / Metryki
- Debugging time: godziny → minuty
- Accuracy: analiza exact version vs generic answers
- Learning: zrozumienie jak biblioteka działa
- Bug reports: precyzyjne, z line numbers

## Wymagania wdrożeniowe
- Narzędzia: Claude Code z dostępem do file system
- Dane: zainstalowane packages (pip/npm/etc.)
- Complexity: **Medium** (wymaga technical knowledge do interpretacji)
- Nie wymaga specjalnego setupu — packages już są zainstalowane

## Warianty / Rozszerzenia
- Automated compatibility check: "Czy ta wersja ma znane issues?"
- Dependency analysis: "Które packages są outdated?"
- Security audit: "Czy są znane vulnerabilities?"
- Migration guide: "Co się zmieniło między v1 i v2?"

## Failure Modes (uwaga!)
- Minified/compiled code → agent nie może czytać
- Closed source libraries → nie działa
- Complex codebases → może się zgubić w flow
- Misinterpretation → zawsze verify przed wdrożeniem fix

## Kiedy używać
- Error message jest niejasny
- Dokumentacja nie odpowiada na pytanie
- Stack Overflow nie ma dobrej odpowiedzi
- Podejrzewasz bug w bibliotece
- Chcesz zrozumieć "dlaczego tak działa"

## Źródło
[Matt Stockton - Using Claude Code to Debug Code You Didn't Write](https://mattstockton.com/2026/01/01/using-claude-code-to-debug-third-party-library-code.html)
[Matt Stockton - Claude Code Posts](../literature/Matt%20Stockton%20-%20Claude%20Code%20Posts.md)
