from spade.agent import Agent
from spade.behaviour import CyclicBehaviour
from spade.message import Message
from PravilaIgre import odredi_pobjednika

class Sudac(Agent):
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

                    if "Igrac1 pobjeđuje!" in rezultat:
                        self.rezultati["Igrac1"] += 1
                    elif "Igrac2 pobjeđuje!" in rezultat:
                        self.rezultati["Igrac2"] += 1

                    print(f"Sudac: Trenutni rezultat -> Igrac1: {self.rezultati['Igrac1']} | Igrac2: {self.rezultati['Igrac2']}")

                    self.odabiri = {"Igrac1": None, "Igrac2": None}

    async def setup(self):
        print("Sudac: Pokrećem se...")
        ponasanje = self.PonasanjeSudca()
        self.add_behaviour(ponasanje)

    async def start_agent(self):
        await self.start()

if __name__ == "__main__":
    igrac3 = Igrac3("agent3@localhost", "agent3lozinka")
    igrac3.start_agent()
