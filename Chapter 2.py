class Chapter2:
    def __init__(self):
        self.note_found = False
        self.staff_interviewed = False
        self.footage_examined = False

    def intro(self):
        print("Chapter 2: Following the Trail")
        print("Using the phone’s last known GPS coordinates, you trace Carter’s last movements.")
        print("The trail leads you to an upscale restaurant where Carter had lunch the afternoon he disappeared.\n")

    def interview_staff(self):
        if self.staff_interviewed:
            print("Staff and customers have been interviewed.")
        else:
            print("You decide to interview the restaurant staff and customers who saw Carter.")
            print("The waiter remembers seeing Carter with an unfamiliar man who seemed agitated.")
            print("Some customers also recall Carter leaving in a hurry...\n")
            self.staff_interviewed = True
            return "You gathered some information from the staff and customers."

    def examine_footage(self):
        if self.footage_examined:
            print("Security footage has been reviewed.")
        else:
            print("You ask the manager for access to the security footage.")
            print("After reviewing the footage, you see Carter sitting with a man who looks nervous.")
            print("They exchange something under the table before leaving separately...\n")
            self.footage_examined = True
            return "You reviewed the security footage."

    def discover_note(self):
        print("While searching the restroom, you find a hidden note taped under the sink.")
        print("The note contains an address with a cryptic message. This could be your next lead!\n")
        return "Chapter 3: Into the Underworld"

    def revisit_building(self):
        print("You decide to revisit the incomplete building to check for overlooked clues.")
        print("Upon arrival, you notice the place looks the same, but you feel like there might be something you missed...\n")
        return "Chapter 1: The Disappearance Continues"

    def chapter2(self):
        self.intro()

        while not self.note_found:
            print("Choose your action:")
            print("1. Interview the restaurant staff and customers who saw Carter")
            print("2. Examine security footage to identify who he was with")
            print("3. Discover a hidden note in the restroom with an address on it (proceed to Chapter 3)")
            print("4. Revisit the incomplete building to check for overlooked clues (loops back to Chapter 1)")
            print("5. Stop Investigation and Exit")
            
            choice = input("Enter the number of your choice: ")

            if choice == "1":
                result = self.interview_staff()
                if result:
                    print(result)
            elif choice == "2":
                result = self.examine_footage()
                if result:
                    print(result)
            elif choice == "3":
                result = self.discover_note()
                print(result)
                self.note_found = True  # Exit loop and proceed to Chapter 3
            elif choice == "4":
                result = self.revisit_building()
                print(result)
                return result  # Loop back to Chapter 1
            elif choice == "5":
                print("Ending the investigation. Game over.")
                break
            else:
                print("Invalid choice. Please try again.")

        if self.note_found:
            return "Proceeding to Chapter 3..."

# Example of running the chapter
if __name__ == "__main__":
    chapter2 = Chapter2()
    next_chapter = chapter2.chapter2()
    print(next_chapter)
