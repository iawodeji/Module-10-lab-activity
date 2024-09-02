class Chapter5:
    def __init__(self):
        self.confrontation_successful = False
        self.dialogue_engaged = False
        self.evidence_used = False
        self.carter_rescued = False

    def intro(self):
        print("Chapter 5: The Final Confrontation")
        print("With enough evidence, you confront the mastermind behind the conspiracy.\n")
        print("The confrontation takes place in a luxurious penthouse overlooking the city.\n")

    def engage_dialogue(self):
        if self.dialogue_engaged:
            print("You already bought enough time.")
        else:
            print("You engage in a tense dialogue with the mastermind, trying to buy time.")
            print("Every word you say is carefully chosen to keep them talking while you plan your next move...\n")
            self.dialogue_engaged = True
            return "You successfully bought time."

    def use_evidence(self):
        if self.evidence_used:
            print("Evidence already collected.")
        else:
            print("You present the evidence you’ve collected, laying out the mastermind's crimes.")
            print("The evidence is undeniable, and you see fear flicker in their eyes...\n")
            self.evidence_used = True
            return "The mastermind is exposed."

    def avoid_traps(self):
        print("As you navigate the penthouse, you encounter hidden traps set by the mastermind.")
        print("You barely avoid getting caught by the traps, but it was a close call...\n")
        
        trapped = input("Did you get trapped? (yes/no): ").strip().lower()
        if trapped == "yes":
            print("You got trapped! You need to escape and loop back to Chapter 4.")
            return False  # Trapped, so loop back to Chapter 4
        else:
            print("You avoided the traps successfully and can now choose another option.\n")
            return True  # Successfully avoided traps, continue in Chapter 5

    def rescue_carter(self):
        if self.carter_rescued:
            print("Carter already rescued.")
        else:
            print("You discover a hidden room where Carter is held captive.")
            print("You quickly free him, ensuring his safety...\n")
            self.carter_rescued = True
            return "Carter is rescued."

    def call_authorities(self):
        print("You call the authorities, who quickly arrive at the scene.")
        print("The mastermind and their henchmen are arrested, and justice is served.\n")
        return "The game concludes. You have successfully completed the investigation!"

    def chapter5(self):
        self.intro()

        while not self.confrontation_successful:
            print("Choose your action:")
            print("1. Engage in a tense dialogue with the mastermind to buy time")
            print("2. Use the evidence collected to expose their crimes")
            print("3. Avoid traps and henchmen trying to stop you (loops back to Chapter 4 if you get trapped)")
            print("4. Rescue Carter, who is held captive in a hidden room")
            print("5. Call the authorities and ensure the criminals are arrested (game concludes)")
            print("6. Stop Investigation and Exit")
            
            choice = input("Enter the number of your choice: ")

            if choice == "1":
                result = self.engage_dialogue()
                if result:
                    print(result)
            elif choice == "2":
                result = self.use_evidence()
                if result:
                    print(result)
            elif choice == "3":
                trap_result = self.avoid_traps()
                if not trap_result:
                    return "Chapter 4: The Conspiracy Unveiled"  # Loop back to Chapter 4 if trapped
            elif choice == "4":
                result = self.rescue_carter()
                if result:
                    print(result)
            elif choice == "5":
                result = self.call_authorities()
                print(result)
                self.confrontation_successful = True  # Game concludes
            elif choice == "6":
                print("Ending the investigation. Game over.")
                break
            else:
                print("Invalid choice. Please try again.")
        
        if self.confrontation_successful:
            return "Congratulations! You’ve completed the game."

# Example of running the chapter
if __name__ == "__main__":
    chapter = Chapter5()
    conclusion = chapter.chapter5()
    print(conclusion)
