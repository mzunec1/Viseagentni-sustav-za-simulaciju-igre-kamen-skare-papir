import random
from spade.agent import Agent
from spade.behaviour import CyclicBehaviour
from spade.message import Message
import asyncio

class Igrac1(Agent):
    class IgrajPotez(CyclicBehaviour):
        async def run(self):
            potezi = ["kamen", "skare", "papir", "vatra", "vodeniBalon"]
            odabir = random.choice(potezi)

            poruka = Message(
                to="agent3@localhost",
                body=f"Igrac1: {odabir}",
                metadata={"performative": "inform"}
            )
            print(f"Igrac1: Moj potez je {odabir}")
            await self.send(poruka)

            await asyncio.sleep(0.5)

    async def setup(self):
        print("Igrac1: Pokrećem se...")
        ponasanje = self.IgrajPotez()
        self.add_behaviour(ponasanje)
