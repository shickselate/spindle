# characterBuilder.py

import random

# Shared faction list (used in both character and event generation)

# Factions
FACTIONS = [
    "Tyrian Pact", "Zarim Alliance", "House Myrrk", "Solaris Union", "Cult of Mirrors",
    "Virel Enclave", "The Obsidian Fold", "Nomads of Icarus", "Driftborn Syndicate", "The Pale Chorus"
]

# Titles / Occupations
TITLES = [
    "Warlord", "High Priestess", "Admiral", "Scientist", "Diplomat", "Spy", "Explorer",
    "Heir", "Governor", "Archivist", "Engineer", "Fleet Commander", "Mediator",
    "Shadow Operative", "Seer", "Terraformer", "Peace Envoy"
]

# Names
NAMES = [
    "Kael", "Aurea", "Vel", "Thorne", "Nyra", "Rika", "Corven", "Syle", "Jalen", "Vexa",
    "Doran", "Zirra", "Ash", "Lira", "Varek", "Myrr", "Zhale", "Erix", "Talon", "Ilyr",
    "Orren", "Sael", "Tyra", "Brax", "Neyth", "Riven"
]

# Role / Domain (location-flavoured titles)
ROLES = [
    "of the Crimson Star", "from Nexus Prime", "of Quarn's Moon", "of the Forgotten Ring",
    "from the Ion Reach", "of Deep Station Nym", "of the Silent Spire", "from Helix Verge",
    "of the Glass Citadel", "from the Astral Chorus", "of the Last Watch"
]

# Personality Traits
TRAITS = [
    "ambitious", "calculating", "honour-bound", "ruthless", "visionary", "spiritual", "enlightened", "wise", "generous", "kind",
    "secretive", "charismatic", "disciplined", "impulsive", "stoic",
    "devout", "curious", "grief-stricken", "joyful", "loyal", "suspicious",
    "unpredictable", "methodical", "haunted", "unflinching"
]


# Function to generate a character
def generate_character():
    name = f"{random.choice(NAMES)} {random.choice(NAMES)}"
    role = random.choice(ROLES)
    faction = random.choice(FACTIONS)
    title = random.choice(TITLES)
    traits = random.sample(TRAITS, 2)  # Two traits

    return {
        "name": name,
        "role": role,
        "faction": faction,
        "title": title,
        "traits": traits
    }

# Optional: test output
if __name__ == "__main__":
    print(generate_character())
