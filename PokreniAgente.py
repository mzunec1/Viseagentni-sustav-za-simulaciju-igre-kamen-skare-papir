import spade
import asyncio
from Agent1 import Igrac1
from Agent2 import Igrac2
from Agent3 import Sudac

async def glavna_funkcija():
    sudac = Sudac("agent3@localhost", "agent3lozinka")
    print("Pokrećem Igrac3 (sudac)...")
    sudac.start()  

    await asyncio.sleep(1)  

    igrac1 = Igrac1("agent1@localhost", "agent1lozinka")
    igrac2 = Igrac2("agent2@localhost", "agent2lozinka")
    
    igrac1.start()  
    igrac2.start()  

    await asyncio.sleep(5)  

    igrac1.stop()
    igrac2.stop()
    sudac.stop()

if __name__ == "__main__":
    asyncio.run(glavna_funkcija())
