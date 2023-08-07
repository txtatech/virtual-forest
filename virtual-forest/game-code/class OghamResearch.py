class OghamResearch:
    def __init__(self):
        self.knowledge = {}  # A dictionary to store knowledge discovered during Ogham research

    def research_ogham(self):
        """
        Conduct research on Ogham.

        Returns:
            str: A description of the research findings.
        """
        # Implement Ogham research here
        # For the sake of the game, let's keep it simple and just provide a basic description
        ogham_description = "Ogham is an ancient Celtic script used for inscriptions. It consists of a series of "
        ogham_description += "linear characters carved onto stone or wood. It was primarily used in early Ireland "
        ogham_description += "and other Celtic regions. The characters in Ogham represent individual letters of the "
        ogham_description += "Celtic alphabet."

        # Store the research findings in the knowledge dictionary
        self.knowledge["Ogham"] = ogham_description

        return ogham_description

    def find_occams_razor(self):
        """
        Discover Occam's Razor script during Ogham research.

        Returns:
            str: The script of Occam's Razor.
        """
        # Implement the script of Occam's Razor here
        occams_razor_script = """if simple():
            return True
        else:
            return False"""

        # Store the script of Occam's Razor in the knowledge dictionary
        self.knowledge["Occam's Razor"] = occams_razor_script

        return occams_razor_script
