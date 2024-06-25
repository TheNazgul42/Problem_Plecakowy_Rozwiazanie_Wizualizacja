import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib

def is_interactive_backend():
    interactive_backends = matplotlib.backends.backend_registry.list_builtin(matplotlib.backends.BackendFilter.INTERACTIVE)
    return matplotlib.get_backend() in interactive_backends

def problem_plecakowy():
    while True:
        # Dane wejściowe od użytkownika
        n = int(input("Podaj liczbę przedmiotów: "))
        max_waga = int(input("Podaj maksymalną wagę plecaka: "))

        przedmioty = []
        for i in range(n):
            wartosc = int(input(f"Podaj wartość dla przedmiotu {i + 1}: "))
            waga = int(input(f"Podaj wagę dla przedmiotu {i + 1}: "))
            przedmioty.append((wartosc, waga))

        # Inicjalizacja tablic DP
        dp = np.zeros((n + 1, max_waga + 1), dtype=int)
        keep = np.zeros((n + 1, max_waga + 1), dtype=int)

        # Wypełnianie tablic DP
        for i in range(1, n + 1):
            wartosc, waga = przedmioty[i - 1]
            for w in range(max_waga + 1):
                dp[i][w] = dp[i - 1][w]
                keep[i][w] = keep[i - 1][w]
                if w >= waga:
                    if dp[i][w] < dp[i][w - waga] + wartosc:
                        dp[i][w] = dp[i][w - waga] + wartosc
                        keep[i][w] = i

        # Znajdowanie przedmiotów do zachowania
        w = max_waga
        przedmioty_do_zachowania = []
        for i in range(n, 0, -1):
            while w >= przedmioty[i - 1][1] and dp[i][w] == dp[i][w - przedmioty[i - 1][1]] + przedmioty[i - 1][0]:
                przedmioty_do_zachowania.append(i)
                w -= przedmioty[i - 1][1]

        # Wyświetlanie wyników
        df_wartosci = pd.DataFrame(dp[1:, 1:], index=range(1, n + 1), columns=range(1, max_waga + 1))
        df_numery = pd.DataFrame(keep[1:, 1:], index=range(1, n + 1), columns=range(1, max_waga + 1))

        print("Tabela Wartości:")
        print(df_wartosci)

        print("Tabela Numerów:")
        print(df_numery)

        print("Maksymalna wartość =", dp[n][max_waga])
        print("Przedmioty do zachowania:", przedmioty_do_zachowania)

        # Rysowanie tabel
        fig, axes = plt.subplots(2, 1, figsize=(15, 10))

        # Plot Tabela Wartości
        cax0 = axes[0].matshow(df_wartosci, cmap='cool', aspect='auto')
        fig.colorbar(cax0, ax=axes[0])
        axes[0].set_title('Tabela Wartości')
        axes[0].set_xlabel('Waga')
        axes[0].set_ylabel('Przedmioty')
        axes[0].set_xticks(np.arange(len(df_wartosci.columns)))
        axes[0].set_xticklabels(df_wartosci.columns)
        axes[0].set_yticks(np.arange(len(df_wartosci.index)))
        axes[0].set_yticklabels(df_wartosci.index)

        for (i, j), val in np.ndenumerate(df_wartosci.values):
            axes[0].text(j, i, f'{val}', ha='center', va='center', color='black')

        # Plot Tabela Numerów
        cax1 = axes[1].matshow(df_numery, cmap='cool', aspect='auto')
        fig.colorbar(cax1, ax=axes[1])
        axes[1].set_title('Tabela Numerów')
        axes[1].set_xlabel('Waga')
        axes[1].set_ylabel('Przedmioty')
        axes[1].set_xticks(np.arange(len(df_numery.columns)))
        axes[1].set_xticklabels(df_numery.columns)
        axes[1].set_yticks(np.arange(len(df_numery.index)))
        axes[1].set_yticklabels(df_numery.index)

        for (i, j), val in np.ndenumerate(df_numery.values):
            axes[1].text(j, i, f'{val}', ha='center', va='center', color='black')

        plt.tight_layout()
        plt.savefig("wyniki_plecakowego.png")

        if is_interactive_backend():
            plt.show()
        else:
            print("Interaktywne wyświetlanie nie jest dostępne. Wykres został zapisany jako 'wyniki_plecakowego.png'.")

        # Pytanie, czy kontynuować
        kontynuacja = input("Czy chcesz kontynuować? (Y/N): ").strip().upper()
        if kontynuacja == 'N':
            break

problem_plecakowy()
