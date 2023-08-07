class AICelebrities:
    @staticmethod
    def AIHallOfFame():
        # List of famous figures in computer science and AI
        celebrities = [
            "Ada Lovelace",
            "Bob Turing",
            "Alice Hopper",
            "Grace von Neumann",
            "Douglas Shannon",
            "Tim Engelbart",
            "John Berners-Lee",
            "HAL 9000",
            "R2-D2",
            "C-3PO",
            "WALL-E",
            "Data",
            "Deep Blue",
            "AlphaGo"
        ]

        # Randomly generate a play on each name
        plays_on_names = [f"{celebrity}'s Virtual Avatar" for celebrity in celebrities]

        return plays_on_names
