import random
from characterBuilder import generate_character, FACTIONS

# Event types and settings
EVENT_TYPES = [
    "battle", "diplomacy", "science", "espionage", "celebration", 
    "election", "exploration", "ceremony", "disaster", "reunion", 
    "prophecy", "migration", "discovery", "contest"
]

LOCATIONS = [
    "Icarus Drift", "Virel System", "Ashen Belt", "Zarim Core", "The Twin Moons of Quarn",
    "Junction Delta", "Cryos Reach", "Deep Station Nym", "The Veiled Expanse",
    "Nexus Prime", "Kepler System", "Drift Core", "Helix Verge", "Ion Reach",
    "Tetra Spire", "Vault of Echoes", "Seraph Array"
]

ENVIRONMENT_TYPES = [
    "ocean world", "asteroid field", "orbital station", "gas giant moon", "crystalline world", 
    "expanse", "comet", "asteroid belt", "plasma field", "wealthy planet", 
    "vegetative planet", "barren planet", "star cluster", "black hole", 
    "living biome", "refugee fleet", "terraforming zone"
]

MAGNITUDE = [
    "minor", "casual", "celebratory", "exciting", "moderate", 
    "major", "critical", "epochal", "historic", "symbolic"
]

INSTABILITY_LEVELS = [
    "booming", "expanding", "thriving", "hopeful", "unified", 
    "suffering", "aggressive", "stable", "tense", "unrest", "fractured", "on brink of revolt"
]

STRATEGIC_IMPORTANCE = [
    "military stronghold", "trade nexus", "research outpost", "ancient ruins", 
    "diplomatic hub", "corridor", "blockade", "city", "megacity", 
    "uncontacted civilisation", "arc ship", "heritage site", "neutral enclave", "refuge zone"
]

COMPLICATIONS = [
    "solar flare", "traitor revealed", "data leak", "supply failure", "psychic interference", 
    "social unrest", "galactic games", "annual festivity", "holiday", 
    "religious holy day", "false signal", "navigation failure", 
    "unexpected guests", "strange transmission", "creature sighting"
]

TRIGGERS = [
    "border violation", "failed negotiation", "ancient signal received", "leadership change", 
    "rival provocation", "galactic games", "prophetic vision", "honour duel", 
    "first contact", "archival discovery", "festival opening", 
    "resource surge", "lost ship returns", "miracle birth", "eclipse event"
]

OUTCOME = {
    "battle": ["victory", "defeat", "stalemate", "retreat", "ceasefire declared"],
    "diplomacy": ["treaty signed", "agreement delayed", "talks collapsed", "new alliance formed"],
    "espionage": ["data stolen", "spy captured", "operation aborted", "false lead followed", "blackmail successful"],
    "exploration": ["new world charted", "anomaly encountered", "team lost", "stable wormhole found"],
    "ceremony": ["alliance sealed", "heir crowned", "ritual disrupted", "blessing received"],
    "disaster": ["evacuation ordered", "colony lost", "containment successful", "miraculous survival"],
    "science": ["breakthrough achieved", "experiment failed", "tech rediscovered", "paradox induced"],
    "celebration": ["peace reaffirmed", "rival factions reunited", "spirits lifted", "scandal erupts"],
    "election": ["leader chosen", "vote disrupted", "unexpected result", "mandate secured"],
    "prophecy": ["foretold event begins", "omens misread", "symbol interpreted", "warning delivered"],
    "migration": ["settlement completed", "ships rerouted", "population dispersed", "host refused"]
}


def generate_event():
    event_type = random.choice(EVENT_TYPES)
    location = random.choice(LOCATIONS)
    environment = random.choice(ENVIRONMENT_TYPES)
    strategic_value = random.choice(STRATEGIC_IMPORTANCE)
    instability = random.choice(INSTABILITY_LEVELS)
    magnitude = random.choice(MAGNITUDE)
    outcome = random.choice(OUTCOME.get(event_type, ["event unresolved"]))
    actor = generate_character()
    opposing_faction = random.choice([f for f in FACTIONS if f != actor["faction"]])
    trigger = random.choice(TRIGGERS)
    complication = random.choice(COMPLICATIONS)

    return {
        "type": event_type,
        "location": location,
        "environment": environment,
        "strategic_importance": strategic_value,
        "instability": instability,
        "magnitude": magnitude,
        "timestamp": "232.94.14.08",
        "main_actor": actor,
        "involved_factions": [actor["faction"], opposing_faction],
        "trigger": trigger,
        "complication": complication,
        "outcome": outcome
    }

if __name__ == "__main__":
    from pprint import pprint
    pprint(generate_event())
