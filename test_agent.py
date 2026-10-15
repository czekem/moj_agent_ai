from agent import PokeAgent

def test_inicjalizacji_agenta():
    # Tworzymy testowego agenta
    testowy_agent = PokeAgent("Tester-007")
    
    # Słowo kluczowe 'assert' (zakładam, że) to podstawa testowania. 
    # Jeśli warunek po prawej stronie jest nieprawdziwy, test z hukiem obleje.
    assert testowy_agent.nazwa == "Tester-007"

def test_pobierania_api_przez_agenta():
    testowy_agent = PokeAgent("Tester-007")
    dane = testowy_agent.pobierz_pokemona("ditto")
    
    # Sprawdzamy, czy agent w ogóle coś zwrócił (czy nie ma błędu 404/500)
    assert dane is not None
    # Sprawdzamy, czy w zwróconym słowniku faktycznie znajduje się klucz "name"
    assert "name" in dane
    # Sprawdzamy, czy API zwróciło poprawnego pokemona
    assert dane["name"] == "ditto"