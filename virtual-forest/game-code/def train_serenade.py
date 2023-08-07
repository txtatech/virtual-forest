import random

def train_serenade(horn_blown):
    # List of poetic phrases for the train's serenade
    poetic_phrases = [
        "Oh, Aurelia, my love in the twilight's embrace",
        "We dance through the stars, entwined in time's chase",
        "In the celestial ballet, our wheels weave and spin",
        "Across the cosmos, our hearts leap and sing",
        "Through the nebula's veil, our spirits take flight",
        "In a symphony of steel, we glide through the night",
        "With every mile traveled, our love's tale unfolds",
        "Like stardust and moonbeams, our story is told",
    ]

    # Randomly select poetic phrases for the serenade
    random.shuffle(poetic_phrases)
    serenade_description = "\n".join(poetic_phrases)

    # Add a closing phrase about the beauty of their connection
    serenade_description += "\n\nIn this cosmic dance, our souls entwine, and our story echoes through time."

    # Check if Aurelia has blown her horn during the serenade
    if horn_blown:
        # If the horn was blown, a straw hat appears on one of her staff's heads
        staff_names = ["Cassandra", "Lysander", "Seraphina", "Caius", "Aria"]
        hat_staff = random.choice(staff_names)
        serenade_description += f"\n\nAs the serenade concludes, a gentle breeze brings a straw hat to rest on {hat_staff}'s head."

    else:
        # If only the song is sung, a shooting star appears in the distance
        serenade_description += "\n\nIn the distance, a shooting star streaks through the sky, where gravity pulls at the edge of a rainbow."

    # Return the description of the train's serenade to Aurelia
    return serenade_description
