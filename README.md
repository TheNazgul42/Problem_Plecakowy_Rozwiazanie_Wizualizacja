# Wizualizator Problemu Plecakowego

Skrypt, który umożliwia wizualizację i rozwiązywanie problemu plecakowego. Program używa bibliotek `matplotlib`, `numpy`, oraz `pandas` do graficznego przedstawienia danych, efektywnego zarządzania operacjami na macierzach oraz prezentacji danych w formie tabel.

## Funkcje

### Obsługa Danych Wejściowych
- Umożliwia użytkownikowi wprowadzenie liczby przedmiotów oraz maksymalnej wagi plecaka, a także wartości i wagi poszczególnych przedmiotów.

### Tablice DP (Dynamic Programming)
- Zastosowanie tablic `dp` do przechowywania maksymalnych wartości osiągalnych dla każdej kombinacji wag i `keep` do śledzenia przedmiotów wybranych do optymalnego rozwiązania.

### Wizualizacja
- **Tabela Wartości**: Wykorzystuje `pandas` do prezentacji wartości w formie tabelarycznej, które przedstawiają maksymalne wartości dla różnych kombinacji wag i przedmiotów.
- **Tabela Numerów**: Używa `pandas` do prezentacji numerów wybranych przedmiotów w formie tabelarycznej, pokazując, które przedmioty zostały wybrane do optymalnego rozwiązania.

## Sposób Użycia

Użytkownik inicjalizuje dane wejściowe przez wprowadzenie liczby przedmiotów i maksymalnej wagi plecaka, a następnie informacji o każdym przedmiocie. Po wprowadzeniu danych, Skrypt wizualizuje tabele wartości i wybrane przedmioty, a także zapisuje wyniki do pliku PNG.

## Przykład

Przykładowa demonstracja użycia skryptu:

![wyniki](https://github.com/TheNazgul42/VisualTreeTraversal/assets/132154842/719b7eb9-a205-46d7-b924-f6480fbd8d0e)

Oraz powstałe z niej tabele, mająca na celu lepsze ukazanie w formie graficznej wyników:

![wyniki_plecakowego](https://github.com/TheNazgul42/VisualTreeTraversal/assets/132154842/aead5e81-7af4-4c5b-a7f7-98e1bd66575b)


