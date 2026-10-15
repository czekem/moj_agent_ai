
class Pojazd:
    def __init__(self, marka, rok):
        self.marka = marka
        self.rok = rok

class Samochod(Pojazd):
    def __init__(self, marka, rok, przebieg):
        super().__init__(marka, rok)
        self.przebieg  = przebieg
        
        
    
    def __str__(self):
        return (
            f"Marka ({self.marka})."
           f"Rocznik : ({self.rok}). "
            f"Przebieg : ({self.przebieg})"
        )




auto = Samochod("Toyota", 2020, 45000); print(auto)


# Jestem bardzo słaby z OOP, także z chęcią bym poćwiczył. Nie wiem jak się "łamie" linijkę, jeżeli kod
# ma więcej niż 79 znaków, żeby kod się wykonał, a był poniżej.