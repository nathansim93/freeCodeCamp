import random

class CYOAGame:
    def __init__(self):
        self.current_hole = 1
        self.score = 0
        self.clubs_yardage = {
            "3 wood": random.randint(180, 220),
            "4 iron": random.randint(170, 200),
            "5 iron": random.randint(160, 190),
            "6 iron": random.randint(150, 180),
            "7 iron": random.randint(140, 170),
            "8 iron": random.randint(130, 160),
            "9 iron": random.randint(120, 150),
            "pitching wedge": random.randint(110, 140),
            "sand wedge": random.randint(80, 110),
            "putter": random.randint(1, 10)  
        }
        self.clubs_yardage["driver"] = 0  # Will be set when choosing a tee

    def choose_tee(self):
        print("Welcome to the CYOA Golf Tournament!")
        print("Choose your tee box:")
        print("1. Champion (Yardage: 6700-7200)")
        print("2. Amateur (Yardage: 6200-6700)")
        print("3. Ladies (Yardage: 5500-6000)")
        choice = input("Enter your choice: ").strip().lower()

        if choice == "1" or choice == "champion":
            self.distance_remaining = random.randint(380, 420)
            self.clubs_yardage["driver"] = random.randint(240, 280)
        elif choice == "2" or choice == "amateur":
            self.distance_remaining = random.randint(350, 380)
            self.clubs_yardage["driver"] = random.randint(220, 260)
        elif choice == "3" or choice == "ladies":
            self.distance_remaining = random.randint(300, 330)
            self.clubs_yardage["driver"] = random.randint(200, 240)
        else:
            print("Invalid choice. Using Amateur tee by default.")
            self.distance_remaining = random.randint(350, 380)
            self.clubs_yardage["driver"] = random.randint(220, 260)

    def get_available_clubs(self, first_shot=False):
        available_clubs = ["driver"] if first_shot else []
        for club, yardage in self.clubs_yardage.items():
            if club != "driver" and yardage <= self.distance_remaining + 20: 
                available_clubs.append(club)
        if self.distance_remaining <= 10:  # Putter only if within 10 yards
            available_clubs.append("putter")
        return available_clubs

    def play_hole(self):
        print(f"\n--- Hole {self.current_hole} ---")
        print(f"Yardage remaining: {self.distance_remaining} yards from tee to green.")
        first_shot = True

        while self.distance_remaining > 0:
            available_clubs = self.get_available_clubs(first_shot)
            first_shot = False
            print("Available clubs:", available_clubs)
            club_choice = input("Choose your club: ").strip().lower()

            if club_choice not in available_clubs:
                print("Invalid club choice. Try again.")
                continue

            shot_distance = self.clubs_yardage[club_choice]
            self.distance_remaining -= shot_distance
            print(f"The shot flies {shot_distance} yards, {self.distance_remaining} yards remaining.")

            if self.distance_remaining <= 0:
                print("The ball lands on the green. It's time to putt!")
                self.putt()

        print(f"The golfer completes hole {self.current_hole} with a par.")
        self.score += 4  # Putting Par as 4 for now until I can perfect par 4 holes.
        self.current_hole += 1
        if self.current_hole <= 18:
            self.set_next_hole_distance()

    def putt(self):
        while self.distance_remaining > 0:
            self.clubs_yardage["putter"] = random.randint(1, max(2, self.distance_remaining))  
            putt_distance = self.clubs_yardage["putter"]
            self.distance_remaining -= putt_distance
            print(f"Putt goes {putt_distance} yards, {self.distance_remaining} yards to the hole.")
            if self.distance_remaining > 0:
                print("Need another putt.")
            else:
                print("The ball drops into the cup! What a fantastic finish!")

    def set_next_hole_distance(self):
        # Randomly choose the next hole's distance
        self.distance_remaining = random.randint(300, 420)

    def play(self):
        self.choose_tee()
        while self.current_hole <= 18:
            self.play_hole()
            print(f"Current score after hole {self.current_hole - 1}: {self.score}")
            if self.current_hole < 18:
                input("Press Enter to start the next hole...")

# Create and start the game
game = CYOAGame()
game.play()
