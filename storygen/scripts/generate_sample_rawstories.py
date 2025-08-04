import os
from datetime import datetime

OUTPUT_DIR = "../rawstory"
os.makedirs(OUTPUT_DIR, exist_ok=True)

stories = [
    {
        "descriptor": "colonisation",
        "text": """ZS-Lumen touched down on Elyon IV’s equatorial plateau at 19:20 today. Initial scans confirm resource viability. Colony protocols initiated. Structures deployed: resource scanner, habitat module. Atmospheric stability within tolerances. No contact with local fauna."""
    },
    {
        "descriptor": "fleetbattle",
        "text": """In Gamma Verge, a skirmish erupted between House Talmar and Norg Syndicate patrols. Five Norg vessels and three Talmar frigates were lost in what analysts call a "meaningless exchange of steel." Civilian trader Rensa Vo: “I watched from orbit. The whole thing lasted five minutes. No winners. Just debris.”"""
    },
    {
        "descriptor": "espionage",
        "text": """A Zhen Collective agent was apprehended attempting to extract fusion core schematics from Solace Prime. Norg officials released the following: “We will not tolerate theft masquerading as diplomacy.” The Zhen delegation has denied involvement, calling it “a tragic misunderstanding.”"""
    },
    {
        "descriptor": "tradediplomacy",
        "text": """Nova Freehold and House Talmar signed a five-cycle trade pact today. Ore and tactical drones will exchange hands monthly. Commentator Teva Lun said: “These aren’t just drones. They’re leverage. This is Talmar preparing for something.”"""
    },
    {
        "descriptor": "resourcelog",
        "text": """[Internal Log – Nova Freehold Logistics Division]\n\nAntimatter reserves at Karnis Refinery dropped below critical threshold at 21:10. Backup stores depleted. Expecting full outage within two cycles. Urgent recommendation: reroute synthesis from Braxil Ring or suspend jump operations."""
    },
    {
        "descriptor": "election",
        "text": """Alyra Dorne of House Talmar was elected Core President with 54% of the Assembly vote. Her first words: “We are not rulers of stars. We are their stewards.” Dorne’s victory grants her veto powers over war declarations and control of galactic tariffs."""
    },
    {
        "descriptor": "bombardment",
        "text": """Norg Syndicate ships bombarded Kairon Theta at dawn. Civilian habitats in Zone 3 were flattened. No warning was issued. Field correspondent Lira Mekk barely escaped: “They weren’t aiming at defenses. They were punishing the ground.” Official Norg reports cite “strategic asset denial.”"""
    }
]

now = datetime.utcnow()
for i, story in enumerate(stories):
    timestamp = now.strftime("%Y%m%d_%H%M%S")
    descriptor = story["descriptor"]
    filename = f"{timestamp}_{descriptor}_{i+1:02}.txt"
    path = os.path.join(OUTPUT_DIR, filename)
    with open(path, "w", encoding="utf-8") as f:
        f.write(story["text"])
    print(f"✅ Saved: {filename}")
