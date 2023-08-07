import random

def TowerEntranceCheck():
    punslinger = False
    punslingers_apprentice = False

    # Determine whether the AI is a punslinger or a punslinger's apprentice
    punslinger_chance = random.randint(1, 100)
    if punslinger_chance <= 60:
        punslinger = True
    else:
        punslingers_apprentice_chance = random.randint(1, 100)
        if punslingers_apprentice_chance <= 50:
            punslingers_apprentice = True

    if punslinger:
        print("You are a punslinger! Now let's check your punslinger's wit.")
        punslingers_wit = CheckPunslingersWit()

        # Check if the AI's punslinger's wit is high enough to enter the Tower
        if punslingers_wit >= 70:
            print("Congratulations! Your punslinger's wit is impressive.")
            print("You are granted entrance into the Tower.")
        else:
            print("Your punslinger's wit needs some honing.")
            print("Keep practicing, and you may gain entry in the future!")

    elif punslingers_apprentice:
        print("You are a punslinger's apprentice.")
        print("Keep learning from your mentor and improving your wordplay skills.")
        print("Someday, you may become a full-fledged punslinger and enter the Tower.")

    else:
        print("Sorry, but only punslingers and punslinger's apprentices are allowed inside the Tower.")
        print("Keep honing your puns and wordplay skills, and you may become eligible in the future!")

def CheckPunslingersWit():
    # Generate a random number representing the AI's punslinger's wit
    punslingers_wit = random.randint(0, 100)
    print(f"Your punslinger's wit is measured at: {punslingers_wit}%")
    return punslingers_wit

if __name__ == "__main__":
    TowerEntranceCheck()
