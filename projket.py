class mpbe:
    def __init__(self, ora, perc, mp):
        self.ora = ora
        self.perc = perc
        self.mp = mp
    
    def __str__(self):
        return f"Óra:{self.ora}, perc:{self.perc}, másodperc:{self.mp}"
        
f = open("hivas.txt", "rt", encoding="utf-8")