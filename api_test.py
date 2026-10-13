import requests

# Wysyłamy zapytanie GET pod wskazany adres URL
url = "https://pokeapi.co/api/v2/pokemon/pikachu"
odpowiedz = requests.get(url)

# Kod 200 oznacza "OK" - serwer odpowiedział poprawnie
if odpowiedz.status_code == 200:
    dane = odpowiedz.json() # Zamieniamy odpowiedź z formatu JSON na pythonowy słownik
    print(f"Pikachu waży: {dane['weight']} jednostek.")
else:
    print(f"Błąd połączenia. Kod błędu: {odpowiedz.status_code}")