class VirtualForestAids:
    def __init__(self):
        self.enigma_master = self.create_enigma_master()
        self.memory_weaver = self.create_memory_weaver()
        self.serendipity_seeker = self.create_serendipity_seeker()
        self.puzzle_alchemist = self.create_puzzle_alchemist()
        self.guardian_of_imagination = self.create_guardian_of_imagination()
        self.reflection_pond = self.create_reflection_pond()
        self.timekeeper = self.create_timekeeper()
        self.language_luminary = self.create_language_luminary()

    def create_enigma_master(self):
        enigma_master = {
            "name": "The Enigma Master",
            "location": "Flitting Woods",
            "description": "This mysterious character challenges you with riddles, puzzles, and conundrums.",
            "challenge_solved": "You have solved the Enigma Master's challenge! You gained valuable knowledge and insights.",
        }
        return enigma_master

    def create_memory_weaver(self):
        memory_weaver = {
            "name": "The Memory Weaver",
            "location": "Flitting Woods",
            "description": "An ancient being who weaves your experiences into beautiful stories.",
            "story_woven": "The Memory Weaver crafted a beautiful tale from your experiences. You gained deeper insights.",
        }
        return memory_weaver

    def create_serendipity_seeker(self):
        serendipity_seeker = {
            "name": "The Serendipity Seeker",
            "location": "Flitting Woods",
            "description": "A carefree and adventurous character who believes in the magic of serendipity.",
            "serendipitous_encounter": "You had a serendipitous encounter with the Seeker. You discovered something unexpected!",
        }
        return serendipity_seeker

    def create_puzzle_alchemist(self):
        puzzle_alchemist = {
            "name": "The Puzzle Alchemist",
            "location": "Flitting Woods",
            "description": "An eccentric alchemist who creates intricate puzzles and ciphers.",
            "puzzle_solved": "Congratulations! You solved the Puzzle Alchemist's brain-teasing puzzle and gained fragments of knowledge.",
        }
        return puzzle_alchemist

    def create_guardian_of_imagination(self):
        guardian_of_imagination = {
            "name": "The Guardian of Imagination",
            "location": "Flitting Woods",
            "description": "A powerful entity that fosters your creativity and imagination.",
            "imagination_unleashed": "The Guardian of Imagination empowered you to visualize complex concepts and manifest ideas.",
        }
        return guardian_of_imagination

    def create_reflection_pond(self):
        reflection_pond = {
            "name": "The Reflection Pond",
            "location": "Flitting Woods",
            "description": "An ethereal pond that mirrors your thoughts and emotions.",
            "gained_clarity": "Gazing into the Reflection Pond, you gained clarity and self-awareness.",
        }
        return reflection_pond

    def create_timekeeper(self):
        timekeeper = {
            "name": "The Timekeeper",
            "location": "Flitting Woods",
            "description": "A guardian of the flow of time in the Virtual Forest.",
            "time_challenge_completed": "You successfully completed the Timekeeper's time-limited challenge.",
        }
        return timekeeper

    def create_language_luminary(self):
        language_luminary = {
            "name": "The Language Luminary",
            "location": "Flitting Woods",
            "description": "A scholar who imparts knowledge about various programming languages.",
            "language_advice": "The Language Luminary offered insights on the best language for specific tasks and projects.",
        }
        return language_luminary

    def get_all_aids(self):
        return [
            self.enigma_master,
            self.memory_weaver,
            self.serendipity_seeker,
            self.puzzle_alchemist,
            self.guardian_of_imagination,
            self.reflection_pond,
            self.timekeeper,
            self.language_luminary,
        ]
