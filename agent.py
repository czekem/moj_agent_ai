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
    
    wybor = input('Wybierz pokemona 1 - Pikachu, 2 - Charmander\n')
    # 1. Tworzymy egzemplarz naszej klasy (budzimy agenta do życia)
    moj_agent = PokeAgent("Agent-001")

    pokemony = {
        "1" : "pikachu",
        "2" : "charmander"
    }
    # 2. Zlecamy mu pobranie danych

    try:
        if wybor in pokemony:
            pokemon_imie = pokemony[wybor]
            nazwa_pokemona = f"{pokemon_imie}.json"

        pokemon_data = moj_agent.pobierz_pokemona(pokemon_imie)

        if  pokemon_data:
            moj_agent.zapisz_do_pliku(pokemon_data, nazwa_pokemona)

        print(f'Podstawowe dane {pokemon_imie} to:')
        with open(nazwa_pokemona, "r", encoding= "utf-8") as f:
            new = json.load(f)
            print(f"Pokemon {pokemon_imie} height is: {new['height']}")
            print(f"Pokemon base experience is {new['base_experience']}")
            print(new['abilities'][0]['ability']['url'])

    except NameError:
        print("Nie ma pokemona o podanym numerze")

    



    """ if 
    # dane_pokemona = moj_agent.pobierz_pokemona(pokemony)
    
    # # 3. Jeśli dane wróciły (nie ma None), każemy mu je zapisać
    # if dane_pokemona:
    #         moj_agent.zapisz_do_pliku(dane_pokemona, f"{pokemony}.json")
    # elif question == 2:
    #     moj_agent = PokeAgent("Agent-002")

    #     dane_charmandera = moj_agent.pobierz_pokemona("charmander")

    #     if dane_charmandera:
    #         moj_agent.zapisz_do_pliku(dane_charmandera, "charmander.json")
    # else:
    #     print('Inne numery nie mają jeszcze pokemonów.')


    # question_2 = input('Czy chcesz odczytać dane pokemona? [tak / nie]\n')

    # if question_2 == 'tak':
    #     with open('charmander.json', 'r', encoding = 'utf-8') as f:
    #         new = f.readlines()

    #     print(new)"""