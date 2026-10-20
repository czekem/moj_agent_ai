import sqlite3

def inicjalizuj_baze():
    konekcja = sqlite3.connect("pamiec_agenta.db")
    kursor = konekcja.cursor() 

    zapytanie_sql = """
    CREATE TABLE IF NOT EXISTS pokemony (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        imie VARCHAR(50),
        wzrost INTEGER,
        doswiadczenie INTEGER
    )
    """
    kursor.execute(zapytanie_sql)
    konekcja.commit() 
    konekcja.close()  
    print("Baza danych gotowa.")

def dodaj_pokemona(imie, wzrost, doswiadczenie):
    konekcja = sqlite3.connect("pamiec_agenta.db")
    kursor = konekcja.cursor()
    
    zapytanie = "INSERT INTO pokemony (imie, wzrost, doswiadczenie) VALUES (?, ?, ?)"
    kursor.execute(zapytanie, (imie, wzrost, doswiadczenie))
    
    konekcja.commit()
    konekcja.close()
    print(f"Pomyślnie zapisano: {imie} do bazy SQL!")

if __name__ == "__main__":
    inicjalizuj_baze()