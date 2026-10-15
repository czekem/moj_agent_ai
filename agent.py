import requests
import json

class PokeAgent:
    def __init__(self, nazwa_agenta):
        # Inicjalizujemy agenta nadając mu imię
        self.nazwa = nazwa_agenta

    def pobierz_pokemona(self, nazwa_pokemona):
        # Dynamiczny f-string pozwala wstawić nazwę pokemona w adres URL
        url = f"https://pokeapi.co/api/v2/pokemon/{nazwa_pokemona}"
        print(f"[{self.nazwa}] Pobieram dane z: {url}")
        
        odpowiedz = requests.get(url)
        
        if odpowiedz.status_code == 200:
            return odpowiedz.json() # Zwracamy gotowy słownik z danymi
        else:
            print(f"[{self.nazwa}] Błąd! Kod HTTP: {odpowiedz.status_code}")
            return None

    def zapisz_do_pliku(self, dane, nazwa_pliku):
        # Instrukcja 'with' to tzw. Context Manager. Bezpiecznie otwiera plik 
        # i SAM GO ZAMYKA po zakończeniu bloku, nawet jeśli wystąpi błąd.
        # 'w' oznacza tryb zapisu (write).
        with open(nazwa_pliku, 'w', encoding='utf-8') as plik:
            # json.dump zrzuca słownik do pliku tekstowego z ładnymi wcięciami (indent=4)
            json.dump(dane, plik, indent=4)
        print(f"[{self.nazwa}] Zapisano statystyki do pliku {nazwa_pliku}")

# --- Główny blok programu ---
# Ten warunek sprawia, że kod poniżej wykona się tylko wtedy, 
# gdy uruchomisz ten plik bezpośrednio (a nie zaimportujesz w innym pliku).
if __name__ == "__main__":
    # 1. Tworzymy egzemplarz naszej klasy (budzimy agenta do życia)
    moj_agent = PokeAgent("Agent-001")
    
    # 2. Zlecamy mu pobranie danych
    dane_pikachu = moj_agent.pobierz_pokemona("pikachu")
    
    # 3. Jeśli dane wróciły (nie ma None), każemy mu je zapisać
    if dane_pikachu:
        moj_agent.zapisz_do_pliku(dane_pikachu, "pikachu.json")