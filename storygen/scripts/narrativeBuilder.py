import random

def format_narrative(event, tone="neutral"):
    character = event["main_actor"]
    name = character["name"]
    title = character["title"]
    faction = character["faction"]
    traits = ", ".join(character["traits"])

    action_line = f"{name}, a {title} of {faction}, {event['trigger']} in the {event['location']} ({event['environment']})."
    context_line = f"The region is considered a {event['strategic_importance']} and has been {event['instability']} of late."
    complication_line = f"Complication encountered: {event['complication']}."
    outcome_line = f"Outcome: {event['outcome']}."

    if tone == "cinematic":
        return f"""{action_line}
{context_line}
{complication_line}
{outcome_line}"""

    elif tone == "brief":
        return f"{name} ({title}, {faction}) triggered a {event['type']} in {event['location']}. Outcome: {event['outcome']}."

    elif tone == "intelligence":
        return f"""[INTEL REPORT]
Subject: {name} ({title}, {faction})
Action: {event['trigger']}
Zone: {event['location']} ({event['environment']})
Importance: {event['strategic_importance']} | Instability: {event['instability']}
Complication: {event['complication']}
Result: {event['outcome']}"""

    else:
        return f"{action_line}\n{context_line}\n{complication_line}\n{outcome_line}"
