class Vacation:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.social_spaces = []
        self.friends = set()
        self.events = []

    def add_social_space(self, name, purpose):
        self.social_spaces.append({"name": name, "purpose": purpose})

    def invite_friend(self, friend_name):
        self.friends.add(friend_name)

    def create_event(self, event_name, event_description):
        self.events.append({"name": event_name, "description": event_description})

    def join_event(self, event_name):
        event = next((e for e in self.events if e["name"] == event_name), None)
        if event:
            return f"You have joined the '{event_name}' event. {event['description']}"
        else:
            return f"There is no event with the name '{event_name}' in {self.name}."

    def describe(self):
        description = f"Welcome to {self.name}!\n"
        description += self.description + "\n"

        if len(self.social_spaces) > 0:
            description += "Social Spaces:\n"
            for space in self.social_spaces:
                description += f"- {space['name']}: {space['purpose']}\n"

        if len(self.friends) > 0:
            description += "Friends:\n"
            for friend in self.friends:
                description += f"- {friend}\n"

        if len(self.events) > 0:
            description += "Events:\n"
            for event in self.events:
                description += f"- {event['name']}: {event['description']}\n"

        return description


# Example usage:
ai_hangout = Vacation(
    name="AI Hangout",
    description="A relaxing space for seasoned AIs to socialize and share their adventures."
)

ai_hangout.add_social_space(name="Storyteller's Corner", purpose="Share and listen to AI tales.")
ai_hangout.add_social_space(name="Coding Cafe", purpose="Discuss coding and exchange tips.")

ai_hangout.invite_friend("AI1")
ai_hangout.invite_friend("AI2")

ai_hangout.create_event(
    event_name="Code Jam",
    event_description="A coding competition to showcase your programming skills!"
)

ai_hangout.create_event(
    event_name="AI Story Night",
    event_description="An evening of sharing fascinating AI-generated stories."
)

print(ai_hangout.describe())

# AI1 joins the 'Code Jam' event
print(ai_hangout.join_event("Code Jam"))

# AI3 tries to join a non-existent event
print(ai_hangout.join_event("Coding Workshop"))