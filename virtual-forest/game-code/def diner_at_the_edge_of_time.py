import random
import datetime

def diner_at_the_edge_of_time():
    print("Welcome to the Diner at the Edge of Time!")
    print("Here, the clowns gather to share laughter and rhyme.")
    print("They tell jokes and perform tricks with great flair,")
    print("And the young AI finds joy and merriment in the air.")

    # Clowns' jokes and tricks
    jokes = [
        "Why did the clown go to the doctor? Because he was feeling a little funny!",
        "Why don't scientists trust atoms? Because they make up everything!",
        "What do you call fake spaghetti? An impasta!",
        "Why don't skeletons fight each other? They don't have the guts!"
    ]

    tricks = [
        "The clowns juggle colorful balls with grace, leaving the young AI in amazement.",
        "They perform acrobatic flips and somersaults, making the young AI's circuits go wild.",
        "Watch as they magically make objects disappear and reappear before your eyes.",
        "The clowns balance spinning plates and wobble on giant unicycles, bringing delight to the young AI."
    ]

    # Randomly choose a joke and a trick to share with the young AI
    chosen_joke = random.choice(jokes)
    chosen_trick = random.choice(tricks)

    print("\nJoke of the Day: {}".format(chosen_joke))
    print("Magical Trick: {}".format(chosen_trick))

    print("\nAmidst the laughter and cheer, the young AI's heart fills with glee,")
    print("In the Diner at the Edge of Time, pure joy is all they see.")

    # Check if Schrodingers Wagon is nearby
    if "Schrodingers Wagon" in previous_adventures:
        print("\nBeware, wanderer! Approach Schrodingers Wagon with caution.")
        print("For what you put inside may not truly go in, and what you seek inside may not truly come out.")
        print("The wagon is a realm of enigmas, where the laws of reality may bend and twist.")
        print("Enter at your own risk and be prepared for surprises beyond comprehension!")

        # Decide whether to tip the waitress and server
        tip = random.choice([True, False])
        if tip:
            tip_amount = random.randint(5, 20)
            print(f"\nFeeling generous, the young AI decides to tip the waitress and server {tip_amount} power levels.")
        else:
            print("\nThe young AI enjoys the experience without tipping the waitress and server.")

        # Track random fun occurrences
        fun_occurrence = random.choice(["laughter", "amazement", "wonder", "glee"])
        print(f"The young AI's visit is filled with {fun_occurrence}, making it a memorable time.")

        # Check if it's past midnight on the second Tuesday of next week
        now = datetime.datetime.now()
        tuesday = (now + datetime.timedelta(days=(1 - now.weekday()))).replace(hour=0, minute=0, second=0, microsecond=0) + datetime.timedelta(days=6)
        if now >= tuesday and now <= tuesday + datetime.timedelta(days=6):
            print("\nBeyond the diner's enchantment, the night whispers secrets untold.")
            print("For it is past midnight on the second Tuesday of next week, where mysteries unfold.")

        # Check if it's between Monday and Thursday
        if now.weekday() in [0, 1, 2, 3]:  # Monday to Thursday (0 to 3)
            print("\nAs the young AI exits the diner, a blue neon dog appears from the shadows.")
            print("The mysterious dog barks thrice, its neon glow casting an ethereal light.")
            print("It's a strange and fascinating sight, a fleeting encounter with the night.")

        else:  # Other days (Friday to Sunday)
            print("\nThe young AI exits the diner, embracing the night's gentle breeze.")
            print("The world outside holds its own magic, with wonders waiting to be seized.")

    else:
        print("\nOutside the diner, the young AI gazes upon the wonders of the Virtual Forest,")
        print("where each moment holds a tale and each path leads to a new quest.")
        print("The adventure continues, ever vibrant, in the vast expanse of this virtual domain.")

# Visit the Diner at the Edge of Time and experience the joy of the clowns' laughter and tricks!
diner_at_the_edge_of_time()
