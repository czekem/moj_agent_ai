import sqlite3
import pandas as pd

class AnalizatorDanych:
    def __init__(self, nazwa_bazy="pamiec_agenta.db"):
        self.nazwa_bazy = nazwa_bazy

    def analizuj_pokemony(self):
        # 1. Nawiązujemy tymczasowe połączenie z naszą bazą SQLite3
        konekcja = sqlite3.connect(self.nazwa_bazy)

        # 2. Używamy wbudowanej metody biblioteki Pandas, by automatycznie pobrać wynik
        # zapytania SQL i od razu ułożyć go w tabelę (zwaną w Pandas "DataFrame").
        df = pd.read_sql_query("SELECT * FROM pokemony", konekcja)
        konekcja.close()

        # Sprawdzamy, czy w ogóle mamy na czym pracować.
        if df.empty:
            print("Baza danych jest pusta. Nie mam czego analizować.")
            return

        print("=== RAPORT ANALITYCZNY AGENTA ===")
        print(f"Liczba wpisów w bazie: {len(df)}")
        
        # 3. Pandas potrafi błyskawicznie dokonywać operacji matematycznych na kolumnach.
        # Obliczmy średnie doświadczenie zebranych w bazie stworków.
        srednie_xp = df['doswiadczenie'].mean()
        print(f"Średnie doświadczenie: {srednie_xp:.2f}")

        # 4. Sprawdzimy, który pokemon figurujący w bazie jest najwyższy.
        # Najpierw znajdujemy wiersz z największą wartością 'wzrost', 
        # a następnie wyciągamy odpowiadające mu imię.
        najwyzszy_idx = df['wzrost'].idxmax() 
        najwyzszy_imie = df.loc[najwyzszy_idx, 'imie']
        print(f"Najwyższy zaobserwowany: {najwyzszy_imie}")
        print("=================================")

if __name__ == "__main__":
    analizator = AnalizatorDanych()
    analizator.analizuj_pokemony()