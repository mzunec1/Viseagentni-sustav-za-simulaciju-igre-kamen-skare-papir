from spade.behaviour import CyclicBehaviour

def odredi_pobjednika(odabiri):
    potez1, potez2 = odabiri.get("Igrac1"), odabiri.get("Igrac2")
    
    if potez1 == potez2:
        return "Neriješeno!"

    pobjednici = {
        "kamen": ["skare", "vatra"],
        "skare": ["papir", "vodeniBalon"],
        "papir": ["kamen", "vodeniBalon"],
        "vodeniBalon": ["kamen", "vatra"],
        "vatra": ["papir", "skare"],    
    }

    if potez2 in pobjednici[potez1]:
        return "Igrac1 pobjeđuje!"
    else:
        return "Igrac2 pobjeđuje!"


class PonasanjeSudca(CyclicBehaviour):
    def __init__(self):
        super().__init__()
        self.odabiri = {"Igrac1": None, "Igrac2": None}
        self.rezultati = {"Igrac1": 0, "Igrac2": 0}

    async def run(self):
        poruka = await self.receive(timeout=10)  
        if poruka:
            posiljatelj, odabir = poruka.body.split(": ")
            self.odabiri[posiljatelj.strip()] = odabir.strip()
            print(f"Sudac: Primljen potez od {posiljatelj}: {odabir}")

            if all(self.odabiri.values()):
                rezultat = odredi_pobjednika(self.odabiri)
                print(f"Sudac: Rezultat runde -> {rezultat}")

                # Ažuriranje rezultata
                if "Igrac1 pobjeđuje!" in rezultat:
                    self.rezultati["Igrac1"] += 1
                elif "Igrac2 pobjeđuje!" in rezultat:
                    self.rezultati["Igrac2"] += 1

                print(f"Sudac: Trenutni rezultat -> Igrac1: {self.rezultati['Igrac1']} | Igrac2: {self.rezultati['Igrac2']}")

                self.odabiri = {"Igrac1": None, "Igrac2": None}

