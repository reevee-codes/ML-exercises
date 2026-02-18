# 🧠 Podstawowe pojęcia ML -- uporządkowana ściąga

## Regresja liniowa

Najprostszy model ML: y = w1*x1 + w2*x2 + w3\*x3 + b. Model uczy się wag
minimalizując błąd.

## Wagi

Określają wpływ cech na wynik. Uczenie = dopasowanie wag.

## Funkcja błędu

error = target - prediction. Model minimalizuje błąd.

## Gradient Descent

Aktualizacja wag: w = w + error \* input \* learning_rate

## Learning Rate

Wielkość kroku uczenia. 0.1 -- za duży, 0.001 -- bezpieczny.

## Epoka

Jedno przejście przez dane treningowe.

## Convergence

Moment gdy błąd przestaje maleć → zatrzymujemy trening.

## Normalizacja danych

Skalowanie danych do zakresu 0--1 stabilizuje uczenie.

## Exploding Gradients

Zbyt duże wagi → overflow → NaN.

## Floating Point Overflow

Limit float ≈ 1.8e308 → po przekroczeniu pojawia się inf i NaN.

## Overtraining

Za dużo epok → brak poprawy i ryzyko niestabilności.

## Early Stopping

Automatyczne zatrzymanie gdy błąd przestaje maleć.

## Pipeline ML

1.  Przygotuj dane
2.  Znormalizuj dane
3.  Trenuj model
4.  Monitoruj błąd
5.  Zatrzymaj trening
6.  Użyj modelu

## Najczęstsze powody NaN

-   za duży learning rate
-   brak normalizacji
-   exploding gradients
-   zbyt długi trening
